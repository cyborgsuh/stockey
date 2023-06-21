def suppliercheck(supp):
    import mysql.connector as ms
    cob=ms.connect(host='localhost',user='root',passwd='suhaib',database='project')
    cur=cob.cursor()
    cur.execute('select supplier from supplier_details')
    x=cur.fetchall()
    l=[]
    for i in x:
        for j in i:
            l.append(j)
    if supp not in l:
        raise exception('supplier not found')