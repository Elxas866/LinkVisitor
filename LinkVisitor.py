import sys
import selenium, selenium.webdriver
from selenium.webdriver.chrome.options import Options
import random
import requests


def open_url_with_proxy(url, proxy_address):
    """Öffnet eine URL mit dem angegebenen Proxy."""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Browser im Hintergrund
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--proxy-server={proxy_address}')

    try:
        driver = selenium.webdriver.Chrome(
            options=chrome_options
        )

        driver.get(url)
        print(f"Opened {url} with proxy {proxy_address}")
        driver.quit()
    except Exception as e:
        print(f"Could not open {url} with proxy {proxy_address}")
        pass




if (len(sys.argv) < 3):
    print("Usage: python LinkVisitor.py <link> <number_of_iterations>")
    sys.exit(1)

link = sys.argv[1]
x = int(sys.argv[2])

for i in range(x):
    proxy_addresses = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit={x}&page=1&sort_by=lastChecked&sort_type=desc').json()['data']
    proxy_address = proxy_addresses[i]['ip'] + ":" + proxy_addresses[i]['port']
    print(f"Trying proxy {proxy_address}")
    open_url_with_proxy(link, proxy_address)
    print("Iteration " + str(i) + " done.")