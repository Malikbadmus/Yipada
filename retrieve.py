import os
import mysql.connector
import pycountry

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = conn.cursor()

cursor.execute("SELECT DISTINCT Currency_code FROM rates")
currency_codes = cursor.fetchall()

# Iterate through each currency code
for (Currency_code,) in currency_codes:

    try:
        country = pycountry.countries.get(alpha_3=Currency_code)
        currency = pycountry.currencies.get(alpha_3=Currency_code)
        
        if country:
            country_name = country.name
            country_code = country.alpha_2
        else:
            country_name = None
            country_code = None
        
        if currency:
            currency_name = currency.name
        else:
            currency_name = None

        print(f"Currency Code: {Currency_code}, Country Name: {country_name}, Country Code: {country_code}, Currency Name: {currency_name}")
        
    except Exception as e:
        print(f"Error retrieving data for Currency Code: {Currency_code}. Error: {e}")
        country_name = None
        country_code = None
        currency_name = None

    update_query = "UPDATE rates SET Country = %s, Country_Code = %s, Currency = %s WHERE Currency_code = %s"
    cursor.execute(update_query, (country_name, country_code, currency_name, Currency_code))
    conn.commit()
    
cursor.close()
conn.close()
