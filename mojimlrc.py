from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


if __name__ == '__main__':
    print('mojim lrc saver')
    print('Author  :  Nakateru (2021.02.03)')
    # print('https://mojim.com/')
    url = input('Input URL:')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument("--lang=en")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    lrc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'fsZx1'))).text
    title = driver.title
    title = re.split(r" 歌[詞词] ", title)[0]
    title = re.sub(r'[\\/:*"<>|]', '', title)
    title = re.sub(r'\?', '？', title)

    tag = "[ti:" + title + "]\n[ar:]\n[al:]\n"

    lrc = re.sub(r"\n(.*?)Mojim.com(.*?)\n", '\n', lrc)
    lrc = re.sub(r"　", ' ', lrc)
    print(lrc)

    with open(title + '.lrc', 'w', encoding='UTF-8') as f:
        f.write(tag + lrc + "\n*終わり*")

    driver.quit()
