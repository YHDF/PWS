import mysql.connector
import selenium_ as selenium
import beautifulsoup as bs
import multiprocessing as mp
import uuid

products = [[]for x in range(2)]
group_ids = []
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yh"
)
cursor = db.cursor(buffered=True)
cursor.execute("USE Testing")



def get_link() :
    link = cursor.execute("SELECT id_group, link, product_class FROM groups")
    row = cursor.fetchall()
    for cell in row:
        if 'amazon' in cell[1] :
            group_ids.append(cell[0])
            a_products = selenium.init(cell[0], cell[1], cell[2])
            products[0].extend(a_products)
        elif 'ebay' in cell[1] :
            group_ids.append(cell[0])
            e_products = bs.init(cell[0], cell[1], cell[2])
            products[1].extend(e_products)
    #print(products[0][10].name)
    sql = "INSERT INTO products (id, group_id, name, link, image, price) VALUES (%s, %s, %s, %s, %s, %s)"
    for arr in products :
        for product in arr :
            print(product.name)
            val = (str(uuid.uuid4()), product.id_group, product.name, product.link, product.img_link, product.price)
            cursor.execute(sql, val)
            db.commit()
    print(cursor.rowcount, "was inserted.")


def main() :
    get_link()
    db.close()

if __name__ == '__main__':
    p = mp.Process(target=main)
    p.start()
    p.join()
