import sys
import requests
import logging

logging.basicConfig(filename="health.log",level=logging.INFO,
                    format="%(asctime)s - %(message)s" )

url = sys.argv[1]
try:
    response = requests.get(url,timeout=5)
    logging.info(f"{url} is UP - status {response.status_code}")
    print(response.status_code)
except Exception as e:
    logging.info(f"{url} is DOWN - {e}")
    print("DOWN:", e)
    