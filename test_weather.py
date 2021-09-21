import requests
import pytest
import json
from pytest import mark


@pytest.fixture
def initial_url():
	url = 'http://api.openweathermap.org/data/2.5/forecast?appid=243ea0672b4a406837fa52e7564fb9b4'
	return url


@mark.parametrize("input_city",
	[('San Francisco'), ('New York'), ('London'), ('Sydney')])
def test_get_weather_by_city_name(input_city, initial_url):
	url = initial_url + '&q=' + input_city
	response = requests.get(url)
	assert response.status_code == 200
	response_body = response.json()
	assert response_body.get('city').get('name') == input_city


@mark.parametrize("input_lat, input_lon",
	[(37.7749, -122.4194), (-37.7749, 122.4194), (35, 139), (-55.5, -37.5)])
def test_get_weather_by_coordinates(input_lat, input_lon, initial_url):
	url = initial_url + '&lat=' + str(input_lat) + '&lon=' + str(input_lon)
	response = requests.get(url)
	assert response.status_code == 200
	response_body = response.json()
	assert response_body.get('city').get('coord').get("lat") == input_lat
	assert response_body.get('city').get('coord').get("lon") == input_lon


@mark.parametrize("input_zip, expected_city", 
	[(10007, 'New York'), (94105, 'San Francisco'),
	(94040, 'Mountain View'), (90808, 'Long Beach')])
def test_get_weather_by_zipcode(input_zip, expected_city, initial_url):	
	url = initial_url + '&zip=' + str(input_zip)
	response = requests.get(url)
	assert response.status_code == 200
	response_body = response.json()
	assert response_body.get('city').get('name') == expected_city
	