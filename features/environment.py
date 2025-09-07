import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import config

def before_all(context):
    screenshots_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

def before_scenario(context, scenario):
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if config.HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(config.IMPLICIT_WAIT)

def after_step(context, step):
    if step.status == "failed":
        _save_screenshot(context, f"step_{step.name}")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        _save_screenshot(context, f"scenario_{scenario.name}")
        context.driver.quit()
        
def _save_screenshot(context, name):
    screenshots_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    if hasattr(context, "browser"):
        filename = f"{name.replace(' ', '_')}.png"
        path = os.path.join(screenshots_dir, filename)
        context.browser.save_screenshot(path)
    
