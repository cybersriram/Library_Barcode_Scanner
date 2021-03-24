from django.shortcuts import render,redirect
import datetime
import sqlite3,xlwt
from .models import in_out_rp,stud_rec
def date():
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y")
    return(date_time)
def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return(current_time)
# Create your views here.
def register(request):
    if (request.method == "POST"):
        roll = request.POST['num']
        name = request.POST['name']
        user = stud_rec(rollno=roll,name=name)
        user.save()
        return render(request,"extend.html")
    else:
        return render(request,"extend.html")
def get_data_db(a):
    conn = sqlite3.connect('entry.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    sql = "SELECT toggle from get_entry_in_out_rp where rollno = "+str(a) 
    cursor.execute(sql)

    #Fetching 1st row from the table
    result = cursor.fetchall();

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()
    temp = 0
    for i in range(len(result)):
        if result[i][0] == "IN":
            return 0
            break
        else:
            temp+=1
    if temp == (len(result)):
        return 1  
def index(request):
    if (request.method =="POST"):
        number = request.POST['num']
        today = date()
        now = time()
        
        if(get_data_db(number)==0):
            connn = sqlite3.connect('entry.db')

            #Creating a cursor object using the cursor() method
            cursor = connn.cursor()
            sql = "update get_entry_in_out_rp set toggle = ?,outtime = ? where rollno = "+str(number)
            t = time()
            # Preparing SQL queries to INSERT a record into the database.
            cursor.execute(sql,("out",t))

            # Commit your changes in the database
            connn.commit()
            print("Records inserted........")

            # Closing the connection
            connn.close()
        else:
            user = in_out_rp(rollno=number,name="sriram",intime=now,outtime="NULL",toggle="IN",date=today)
            user.save()
        return render(request,"index.html")
    else:
        return render(request,"index.html")
def con(request):
    from_date = request.POST['from']
    to_date = request.POST['to']
    conn = sqlite3.connect('entry.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    sql = "SELECT rollno,name,intime,outtime,date from get_entry_in_out_rp where date between ? and ?"
    cursor.execute(sql,(from_date,to_date))
    #Fetching 1st row from the table
    result = cursor.fetchall();

    #Commit your changes in the database
    conn.commit()
    
    #Closing the connection
    conn.close()
    style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',
    num_format_str='#,##0.00')
    style1 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
    num_format_str='#,##0.00')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Entries1')
    ws.write(0, 0, "ROLLNO", style0)
    ws.write(0, 1, "NAME", style0)
    ws.write(0, 2, "INTIME", style0)
    ws.write(0, 3, "OUTTIME", style0)
    ws.write(0, 4, "DAY", style0)
    print(len(result))
    for i in range (len(result)):
        for j in range (5):
            ws.write(i+1, j, result[i][j], style1)
    wb.save('entry1.xls')
    return redirect("index")