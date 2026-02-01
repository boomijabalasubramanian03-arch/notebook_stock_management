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
    