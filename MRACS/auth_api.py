import rsa
import db_api

class authenticator():
    def __init__(self, path, db_type, table):
        self.path = path
        self.table = table
        self.db_type = db_type
        self.db = db_api.connect_to_db(self.path, self.db_type)    

#default PAP    
    def pap(self, login, password):
        print(f'Checking login={login} with password={password}')
        check = db_api.select_item_from_table(self.db, self.table, 'password', f'login="{login}"')
        if check != None:        
            if password == check:
                status, message =True, 'Authentication succeeded (password)'            
            else:
                status, message = False, "ERROR"            
        else:
           status, message = False, "Error"            
        return status, message

#weakness "none" 
    def pap_hash_md5(self, login, hash):        
        print(f'Checking login={login} with hashed_password={hash}')
        check = db_api.select_item_from_table(self.db, self.table, 'password', f'login="{login}"')
        if hash == check:
            print('Authentication succeeded (password)')
            return True
        else:
            return False

    def chap(self, login, password):
        return False
    
    def rsa_auth(self, login, pubkey):
        return False


