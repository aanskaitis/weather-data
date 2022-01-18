import mysql.connector
import getpass
import pandas as pd

password = getpass.getpass("pwd:")

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd=password,
   database="weather_db"
)

cursor = db.cursor()

# create database
# cursor.execute("CREATE DATABASE weather_db")

cursor.execute("CREATE TABLE country ("
               "id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
               "name VARCHAR(50) NOT NULL,"
               "capital VARCHAR(50),"
               "population int UNSIGNED,"
               "land_area int UNSIGNED)")

cursor.execute("CREATE TABLE city ("
               "id int UNSIGNED PRIMARY KEY NOT NULL,"
               "country_id int NOT NULL,"
               "name VARCHAR(50) NOT NULL,"
               "timezone int,"
               "FOREIGN KEY (country_id) REFERENCES country(id))")

cursor.execute("CREATE TABLE weather ("
               "id int UNSIGNED PRIMARY KEY NOT NULL,"
               "main VARCHAR(50) NOT NULL,"
               "description VARCHAR(255),"
               "icon_day VARCHAR(3),"
               "icon_night VARCHAR(3))")

cursor.execute("CREATE TABLE measurement ("
               "id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
               "city_id int UNSIGNED NOT NULL,"
               "weather_id int UNSIGNED,"
               "lon real NOT NULL,"
               "lat real NOT NULL,"
               "timestamp TIMESTAMP NOT NULL,"
               "temperature real NOT NULL,"
               "pressure int UNSIGNED,"
               "humidity int UNSIGNED,"
               "wind_speed int UNSIGNED,"
               "wind_direction VARCHAR(2),"
               "cloudiness int UNSIGNED,"
               "FOREIGN KEY (city_id) REFERENCES city(id),"
               "FOREIGN KEY (weather_id) REFERENCES weather(id))")


df_countries = pd.read_csv('data/countries.csv')
LT_country = df_countries[df_countries['country'] == 'Lithuania'].squeeze()
LV_country = df_countries[df_countries['country'] == 'Latvia'].squeeze()
EE_country = df_countries[df_countries['country'] == 'Estonia'].squeeze()

df_capitals = pd.read_csv('data/capitals.csv')
LT_capital = df_capitals[df_capitals['country'] == 'Lithuania'].squeeze()
LV_capital = df_capitals[df_capitals['country'] == 'Latvia'].squeeze()
EE_capital = df_capitals[df_capitals['country'] == 'Estonia'].squeeze()

countries_data = [
    ('Lithuania', LT_capital.capital_city, int(LT_country.population), int(LT_country.land_area)),
    ('Latvia', LV_capital.capital_city, int(LV_country.population), int(LV_country.land_area)),
    ('Estonia', EE_capital.capital_city, int(EE_country.population), int(EE_country.land_area)),
]

cursor.executemany("INSERT INTO country (name, capital, population, land_area) VALUES (%s, %s, %s, %s)", countries_data)

timezones = {
    'Vilnius': 7200,
    'Riga': 7200,
    'Tallinn': 7200
}

cities_data = [
    (593116, 1, 'Vilnius', timezones['Vilnius']),
    (456173, 2, 'Riga', timezones['Riga']),
    (588409, 3, 'Tallinn', timezones['Tallinn']),
]

cursor.executemany("INSERT INTO city (id, country_id, name, timezone) VALUES (%s, %s, %s, %s)", cities_data)

weather_data = [
    (200, 'Thunderstorm', 'thunderstorm with light rain', '11d', '11n'),
    (201, 'Thunderstorm', 'thunderstorm with rain', '11d', '11n'),
    (202, 'Thunderstorm', 'thunderstorm with heavy rain', '11d', '11n'),
    (210, 'Thunderstorm', 'light thunderstorm', '11d', '11n'),
    (211, 'Thunderstorm', 'thunderstorm', '11d', '11n'),
    (212, 'Thunderstorm', 'heavy thunderstorm', '11d', '11n'),
    (221, 'Thunderstorm', 'ragged thunderstorm', '11d', '11n'),
    (230, 'Thunderstorm', 'thunderstorm with light drizzle', '11d', '11n'),
    (231, 'Thunderstorm', 'thunderstorm with drizzle', '11d', '11n'),
    (232, 'Thunderstorm', 'thunderstorm with heavy drizzle', '11d', '11n'),
    (300, 'Drizzle', 'light intensity drizzle', '09d', '09n'),
    (301, 'Drizzle', 'drizzle', '09d', '09n'),
    (302, 'Drizzle', 'heavy intensity drizzle', '09d', '09n'),
    (310, 'Drizzle', 'light intensity drizzle rain', '09d', '09n'),
    (311, 'Drizzle', 'drizzle rain', '09d', '09n'),
    (312, 'Drizzle', 'heavy intensity drizzle rain', '09d', '09n'),
    (313, 'Drizzle', 'shower rain and drizzle', '09d', '09n'),
    (314, 'Drizzle', 'heavy shower rain and drizzle', '09d', '09n'),
    (321, 'Drizzle', 'shower drizzle', '09d', '09n'),
    (500, 'Rain', 'light rain', '10d', '10n'),
    (501, 'Rain', 'moderate rain', '10d', '10n'),
    (502, 'Rain', 'heavy intensity rain', '10d', '10n'),
    (503, 'Rain', 'very heavy rain', '10d', '10n'),
    (504, 'Rain', 'extreme rain', '10d', '10n'),
    (511, 'Rain', 'freezing rain', '13d', '13n'),
    (520, 'Rain', 'light intensity shower rain', '09d', '09n'),
    (521, 'Rain', 'shower rain', '09d', '09n'),
    (522, 'Rain', 'heavy intensity shower rain', '09d', '09n'),
    (531, 'Rain', 'ragged shower rain', '09d', '09n'),
    (600, 'Snow', 'light snow', '13d', '13n'),
    (601, 'Snow', 'snow', '13d', '13n'),
    (602, 'Snow', 'heavy snow', '13d', '13n'),
    (611, 'Snow', 'sleet', '13d', '13n'),
    (612, 'Snow', 'light shower sleet', '13d', '13n'),
    (613, 'Snow', 'shower sleet', '13d', '13n'),
    (615, 'Snow', 'light rain and snow', '13d', '13n'),
    (616, 'Snow', 'rain and snow', '13d', '13n'),
    (620, 'Snow', 'light shower snow', '13d', '13n'),
    (621, 'Snow', 'shower snow', '13d', '13n'),
    (622, 'Snow', 'heavy shower snow', '13d', '13n'),
    (701, 'Mist', 'mist', '50d', '50n'),
    (711, 'Smoke', 'smoke', '50d', '50n'),
    (721, 'Haze', 'haze', '50d', '50n'),
    (731, 'Dust', 'sand and dust whirls', '50d', '50n'),
    (741, 'Fog', 'fog', '50d', '50n'),
    (751, 'Sand', 'sand', '50d', '50n'),
    (761, 'Dust', 'dust', '50d', '50n'),
    (762, 'Ash', 'volcanic ash', '50d', '50n'),
    (771, 'Squall', 'squalls', '50d', '50n'),
    (781, 'Tornado', 'tornado', '50d', '50n'),
    (800, 'Clear', 'clear sky', '01d', '01n'),
    (801, 'Clouds', 'few clouds: 11-25%', '02d', '02n'),
    (802, 'Clouds', 'scattered clouds: 25-50%', '03d', '03n'),
    (803, 'Clouds', 'broken clouds: 51-84%', '04d', '04n'),
    (804, 'Clouds', 'overcast clouds: 85-100%', '04d', '04n'),
]

cursor.executemany("INSERT INTO weather (id, main, description, icon_day, icon_night) VALUES (%s, %s, %s, %s, %s)", weather_data)

db.commit()

