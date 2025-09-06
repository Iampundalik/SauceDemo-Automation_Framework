import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import config
from utils.logger import get_logger

def before_all(context):
    context.logger = get_logger('behave')

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
    if step.status == 'failed':
        ts = time.strftime('%Y%m%d_%H%M%S')
        name = f"{step.name[:40].replace(' ', '_')}_{ts}.png"
        fp = os.path.join('screenshots', name)
        context.driver.save_screenshot(fp)
        context.logger.info(f"Saved screenshot: {fp}")

def after_scenario(context, scenario):
    context.driver.quit()
