def checkbar():
    import matplotlib.pyplot as plt
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item,net_value from stock_management')
    data=cur.fetchall()
    x=[]
    y=[]
    for i in data:
        x.append(i[0])
        y.append(i[1])
    plt.bar(x,y,width=0.4,edgecolor='red',hatch='/')
    plt.title('net value of items')
    plt.xlabel('items')
    plt.ylabel('value')
    plt.show()
def checktable():
    import matplotlib.pyplot as plt
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item,net_value from stock_management')
    data=cur.fetchall()
    print('-'*48)
    print('|','%30s'%'item','|','%11s'%'net value','|')
    print('-'*48)
    for i in data:
        print('|','%30s'%i[0],'|','%11s'%i[1],'|')
        print('-'*48)
def checkall():
    import matplotlib.pyplot as plt
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select sum(net_value) from stock_management')
    x=cur.fetchall()
    data=x[0][0]
    return data
