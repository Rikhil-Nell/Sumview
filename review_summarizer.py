from transformers import pipeline


class ReviewSummarizer:
    def __init__(self, reviews_summarization):
        self.reviews = reviews_summarization


    def summarize_reviews(self):
        review_text = [review['review'] for review in self.reviews]
        summarizer = pipeline('summarization', tokenizer='snowball', lang='en')
        summary = summarizer(review_text)