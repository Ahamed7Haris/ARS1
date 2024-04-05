from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
a=[]
s=0
a=[0]*1
print(a)
mydb=mysql.connector.connect(host='localhost',database='Route1',user='Ahamed',password='Ahamed@2003',auth_plugin='caching_sha2_password') 
cu=mydb.cursor()
def fetch(deptci,arrci,sclass):  
    try:
        if mydb.is_connected():
            print("Connected")       
    except mysql.connector.Error as r:
        print(f'Error:{r}')
    
    deptci=str(request.form.get('Dep'))
    arrci=str(request.form.get('Arr'))
    sclass=sclass
    query="select * from route where Deptcity=(%s) and Arrcity=(%s)and class=(%s)"
    cu.execute(query,(deptci,arrci,sclass))
    ff=cu.fetchall()
    return ff  
app=Flask(__name__,template_folder="templates") 
@app.route('/',methods=['GET'])
def index():
    return render_template("Untitled.html")
@app.route('/',methods=["POST"])
def enabbook():
    passcount=request.form.get('Passe')
    s=passcount
    deptci=str(request.form.get('Dep'))
    arrci=str(request.form.get('Arr'))
    passc=(request.form.get('Passe'))
    print(passc)
    Class=request.form.get(('Class'))
    failmsg=""
    print((deptci),(arrci))
    if len(deptci)==0:
        failmsg="Please fill the necessary fields"
        return render_template("Untitled.html", failmsg=failmsg) 
    if  len(arrci)==0:
        failmsg="Please fill the necessary fields"
        return render_template("Untitled.html", failmsg=failmsg)
    if deptci==arrci:
        return render_template("Untitled.html", failmsg="Please choose a different arrival and departure city")
        
    else:
        rows=fetch((deptci),(arrci),(Class))
        p=[]
        v1=""
        for i in rows:
            v1=i[1] #departure city
            v2=i[2] #Arrival city
            v3=i[3] #stops
            v4=i[4] #Date
            v5=int(i[5])*int(passc) #price  
            v6=i[6] #Flightid
            v7=i[7]
            print(type(v5))
            p.append((v1,v2,int(v5),v6,v3,v4,v7,passcount))
        a.pop(0)

        for i in range(len(p)):
            a.append(p[i])
        if deptci!=v1:
            return render_template("Info.html",failmsg="Sorry Flight not available")
        else:
            return render_template('Info.html',processed_rows=p) 
@app.route('/Billbef', methods=['POST'])
def load_bill():
    # Redirect to Billbef.html after form submission
    print(len(a))
    print(a)
    return redirect(url_for('billbef'))

# Route to render Billbef.html
@app.route('/billbef')
def billbef():
    return render_template("Billbef.html",a=a)
@app.route('/Modif',methods=['GET'])
def mod():
    return render_template('Modif.html')

# def   ():
#     
# @app.route('/')
# def fecsh():  
#     try:
#         if mydb.is_connected():
#             print("Connected")       
#     except mysql.connector.Error as r:
#         print(f'Error:{r}')
#     a=str(request.form.get('name'))
#     b=request.form.get('email')
#     c=request.form.get('mobile')
#     d=request.form.get('dob')
#     e=request.form.get('price')
#     f=request.form.get('price1')
#     g=request.form.get('price2') 
#     dat=request.form.get('dob') #Change this 
#     classs=request.form.get('class')
#     depcit=request.form.get('depc')
#     arrcit=request.form.get('arc')
#     id=request.form.get('id')
#     s=[a,b,c,d,e,f,g,d,c,depcit,arrcit,id] 
#     return s
def fetcsh():  
    try:
        if mydb.is_connected():
            print("Connected")       
    except mysql.connector.Error as r:
        print(f'Error:{r}')
    a=str(request.form.get('name'))
    b=request.form.get('email')
    c=request.form.get('mobile')
    d=request.form.get('dob')
    e=request.form.get('price')
    f=request.form.get('price1')
    g=request.form.get('price2') 
    dat=request.form.get('dob') #Change this 
    classs=request.form.get('class')
    depcit=request.form.get('depc')
    arrcit=request.form.get('arc')
    id=request.form.get('id')
    s=[a,b,c,d,e,f,g,d,c,depcit,arrcit,id] 
    query="insert into passenger(name,email,Mobileno,dob,Origprice,Totprice,Finalpri,Depdate,Depcity,Arrcity,Flightid,class) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cu.execute(query,(a,b,c,d,e,f,g,dat,depcit,arrcit,id,classs))
    mydb.commit()


@app.route('/download',methods=['POST']) 
def down():
    fetcsh()
    query="Select * from passenger where Name=(%s) and Depdate=(%s) and  Depcity=(%s) and Arrcity=(%s) and Flightid=(%s)"
    cu.execute(query,((str(request.form.get('name'))),request.form.get('dob'),request.form.get('depc'),request.form.get('arc'),request.form.get('id')))
    ff=cu.fetchone()
    print(ff)
    a=[]
    for i in range(0,1):
        a.append(ff)
        
    return render_template('download.html',processed_row=a)
@app.route('/Pay',methods=['POST']) 
def doswn():
  

    return render_template('Pay.html')
def fetchh():
     query="Select * from passenger"
     cu.execute(query)
     ff=cu.fetchone()
     return ff

@app.route('/download1',methods=['POST']) 
def downd():
    
    ff=fetchh()
    print(ff)
    a=[]
    for i in range(1):
        a.append(ff)
    print(a)
    return render_template('download1.html',processed_row=a)
if  __name__== "__main__":
    app.run(debug=True,port=8000)
