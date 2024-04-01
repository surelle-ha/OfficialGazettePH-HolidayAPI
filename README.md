# README for Web Server API

## Project Overview

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

## Installation

First, ensure you have Python 3.x installed. Then, install the required packages using pip:

```bash
pip install Flask requests beautifulsoup4
```

## Usage

To start the web server, run the script:

```bash
python main.py
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
