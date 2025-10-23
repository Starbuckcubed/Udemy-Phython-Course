import requests


country = input("Type a country name and press enter for more information about the country: ")
#if they don't enter anything, keep asking
if not country.strip():
    print("You must enter a country name to get information.")
    country = input("Type a country name and press enter for more information about the country: ")

url = f'https://restcountries.com/v3.1/name/{country}'

response = requests.get(url)
data = response.json()

events = data[0]

# Extracting and printing various country info such as name, capital, etc.
print(f"Country: {events['name']['common']}")
print(f"Capital: {events['capital'][0]}")
print(f"Region: {events['region']}")
print(f"Population: {events['population']}")    
print(f"Area: {events['area']} km²")
print(f"Timezones: {', '.join(events['timezones'])}")
print(f"Currencies: {', '.join([currency['name'] for currency in events['currencies'].values()])}")
print(f"Languages: {', '.join(events['languages'].values())}")  

# The empty input check is now done before making the API request.