def check():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item_code from stock_management')
    x=cur.fetchall()
    l=[]
    for i in x:
        for j in i:
            l.append(j)
    n=eval(input('enter item_code:'))
    if n not in l:
        raise Exception('Code not found')
    return n