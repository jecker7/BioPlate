from general_db import general_db



class create_plate_db(general_db):
        
    @property    
    @general_db.open_close(commit=True)
    def create_table(cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS plates (id integer primary key autoincrement, numWell integer, numColumns integer, numRows integer, surfWell real, volWell real, workVol real, refURL text)")
     
    @general_db.open_close(commit=True)   	
    def add_value(cursor, value):
        cursor.execute("INSERT INTO plates VALUES (Null,?,?,?,?,?,?,?) ", value) 

        
    @general_db.open_close(cursor=True)
    def get_by_numWell(cursor, numWell):
        cursor.execute('SELECT * FROM plates WHERE numWell=?', (numWell,)) 
        return cursor.fetchone() 
    
    @property
    @general_db.open_close(cursor=True)    
    def get_all(cursor):
        cursor.execute('SELECT * FROM plates')
        return cursor.fetchall()
        
    @general_db.open_close(commit=True)   
    def delete_by_id(cursor, id):
        cursor.execute('DELETE FROM plates WHERE id=?', (id,))
        
    @property
    @general_db.open_close(cursor=True)
    def get_column_name(cursor):
        curs = cursor.execute('SELECT * FROM plates WHERE id=0')
        names = [description[0] for description in curs.description]
        return names
    
        
    def get_dict(self, querys, key=False):
        names = self.get_column_name
        results = {}
        if isinstance(querys, list):
            for query in querys:
                if key == "numWell":
                    results[query[1]] = {}
                    dico = results[query[1]]
                else:
                    results[query[0]] = {}
                    dico = results[query[0]]
                for name, value in zip(names, query):
                    dico[name] = value
        elif isinstance(querys, tuple):
            for name, value in zip(names, querys):
                    results[name] = value
        else:
            print("This is not a proper object : " + querys) 
        return results       
            
    def add_column_text(self, name):
        self.c.execute('ALTER TABLE plates ADD COLUMN ? TEXT', (name,)) 
        self.conn.commit()
        
if __name__ == "__main__":
    #path = '/storage/emulated/0/qpython/projects3/BioPlate/database/plates.db'
    #path = os.path.join(sys.path[0], 'plates.db')
    Plates = create_plate_db('plates.db')
    Plates.close
    #Plates.create_table
    #Plates.add_value((96, 12, 8, 0.29, 200, 200, 'https://www.google.ca/url?sa=t&source=web&rct=j&url=http://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf&ved=0ahUKEwiEueSp8tnXAhXySd8KHd_ECXgQFgg1MAA&usg=AOvVaw2X9oIuhZs3izCw7OmvQE_f'))
    #Plates.add_value((6, 3, 2, 9.5, 2000, 2000,  ' https://www.google.ca/url?sa=t&source=web&rct=j&url=http://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf&ved=0ahUKEwiEueSp8tnXAhXySd8KHd_ECXgQFgg1MAA&usg=AOvVaw2X9oIuhZs3izCw7OmvQE_f'))
    #Plates.add_value((24, 6, 4, 0.33, 400, 400, 'https://www.google.ca/url?sa=t&source=web&rct=j&url=http://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf&ved=0ahUKEwiEueSp8tnXAhXySd8KHd_ECXgQFgg1MAA&usg=AOvVaw2X9oIuhZs3izCw7OmvQE_f'))
    #print(Plates.get_by_numWell(6))
    #Plates.delete_by_id(2)
    #print(Plates.get_all())
    #print(Plates.get_column_name)
    #Plates.add_column_text("refURL")
    #plate = Plates.get_dict(Plates.get_by_numWell(96))
    #print(plate['numWell'], plate['refURL']) 
    #print(Plates.get_by_numWell(24))
    #All = Plates.get_all
    well = Plates.get_by_numWell(96)
    #print(All)
    #print(Plates.get_column_name)
    print(Plates.get_dict(well , key="numWell"))
    #print(Plates.get_dict(Plates.get_by_numWell(24), key="numWell"))
        
        
        
    