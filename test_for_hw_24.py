import requests


def test_first():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'regex',
        'value1': 'images/\\w+\\.png'
    }

    response = requests.request("POST", url, json=payload)
    assert response.status_code == 200
    assert '100.43.83.137' in response.text
