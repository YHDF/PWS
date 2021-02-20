import mysql.connector
import selenium_ as selenium
import beautifulsoup as bs
import multiprocessing as mp

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yh"
)
cursor = db.cursor(buffered=True)
cursor.execute("USE Testing")

def get_link() :
    link = cursor.execute("SELECT link, product_class FROM groups")
    row = cursor.fetchall()
    for cell in row:
        if 'amazon' in cell[0] :
            products = selenium.init(cell[0], cell[1])
        elif 'ebay' in cell[0] :
            products = bs.init(cell[0], cell[1])

        print(products[0].name)



def main() :
    get_link()
    db.close()

if __name__ == '__main__':
    p = mp.Process(target=main)
    p.start()
    p.join()
