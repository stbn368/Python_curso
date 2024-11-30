from selenium import webdriver

# Inicializa el navegador
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Finaliza el navegador
driver.quit()
