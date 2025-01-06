import requests
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_weather_data(latitude, longitude):
    # API URL de Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=auto"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos del clima: {response.status_code}")
        return None

def filter_weather_data(weather_data):
    # Obtener datos de temperatura y tiempo
    hourly_time = weather_data["hourly"]["time"]
    hourly_temp = weather_data["hourly"]["temperature_2m"]

    # Fecha de hoy y mañana
    today = datetime.now().date()
    tomorrow = today.replace(day=today.day + 1)

    # Filtrar temperaturas por fecha
    today_temps = []
    tomorrow_temps = []
    hours_today = []
    hours_tomorrow = []

    for time, temp in zip(hourly_time, hourly_temp):
        hour = datetime.fromisoformat(time)
        if hour.date() == today:
            today_temps.append(temp)
            hours_today.append(hour.strftime("%H:%M"))
        elif hour.date() == tomorrow:
            tomorrow_temps.append(temp)
            hours_tomorrow.append(hour.strftime("%H:%M"))

    return hours_today, today_temps, hours_tomorrow, tomorrow_temps

def plot_weather(hours_today, today_temps, hours_tomorrow, tomorrow_temps):
    plt.figure(figsize=(10, 6))
    
    # Graficar las temperaturas de hoy
    plt.plot(hours_today, today_temps, label="Hoy", marker="o", color="blue")
    
    # Graficar las temperaturas de mañana
    plt.plot(hours_tomorrow, tomorrow_temps, label="Mañana", marker="o", color="red")
    
    # Configuración del gráfico
    plt.title("Pronóstico de Temperatura: Hoy y Mañana")
    plt.xlabel("Hora")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    
    # Guardar el gráfico como imagen
    plt.tight_layout()
    plt.savefig("forecast.png")
    print("Gráfico generado: forecast.png")
    plt.show()

def main():
    # Coordenadas de la ubicación
    latitude = -33.215544441886905  # Latitud
    longitude = -70.66355361024546  # Longitud

    # Obtener datos del clima
    weather_data = fetch_weather_data(latitude, longitude)
    if weather_data is None:
        return

    # Filtrar los datos por hoy y mañana
    hours_today, today_temps, hours_tomorrow, tomorrow_temps = filter_weather_data(weather_data)

    # Graficar los datos
    plot_weather(hours_today, today_temps, hours_tomorrow, tomorrow_temps)

if __name__ == "__main__":
    main()