from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Correct path and use Service with Edge
edge_driver_path = r'edgedriver_win64/msedgedriver.exe'
service = Service(edge_driver_path)

# Create a new Edge WebDriver instance
browser = webdriver.Edge(service=service)

# Login telegram by QR
url = "https://web.telegram.org/"
browser.get(url)

# Wait for 20 seconds
time.sleep(20)
import asyncio
import websockets
import json
import re
import requests
import pandas as pd
import requests
from bs4 import BeautifulSoup
# import testbeatifullsoup4
from testbeatifullsoup4 import scraplink

# Function to get SOL to USD conversion rate
def get_sol_to_usd_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        sol_price_in_usd = data['solana']['usd']
        return sol_price_in_usd
    else:
        print("Failed to retrieve data")
        return None

async def subscribe_to_new_tokens(websocket):
    # Subscribing to token creation events
    payload = {
        "method": "subscribeNewToken",
    }
    await websocket.send(json.dumps(payload))

    # Get the current SOL to USD price
    sol_to_usd = get_sol_to_usd_price()
    i = 1
    # Continuously receive messages from the websocket
    async for message in websocket:
        data = json.loads(message)
        df = []
        # Check if the message contains new token information
        if data.get("txType") == "create":
        # Memanggil value dari key 'mint', 'name', 'symbol', dan 'marketCapSol'
            mint = data['mint']
            name = data['name']
            symbol = data['symbol']
            mc_sol = data['marketCapSol']  # Market cap in SOL
            initialbuy = int(data['initialBuy'])
            mc_usd = mc_sol * sol_to_usd
            # Convert market cap to USD
            # URL yang ingin di-scrape
            link = f'https://pump.fun/{mint}'
            response = requests.get(link)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    json_datas = soup.find_all('script')
                    json_data = str(json_datas)

                    if json_data:
                        cleaned_data_string = re.search(r'\[1,"8:\[\[(.*?)\]\]', json_data, re.DOTALL)
        
                        if cleaned_data_string:
                            # mat = mat.group(1)
                            # Mengambil grup pertama yang berisi JSON
                            json_string = cleaned_data_string.group(1)
                            json_string = json_string.replace('\\', '')
                            # print(json_string)
                            start_seq = '{"coin":'
                            start_index = json_string.find(start_seq)
                            brace_count = 0
                            end_index = start_index
                            for j in range(start_index, len(json_string)):
                                char = json_string[j]
                                if char == '{':
                                    brace_count += 1
                                elif char == '}':
                                    brace_count -= 1
                                    if brace_count == 0:
                                        end_index = j
                                        break
                            data = json_string[start_index:end_index+1]
                except Exception as e:
                    print(e)
            else:
                continue
            try:
                data = json.loads(data)
            except:
                continue
            twitter = data['coin'].get("twitter").split(' ')[0] if data['coin'].get("twitter") else None
            telegram = data['coin'].get("telegram").split(' ')[0] if data['coin'].get("telegram") else None
            website = data['coin'].get("website").split(' ')[0] if data['coin'].get("website") else None
            social_links = [twitter, telegram, website]
            # print(social_links)
            if mint[-4:].lower() == "pump" and initialbuy < 50000000 and telegram != None:
                browser.get(f"https://web.t.me/helenus_trojanbot?start=r-oketokwes-{mint}")
                # Print the token information
                print("New Token:", i)
                print("Mint:", mint)
                print("Name:", name)
                print("Symbol:", symbol)
                print(f"Market Cap (SOL): {mc_sol:.2f} SOL")
                print(f"Market Cap (USD): ${mc_usd:.2f} USD")
                print("initialbuy:", f"{initialbuy:,}".replace(",", "."))
                print("Snipe:", f"https://t.me/maestro?start={mint}-oketokwes")
                print(f"Twitter : {twitter}", None )
                print(f"Telegram : {telegram}")
                print(f"Website : {website}")
                print("--------------------")
                i += 1
                if i == 45:
                    break
            
async def main():
    # Ganti dengan URL websocket yang benar
    url = "wss://pumpportal.fun/api/data"

    async with websockets.connect(url, ping_timeout=600, close_timeout=10) as websocket:
        await subscribe_to_new_tokens(websocket)

if __name__ == "__main__":
    asyncio.run(main())
