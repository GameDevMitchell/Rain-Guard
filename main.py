import requests
from twilio.rest import Client

api_key = "__YOUR_OWM_API_KEY__"
account_sid = "YOUR_TWILIO_ACCOUNT_ID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

MY_LAT = 35.185566  # you can replace with your own latitudes and longitudes
MY_LONG = 33.382275

parameters = {"lat": MY_LAT, "lon": MY_LONG, "appid": api_key, "cnt": 4}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
response.raise_for_status()
data = response.json()
weather_list = data["list"]


description_list = []
for number in range(len(weather_list)):
    info = weather_list[number]["weather"][0]["description"]
    description_list.append(info)

id_list = []
for number in range(len(weather_list)):
    data = weather_list[number]["weather"][0]["id"]
    id_list.append(data)
print(id_list)

# id_dictionary = {}
# for number in range(len(id_list)):
#     id_dictionary[f"{id_list[number]}"] = description_list[number]

will_rain = False
for number in id_list:
    if int(number) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="YOUR_TWILIO_VIRTUAL_NUMBER",
        body="It's going to rain today! Remember to bring an Umbrella ☂️.If you don't have one, get one. "
        "You can also get a raincoat if you want. Just make sure you're prepared!",
        to="YOUR_TWILIO_VERIFIED_REAL_NUMBER",
    )

    print(message.sid)
