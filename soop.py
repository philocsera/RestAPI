from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_soop_data():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.sooplive.co.kr/directory/category/268/live")
    time.sleep(3)  # Wait for the page to load

    items = driver.find_elements(By.CSS_SELECTOR, "li[data-type='cBox']")
    results = []
    
    for item in items:
        try:
            link = item.find_element(By.CSS_SELECTOR, ".thumbs-box > a").get_attribute("href")
            img = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            nick = item.find_element(By.CSS_SELECTOR, "a.nick").text
            results.append({"nick": nick, "link": link, "img": img})
        except:
            continue
    
    driver.quit()
    return results

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    soop_data = get_soop_data()
    return templates.TemplateResponse("index.html", {"request": request, "soop_data": soop_data})