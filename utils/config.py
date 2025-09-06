import os

BASE_URL = os.getenv('BASE_URL', 'https://www.saucedemo.com/')
HEADLESS = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '5'))
EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '10'))
