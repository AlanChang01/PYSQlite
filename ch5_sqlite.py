import sqlite3
import csv


def execute_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    db_name = 'db.sqlite'
    print('建立資料庫及資料表')
    cmd = 'CREATE TABLE record (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, shop TEXT)'
    execute_db(db_name, cmd)

print('插入測試資料')
cmd = 'INSERT INTO record (item, price, shop) VALUES ("PS4測試機2", 1000, "測試賣家")'
execute_db(db_name, cmd)


print('更新資料')
cmd = 'UPDATE record SET shop="EZ賣家" where shop="測試賣家"'
execute_db(db_name, cmd)