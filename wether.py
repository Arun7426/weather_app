import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            print(f"Weather in {city}: {description.capitalize()}, Temperature: {temperature}°C")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = '6ac51341fbe25af0043f9a7e166961c4'
    city = input("Enter the city name or ZIP code: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
