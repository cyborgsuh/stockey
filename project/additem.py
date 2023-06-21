def additem():
    import itemcodecheck
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',passwd='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item_no from stock_management')
    x=cur.fetchall()
    l=[]
    for i in x:
        for j in i:
            l.append(j)
    try:
        n=max(l)+1
    except:
        n=1
    while True:
        try:
            a=itemcodecheck.check()
            print('code is not unique!!! enter unique code')
        except:
            print('code is unique')
            code=eval(input('re enter unique item code:'))
            break
    name=input('enter item name:')
    price=eval(input('enter the price of item:'))
    quantity=eval(input('enter quantity:'))
    supplier=input('enter supplier name:')     
    nv=price*quantity
    query="insert into stock_management values({},{},'{}',{},{},'{}',{})".format(n,code,name,price,quantity,supplier,nv)
    cur.execute(query)
    try:
        import suppliercheck
        suppliercheck.suppliercheck(supplier)
        cur.execute("update supplier_details set items_supplied=items_supplied+1 where supplier='{}'".format(supplier))
    except:
        supp_contact=input('enter supplier contact number:')
        supp_address=input('enter supplier adresss:')
        cur.execute("insert into supplier_details values('{}',1,'{}',{})".format(supplier,supp_address,supp_contact))
    cob.commit()
    print('item succesfully added')