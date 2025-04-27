### BY TAHA ###
import requests
from concurrent.futures import ThreadPoolExecutor

much = 7

url = "YOUR_END_POINT"

data = {
    'correction_point': '1',
    'commit': 'Donate'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Content-Type": "application/x-www-form-urlencoded",
}

cookies = {
    "_intra_42_session_production": "YOUR_SESSION_ID",
}

def send_post():
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    print(f"status : {response.status_code}")

with ThreadPoolExecutor(max_workers=much) as executor:
    futures = [executor.submit(send_post) for _ in range(much)]
