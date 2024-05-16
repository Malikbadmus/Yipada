import os
import mysql.connector
import pycountry

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

try:
    with connection.cursor() as cursor:
        
        sql_commands = [
            "DELETE FROM rates WHERE Id = 128",
            "UPDATE rates SET Currency = 'Tuvaluan dollar' WHERE Id = 143",
            "UPDATE rates SET Currency = 'Guernsey Pound' WHERE Id = 50",
            "UPDATE rates SET Currency = 'Manx Pound' WHERE Id = 64",
            "UPDATE rates SET Currency = 'Jersey Pound' WHERE Id = 69",
            "UPDATE rates SET Currency = 'Kiribati dollar' WHERE Id = 76",
            "UPDATE rates SET Currency = 'Faroese Krona' WHERE Id = 47"
        ]

        
        for command in sql_commands:
            cursor.execute(command)

    
    connection.commit()
    print('SQL commands executed successfully!')

finally:
   
    connection.close()
