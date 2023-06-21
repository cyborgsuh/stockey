def addstock():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    while True:
        s=input('search item by item_no or item_code:')
        if s=='item_no':
            import itemnocheck
            n=itemnocheck.check()
            a=eval(input('enter quantity of stock you want to add:'))
            query='update stock_management set quantity=quantity+{} where item_no={}'.format(a,n)
            cur.execute(query)
            cob.commit()
            cur.execute('select quantity,price from stock_management where item_no={}'.format(n))
            x=cur.fetchall()
            q=x[0][0]
            p=x[0][1]
            nv=q*p
            cur.execute('update stock_management set net_value={} where item_no={}'.format(nv,n))
            cob.commit()
            print('succesfully added')
            break
        elif s=='item_code':
            import itemcodecheck
            n=itemcodecheck.check()
            a=eval(input('enter quantity of stock you want to add:'))
            query='update stock_management set quantity=quantity+{} where item_code={}'.format(a,n)
            cur.execute(query)
            cob.commit()
            cur.execute('select quantity,price from stock_management where item_code={}'.format(n))
            x=cur.fetchall()
            q=x[0][0]
            p=x[0][1]
            nv=q*p
            cur.execute('update stock_management set net_value={} where item_code={}'.format(nv,n))
            cob.commit()
            print('succesfully added')
            break
        else:
            print('enter item_no or item_code!!!')
