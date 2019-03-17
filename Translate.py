from PIL import Image
import pytesseract
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

name = 'image2.png'
text = pytesseract.image_to_string(Image.open(name), lang ='eng' ,config=tessdata_dir_config )

unwanted = ";'.></\="

for char in unwanted:
    text = text.replace(char,"")
    
print(text)
text = str(text)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('E:/chromedriver',options=options)
driver.get('https://www.bing.com/translator')
search_query = driver.find_element_by_id('t_sv')
search_query.send_keys(text)
time.sleep(3)

select = Select(driver.find_element_by_id('t_sl'))
selected_option = select.first_selected_option
s  = selected_option.text
d = s.split()[0]
print(d)

driver.get('https://www.collinsdictionary.com/translator')
select_fr = Select(driver.find_element_by_id("select-input"))
select_fr.select_by_value(d)
search = driver.find_element_by_id('input-text')
search.send_keys(text)

select_desire = Select(driver.find_element_by_id("select-output"))
alllang = driver.find_element_by_id("select-output")
print(alllang.text)
print("Choose Your Language")
lang = input()
select_desire.select_by_value(lang)



driver.find_element_by_class_name('spinner').click()

ans = driver.find_element_by_id('output-text')
print(ans.text)
meaning  = driver.find_elements_by_css_selector('.blocDefinition.page')
for mean in  meaning:
    print(mean.text)
