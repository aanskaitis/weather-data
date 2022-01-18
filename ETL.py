import data_extraction, data_transform, data_storage


def run_pipeline(city, api_key, db):
    response = data_extraction.request_weather_data(city, api_key)
    measurement = data_transform.json_response_to_measurement(response)
    data_storage.insert_measurement(db, measurement)


def run_pipeline_multiple_cities(cities, api_key, db):
    for city in cities:
        run_pipeline(city, api_key, db)
