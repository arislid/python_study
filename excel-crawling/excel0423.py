import sqlite3

#sqlite3 임포트 후 sqlite3 . connect (“ DB 이름”)으로 데이터베이스와 연결
con = sqlite3.connect('C:\sqlite-tools-win32-x86-3350500\sqlite-tools-win32-x86-3350500/naverDB.db')
#커서( Cursor ) : 데이터베이스에 SQL 문을 실행 또는 실행된 결과를 돌려받는 통로
cur = con.cursor()

#cur.execute("CREATE TABLE pythonTable (id char(4), userName char(10), program char(30))")
#위 문구는 새로 테이블을 형성하는 것이므로, 기존 테이블이 있다면 생략한다
# datetime A combination of a date and a time. Attributes: () -> 요건 뭘까...?

cur.execute("INSERT INTO pythonTable VALUES('park', 'minji', 'C, C++, python, SQLite, Javascript') ")

#SQL 문을 실행 다 했으면 commit 한 다음에 close 시켜 sql을 종료한다.
con.commit()
con.close()