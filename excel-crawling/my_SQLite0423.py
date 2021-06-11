import sqlite3
## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4, data5 = "", "", "", "", ""
sql=""

## 메인 동작 부분 ##
con = sqlite3.connect('./myFirstDB.db')
cur = con.cursor()

while(True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("나이 ==> ")
    data4 = input("email ==> ")
    data5 = input("핸드폰 ==> ")
    sql = "INSERT INTO firstTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + "," + data5 + ")"
    cur.execute(sql)
    
con.commit()
con.close()