import sqlite3

con = sqlite3.connect("todo.db")
cur = con.cursor()

'''
C -> Create
R -> Read
U -> Update
D -> Delete
'''

table_name = 'todos'

# TODO: create a table
#  create table if not exists table_name (id integer primary key autoincrement, taskname text)
def create_table():
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer primary key autoincrement, taskname text)'
    cur.execute(sql)

# TODO: add data(todo) in table
# insert into table_name (column_name) values (column_values)
def add_todo(todo):
    cur.execute('INSERT INTO ' + table_name + ' (taskname) VALUES (?)', [todo] )
    print(f" {todo} added sccessfully")
    con.commit()

# TODO: Read data(todos) from table
# select * from table_name
# select column_name1, column_name2 from table_name   

def read_todos():
    cur.execute('SELECT * FROM ' + table_name)
    
    for row in cur.fetchall():
        print(f"{row[0]} --> {row[1]}")

# TODO: Update certain value(todo) in table
# update table_name set column_name=new_value where ID=index
def update_todo(idx, new_todo):
    cur.execute('UPDATE ' + table_name + ' SET taskname = (?) WHERE id = (?)', [new_todo, idx] )
    con.commit()
    print("TODO UPDATED SUCCESSFULLY !")

# TODO: Delete value(todo) from DB 
def delete_todo(idx):
    # delete from table_name where id = index
    pass

# TODO: closing the db connection
def close_connection():
    cur.close()
    con.close()