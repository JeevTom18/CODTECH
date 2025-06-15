import requests
import matplotlib.pyplot as plt
import datetime

# Replace with your actual OpenWeatherMap API key
API_KEY = "a8e93991aeb8f0c257842c94cd784bbb"
CITY = "Chennai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = []
temps = []
humidities = []

# Extract data for every 3-hour interval
for entry in data["list"]:
    dt = datetime.datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
    temp = entry["main"]["temp"]
    humidity = entry["main"]["humidity"]
    
    dates.append(dt)
    temps.append(temp)
    humidities.append(humidity)

# Create plot
plt.figure(figsize=(12, 6))

# Temperature plot
plt.plot(dates, temps, label="Temperature (°C)", color="orange", marker='o')
# Humidity plot
plt.plot(dates, humidities, label="Humidity (%)", color="blue", linestyle='--', marker='x')

plt.xlabel("Date and Time")
plt.ylabel("Values")
plt.title(f"5-Day Weather Forecast for {CITY}")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)

plt.savefig("weather_dashboard.png")
plt.show()
