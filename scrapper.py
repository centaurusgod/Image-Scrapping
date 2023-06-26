import time
import io
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import Tk, Entry, Button, filedialog, Label

def get_images_from_google(wd, delay, max_images):
    def scroll_down():
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(delay)

    url = url_entry.get()  # Get the URL from the input box

    wd.get(url)

    image_urls = []
    while len(image_urls) < max_images:
        thumbnails = wd.find_elements(By.CLASS_NAME, 'Q4LuWd')

        for thumbnail in thumbnails[len(image_urls):max_images]:
            try:
                thumbnail.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, 'r48jcc.pT0Scc.iPVvYb')

            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    url = image.get_attribute('src')
                    print(f'Found: {url}')

                    try:
                        download_image(download_path, url, f'image{len(image_urls)+1}.jpg', timeout=10)
                        image_urls.append(url)
                    except TimeoutError:
                        print(f'Skipped: {url} (Timeout)')

        scroll_down()

    return image_urls


def download_image(download_path, url, filename, timeout):
    try:
        image_content = requests.get(url, timeout=timeout).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + filename

        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG')

        print('Success')

    except requests.exceptions.Timeout:
        raise TimeoutError('Download timeout')

    except Exception as e:
        print(f'Failed - {e}')


def open_file_dialog():
    directory = filedialog.askdirectory()  # Show file dialog to select download directory
    global download_path
    download_path = directory + '/'


# Specify the path to the WebDriver executable
webdriver_path = r'C:\Users\ozone\Desktop\ImageScraping\Image-Scrapping\chromedriver_win32\chromedriver.exe'

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run WebDriver in headless mode
wd = webdriver.Chrome(executable_path=webdriver_path, options=options)

#webdriver_path = r'C:\Users\ozone\Desktop\ImageScraping\Image-Scrapping\chromedriver_win32'

# Create the GUI window
window = Tk()
window.title("Image Downloader")

# URL input box
url_label = Label(window, text="URL:")
url_label.pack()
url_entry = Entry(window, width=50)
url_entry.pack()

# Button to open file dialog
file_dialog_button = Button(window, text="Select Directory", command=open_file_dialog)
file_dialog_button.pack()

# Button to start download
download_button = Button(window, text="Start Download", command=lambda: get_images_from_google(wd, 0.1, 150))
download_button.pack()

# Start the GUI event loop
window.mainloop()

# Quit WebDriver
wd.quit()
