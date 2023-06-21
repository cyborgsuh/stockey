entry=eval(input('Admin(1)/Employee(2):'))
import additem
import addstock
import changeprice
import checkstock
import sell
import supplierdetails
import delete
import checknetvalue
import checkprice
import itemcodeandno
import employee
import mysql.connector as ms
import crucialinfo
cob=ms.connect(host='127.0.0.1',passwd='suhaib',user='root')
cur=cob.cursor()
cur.execute("create database if not exists project")
cur.execute("use project")
cur.execute("create table if not exists stock_management(item_no int not null unique primary key,item_code int not null unique,item char(30) unique not null,price int not null,quantity int,supplier char(30) default null,net_value int)")
cur.execute('create table if not exists supplier_details(supplier char(30) not null unique primary key,items_supplied int ,address varchar(30) not null,contact int(20) not null)')
cur.execute('create table if not exists emp(ename varchar(30),epass varchar(30),salary int)')
cob.commit()
password=crucialinfo.x
if entry==1:
    ps=input('enter password:')
    if ps==password:
        while True:
            print('-'*100)
            print('~~~~~~~~| MENU |~~~~~~~~')
            print('enter 1 to add item')
            print('enter 2 to add stock')
            print('enter 3 to sell item')
            print('enter 4 to change price')
            print('enter 5 to check stock')
            print('enter 6 to check supplier details')
            print('enter 7 to delete item')
            print('enter 8 to see the net value of items')
            print('enter 9 to see the net value of stock')
            print('enter 10 to check price')
            print('enter 11 to check item_code and item_no')
            print('enter 12 to add new employee')
            print('enter 13 to see employee details')
            print('enter 0 to exit')
            ch=eval(input('enter your choice:'))
            if ch==1:
                additem.additem()
            elif ch==2:
                addstock.addstock()
            elif ch==3:
                sell.sell()
            elif ch==4:
                changeprice.prch()
            elif ch==5:
                bt=input('check stock using bar graph or table:')
                if bt=='bar graph':
                    checkstock.checkbar()
                elif bt=='table':
                    checkstock.checktable()
            elif ch==6:
                supplierdetails.suppdetails()
            elif ch==7:
                delete.delete()
            elif ch==0:
                break
            elif ch==8:
                choice=input('check net value using bar graph of table:')
                if choice=='bar graph':
                    checknetvalue.checkbar()
                elif choice=='table':
                    checknetvalue.checktable()
            elif ch==9:
                a=checknetvalue.checkall()
                print('net value of stock is',a)
            elif ch==10:
                checkprice.checkprice()
            elif ch==11:
                itemcodeandno.details()
            elif ch==12:
                employee.newemployee()
            elif ch==13:
                employee.empdetails()
            else:
                print('ENTER VALID OPTION')
    else:
        print('WRONG PASSWORD')
elif entry==2:
    ename=input('enter your name:')
    cur.execute("select * from emp where ename='{}'".format(ename))
    x=cur.fetchall()
    if cur.rowcount==0:
        print('employee not found')
    else:
        psw=input('enter the password:')
        if psw==x[0][1]:
            while True:
                print('-'*100)
                print('enter 1 to sell item')
                print('enter 2 to check stock')
                print('enter 3 to checkprice')
                print('enter 4 to check item_code and item_no')
                print('enter 0 to exit')
                ch=eval(input('enter your choice:'))
                if ch==1:
                    sell.sell()
                elif ch==2:
                    bt=input('check stock using bar graph or table:')
                    if bt=='bar graph':
                        checkstock.checkbar()
                    elif bt=='table':
                        checkstock.checktable()
                elif ch==3:
                    checkprice.checkprice()
                elif ch==4:
                    itemcodeandno.details()
                elif ch==0:
                    break
                else:
                    print('ENTER VALID OPTION')
        else:
            print('WRONG PASSWORD')
