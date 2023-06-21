def check():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item_no from stock_management')
    x=cur.fetchall()
    l=[]
    for i in x:
        for j in i:
            l.append(j)
    n=eval(input('enter item_no:'))
    if n not in l:
        raise Exception('item_no not found')
    return n