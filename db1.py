# db1.py

import sqlite3

# 연결객체 생성(일단 메모리에 임시 저장)
con = sqlite3.connect(":memory:")

# 구문 수행할 커서 객체 생성
cur = con.cursor()

# 데이터를 담을 테이블 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")

# 1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

# 결과 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)