from selenium import webdriver
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

# Path ke EdgeDriver yang benar
edge_driver_path = r'edgedriver_win64/msedgedriver.exe'
service = Service(edge_driver_path)

# Gunakan EdgeOptions, bukan ChromeOptions
edge_options = Options()
edge_options.add_argument("--disable-notifications")  # Menonaktifkan notifikasi

# Membuat instance WebDriver Edge
browser = webdriver.Edge(service=service, options=edge_options)

# Buka URL Telegram Web
url = "https://web.telegram.org/a/#5486942816"
browser.get(url)

# Tunggu 20 detik
time.sleep(20)

# Open the URL in the browser
browser.get('https://web.t.me/maestro?start=E62hvqUAavk2VCyDSw5ifbTsBkNpip9r7EpTHzAmpump-oketokwes')

# Wait for the page to load (adjust timing as needed)
time.sleep(10)

webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
# browser.switch_to.alert().dismiss()
# common.alert.Alert(browser).dismiss()

# Close the pop-up (click "Cancel" button)
try:
    # Arahkan mouse ke koordinat tertentu untuk menutup popup
    ActionChains(browser).move_by_offset(100, 100).click().perform()
    print("Pop-up closed.")
except Exception as e:
    print("Error closing pop-up:", e)

# Wait for the page to adjust after closing the pop-up
time.sleep(10)

# webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()

# Click the "OPEN IN WEB" button
try:
    open_in_web_button = browser.find_element(By.CLASS_NAME, 'tgme_action_web_button')
    open_in_web_button.click()
    print("Clicked 'Open in Web'.")
except Exception as e:
    print("Error clicking 'Open in Web':", e)

# Let the browser stay open for a while to observe the results (adjust timing as needed)
time.sleep(60)

# Close the browser
browser.quit()
