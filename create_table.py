import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="nawaz123",db="Cowork_PV")
cursor = connection.cursor()

query = "Create table if not exists dw_users2(id INTEGER primary key auto_increment,username varchar(255),password varchar(255))"
cursor.execute(query)

query = "Create table if not exists dw_items(id INTEGER primary key auto_increment,name varchar(255),price float)"
cursor.execute(query)

# cursor.execute("Insert into dw_items values ('test',10.99)")

connection.commit()
connection.close()
