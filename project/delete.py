def delete():
    import itemcodecheck
    import itemnocheck
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',passwd='suhaib',database='project')
    cur=cob.cursor()
    while True:
        s=input('delete using item_no or item_code:')
        if s=='item_no':
            a=itemnocheck.check()
            cur.execute('select supplier from stock_management where item_no={}'.format(a))
            x=cur.fetchall()
            supp=x[0][0]
            cur.execute("update supplier_details set items_supplied=items_supplied-1 where supplier='{}'".format(supp))
            query='delete from stock_management where item_no={}'.format(a)
            cur.execute(query)
            cob.commit()
            print('successfully deleted')
            break
        elif s=='item_code':
            a=itemcodecheck.check()
            cur.execute('select supplier from stock_management where item_code={}'.format(a))
            x=cur.fetchall()
            supp=x[0][0]
            cur.execute("update supplier_details set items_supplied=items_supplied-1 where supplier='{}'".format(supp))
            query='delete from stock_management where item_code={}'.format(a)
            cur.execute(query)
            cob.commit()
            print('succesfully deleted')
            break
        else:
            print('enter item_no or item_code!!!')