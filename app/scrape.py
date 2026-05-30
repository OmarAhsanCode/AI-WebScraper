from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time # Import the time module
from bs4 import BeautifulSoup # Import the BeautifulSoup module

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=options)

def scrape_website(website):
    print("Launching Browser")

    driver = get_driver()

    try:
        driver.get(website)
        print("Page Loaded")
        html = driver.page_source # Get the html of the page
        time.sleep(10) # Wait for 5 seconds

        return html 
    finally:
        driver.quit() # Close the browser   

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser') # Create a BeautifulSoup object
    body_content = soup.body # Get the body content

    if body_content:
        return str(body_content) # Return the body content as a string
    return ''

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser') # Create a BeautifulSoup object
    for script_or_style in soup(["script", "style"]): # Remove all javascript and stylesheet code
        script_or_style.extract()

    cleaned_content = soup.get_text(separator = "\n") # Get the text from the body content
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) # Remove empty lines

    return cleaned_content

def split_dom_content(dom_content, max_length=15000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)] # Split the content into chunks of 15000 characters


