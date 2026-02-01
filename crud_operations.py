def add_into_rm():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    while True:
        rm_id = int(input("ENTER THE ID:"))
        name_of_rm = input("ENTER THE NAME:")
        description = input("ENTER THE DESCRIPTION:")
        quantity_a = input("ENTER THE QUANTITY AVAILABLE:")
        quantity_b = input("ENTER THE QUANTITY BOUGHT:")
        supplier = input("ENTER THE SUPPLIER NAME:")
        purchase_date = input("ENTER THE DATE_PURCHASED:")
        expiration_date = input("ENTER THE DATE OF EXPIRATION:")
        price = int(input("ENTER THE PRICE:"))
        insert_rm = "insert into raw_materials values({},'{}','{}','{}','{}','{}','{}','{}',{})".format(rm_id,name_of_rm,description,quantity_a,quantity_b,supplier,purchase_date,expiration_date,price)
        mycur.execute(insert_rm)
        mycon.commit()
        print("THE DETAILS OF RAW MATERIALS HAS BEEN INSERTED SUCCESSFULLY!!!")
        choice = input("DO YOU WANT TO CONTINUE:")
        if choice in "Nn":
            break
    mycon.close()

def add_into_nb():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    while True:
        nb_id = int(input("ENTER  THE ID:"))
        nb_name = input("ENTER THE NAME:")
        category = input("ENTER THE CATEGORY:")
        num_p = int(input("NO OF NOTEBOOKS PRODUCED:"))
        num_d = int(input("NO OF NOTEBOOKS DELIVERED:"))
        num_a = int(input("NO OF NOTEBOOKS AVAILABLE:"))
        insert_nb = "insert into notebook_entries values ({},'{}','{}',{},{},{})".format(nb_id,nb_name,category,num_p,num_d,num_a)
        mycur.execute(insert_nb)
        mycon.commit()
        print("THE DETAILS OF NOTEBOOKS HAS BEEN INSERTED SUCCESSFULLY!!!")
        choice = input("DO YOU WANT TO CONTINUE:")
        if choice in "Nn":
            break
    mycon.close()

def add_into_cus():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    while True:
        bill_no = int(input("ENTER THE BILL NUMBER:"))
        name_of_enterprise = input("ENTER THE NAME:")
        address = input("ENTER THE ADDRESS:")
        phone_no = input("ENTER THE PHONE NUMBER:")
        date_of_order = input("ENTER THE DATE_O:")
        date_of_delivery = input("ENTER THE DATE_D:")
        products_o = input("ENTER THE PRODUCTS NAME:")
        num_o = input("ENTER THE NO OF PRODUCTS:")
        insert_cus = "insert into customers values({},'{}','{}','{}','{}','{}','{}','{}')".format(bill_no,name_of_enterprise,address,phone_no,date_of_order,date_of_delivery,products_o,num_o)
        mycur.execute(insert_cus)
        mycon.commit()
        print("THE CUSTOMER DETAILS HAS BEEN INSERTED SUCCESSFULLY!!!")
        choice = input("DO YOU WANT TO CONTINUE:")
        if choice in "Nn":
            break
    mycon.close()

def get_from_rm():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()      
    mycur.execute("select * from raw_materials ")
    rec= mycur.fetchall()
    for i in rec:
        print(i)
    mycon.close()

def get_from_nb():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    mycur.execute("select * from notebook_entries ")
    rec= mycur.fetchall()
    for i in rec:
        print(i)
    mycon.close()

def get_from_cus():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    mycur.execute("select * from customers ")
    rec= mycur.fetchall()
    for i in rec:
        print(i)
    mycon.close()



def update_nb():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    newnum_p = int(input(" NO OF NOTEBOOKS PRODUCED:"))
    newnum_d = int(input("NO OF NOTEBOOKS DELIVERED:"))
    newnum_a = int(input("NO OF NOTEBOOKS AVAILABLE:"))
    ID = int(input("ENTER THE NOTEBOOK ID:"))
    update_nb = "update notebook_entries set num_p = %s ,num_d = %s,num_a = %s where nb_id = %s"
    data_nb =  (newnum_p,newnum_d,newnum_a,ID)
    mycur.execute(update_nb,data_nb)
    mycon.commit()
    print("THE NOTEBOOK DETAILS HAS BEEN UPDATED SUCCESSFULLY!!!")
    mycon.close()


def update_rm_quantity():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    new_quantity_b = int(input("ENTER THE QUANTITY BOUGHT:"))
    rm_id= int(input("ENTER THE RAW MATERIAL ID:"))
    update_rm = "update raw_materials set quantity_b = '%s'  where rm_id = %s"
    data_rm =  (new_quantity_b,rm_id)
    mycur.execute(update_rm,data_rm)
    mycon.commit()
    print("THE QUANTITY HAS BEEN UPDATED SUCCESSFULLY!!!")
    mycon.close()

def update_rm_price():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    new_price = int(input("ENTER THE PRICE:"))
    rm_id= int(input("ENTER THE RAW MATERIAL ID:"))
    update_rmp = "update raw_materials set price= %s  where rm_id = %s"
    data_rmp=  (new_price,rm_id)
    mycur.execute(update_rmp,data_rmp)
    mycon.commit()
    print("THE  PRICE HAS BEEN UPDATED SUCCESSFULLY!!!")
    mycon.close()

def update_cus():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    new_pno = input("ENTER THE NEW PHONE NUMBER:")
    new_address = input("ENTER THE ADDRESS:")
    billno= int(input("ENTER THE BILL NUMBER:"))
    update_cus = "update customers set phone_no = '{}',address = '{}'  where bill_no = {}".format(new_pno,new_address,billno)
    mycur.execute(update_cus)
    mycon.commit()
    print("THE CUSTOMER DETAILS HAS BEEN UPDATED SUCCESSFULLY!!!")
    mycon.close()


def delete_from_nb():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    ID= int(input("ENTER NOTEBOOK ID TO BE DELETED:"))
    delete_nb= "delete from notebook_entries where nb_id = {}".format(ID)
    mycur.execute(delete_nb)
    mycon.commit()
    print("THE NOTEBOOK DETAILS HAS BEEN DELETED SUCCESSFULLY!!!")
    mycon.close()

def delete_from_rm():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    ID = int(input("ENTER RAW MATERIAL ID TO BE DELETED:"))
    delete_rm = "delete from raw_materials where rm_id = {}".format(ID)
    mycur.execute(delete_rm)
    mycon.commit()
    print("THE RAW MATERIAL DETAILS HAS BEEN DELETED SUCCESSFULLY!!!")
    mycon.close()

def delete_from_cus():
    mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
    mycur = mycon.cursor()
    BILLNO = int(input("ENTER CUSTOMER ID TO BE DELETED:"))
    delete_cus = "delete from customers where bill_no = {}".format(BILLNO)
    mycur.execute(delete_cus)
    mycon.commit()
    print("THE CUSTOMERS DETAILS HAS BEEN DELETED SUCCESSFULLY!!!")
    mycon.close()


