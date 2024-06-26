# Rain-Guard

Stay one step ahead of the weather with RainGuard – your personal rain alert app!
Rain Guard is a weather forecasting app designed to alert you when it's likely to rain. The app connects to the OpenWeatherMap API to retrieve weather data for a specific location. If rain is predicted, it sends you a reminder message using the Twilio API.

## Features

- Uses OpenWeatherMap API to fetch weather data.
- Automatically sends SMS reminders via Twilio API if rain is forecasted.
- Set a specific location for weather updates (currently set to a default location).

## Getting Started

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api). This will require signing up for a free account.

   - After signing up, naviagte to your profile and [generate](https://home.openweathermap.org/api_keys) a new API key
     ![API key](https://github.com/GameDevMitchell/Rain-Guard/assets/146736445/caa502cc-8f20-486c-a27e-8fd27686d7ee)
   - Copy your API key and replace it with the `api_key` in `main.py`

2. Sign up for a [Twilio](https://www.twilio.com/) account to get your Account SID, Auth Token, and to verify your real phone number.

   - To get your Account SID and Auth Token, log in to your Twilio account and navigate to the Dashboard.
   - To get a Twilio Virtual Number, navigate to the "Active Numbers" section on your Dashboard. If you don't have one yet, you can buy a number by clicking "Buy a Number".
   - To verify your real phone number, navigate to the "Verified CallER IDs" section on your Dashboard. Add your real phone number to the list of verified numbers.
   - ![Twilio](https://github.com/GameDevMitchell/Rain-Guard/assets/146736445/7cc29f89-2f5a-42c0-91b4-0f0113bb1dc0)

3. Update the `api_key`, `account_sid`, `auth_token`, `from_`, and `to` fields in the `main.py` file with the corresponding values you obtained from steps 1 and 2.

4. If you want to set your own location for weather updates, update the `MY_LAT` and `MY_LONG` variables in the `main.py` file with your desired latitude and longitude.

## Usage

1. Make sure Python is installed on your machine.

2. Install the required dependencies by running the following command in your terminal:

```sh

pip install requests twilio

```

3. Run the main.py script to start monitoring the weather:

```Sh

python main.py

```

4. If rain is predicted, you'll receive an SMS alert on the phone number you specified in the to field.<b>
   Never be caught off guard again and be ready for whatever Mother Nature has in store!
![rain-alert](https://github.com/GameDevMitchell/Rain-Guard/assets/146736445/7c5c36d3-4a68-415e-9365-7cc8e9c8eef6)

