
import pip._vendor .requests as req

def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid=b6907d289e10d714a6e88b30761fae22"
    response = req.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please check your internet connection or try again later.")
        return None

def get_temperature(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['temp']
    return None

def get_wind_speed(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['wind']['speed']
    return None

def get_pressure(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['pressure']
    return None

if __name__ == "__main__":
    city = "London,us"
    data = get_weather_data(city)

    if data is not None:
        while True:
            print("\nMenu:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                date = input("Enter the date (yyyy-mm-dd): ")
                temperature = get_temperature(data, date)
                if temperature is not None:
                    print(f"The temperature on {date} in {city} is {temperature} °C")
                else:
                    print(f"Data not available for {date}")

            elif choice == "2":
                date = input("Enter the date (yyyy-mm-dd): ")
                wind_speed = get_wind_speed(data, date)
                if wind_speed is not None:
                    print(f"The wind speed on {date} in {city} is {wind_speed} m/s")
                else:
                    print(f"Data not available for {date}")

            elif choice == "3":
                date = input("Enter the date (yyyy-mm-dd): ")
                pressure = get_pressure(data, date)
                if pressure is not None:
                    print(f"The pressure on {date} in {city} is {pressure} hPa")
                else:
                    print(f"Data not available for {date}")

            elif choice == "0":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
