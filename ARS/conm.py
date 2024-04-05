import mysql.connector 
try:
    mydb=mysql.connector.connect(host='localhost',database='Route1',user='Ahamed',password='Ahamed@2003',auth_plugin='caching_sha2_password')
    if mydb.is_connected():
        print("Connected")
        mydb.close()
except mysql.connector.Error as r:
    print(f'Error:{r}')