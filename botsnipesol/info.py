from bs4 import BeautifulSoup
import json
import requests
import re

# Misalnya, ini adalah URL yang ingin kita ambil datanya
url = 'https://pump.fun/7L8Vz9bB1SXV9ms7upFoZVQMv8s1rdYfvV6MrANqpump'
response = requests.get(url)

# Pastikan respons berhasil
if response.status_code == 200:
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mengambil semua tag <script>
    script_tags = soup.find_all('script')

    json_data = None
    for script in script_tags:
        if 'coin' in script.string:  # Memeriksa apakah JSON ada di dalam teks
            json_data = script.string
            break

    if json_data:
        # Langkah 1: Menghapus karakter yang tidak diinginkan dari string JSON
        # Menggunakan regex untuk menangkap bagian JSON yang valid
        cleaned_data_string = re.search(r'\[1,"8:\[\[(.*?)\]\]', json_data, re.DOTALL)
        
        if cleaned_data_string:
            # Mengambil grup pertama yang berisi JSON
            json_string = cleaned_data_string.group(1)
            json_string = json_string.replace('\"', '"')  # Memperbaiki tanda kutip

            # Langkah 2: Menambahkan bracket yang hilang dan mem-parsing string menjadi JSON
            json_string = f"{{\"coin\": {{{json_string}}}}}"

            try:
                data = json.loads(json_string)

                # Langkah 3: Ambil informasi yang dibutuhkan
                twitter_link = data['coin'].get("twitter")
                telegram_link = data['coin'].get("telegram")
                website_link = data['coin'].get("website")

                print(f"Twitter: {twitter_link}")
                print(f"Telegram: {telegram_link}")
                print(f"Website: {website_link}")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
        else:
            print("Tidak menemukan data JSON yang valid di dalam teks script.")
    else:
        print("Tidak menemukan data JSON di dalam HTML.")
else:
    print("Error fetching the page.")
