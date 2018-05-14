from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import json


# login and upload every file
def upload(args):
    start_time = time.time()

    # set relative paths
    upload_queue = "upload_queue"
    chrome_driver_executable = "chromedriver"

    # set real path
    cd_path = os.path.dirname(os.path.realpath(__file__))
    print("Driver should be located at " + cd_path + "/" + chrome_driver_executable)

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print("Print queue should be located at: " + project_path + "/" + upload_queue)

    # get driver
    driver = webdriver.Chrome(executable_path=cd_path + '/' + chrome_driver_executable)

    try:

        # login into DPrint
        print("Attempting to login...")
        login(driver)
        print("Login successful!")

        # list files
        file_list = os.listdir(os.path.expanduser(project_path + '/' + upload_queue))

        print("*** Uploading all files in the upload queue")
        for files in file_list:
            upload_file(files, driver, project_path, upload_queue)

    except Exception as e:
        print("A problem has occured:")
        print(e)
        driver.quit()

    driver.quit()
    print("-- All uploads have been completed, it took %s seconds --" % (time.time() - start_time))


# upload a single file
def upload_file(file_name, driver, project_path, upload_queue):

    start_time = time.time()

    if file_name[0] == '.':
        print('Ignoring file: ' + str(file_name))
        return

    print("- Uploading file: " + file_name)

    inputFile = driver.find_element_by_xpath('/html/body/div/form/div[3]/table/tbody/tr[1]/td[2]/input')
    inputFile.send_keys(project_path + '/' + upload_queue + '/' + file_name)

    driver.find_element_by_xpath('/html/body/div/form/div[8]/div/input').click()
    driver.find_element_by_xpath('/html/body/div/form/div[8]/div[1]/input').click()

    #switch to dynamic upload frame
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/div[3]/iframe'))

    # wait for the first part of the upload
    continueJob = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div[2]/p/a'))
    )
    continueJob.click()

    # wait for the second part of the upload
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/table/tbody/tr/td[1]/div'))
    )

    #switch back to default frame to click "another job"
    driver.switch_to.default_content()
    driver.find_element_by_xpath('/html/body/div/div[4]/table/tbody/tr[1]/td[1]/p/a').click()

    print("* Upload successful, took %.1f seconds --" % (time.time() - start_time))


def login(driver):
    # parse credentials
    real_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    with open(real_path + '/credentials.json') as f:
        credentials = json.load(f)

    # navigate the site and login
    driver.get("https://webprint.concordia.ca/cps/")
    driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/form/input').click()
    driver.find_element_by_xpath('//*[@id="regularLogin"]/table/tbody/tr[1]/td[2]/input').send_keys(
        credentials["login"])
    driver.find_element_by_xpath('//*[@id="regularLogin"]/table/tbody/tr[2]/td[2]/input').send_keys(
        credentials["password"])

    driver.find_element_by_xpath('//*[@id="regularLogin"]/input[2]').click()
    
    # next line selects black and white
    driver.find_element_by_xpath('//*[@id="tablelisting"]/div/table/tbody/tr[1]/td[1]/div/a').click()

