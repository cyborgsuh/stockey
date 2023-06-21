def prch():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    while True:
        s=input('search item by item_no or item_code:')
        if s=='item_no':
            import itemnocheck
            n=itemnocheck.check()
            p=eval(input('enter new price:'))
            query="update stock_management set price={} where item_no={}".format(p,n)
            cur.execute(query)
            cob.commit()
            print('seccessfully executed')
            cur.execute('select quantity,price from stock_management where item_no={}'.format(n))
            x=cur.fetchall()
            q=x[0][0]
            p=x[0][1]
            nv=q*p
            cur.execute('update stock_management set net_value={} where item_no={}'.format(nv,n))
            cob.commit()
            break
        elif s=='item_code':
            import itemcodecheck    
            n=itemcodecheck.check()
            p=eval(input('enter new price:'))
            query="update stock_management set price={} where item_code={}".format(p,n)
            cur.execute(query)
            cob.commit()
            print('seccessfully executed')
            cur.execute('select quantity,price from stock_management where item_code={}'.format(n))
            x=cur.fetchall()
            q=x[0][0]
            p=x[0][1]
            nv=q*p
            cur.execute('update stock_management set net_value={} where item_code={}'.format(nv,n))
            cob.commit()
            break
        else:
            print('enter item_no or item_code!!!')