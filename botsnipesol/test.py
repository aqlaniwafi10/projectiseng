from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pandas as pd

# Path ke EdgeDriver
# Path ke EdgeDriver yang benar
edge_driver_path = r'edgedriver_win64/msedgedriver.exe'
service = Service(edge_driver_path)

# Gunakan EdgeOptions, bukan ChromeOptions
edge_options = Options()
edge_options.add_argument("--disable-notifications")  # Menonaktifkan notifikasi

# Membuat instance WebDriver Edge
browser = webdriver.Edge(service=service)
df = pd.read_excel(r'output_href.xlsx')
df = pd.DataFrame(df)
# Misal akses ke URL tertentu
print('login telegram')
browser.get("https://web.telegram.org/")
time.sleep(60)

print('masuk maestro bot')
browser.get("https://web.telegram.org/a/#5486942816")
time.sleep(15)

# Fungsi untuk memicu munculnya div InitialButtons (misalnya dengan klik tombol tertentu)
def trigger_initialbuttons(a):
    # Cari kolom teks untuk mengirim pesan
    print('Mencari kolom text')
    message_box = browser.find_element(By.ID, "editable-message-text")
    
    # Paste teks 'ca' ke dalam kolom pesan
    print('paste ca')
    message_box.send_keys(f"{df.contract_address[a]}")
    
    # Tunggu sebentar
    time.sleep(5)

    # Tekan tombol "Send" untuk mengirim pesan
    print('kirim pesan')
    send_button = browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Send Message"]')
    send_button.click()

    # Tunggu sebentar sebelum lanjut ke aksi berikutnya
    time.sleep(5)
    
print('mulai looping')
# Loop untuk memicu dan menunggu div baru, lalu klik tombol 100% di dalamnya
for i in range(14, len(df)):  # Anggap akan ada 5 div InitialButtons yang muncul bertahap
    # Memicu munculnya div InitialButtons
    trigger_initialbuttons(i)
        
    # Cari semua div InitialButtons
    all_divs = browser.find_elements(By.CLASS_NAME, 'InlineButtons')
    
    # Pilih div InitialButtons yang terakhir (paling baru)
    new_div = all_divs[-1]  # Mengambil elemen terakhir dari daftar div InitialButtons
    
    # Setelah muncul, cari tombol "Track" di dalam div tersebut dan klik
    track = new_div.find_elements(By.TAG_NAME, 'button')
    for button in track:
        if button.text == 'Track':
            print(f"Track ditemukan di div InitialButtons {i + 1}, mengklik tombol...")
            button.click()  # Mengklik tombol "100%"
            break  # Berhenti setelah menemukan dan mengklik tombol "100%"
        
    time.sleep(5)
    # Cari semua div InitialButtons
    all_divs2 = browser.find_elements(By.CLASS_NAME, 'InlineButtons')
    print('menacri inlinebuttons baru')
    
    # Pilih div InitialButtons yang terakhir (paling baru)
    new_div2 = all_divs2[-1]  # Mengambil elemen terakhir dari daftar div InitialButtons
    print('nemu inlinebuttons baru')
    
    # Setelah muncul, cari tombol "100%" di dalam div tersebut dan klik
    monitor = new_div2.find_elements(By.TAG_NAME, 'button')
    print('filter semua buttons')
    for button in monitor:
        # Cari semua gambar di dalam tombol yang memiliki class "emoji emoji-small"
        images = button.find_elements(By.CLASS_NAME, 'emoji-small')
        for img in images:
            # Ambil atribut 'src' dari gambar dan cek apakah itu gambar nuklir
            img_src = img.get_attribute('src') 
            print(img_src)   
            if img_src == 'https://web.telegram.org/a/img-apple-64/2622.png':
                print(f"klik tombol sell")
                button.click()  # Mengklik tombol "Sell" dengan gambar nuklir
                time.sleep(5)
                print(f"klik tombol confirm sell")
                button.click()
                break  # Berhenti setelah menemukan dan mengklik tombol yang benar
            
    #Proses delete dari monitor        
    for button in monitor:
        images = button.find_elements(By.CLASS_NAME, 'emoji-small')
        for img in images:
            # Ambil atribut 'src' dari gambar dan cek apakah itu gambar nuklir
            img_src = img.get_attribute('src') 
            print(img_src)   
            if button.text == 'Delete' and img_src == 'https://web.telegram.org/a/img-apple-64/274c.png':
                print(f"klik tombol Dellete")
                button.click()  # Mengklik tombol "Sell" dengan gambar nuklir
                time.sleep(5)
                break  # Berhenti setelah menemukan dan mengklik tombol yang benar
    time.sleep(8)

# Jangan lupa tutup browser setelah selesai
print('sukses jual semua')
browser.quit()
