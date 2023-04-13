import requests
from flight_data import FlightData
from pprint import pprint
from dotenv.main import load_dotenv
import os

load_dotenv()
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
tequila_api_key = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_name):
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": tequila_api_key}
        for city in city_name:
            query = {"term": city_name, "location_type": "city"}
            response = requests.get(url=location_endpoint, params=query, headers=headers)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": tequila_api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            params=query,
            headers=headers
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                departure_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                departure_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            # print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
