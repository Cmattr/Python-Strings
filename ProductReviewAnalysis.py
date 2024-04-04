reviews = [
     "really good. I'm impressed with this product ish its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
#universal variables
counter = 0

# Task 1
for review in reviews:
    for keyword in keywords:
        if keyword in review.lower():
               
                review = review.replace (keyword, keyword.upper())
        print(review)
            
# Task 2
def good_review(positive_words, reviews, counter):
    for review in reviews:
        for good in positive_words:
            if good in review:
                counter == 0
                counter += 1



i = good_review(positive_words, reviews, counter)
print(f"there are {i} good words")