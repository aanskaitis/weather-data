import requests
import json
import logging
import time

logging.basicConfig(filename='warnings.log', format='%(asctime)s %(message)s', level=logging.WARNING)


def request_weather_data(city, api_key):
    attempts = 0

    while attempts < 3:
        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}'
            response = requests.get(url)
            response.raise_for_status()

            return json.loads(response.text)
        except requests.exceptions.ConnectionError as err_c:
            logging.warning(err_c)
            attempts += 1
            time.sleep(2)

        except requests.exceptions.HTTPError as err_h:
            logging.warning(err_h)
            print(f'HTTP error status code: {response.status_code}')
            attempts += 1
            time.sleep(2)

        except requests.exceptions.RequestException as err:
            raise err