def newemployee():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    name=input('enter employee name:')
    pswd=input('enter password for employee:')
    sal=eval(input('enter the salary of employee:'))
    cur.execute("insert into emp values('{}','{}',{})".format(name,pswd,sal))
    cob.commit()
def empdetails():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select * from emp')
    x=cur.fetchall()
    print('|','%30s'%'employee name','|','%30s'%'employee password','|','%11s'%'salary','|')
    print('-'*81)
    for i in x:
        print('|','%30s'%i[0],'|','%30s'%i[1],'|','%11s'%i[2],'|')
        print('-'*81)