def suppdetails():
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',password='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select * from supplier_details')
    x=cur.fetchall()
    print('|','%30s'%'supplier','|','%15s'%'supplied items','|','%30s'%'address','|','%20s'%'contact','|')
    for i in x:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('|','%30s'%i[0],'|','%15s'%i[1],'|','%30s'%i[2],'|','%20s'%i[3],'|')