from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def bot_yaz():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.m5bilisim.com/tr/on-parmak/hiz-testi/")  # Sitenin URL'sini buraya ekleyin

        time.sleep(5)  

        words_element = driver.find_element(By.ID, "satir")
        kelimeler = words_element.find_elements(By.TAG_NAME, "span")
        input_element = driver.find_element(By.ID, "yaziyaz")

        for kelime in kelimeler:
            input_element.send_keys(kelime.text + " ")

            time.sleep(0.01)
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        input("Programı sonlandırmak için bir tuşa basın...")
        driver.quit()  

if __name__ == "__main__":
    bot_yaz()
