from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location_and_temperature(ip):
    # Dummy data for example purposes
    location = "Nairobi"
    temperature = 11  # degrees Celsius
    return location, temperature

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr
    location, temperature = get_location_and_temperature(client_ip)
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
