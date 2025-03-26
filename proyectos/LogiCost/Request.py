import requests
from bs4 import BeautifulSoup

url = "https://www.globalpetrolprices.com/Ecuador/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_fuel_price():   
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for the first table on the page
        tables = soup.find_all('table')
        
        if not tables:
            print("No tables found.")
        else:
            fuel_table = tables[0]  # First table: fuel prices

            rows = fuel_table.find('tbody').find_all('tr')
            # print(rows)
            second_row = rows[1]  # Index starts at 0, so this is the second row
            cols = second_row.find_all(['th', 'td'])

            # Extract info from the columns
            label = cols[0].text.strip()
            date = cols[1].text.strip()
            price_usd = cols[2].text.strip()

            return float(price_usd)/0.264172

    else:
        print("Failed to load page:", response.status_code)