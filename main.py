import ETL
import getpass
import mysql.connector
import config
import time

password = getpass.getpass("pwd:")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database="weather_db"
)

cities = ['Vilnius', 'Riga', 'Tallinn']


def main():
    while True:
        ETL.run_pipeline_multiple_cities(cities, config.API_key, db)
        time.sleep(300)


if __name__ == "__main__":
    main()
