from selenium.webdriver.common.by import By

class Locator():
    SEARCH_TEXTBOX= (By.NAME, "q")

    SEARCH_SUGGESTION= (By.CSS_SELECTOR, "[id=\"fprsl\"]")

    SEARCH_RESULTS= (By.CSS_SELECTOR, ".r h3")