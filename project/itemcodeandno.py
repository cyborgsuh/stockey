def details():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',passwd='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item_no,item_code,item from stock_management')
    x=cur.fetchall()
    print('|','%7s'%'item_no','|','%10s'%'item_code','|','%30s'%'item','|')
    print('-'*57)
    for i in x:
        print('|','%7s'%i[0],'|','%10s'%i[1],'|','%30s'%i[2],'|')
        print('-'*57)