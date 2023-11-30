import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect
from local_settings import API_KEY

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', status_code=200);

@app.route('/city', methods=('GET', 'POST'))
def getCityWeather():
	if request.method == 'GET':
		return redirect('/')
	cityName = request.form['city']
	if cityName.strip() == '':
		return redirect('/')
	statusCode, currentData, forecastData = getWeatherByCityName(cityName)
	return render_template('index.html', status_code=statusCode, 
												current_data=currentData, forecast_data=forecastData, city=cityName)

@app.route('/current-location', methods=('GET', 'POST'))
def getCurrentLocationWeather():
	if request.method == 'GET':
		return redirect('/')
	lat = request.form['latitude']
	lon = request.form['longitude']
	# print(f"lat = {lat}\tlon = {lon}")
	cityName = getCityName(lat, lon)
	statusCode, currentData, forecastData = getWeatherByCityName(cityName)
	return render_template('index.html', status_code=statusCode, 
												current_data=currentData, forecast_data=forecastData)

def formatDate(timestamp, timezone):
	return datetime.utcfromtimestamp(timestamp + timezone).strftime('%A')

def formatTime(timestamp, timezone):
	return datetime.utcfromtimestamp(timestamp + timezone).strftime('%H:%M')

def getCityName(lat, lon):
	url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}"
	response = requests.get(url)
	cityName = " "
	if response.status_code == 200:
		cityData = response.json()
		cityName = cityData[0]['name']
	return cityName

def getWeatherByCityName(cityName):
	url = f'https://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={API_KEY}&units=metric&lang=vi'
	response = requests.get(url)
	statusCode = response.status_code
	currentData = None
	forecastData = None
	if (response.status_code == 200):
		weatherData = response.json()
		fiveDaysForecast = []
		fiveDaysForecast.append(weatherData['list'][0]);
		fiveDaysForecast.append(weatherData['list'][8])
		fiveDaysForecast.append(weatherData['list'][16])
		fiveDaysForecast.append(weatherData['list'][24])
		fiveDaysForecast.append(weatherData['list'][32])
		fiveDaysForecast.append(weatherData['list'][39])
		# print(formatTime(weatherData['list'][0]['dt'], weatherData['city']['timezone']))
		previousDate = None
		for item in fiveDaysForecast[:]:
			currentDate = formatDate(item['dt'], weatherData['city']['timezone'])
			if currentDate != previousDate:
				item['formated_date'] = currentDate
			else:
				fiveDaysForecast.remove(item)
			previousDate = currentDate
		currentData = fiveDaysForecast[:1][0]
		forecastData = fiveDaysForecast[1:]
		currentData['name'] = weatherData['city']['name']
		currentData['timezone'] = weatherData['city']['timezone']
		currentData['sunrise'] = formatTime(weatherData['city']['sunrise'], currentData['timezone'])
		currentData['sunset'] = formatTime(weatherData['city']['sunset'], currentData['timezone'])
	return statusCode, currentData, forecastData

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)
