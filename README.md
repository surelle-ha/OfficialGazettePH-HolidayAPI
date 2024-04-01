# Official Gazette PH Holiday API

This is a Python-based web server API developed using Flask. It's designed to scrape data about nationwide holidays from the "Official Gazette" website of the Philippines for the current year and return this information in a JSON format.

## Features

- Scraping holiday data from a specified URL.
- Categorization of holidays into 'Regular' and 'Special (Non-Working)'.
- Returning detailed JSON responses including event names, dates, and types.
- Performance metrics such as request timestamp and response duration.
- Error handling for unsuccessful data retrieval.

## Requirements

- Python 3.x
- Flask
- Requests
- BeautifulSoup4

## Deployment

### Tunnel Local via Ngrok (Optional)

Ngrok is a cross-platform tool that creates secure tunnels between your local development server and the internet, allowing you to expose locally hosted services to the web. It’s often used for testing and development purposes.

##### 1. Download Ngrok

[![Ngrok](https://img.shields.io/badge/Ngrok-purple?style=for-the-badge&logo=ngrok)](https://ngrok.com/download)

##### 2. Register and get your Auth token

##### 3. Run this script on your Ngrok directory.

    ngrok config add-authtoken <token>

##### 4. Start a tunnel

    ngrok http <port>

### Or Deploy via Render (Optional)

Create an account on Render and setup environment variable before you click the button below.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/surelle-ha/OfficialGazettePH-HolidayAPI.git)

## Local Installation

First, ensure you have Python 3.x installed. Then, clone the repository from Github.

```git
git clone https://github.com/surelle-ha/OfficialGazettePH-HolidayAPI.git
```

Next, install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To start the web server, run the script:

```bash
python app.py
```

Once the server is running, you can access the API endpoint /holidays via a GET request to receive the current year's holiday data.

### Example Request:

```bash
GET /holidays
```

### Response Structure:

```json
{
  "request_timestamp": "YYYY-MM-DD HH:MM:SS",
  "response_duration_seconds": X.XX,
  "source_url": "URL",
  "source_ip": "IP Address",
  "number_of_holidays": X,
  "holidays": [
    {
      "event": "Event Name",
      "date": "YYYY-MM-DD",
      "type": "Holiday Type"
    },
    ...
  ]
}
```

## Configuration

- The target URL for scraping is set to the Official Gazette's holiday page for the current year.
- The Flask app runs in debug mode by default.

## Notes

- The web server scrapes data in real-time; response times may vary based on network conditions and the source website's response time.
- This web server scrapes data from [Philippine Official Gazette](https://www.officialgazette.gov.ph/nationwide-holidays/)
