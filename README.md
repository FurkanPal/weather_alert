 # Weather Alert System with Twilio Integration

This script utilizes the OpenWeatherMap API to check if it will rain within the next 12 hours at a specific location. If rain is predicted, it sends an SMS alert using Twilio to a designated phone number.

## Prerequisites

Before using this script, make sure you have the following:

1. **accuweather API Key**: You need to sign up for an account on [accuweather](https://developer.accuweather.com/) to get an API key. This key allows you to access weather data.

2. **Twilio Account SID and Auth Token**: You must have a Twilio account ([Twilio](https://www.twilio.com/)) and obtain your Account SID and Auth Token from the Twilio dashboard.

3. **Python Libraries**:
    - `requests`: To make HTTP requests to the OpenWeatherMap API.
    - `twilio`: To interact with the Twilio API and send SMS messages.
4.  ****: will pull your location, by using this tool you will aggree to share your location.**
## Setup

1. **Clone or Download**: Clone the repository to your local machine.
   ```bash
    git clone <https://github.com/backQL/ForecastWarning>
    ```
2. **Install Dependencies**: Install the required Python libraries using pip:
    ```bash
    pip install requests twilio
    ```

3. **Environment Variables**:
    - Set environment variables for `api_key` (OpenWeatherMap API key) and `token` (Twilio Auth Token) in your operating system or in a `.env` file. This ensures sensitive information is not hardcoded in the script.

## Usage

Run the script `weather_alert.py` from the command line or your preferred Python environment:
```bash
python weather_alert.py
```

## Script Overview

- **AccuWeather API Endpoint**: The script uses the forecast API endpoint (`http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location}`) to fetch weather data for a specific location.

- **Twilio Integration**: If rain is predicted within the next 12 hours, the script sends an SMS alert using Twilio. Ensure you have sufficient Twilio credits or balance to send SMS messages.

- **Nominatim Api**: This api will pull your location `query_params` dictionary to specify the location to check the weather where ever you are. You can also adjust other parameters such as `exclude` to include or exclude specific weather data (e.g., current weather, minutely forecast, daily forecast).


## Customization

- **SMS Message Content**: Customize the message content sent via SMS by modifying the `body` parameter in the Twilio `client.messages.create()` method.

- **Phone Numbers**: Replace the placeholder phone numbers (`from_` and `to`) with your actual Twilio phone number and the recipient's phone number.

## Notes

- **Rate Limits**: Be mindful of rate limits imposed by the AccuWeather API and Twilio to avoid exceeding usage limits.

- **Cost Considerations**: Check the pricing plans for both AccuWeather and Twilio, as excessive usage may incur costs.
