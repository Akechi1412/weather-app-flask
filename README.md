# Weather App using Python Flask and Jinja2

This is a simple weather app implemented in Python using the Flask web framework and Jinja2 templating engine.

## Features

- Display current weather information and a 4-5 day weather forecast based on the current location.
- Display current weather information and a 4-5 day weather forecast for a specific city.
- Responsive design for a better user experience.

## Prerequisites

Make sure you have the following installed before running the app:

- Python 3.6 or higher
- API Key from [OpenWeather](https://home.openweathermap.org/api_keys)
- Flask
- [Other dependencies, if any]

## Getting Started with Virtual Environment

1. Clone the repository:

```bash
   git clone https://github.com/Akechi1412/weather-app-flask.git
   cd weather-app-flask
```

2. Create a file named `local_settings.py` and copy the following code:

```python
  API_KEY = "Your API Key"
```

3. Create and activate a virtual environment:

- For Window

```bash
  py -3 -m venv .venv
  .venv\Scripts\activate
```

- For MacOs/Linux

```bash
  python3 -m venv .venv
  . .venv/bin/activate
```

4. Install dependencies:

```bash
  pip install -r requirements.txt
```

5. Run the application.

```bash
  python main.py
```

6. Open your web browser and navigate to http://localhost:5000 to view the app.

Remember to deactivate the virtual environment after you're done:

```bash
  deactivate
```

This ensures that your dependencies are contained within the virtual environment and don't interfere with your system-wide Python installation.
