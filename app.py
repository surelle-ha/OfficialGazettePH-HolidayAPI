from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import time
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/holidays', methods=['GET'])
@app.route('/holidays/<int:year>', methods=['GET'])
def get_holidays(year=datetime.now().year):
    start_time = time.time()

    url = f'https://www.officialgazette.gov.ph/nationwide-holidays/{year}/'
    domain = url.split("//")[-1].split("/")[0]
    
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        return jsonify({'error': 'Failed to resolve domain name'})

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.ConnectionError:
        return jsonify({'error': 'Failed to connect to the source URL'})
    except requests.Timeout:
        return jsonify({'error': 'Request to the source URL timed out'})
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {e}'})

    if response.status_code != 200:
        return jsonify({'error': f'Failed to retrieve data, status code: {response.status_code}'})

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        holidays = []

        tables = soup.find_all("table")
        for i, table in enumerate(tables):
            holiday_type = "Regular Holidays" if i == 0 else "Special (Non-Working) Holidays"
            rows = table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                event = cols[0].get_text(strip=True)
                date = cols[1].get_text(strip=True)
                holidays.append({'event': event, 'date': date, 'type': holiday_type})

    except Exception as e:
        return jsonify({'error': f'Error processing HTML content: {e}'})

    response_time = time.time() - start_time
    return jsonify({
        'request_timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
        'response_duration_seconds': round(response_time, 2),
        'source_url': url,
        'source_ip': ip_address,
        'number_of_holidays': len(holidays),
        'holidays': holidays
    })

if __name__ == '__main__':
    app.run(debug=True)
