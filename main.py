from driver_init import SeleniumDriver
from review_scraper import ReviewScraper, parse_reviews
from review_summarizer import ReviewSummarizer
from review_link import ReviewLink
from review_charting import ReviewCharting
import time
import itertools

def main():
    start_time = time.time()
    url = input("Enter your product URL: \n")
    # Creating an object for constructing review URLs
    link_constructor = ReviewLink(url)
    # Constructing the review URL
    review_url = link_constructor.construct_review_url()
    print(f"Constructed review URL: \n{review_url}")

    # Creating an object of the SeleniumDriver class
    selenium_driver = SeleniumDriver()
    # Setting up the WebDriver
    driver = selenium_driver.get_driver()

    try:
        # Creating an object of the ReviewScraper class
        review_scraper = ReviewScraper(driver)
        page_sources_summarization, page_sources_sentiment = review_scraper.navigate_to_reviews(review_url)

        # Check if we have the required page sources
        if len(page_sources_summarization) >= 2:
            # Parse reviews
            positive_reviews = parse_reviews(page_sources_summarization[0])
            negative_reviews = parse_reviews(page_sources_summarization[1])

            # Combine positive and negative reviews
            reviews_summarization = positive_reviews + negative_reviews

            # Creating ReviewSummarizer Object
            review_summarizer = ReviewSummarizer(reviews_summarization)
            review_summarizer.summarize_reviews()

            print("All reviews parsed successfully")

        # Parse sentiment reviews
        list_parsed_reviews = [parse_reviews(page_source) for page_source in page_sources_sentiment]
        reviews_sentiment = list(itertools.chain.from_iterable(list_parsed_reviews))

        # Creating ReviewCharting Object
        review_charting = ReviewCharting(reviews_sentiment)
        review_charting.classify_reviews()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the driver to reduce system usage
        selenium_driver.close_driver()

    end_time = time.time() - start_time
    print("Time Taken: ",end_time)

if __name__ == "__main__":
    main()