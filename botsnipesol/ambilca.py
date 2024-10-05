from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
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
url = "https://gmgn.ai/sol/address/6U7x6CkU_sTBBDFFSvPY2saac2Gy14EoFhv5BFf8GhgXnTmDG2Xy"
browser.get(url)
time.sleep(5)
# Klik tombol Recent PnL
recent_pnl_button = browser.find_element(By.ID, "tabs-leftTabs--tab-0")
recent_pnl_button.click()

# Tunggu hingga elemen muncul
browser.implicitly_wait(10)
time.sleep(60)
# Temukan elemen <a> dengan kelas 'css-klael4' dan ambil atribut href
elements = browser.find_elements(By.CLASS_NAME, "css-klael4")

# Buat list untuk menyimpan href
href_list = []

# Loop melalui semua elemen dan ambil href-nya
for element in elements:
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Tunggu untuk melihat hasil scroll
    
    href = element.get_attribute("href")
    token = href.replace('https://gmgn.ai/sol/token/', '')
    href_list.append(token)
    # href_list.append(href)

# Buat DataFrame dari list href
df = pd.DataFrame(href_list, columns=['contract_address'])

# Simpan DataFrame ke file Excel
df.to_excel("output_href.xlsx", index=False)

# Tutup browser setelah selesai
browser.quit()

print("Data berhasil diekspor ke 'output_href.xlsx'")
print(df)
