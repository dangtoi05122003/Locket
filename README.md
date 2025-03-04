# Locket widget

##Introduction
This project uses Appium and Python to automate the login process into the Locket Widget application on Android.

##Table of Contents
#Introduction
#Installation
#User Guide
#Important Notes

1.Introduction 

The purpose is to save time by automating the login process, granting permissions to the app, and collecting data from the Locket app, including username, time, text, and related images. The collected data will be saved into a JSON file, while images will be stored in a separate folder. This process includes steps like logging in via email and password, granting permissions to the app, and collecting information from elements in the app's interface. This app will assist users in automating tasks on Android phones.

2.Installation

First, you need to install Python on your computer if you don't have it already. You can download Python from the official website at https://www.python.org.

Next, you need to download the "Appium Server Gui" application from “https://github.com/appium/appium-inspector/releases” to use this code. Alternatively, you can access the Google Drive link “https://drive.google.com/drive/folders/1dOFEsEJSYL8VzUDIaQWWydGERFdayXde?usp=drive_link” for an easier download experience.

![Picture 1](https://github.com/dangtoi05122003/Locket/raw/main/images/pic1.png)

One essential step to run the code is to download Android Studio to have an emulator for monitoring the code's status.

Finally, the code may require the APK link of the Locket app. This can be downloaded from the internet or accessed via the Google Drive link “https://drive.google.com/drive/folders/1dOFEsEJSYL8VzUDIaQWWydGERFdayXde?usp=drive_link” for convenience. The code may or may not require the APK, but it only needs the APK link and doesn't need to be installed on the device.

3.User Guide 

First, you need to open the Appium Server Gui and set up a few things before starting, as shown in the image below:
![Picture 2](https://github.com/dangtoi05122003/Locket/raw/main/images/pic2.png)

Next, when running the code, you need to visit the website link “https://inspector.appiumpro.com/” which will help you verify the device connection after launching Appium Server Gui, and it helps to check the xpath of each element in the Locket app. To better understand the usage, you can refer to the image below:
![Picture 3](https://github.com/dangtoi05122003/Locket/raw/main/images/pic3.png)
Once you have everything set up, you'll need to modify this information in the Python script to match the device.

4.Important Notes

This script is not fully completed and is still in the demo phase, making it suitable for scientific research or educational purposes.
