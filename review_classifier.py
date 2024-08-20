from transformers import pipeline


class ReviewClassifier:
    def __init__(self, reviews):
        self.classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli', device=0)
        self.reviews = reviews

    labels = ["positive", "negative", "somewhat positive", "somewhat negative", "neutral"]

    def classify_reviews(self):
        results = self.classifier(self.reviews, candidate_labels=self.labels)

        for review, result in zip(self.reviews, results):
            print(f"Review: {review}")
            print(f"Classification: {result['labels'][0]} with score {result['scores'][0]:.2f}")
            print()
