# Weather API Wrapper Service

A simple Django REST API that fetches current weather data from the [WeatherAPI](https://www.weatherapi.com/) and caches responses using Redis for better performance. 

## Features

- Uses environment variables for API key security
- In-memory caching with Redis (12h expiry)
- Clean architecture (`services.py` separation)
- Query-based endpoint (example: `?city=izmir`)
- Ready for testing, Dockerization & deployment

---

## How to Run

### 1. Clone the repo

```bash
git clone https://github.com/mcanktc/Weather-API-Wrapper-Service.git
cd weather-api-wrapper
````


```bash
python -m venv env
source env/bin/activate  
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
WEATHER_API_KEY=your_real_api_key_here
```

### 4. Run Redis server

> Make sure Redis is installed and running on default port `6379`

### 5. Run the server

```bash
python manage.py runserver
```

---

## API Endpoint

| Method | Endpoint | Description                      | Query Param   | Response Type |
| ------ | -------- | -------------------------------- | ------------- | ------------- |
| GET    | `/`      | Get current weather data by city | `?city=izmir` | JSON          |

**Example Request:**

```
GET http://127.0.0.1:8000/?city=izmir
```

**Example Response:**

```json
{
  "city": "Izmir",
  "country": "Turkey",
  "temperature": 36.0,
  "condition": "Sunny",
  "icon": "https://cdn.weatherapi.com/weather/64x64/day/113.png"
}
```


