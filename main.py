import ETL
import mysql.connector
import config
import time


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config.pwd,
    database="weather_db"
)

cities = ['Vilnius', 'Riga', 'Tallinn']


def main():
    while True:
        ETL.run_pipeline_multiple_cities(cities, config.API_key, db)
        time.sleep(600)


if __name__ == "__main__":
    main()
