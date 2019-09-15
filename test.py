import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="nawaz123",db="Cowork_PV")
cursor = connection.cursor()
create_table = "CREATE TABLE dw_users(id int,username varchar(200),password varchar(200))"
cursor.execute(create_table)

insert_table = "INSERT INTO dw_users values ({},{},{})".format(1,"'nawaz'","'nawaz1'")
# user = (1,'nawaz','nawaz1')
cursor.execute(insert_table)
insert_table = "INSERT INTO dw_users values ({},{},{})".format(1,"'nawaz2'","'nawaz2'")
cursor.execute(insert_table)

select_query = "Select id,username from dw_users"
res = cursor.execute(select_query)
print(res)
for row in cursor.fetchall():
    print(row)
connection.commit()
connection.close()