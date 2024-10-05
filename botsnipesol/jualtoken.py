from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

# Path ke EdgeDriver yang benar
edge_driver_path = r'edgedriver_win64/msedgedriver.exe'
service = Service(edge_driver_path)

# Gunakan EdgeOptions, bukan ChromeOptions
edge_options = Options()
edge_options.add_argument("--disable-notifications")  # Menonaktifkan notifikasi

# Membuat instance WebDriver Edge
browser = webdriver.Edge(service=service, options=edge_options)

# Buka URL Telegram Web
url = "https://web.telegram.org/"
browser.get(url)
time.sleep(60)
print("Silakan login ke Telegram Web. Tunggu proses login selesai...")

# # Tunggu hingga halaman selesai dimuat dan temukan kolom teks untuk pesan
# url = "https://web.telegram.org/a/#5486942816"
# browser.get(url)
# time.sleep(5)
df = pd.read_excel(r'output_href.xlsx')
df = pd.DataFrame(df)
browser.implicitly_wait(10)
time.sleep(10)
# Looping untuk mengirim banyak pesan 'ca'
for i in range(len(df)):  # Loop sebanyak 10 kali (sesuaikan sesuai kebutuhan)
    # Cari kolom teks untuk mengirim pesan
    print('Mencari kolom text')
    message_box = browser.find_element(By.ID, "editable-message-text")
    
    # Paste teks 'ca' ke dalam kolom pesan
    print('paste ca')
    message_box.send_keys(f"{df.contract_address[i]}")
    
    # Tunggu sebentar
    time.sleep(5)

    # Tekan tombol "Send" untuk mengirim pesan
    print('kirim pesan')
    send_button = browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Send Message"]')
    send_button.click()

    # Tunggu sebentar sebelum lanjut ke aksi berikutnya
    time.sleep(5)

    # Tekan tombol "Track" (simbol 📍)
    print('track')
    track_button = browser.find_element(By.XPATH, "//button[contains(., 'Track')]")
    track_button.click()
    
    # Scroll to the bottom of the page
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Add a delay to ensure the page loads after scrolling
        # Find all "100%" buttons on the page
    try:
        button_100 = browser.find_element(By.XPATH, "//button[contains(., '100%')]").click()
    except Exception as e:
        print("Terjadi kesalahan:", e)
    
    # button_100 = browser.find_element(By.XPATH, "//button[contains(., '100%')]").click()
    # Tunggu beberapa detik sebelum mengulangi siklus
    time.sleep(7)

    # Tekan tombol "Confirm 100%" untuk Confirm menjual 100%
    print('confirm 100%')
    try:
        button_confirm_100 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Confirm 100%')]"))
    )
        button_confirm_100.click()
    except Exception as e:
        print("Terjadi kesalahan:", e)
    print("berhasil klick confirm 100%")

    # Tunggu beberapa detik sebelum mengulangi siklus
    time.sleep(5)
# Tutup browser setelah selesai
browser.quit()

print("Proses selesai!")
