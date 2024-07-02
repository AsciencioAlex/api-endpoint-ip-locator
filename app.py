from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = 'InsertYourWeatherApiKey'

def get_client_ip():
    # Get the real IP address from the headers
    if request.headers.get('X-Forwarded-For'):
        client_ip = request.headers['X-Forwarded-For'].split(',')[0]
    else:
        client_ip = request.remote_addr
    return client_ip

def get_location_and_temperature(ip):
    if ip == "127.0.0.1":
        ip = "8.8.8.8"  # Use a known public IP address for local testing

    # Use ipinfo.io to get location based on IP
    ip_info_url = f'http://ipinfo.io/{ip}/json'
    print(f"Fetching location for IP: {ip}")
    ip_info_response = requests.get(ip_info_url)
    
    if ip_info_response.status_code != 200:
        print(f"Failed to get location data for IP: {ip}, Status Code: {ip_info_response.status_code}")
        print(f"Response: {ip_info_response.text}")
        return "Unknown", None

    ip_info = ip_info_response.json()
    print(f"IP Info: {ip_info}")

    location = ip_info.get('city', 'Unknown')
    if location == 'Unknown':
        print(f"Could not determine the city from IP info: {ip_info}")
        return location, None

    # Use OpenWeatherMap API to get the current temperature
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_response.status_code != 200 or 'main' not in weather_data:
        print(f"Failed to get weather data for location: {location}, Status Code: {weather_response.status_code}, Data: {weather_data}")
        return location, None

    temperature = weather_data['main']['temp']
    return location, temperature

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = get_client_ip()
    print(f"Client IP: {client_ip}")
    
    location, temperature = get_location_and_temperature(client_ip)
    if temperature is None:
        greeting = f"Hello, {visitor_name}!, but we couldn't determine the temperature in {location}"
    else:
        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
