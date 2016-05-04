'''
Created on Apr 28, 2016

@author: goodmaj1
'''
import pypyodbc as db

def main():
    
    connection = db.connect("Driver={SQL Server};" 
                            'Server=titan.csse.rose-hulman.edu;'
                            'Database=The_FOOOD;'
                            'uid=goodmaj1;pwd=left4226')
    cursor = connection.cursor() 
    SQLCommand = ("SELECT * "
                  "FROM Ingredient")
    cursor.execute(SQLCommand)
    results = cursor.fetchall()
    for answer in results:
        print(answer)
    connection.close()
    


if __name__ == '__main__':
    main()