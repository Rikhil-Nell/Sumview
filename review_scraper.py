from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def parse_reviews(page_source):
    if page_source:
        soup = BeautifulSoup(page_source, 'html.parser')
        reviews = soup.find_all('span', {'data-hook': 'review-body'})
        dates = soup.find_all('span', {'data-hook': 'review-date'})

        review_data = []
        for review, date in zip(reviews, dates):
            review_data.append({
                'review': review.get_text(strip=True),
                'date': date.get_text(strip=True)
            })

        return review_data

    print("Page sources parsed.")
    return None


class ReviewScraper:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_reviews(self, url):
        self.driver.get(url)

        # Wait for the "Product" button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "a-text-ellipsis", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "a-link-normal", " " ))]'))
        )

        page_sources_summarization = []
        page_sources_sentiment = []

        for i in range (1,11):
            page_sources_sentiment.append(self.driver.page_source)
            next_page_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'.a-last a'))
            )
            next_page_link.click()


        # Click on the "Positive reviews" link
        positive_reviews_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_lft"]'))
        )
        positive_reviews_link.click()
        time.sleep(2)  # Short sleep to ensure the page has loaded
        page_sources_summarization.append(self.driver.page_source)
        print("Obtained positive page source")

        # Click on the "Critical reviews" link
        critical_reviews_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_rgt"]'))
        )
        critical_reviews_link.click()
        time.sleep(2)  # Short sleep to ensure the page has loaded
        page_sources_summarization.append(self.driver.page_source)
        print("Obtained critical page source")

        return page_sources_summarization, page_sources_sentiment
