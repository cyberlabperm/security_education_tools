import db_api

class DAC_PDP():
    def __init__(self, path, db_type, table):
        self.path = path
        self.table = table
        self.db_type = db_type
        self.db = db_api.connect_to_db(self.path, self.db_type)        

    def check(self, path, user, req):
        check = db_api.select_item_from_table(self.db, self.table, 'actions', where=f'path="{path}" AND user="{user}"')        
        if check == None:
            return False
        else:            
            if req in check:
                return True
            else:
                return False      
    
class MAC_PDP():
    def __init__(self, db_address, db_type, table_object, table_subject):
        self.path = db_address
        self.table_objects = table_object
        self.table_subject = table_subject
        self.db_type = db_type
        self.db = db_api.connect_to_db(self.path, self.db_type) 

    def check(self, object, user, action):
        obj_class = db_api.select_item_from_table(self.db, self.table_objects,'class', where=f'object="{object}"' )
        admission = db_api.select_item_from_table(self.db, self.table_subject, 'admission', where=f'user="{user}"')
        iso = db_api.MAC.security_class.index(obj_class)
        iss = db_api.MAC.admission_levels.index(admission)
        if obj_class or admission == None:
            return False
        if iss >= iso and action == 'r':
            return True
        elif iss <= iso and action =='w':
            return True
        else:
            return False

class RBAC_PDP():
    def __init__(self) -> None:
        pass    
    def RBAC(object, user, action):
        return False


