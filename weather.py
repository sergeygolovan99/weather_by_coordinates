import urllib.request
import json
import requests


#Open Weather Map API

def kelvin_to_celsius(temp):
	return temp - 273.15

def get_tempreture(longitude, latitude):
	url = "https://community-open-weather-map.p.rapidapi.com/weather"
	querystring = {"lon": longitude, "lat": latitude, "lang": "Russian"}
	headers = {
    	'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    	'x-rapidapi-key': "04b860f163msh2e2362261d8a46fp14775bjsnc3397c507230"
    }


	response = requests.request("GET", url, headers=headers, params=querystring)


	current_tempreture =  kelvin_to_celsius(response.json()["main"]["temp"])
	feels_like = kelvin_to_celsius(response.json()["main"]["feels_like"])
	print(f'Current_tempreture: {current_tempreture:.2f}')
	print(f'Feels like: {feels_like:.2f}')
	return (current_tempreture, feels_like)



longitude = float(input())
latitude = float(input())


cur, fl = get_tempreture(longitude, latitude)
