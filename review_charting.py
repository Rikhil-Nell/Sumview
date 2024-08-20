from review_classifier import ReviewClassifier
import matplotlib.pyplot as plt
class ReviewCharting(ReviewClassifier):

    def __init__(self, reviews_sentiment):
        self.reviews = reviews_sentiment


    def charting (self):
        review_text = [review['review'] for review in self.reviews]
        review_dates = [review['date'] for review in self.reviews]

        # Creating ReviewClassifier Object
        review_classifier = ReviewClassifier(review_text)
        review_classifier.classify_reviews()

