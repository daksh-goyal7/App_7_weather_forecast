import requests
API_KEY="ea251c322fa57a806df7d4f1e7fdfb65"
def get_data(place,forecast_days=None,kind=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list']
    nr_values=8*forecast_days
    filtered_data=filtered_data[:nr_values]
    return filtered_data
