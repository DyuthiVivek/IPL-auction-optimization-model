from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')



class Scrapper:

    def __init__(self,driver_path='/Users/amit/Documents/Sem 5/Optimisation/Optimization-project/chrome-mac-arm64'):
        self.driver_path=driver_path
        os.environ['PATH'] = driver_path
        super(Scrapper,self).__init__()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()

    def get_webpage(self):
        driver=self.driver
        driver.get('https://www.iplt20.com/auction/2022')
        time.sleep(2)

    def tabSelector(self):
        driver=self.driver
        # driver.find_element('css selector','button[aria-label="Regional settings"]').click()
        try:
            time.sleep(3)
            # Find the button using XPath
            link = driver.find_element(By.XPATH, "//li[@class='auction-tab-switch']/a[text()='UNSOLD PLAYERS']")

            # Click the button
            link.click()
            
        except Exception as e:
            print(e)
            driver.quit()
            exit()
        time.sleep(2)

    def getTable(self):
       
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        # Locate the section and the div with class 'tab-content'
        section = soup.find('div', class_='tab-content')
        if section:
            tab_content = section.find('div', id='autab4-2022')
            if tab_content:
                with open('tab_content.txt', 'w', encoding='utf-8') as f:
                    f.write(tab_content.prettify())
            else:
                print("No div with class 'tab-content' found.")
        else:
            print("No section with class 'auction-tab-section' found.")

    def makeCSV(self):

        # Load the HTML content from the text file
        with open('tab_content.txt', 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML with Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Open a CSV file to write the extracted data
        with open('unsold_players.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Player Name', 'Nationality', 'Type', 'Base Price'])  # Write headers

            # Locate the table body containing player data
            tbody = soup.find('tbody', id='pointsdata')
            
            if tbody:
                # Iterate through each row in the table body
                for row in tbody.find_all('tr'):
                    # Extract player name, nationality, type, and base price
                    player_name = row.find_all('td')[0].get_text(strip=True)
                    nationality = row.find_all('td')[1].get_text(strip=True)
                    player_type = row.find_all('td')[2].get_text(strip=True)
                    base_price = row.find_all('td')[3].get_text(strip=True)

                    # Write the extracted data to the CSV file
                    writer.writerow([player_name, nationality, player_type, base_price])

        print("Data extracted and saved to unsold_players.csv")



#Calling all the relevant functions defined above
sc = Scrapper()
sc.get_webpage()
sc.tabSelector()
sc.getTable()
sc.makeCSV()