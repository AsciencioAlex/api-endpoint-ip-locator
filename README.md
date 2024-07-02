# Flask API on Vercel

This project is a simple Flask application that exposes an API endpoint to greet visitors. The application is deployed on Vercel.

## Project Structure

- `app.py`: The main Flask application file.
- `requirements.txt`: A list of Python dependencies.
- `runtime.txt`: Specifies the Python version to be used.
- `vercel.json`: Vercel configuration file.

## API Endpoint

- `GET /api/hello?visitor_name=<Alex>`

### Response

```json
{
  "client_ip": "127.0.0.1",
  "location": "Nairobi",
  "greeting": "Hello, Alex!, the temperature is 11 degrees Celsius in Nairobi"
}
