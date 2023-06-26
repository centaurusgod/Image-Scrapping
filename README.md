# Image-Scrapping for Classification Project
A Python-based project for scraping images and organizing them for a classification project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Installation

**Prerequisite** Download the Chrome WebDriver from the following website: [WebDriver Repository](https://chromedriver.chromium.org/downloads). 
### Using Python
**Step 1:** Clone the repo
```shell
git clone https://github.com/centaurusgod/Image-Scrapping.git
```
**Step 2:** Change directory to the root folder
```shell
cd Image-Scrapping
```
**Step 3:** Install necessary dependencies
```shell
pip install -r requirements.txt
```
### Using Anaconda 
**Step 1:** Clone the repo
```shell
git clone https://github.com/centaurusgod/Image-Scrapping.git
```
**Step 2:** Change directory to the root folder
```shell
cd Image-Scrapping
```
**Step 3:** Create a virtual environment (For example "conda create --name my_environment). You can provide any name that you like.
```shell
conda create --name your_environment_name
```
**Step 4:** Activate the virtual environment
```shell
conda activate your_environment_name
```
**Step 5:** Install necessary dependencies
```shell
conda install --file requirements.txt
```
## Usage
**How to run?** Simply run the following command either in you python or Conda environment.
```shell
python scrapper.py
```
**Step 1:** Go to [Google](https://www.google.com/) & search the image you want to scrap. 
![Google](https://i.ibb.co/yyF1K5Q/image.png)

**Step 2:** Click on Image section of the search and copy the URL from the address bar

**Step 3:** Paste the copied URL in the URL textbox of application

**Step 4:** Input the number of images you want to scrap & Select the directory you want to save the Images

**Step 5:(Very Important)** Click on "Select WebDriver". It will open a fial dialog box. Go to the folder you have downloaded and extracted the webdriver from the website mentioned above in "Prerequisite" section. Click and select the webdriver application and 
click open.

**Step 6:** Click "Start Download"

It will take a while to download images. You can go to the folder that you selected and see the images being updated there. Let it run in background and finish its job. 


## Acknowledgments
**Thank you @dearcutie Nirajan Poudel for the initiation of this script.**

## Contact
**Email:** ozonewagle998@gmail.com


