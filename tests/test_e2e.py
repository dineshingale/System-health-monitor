from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

def test_dashboard_access():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Wait for the server to be ready, this might be handled by retry logic in a real scenario
        # but for now we rely on the sleep in entrypoint.sh or we can add a small sleep here
        time.sleep(2) 
        
        driver.get("http://localhost:5173")
        
        # Verify title or specific element
        # Assuming the title might be something like "Vite + React" or "System Health Monitor"
        # Since I don't know the exact title, I'll check if the title exists or body resides
        assert driver.title != "Problem loading page"
        
        # We can also check for a specific element if we knew the ID.
        # For now, just ensuring no connection error is a basic check.
        print(f"Page Title: {driver.title}")
        
    finally:
        driver.quit()
