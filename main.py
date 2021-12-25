import mysql.connector
import selenium_ as selenium
import beautifulsoup as bs
import multiprocessing as mp
import uuid

from mapping import Products
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

#to edit and add the URI corresponding depending on the system 
engine = create_engine('mariadb://localhost:3306/(Schema-Name)?user=(username)&password=(password)', echo=True)


products = [[]for x in range(2)]
group_ids = []
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yh"
)
cursor = db.cursor(buffered=True)
cursor.execute("USE Testing")

nbpage = 10


def get_link() :
    link = cursor.execute("SELECT id_group, link, product_class FROM groups")
    row = cursor.fetchall()
    for cell in row:
        if 'amazon' in cell[1] :
            group_ids.append(cell[0])
            for n in range(0,nbpage) :
                a_products = selenium.init(cell[0], cell[1] + str(n), cell[2])
            products[0].extend(a_products)
        elif 'ebay' in cell[1] :
            group_ids.append(cell[0])
            for n in range(0, nbpage) : 
                e_products = bs.init(cell[0], cell[1] + str(n), cell[2])
            products[1].extend(e_products)


    Session = sessionmaker(bind=engine)
    session = Session()
    for arr in products:
        for product in arr :
            result = Products(id = str(uuid.uuid4()),group_id=product.id_group ,name=product.name, link=product.link, image=product.img_link, price=product.price)
            session.add(result)
    session.commit()


def main() :
    get_link()
    db.close()

if __name__ == '__main__':
    p = mp.Process(target=main)
    p.start()
    p.join()
