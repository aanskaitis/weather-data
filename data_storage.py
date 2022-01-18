def insert_measurement(db, measurement):
    cursor = db.cursor()
    cursor.execute("INSERT INTO measurement (city_id, weather_id, lon, lat, datetime, temperature, pressure, humidity, "
                   "wind_speed, wind_direction, cloudiness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", measurement)
    db.commit()
