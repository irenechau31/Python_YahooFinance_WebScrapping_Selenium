from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#backslashes (\) in strings are interpreted as escape characters in Python. To fix this, put r in front

path=r'C:\Users\User\OneDrive\Desktop\Coding Learning\chromedriver-win32\chromedriver-win32\chromedriver.exe'

service = webdriver.chrome.service.Service(path)
service.start()

ticker = 'AAPL'
url='https://finance.yahoo.com/quote/{}/financials'.format(ticker,ticker)

driver=webdriver.Chrome(service=service)
driver.get(url)
driver.implicitly_wait(2)

#get data from the table, without hidden row

#use explicit waits up to 10 seconds for the element to be present on the page before attempting to locate it
table = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='table svelte-1pgoo1f']"))
    ).text
print(table)

#scraping hidden rows, and entire table with balance sheet, CF, etc.
#"//article" used to search for article, "//button" used to search for button
# the buttons variable is expected to be a list of WebElement objects
#=> using "presence_of_all_elements_located" instead of "presence_of_element_located"
buttons = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, "//section[@class='container svelte-1pgoo1f']//button"))
    )
for button in buttons:
    print(button.accessible_name) #access all the click-able


