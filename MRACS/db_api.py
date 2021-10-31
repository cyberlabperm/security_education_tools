import configparser
import sqlite3

def connect_to_db(path, type):
    if type == 'sqlite3':
        db = sqlite3.connect(path)
        return db   

def do_schema(template, type):    
    if type == 'CREATE':
        pattern = '{} TEXT'
    elif type == 'INSERT':
        pattern = '{}'
    elif type == 'VALUES':
        pattern = "'{}'"
    schema = ''
    for i in range(0, len(template)):
        if i == 0:
            schema += pattern
        else:
            schema +=', ' + pattern 
    return schema 

def delete_table(db, table_name):
    db.cursor().execute(f'DELETE TABLE {table_name}')
    db.commit()

def create_table(db, table_name, template):    
    schema = do_schema(template, 'CREATE').format(*template)
    db.cursor().execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
    db.commit()

def select_all_from_table(db, table, where=''):
    if len(where) == 0:
        data = db.cursor().execute(f'SELECT * FROM {table};').fetchall() 
    else:
        data = db.cursor().execute(f'SELECT * FROM {table} WHERE {where};').fetchall() 
    return data

def select_item_from_table(db, table, key, where=''):
    db.row_factory = lambda cursor, row: row[0]        
    if len(where) == 0:
        dbreq = f'SELECT {key} FROM {table};'
    else:       
        dbreq = f'SELECT {key} FROM {table} WHERE {where};'
    print(dbreq)    
    data = db.cursor().execute(dbreq).fetchone()    
    return data

def insert_data(db, table, template, values):
    if len(template) != len(values):
        print('Error: Data is not suitable for this template. Operation aborted')
    else:
        schema = do_schema(template,'INSERT').format(*template)
        data = do_schema(values, 'VALUES').format(*values)
        db.cursor().execute(f"INSERT INTO {table} ({schema}) VALUES ({data});")
        db.commit()    

def delete_data(db, table, where):
    db.cursor().execute(f'DELETE FROM {table} WHERE {where}')
    db.commit()

class users_db:
    template = ('login', 'password')

class DAC:
    template = ('path', 'user', 'actions')

class RBAC:
    object_template = ('path', 'roles')
    subject_template = ('user', 'group')

class MAC:
    object_template = ('object', 'class')
    subject_template = ('user', 'admission')
    security_class = ('none', 'basic', 'secret', 'top_secret')
    admission_levels = ('none', 'basic', 'advanced', 'full')
 


