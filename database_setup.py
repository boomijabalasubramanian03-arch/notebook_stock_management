print('WELCOME :)')
print('NOTEBOOK_STOCK_MANAGEMENT')
print('_________________________')
print()
import mysql.connector as m

mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8')
mycur=mycon.cursor()
database_name = input('ENTER THE DATABASE TO BE CREATED :')
mycur.execute('create database if not exists %s'%(database_name))
mycon.close()
print("THE DATABASE HAS BEEN CREATED SUCCESSFULLY!!!")

mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
mycur = mycon.cursor()
mycur.execute("create table raw_materials(rm_id int primary key,\
              name_of_rm varchar(30),\
              description varchar(50),\
              quantity_a varchar(10),\
              quantity_b varchar(10),\
              supplier varchar(30),\
              purchase_date date,\
              expiration_date date,\
              price decimal(10,2))")
mycur.close()
mycon.close()
print("THE RAW MATERIAL TABLE HAS BEEN CREATED SUCCESSFULLY!!!")
print('_______________________________________________________')
print()
mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
mycur = mycon.cursor()
mycur.execute("create table notebook_entries(nb_id int primary key,\
              nb_name varchar(25),\
              category varchar(25),\
              num_p int,\
              num_d int,\
              num_a int)")
mycur.close()
mycon.close()
print("THE NOTEBOOK ENTRY TABLE HAS BEEN CREATED SUCCESSFULLY!!!")
print('_________________________________________________________')
print()

mycon = m.connect(host = "localhost",user = "root",password = "dude3579",charset = 'utf8',database = "BKS_ENTERPRISE" )
mycur = mycon.cursor()
mycur.execute("create table customers(bill_no int primary key,\
              name_of_enterprise varchar(30),\
              address varchar(50),\
              phone_no varchar(20),\
              date_of_order date,\
              date_of_delivery date,\
              products_o varchar(100),\
              num_o varchar(15))")
mycur.close()
mycon.close()
print("THE CUSTOMER TABLE HAS BEEN CREATED SUCCESSFULLY!!!")
print('___________________________________________________')
print()

import mysql.connector as m

