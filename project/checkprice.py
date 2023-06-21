def checkprice():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    while True:
        ch=input('check price using item_no or item_code:')
        if ch=='item_code':
            import itemcodecheck
            n=itemcodecheck.check()
            query='select item,price from stock_management where item_code={}'.format(n)
            cur.execute(query)
            x=cur.fetchall()
            item=x[0][0]
            price=x[0][1]
            print(item,'costs',price)
            break
        elif ch=='item_no':
            import itemnocheck
            n=itemnocheck.check()
            query='select item,price from stock_management where item_no={}'.format(n)
            cur.execute(query)
            x=cur.fetchall()
            item=x[0][0]
            price=x[0][1]
            print(item,'costs',price)
            break
        else:
            print('enter item_no or item_code!!!')
