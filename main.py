from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
import re
from selenium.webdriver.chrome.options import Options

service = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
web = "https://arithmetic.zetamac.com/"

driver.get(web)

startButton = driver.find_element(By.XPATH, "//form[@class='game-options']//input[@type='submit']")
startButton.click()

while True: 
    try: 
        timer = driver.find_element(By.XPATH, "//div[@id = 'game']//span[@class = 'left']").text
        match = re.search(r'\d+', timer)
        if match: 
            secondsLeft = int(match.group())

            if secondsLeft == 0:
                break
            else: 
                problem = driver.find_element(By.XPATH, "//div[@class = 'start']//span[@class = 'problem']").text
                expression = problem.replace('÷', '/').replace('×', '*').replace('–', '-')
                answer = int(eval(expression))

                inputBox = driver.find_element(By.XPATH, "//div[@class = 'start']//input[@class = 'answer']")
                inputBox.send_keys(str(answer))  
                inputBox.send_keys("\n")
        else:
            break

    except Exception as e:
        print("Error:", e)
        break

time.sleep(2)