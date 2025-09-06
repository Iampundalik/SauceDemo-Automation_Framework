# SauceDemo Automation Framework (Selenium + Behave BDD + POM)

A robust and clean test automation framework built with **Python + Selenium + Behave (BDD) + Page Object Model (POM)** for the [SauceDemo](https://www.saucedemo.com/) web app.

---

## Features

- **Positive Scenarios:** Valid login, add to cart, complete checkout
- **Negative Scenarios:** Invalid login, locked user, checkout validation errors
- **Logout:** User can logout and is redirected to login page
- **Sorting Validation:** Verify sorting by price: low to high
- **Reporting:** Pretty console, HTML, screenshots on failure, structured logging
- **CI-ready:** Environment-driven config, quick setup

---

## Quick Start (Windows)

**Prerequisites**
- **Python 3.7+** (use `py` launcher)
- **Google Chrome** (latest stable; ChromeDriver is auto-managed)

**Setup & Run:**
```bat
REM 1. Create & activate virtualenv
py -m venv .venv
.venv\Scripts\activate

REM 2. Install dependencies
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

REM 3. Run all tests (headed by default)
py -m behave ```

**Headless Mode:**
```bat
set HEADLESS=true
py -m behave
```

**Change Base URL or Waits:**
```bat
set BASE_URL=https://www.saucedemo.com/
set IMPLICIT_WAIT=5
set EXPLICIT_WAIT=10
py -m behave
```

> **Screenshots** on failure are saved in `screenshots/` named by scenario + timestamp.

---

## Project Structure

```
SauceDemo-Automation_Framework/
├── behave.ini
├── requirements.txt
├── README.md
├── features/
│   ├── saucedemo_login.feature
│   ├── saucedemo_cart.feature
│   ├── saucedemo_cart_negative.feature
│   ├── saucedemo_logout_positive.feature
│   ├── saucedemo_sorting.feature
│   ├── steps/
│   │   ├── common_steps.py
│   │   ├── login_steps.py
│   │   ├── cart_steps.py
│   │   └── sorting_steps.py
│   └── environment.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── utils/
│   ├── config.py
│   ├── helpers.py
│   └── logger.py
├── reports/
└── screenshots/```

---

## Scenarios Included

### Positive
- **Login with valid user** → Inventory page loads
- **Add item & checkout** → Order completed successfully

### Negative
- **Invalid login** → Error message shown
- **Locked out user** → Shows locked-out error
- **Checkout with missing info** → Validates required fields

### Logout
- **User can logout** → Should see login page after logout

### Extra
- **Sorting by price** → Verifies ascending order

---


## Design Highlights

- **Page Object Model:** Clean separation of page actions/locators
- **Behave BDD:** Business-readable scenarios, easy for teams to extend
- **Centralized Hooks:** Driver, logging, screenshots in `environment.py`
- **Explicit Waits:** Stable on dynamic pages
- **Environment-driven Config:** For local and CI runs
- **Stable Selectors:** Uses `data-test` attributes where possible
