import os
import requests
import pymysql
from datetime import datetime


def scrape_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/NGN'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rates = data['rates']

        return exchange_rates
    else:

        print('Failed to fetch exchange rate data:', response.status_code)
        return None
    


def update_database(exchange_rates):
    DB_HOST = os.environ.get("DB_HOST")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_DATABASE = os.environ.get("DB_DATABASE")
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM rates'
            cursor.execute(sql)
            sql1 = 'ALTER TABLE rates AUTO_INCREMENT = 1'
            cursor.execute(sql1)

            for currency, rate in exchange_rates.items():

                sql = 'INSERT INTO rates (currency_Code, Exchange_Rate, last_updated) VALUES (%s, %s, %s)'
                cursor.execute(sql, (currency, rate, datetime.now()))

        connection.commit()
        print('Rates updated successfully!')

    finally:
        
        connection.close()

# Main function
def main():
    
    exchange_rates = scrape_exchange_rates()

    if exchange_rates:
       
        update_database(exchange_rates)
    else:
        print('No exchange rate data available.')

if __name__ == '__main__':
    main()
