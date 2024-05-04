# Rain-Guard

Stay one step ahead of the weather with RainGuard – your personal rain alert app!

# Rain Guard App

Rain Guard is a weather forecasting app designed to alert you when it's likely to rain. The app connects to the OpenWeatherMap API to retrieve weather data for a specific location. If rain is predicted, it sends you a reminder message using the Twilio API.

## Features

- Uses OpenWeatherMap API to fetch weather data.
- Automatically sends SMS reminders via Twilio API if rain is forecasted.
- Set a specific location for weather updates (currently set to a default location).

## Getting Started

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api). This will require signing up for a free account.

2. Sign up for a [Twilio](https://www.twilio.com/) account to get your Account SID, Auth Token, and to verify your real phone number.

   - To get your Account SID and Auth Token, log in to your Twilio account and navigate to the Dashboard.
   - To get a Twilio Virtual Number, navigate to the "Active Numbers" section on your Dashboard. If you don't have one yet, you can buy a number by clicking "Buy a Number".
   - To verify your real phone number, navigate to the "Verified CallER IDs" section on your Dashboard. Add your real phone number to the list of verified numbers.

3. Update the `api_key`, `account_sid`, `auth_token`, `from_`, and `to` fields in the `main.py` file with the corresponding values you obtained from steps 1 and 2.

4. If you want to set your own location for weather updates, update the `MY_LAT` and `MY_LONG` variables in the `main.py` file with your desired latitude and longitude.

## Usage

1. Make sure Python is installed on your machine.

2. Install the required dependencies by running the following command in your terminal:

```sh

pip install requests twilio vonage

```
