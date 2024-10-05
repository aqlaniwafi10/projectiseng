import requests
from bs4 import BeautifulSoup
import json
import re

# # URL yang ingin di-scrape
# url = 'https://pump.fun/8DHMuVEWtUKsCLMKwAHCXuTvd4ngFnz3odX64EqQpump'

# # Lakukan request ke halaman
# response = requests.get(url)
# # print(response)
def scraplink(url):
    # Jika request berhasil
    # URL yang ingin di-scrape
    # Lakukan request ke halaman    
    response = requests.get(url)
    if response.status_code == 200:
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
                for i in range(start_index, len(json_string)):
                    char = json_string[i]
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_index = i
                            break
                data = json_string[start_index:end_index+1]
            
                try:
                    data = json.loads(data)

                # Langkah 3: Ambil informasi yang dibutuhkan dan memisahkan hingga spasi
                    twitter_link = data['coin'].get("twitter").split(' ')[0] if data['coin'].get("twitter") else None
                    telegram_link = data['coin'].get("telegram").split(' ')[0] if data['coin'].get("telegram") else None
                    website_link = data['coin'].get("website").split(' ')[0] if data['coin'].get("website") else None

                    # print(f"Twitter: {twitter_link}")
                    # print(f"Telegram: {telegram_link}")
                    # print(f"Website: {website_link}")
                    return twitter_link, telegram_link, website_link
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
            else:
                print("Tidak menemukan data JSON yang valid di dalam teks script.")
        else:
            print("Tidak menemukan data JSON di dalam HTML.")
    else:
        print("Error fetching the page.")
        return None
   
