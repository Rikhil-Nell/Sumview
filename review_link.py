import re


class ReviewLink:
    def __init__(self, url):
        self.url = url

    def construct_review_url(self):
        # Extract ASIN from the product URL
        asin_match = re.search(r'/dp/([A-Z0-9]{10})', self.url)
        if asin_match:
            asin = asin_match.group(1)
            # Construct the review URL
            review_url = f'https://www.amazon.in/product-reviews/{asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
            return review_url
        else:
            raise ValueError("ASIN not found in the product URL.")
