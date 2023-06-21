def checkbar():
    import matplotlib.pyplot as plt
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item,quantity from stock_management')
    data=cur.fetchall()
    x=[]
    y=[]
    for i in data:
        x.append(i[0])
        y.append(i[1])
    plt.bar(x,y,width=0.4,edgecolor='red',hatch='/')
    plt.xlabel('item')
    plt.ylabel('quantity')
    plt.title('Stock')
    plt.show()
def checktable():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select item,quantity from stock_management')
    data=cur.fetchall()
    print('-'*48)
    print('|','%30s'%'item','|','%11s'%'quantity','|')
    print('-'*48)
    for i in data:
        print('|','%30s'%i[0],'|','%11s'%i[1],'|')
        print('-'*48)