from pandas.tests.groupby.test_value_counts import df
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from bs4 import BeautifulSoup
import requests
# import byPassCaptcha
import pytest
import time
import re
import json
import autopy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

class EasyApplyDice:

    def __init__(self, data):
        """Parameter initialization"""

        self.email = data['email']
        self.password = data['password']
        self.driver = webdriver.Chrome()

    def login_dice(self):
        """This function logs into your personal LinkedIn profile"""

        # go to the LinkedIn login url
        self.driver.get("https://www.dice.com/dashboard/login")
        time.sleep(5)
        # introduce email and password and hit enter
        login_email = self.driver.find_element_by_name('email')
        login_email.clear()
        login_email.send_keys(self.email)
        login_pass = self.driver.find_element_by_name('password')
        login_pass.clear()
        login_pass.send_keys(self.password)
        login_pass.send_keys(Keys.RETURN)

    def job_search(self):
        variable = pd.read_csv(r"C:\Users\Quadrant\Desktop\Resumedataset10 (1).csv")
        df = pd.DataFrame(variable)
        df.at[0, 'ROLL'] = 'aws developer'
        df.at[1, 'ROLL'] = 'java developer'
        #print(df)
        for i, j in df.iterrows():
            jobs = []
            jd = []
            job_link = []
            self.driver.get("https://www.dice.com/home/home-feed")
            search_keywords = self.driver.find_element_by_xpath("//input[starts-with(@class,'form-control ng-tns-c31-0 ng-star-inserted')]")
            search_keywords.clear()
            search_keywords.send_keys(j.ROLL)
            time.sleep(2)
            search_location = self.driver.find_element_by_xpath("//input[starts-with(@id,'google-location-search')]")
            search_location.clear()
            search_location.send_keys(j.LOCATION)
            search_location.send_keys(Keys.RETURN)
            time.sleep(10)
            current_page = self.driver.current_url
            time.sleep(2)
            for job in self.driver.find_elements_by_class_name('search-card'):
                soup = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')
                # print(soup.prettify())
                title = soup.find("a", class_="card-title-link").text.replace("\n", "").strip()
                print(title)
                jobs.append(title)
                time.sleep(2)
                for link in soup.find_all('a', {'class': "card-title-link bold"}):
                    href = link['href']
                    #href.append(link['href'])
                    print(href)
                    job_link.append(href)
            for desc in job_link:
                x = desc
                print(x)
                self.driver.get(x)
                job_desc = self.driver.find_element_by_xpath("//div[contains(@class,'highlight-black')]").text
                print(job_desc)
                jd.append(job_desc)
            print(jd)
            AccuracyList = [0.01, 0.4, 0.9, 0.1, 0.4, 0.5, 0.8, 0.22, 0.01, 0.77, 0.6]
            desc_list = [i[0] for i in sorted(enumerate(AccuracyList), key=lambda k: k[1], reverse=True)]
            print(desc_list)
            print(len(job_link))
            applied_links = []
            applied_titles = []
            applied_jd =[]
            top_accuracy =[]
            i = 0
            while i <= 4:
                index_value = desc_list[i]
                top = AccuracyList[index_value]
                top_accuracy.append(top)

                print(AccuracyList[index_value])
                links = job_link[index_value]
                print(links)
                applied_links.append(links)
                apply_titles = jobs[index_value]
                print(apply_titles)
                applied_titles.append(apply_titles)
                apply_jd = jd[index_value]
                print(apply_jd)
                applied_jd.append(apply_jd)

                time.sleep(2)

                i = i + 1
            print(applied_jd)
            print(applied_titles)
            print(top_accuracy)
            print(applied_links)
            for y in applied_links:
                self.driver.get(y)
                time.sleep(5)
                try:
                    in_apply = self.driver.find_element_by_xpath("//button[contains(@id,'applybtn')]")
                    in_apply.click()
                    time.sleep(5)
                    radio_button = self.driver.find_element_by_id("upload-resume-radio")
                    radio_button.click()
                    time.sleep(5)
                    file_upload = self.driver.find_element_by_xpath(
                        "//input[starts-with(@id,'upload-resume-file-input')]").send_keys(
                        r'C:\Users\Quadrant\Desktop/SravanthiAnuchuri.pdf')
                    time.sleep(5)
                    page = []
                    current_url1 = self.driver.current_url
                    print(current_url1)
                    page.append(current_url1)
                    time.sleep(3)

                    service_key = '6ac9c9f6e469993bd75049eae8d6103b'  # 2captcha service key
                    google_site_key = '6LcleDIUAAAAANqkex-vX88sMHw8FXuJQ3A4JKK9'
                    pageurl = ' '.join([str(elem) for elem in page])
                    url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key + "&pageurl=" + pageurl
                    resp = requests.get(url)

                    if resp.text[0:2] != 'OK':
                        quit('Service error. Error code:' + resp.text)
                    captcha_id = resp.text[3]
                    fetch_url = "http://2captcha.com/res.php?key=" + service_key + "&action=get&id=" + captcha_id

                    for i in range(1, 10):
                        time.sleep(5)  # wait 5 sec.
                        resp = requests.get(fetch_url)
                        if resp.text[0:2] == 'OK':
                            break

                    self.driver.execute_script(
                        'var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

                    self.driver.find_element_by_xpath("//*[@id='g-recaptcha-response']").send_keys(
                        resp.text[3:])  # ERROR HERE <<<<<<
                    time.sleep(5)
                    apply = self.driver.find_element_by_id("submit-job-btn")
                    apply.click()
                    time.sleep(10)
                except:
                    print("You are already applied for this job")
                    pass



if __name__ == '__main__':
    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = EasyApplyDice(data)
    bot.login_dice()
    time.sleep(3)
    bot.job_search()
    time.sleep(3)
    # byPassCaptcha.captcha()
    # bot.find_offers()
    # bot.apply()

