import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

# OpenWeatherMap API Configuration
API_KEY = "282737c7d1d84b4b2f03c58da2e55060"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch Data from API
response = requests.get(URL)
weather_data = response.json()

# Extract Data for Visualization
dates = []
temps = []

for forecast in weather_data["list"]:
    dates.append(forecast["dt_txt"])  # Timestamp
    temps.append(forecast["main"]["temp"])  # Temperature

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker="o", color="b")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Forecast for {CITY}")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
