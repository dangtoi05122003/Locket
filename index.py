from account import username, password
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
from PIL import Image
from io import BytesIO
import base64
import os
import logging


logging.basicConfig(level=logging.CRITICAL)



options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "API"
options.app = "C:\\Users\\admin\\Code\\NCKH\\Appium\\apk\\Locket Widget_1.180.8_APKPure\\com.locket.Locket.apk"
options.app_package = "com.locket.Locket"
options.app_activity = "com.locket.Locket.MainActivity"
from datetime import datetime, timedelta

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

print("Success")



time.sleep(5)


try:
    sign_in = driver.find_element(
        By.XPATH, '//android.view.ViewGroup[@content-desc="Sign in"]')
    sign_in.click()

except Exception as e:
    print(f"Không thể tìm thấy nút 'Sign in' {e}")


time.sleep(5)


try:
    email = driver.find_element(
        By.XPATH, '//android.widget.TextView[@text="Use email instead"]')
    email.click()

except Exception as e:
    print(f"Không thể tìm thấ 'Use email instead' (XPath): {e}")

try:
    email_path = driver.find_element(
        By.XPATH, '//android.widget.EditText[@text="Email address"]')
    email_path.click()
    email_path.send_keys(f"{username}")

except Exception as e:
    print(f"Không thể tìm thấy email: {e}")


try:
    email_click= driver.find_element(
        By.XPATH, '//android.widget.TextView[@text="Continue"]')
    email_click.click()

except Exception as e:
    print(f"Không thể tìm thấy 'Continue'{e}")
try:
    allow_foreground = driver.find_element(
        By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    allow_foreground.click()

except Exception as e:
    print(f"Không thể tìm thấy 'Allow Foreground': {e}")


time.sleep(3)


try:
    allow_button= driver.find_element(
        By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    allow_button.click()

except Exception as e:
    print(f"Không thể tìm thấy nút 'Allow': {e}")

time.sleep(3)


try:
    password_field = driver.find_element(
        By.XPATH, '//android.widget.EditText[@text="Password"]')
    password_field.click()
    password_field.send_keys(f"{password}")  
except Exception as e:
    print(f"Không thể tìm thấy mật khẩu: {e}")


time.sleep(3)

try:
    password_click = driver.find_element(
        By.XPATH, '//android.widget.TextView[@text="Continue"]')
    password_click.click()
    print("Đã nhấn nút 'Continue' sau khi nhập mật khẩu.")
except Exception as e:
    print(f"Không thể tìm thấy 'Continue'{e}")


time.sleep(5)
try:
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "android:id/autofill_save_no"))
    )
    save.click()

except Exception as e:
    print(f"Không thể tìm thấy'Save': {e}")
time.sleep(5)



try:

    allow_foreground = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
    )
    allow_foreground.click()

except Exception as e:
    print(f"Không thể tìm thấy 'Allow Foreground Only': {e}")

time.sleep(5)


try:
    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
    )
    allow_button.click() 

except Exception as e:
    print(f"Không thể tìm thấy'Allow': {e}")

time.sleep(5)


try:

    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
    )
    allow_button.click()  
    print("Đã nhấn vào nút 'Allow'.")
except Exception as e:
    print(f"Không thể tìm thấy hoặc nhấn vào nút 'Allow': {e}")



time.sleep(5)


try:
    allow_button = driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    allow_button.click()
except Exception as e:
    print(f"Không thể tìm thấy nút 'Allow': {e}")
time.sleep(3)

image_folder = r"C:\Users\admin\Code\NCKH\test\image"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
def convert_relative_date(relative_date):
    try:

        if relative_date.endswith("m"):
            minutes = int(relative_date[:-1])
            current_time = datetime.now()
            new_time = current_time - timedelta(minutes=minutes)
            return new_time.strftime("%b %d, %Y %H:%M") 


        elif relative_date.endswith("h"):
            hours = int(relative_date[:-1]) 
            current_time = datetime.now()
            new_time = current_time - timedelta(hours=hours)
            return new_time.strftime("%b %d, %Y %H:%M")


        return relative_date

    except Exception as e:
        print(f"Error while converting date: {e}")
        return relative_date 
scroll_count = 0
max_scrolls = 8  
data = []


xpath_section = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]"
xpath_section2 = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"


def check_duplicate(user_name, date, data):
    for item in data:
        if item["user_name"] == user_name and item["date"] == date:
            return True
    return False


while scroll_count < max_scrolls:
    try:

        driver.swipe(0, 1500, 0, 0, 1600)
        print("Đã vuốt xuống gấp đôi.")
        time.sleep(2)


        text_elements_section = driver.find_elements(By.XPATH, xpath_section + "/android.widget.TextView[@text]")

        if not text_elements_section:
            print("Không còn phần tử nào để lấy từ xpath_section.")
            break


        text_elements_section2 = driver.find_elements(By.XPATH, xpath_section2 + "/android.widget.TextView[@text]")


        if not text_elements_section2:
            text = ""
        else:
            text = text_elements_section2[0].text 


        if len(text_elements_section) >= 2:  
            user_name = text_elements_section[0].text 
            date = text_elements_section[1].text 
            date = convert_relative_date(date)

 
            print(f"user_name: {user_name}, date: {date}, text: {text}")


            if check_duplicate(user_name, date, data):
                print(f"Dữ liệu trùng lặp (user_name: {user_name}, date: {date}). Stop.")
                break 


            element_data = {
                "user_name": user_name,
                "date": date,
                "text": text 
            }


            try:
                image_element = driver.find_element(By.XPATH, "//android.widget.ImageView")
                image_base64 = image_element.screenshot_as_base64 


                image_data = BytesIO(base64.b64decode(image_base64))
                image = Image.open(image_data)


                image_file = f"image_{scroll_count}.png"
                image_path = os.path.join(image_folder, image_file)


                image.save(image_path)
                print(f"Đã lưu ảnh của {user_name} vào {image_path}")


                element_data["image"] = image_path

            except Exception as e:
                print(f"Không thể lấy ảnh từ ImageView: {e}")


            data.append(element_data)


        scroll_count += 1

    except Exception as e:
        print(f"Không thể tìm thấy các phần tử hoặc vuốt xuống thêm: {e}")
        break


with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Đã đóng kết nối.")