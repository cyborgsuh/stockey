def sell():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    import itemcodecheck
    s=itemcodecheck.check()
    q=input('enter quantity of the item to be sold:')       # quantity
    query='update stock_management set quantity=quantity-{} where item_code={}'.format(q,s)
    cur.execute(query)
    cob.commit()
    cur.execute('select item,quantity,price from stock_management where item_code=%s'%(s,))
    x=cur.fetchall()
    quan=x[0][1]         
    pr=x[0][2]     #price
    it=x[0][0]       # item name
    nv=quan*pr
    cur.execute('update stock_management set net_value={} where item_code={}'.format(nv,s))
    cob.commit()
    print('%55s'%'~~~~~~~~~~~~~~BILL~~~~~~~~~~~~~~')
    import datetime
    x = datetime.datetime.now()
    print('Time')
    print(x.strftime("%I:%M"))
    print('Date')
    print(x.strftime("%A, %d %B %Y"))
    print("%30s"%'item','|',"%11s"%'quantity','|','%11s'%'total price','|',)
    print('--------------------------------------------------------------------')
    tp=int(q)*pr
    print("%30s"%it,'|','%11s'%q,'|',"%11s"%tp,'|')
