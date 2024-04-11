import re
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

counter = 0


# Task 1: Keyword Highlighter

for review in reviews: 
    for keyword in keywords:
        if (keyword in review.lower()):
            capital = review.replace(keyword.lower(), keyword.upper())
            print(capital)
            
    else:
        print()

# Task 2: Sentiment Tally
def good_review(positive_words, reviews, counter):
    for review in reviews:
        for good in positive_words:
            if good in review:
                counter += 1
            
    return(counter)

def good_review(negative_words, reviews, counter):
    for review in reviews:
        for bad in negative_words:
            if bad in review:
                counter += 1
            
    return(counter)

# Task 3: Review Summary
def create_summary(review, max_length=30):
    words = review.split()
    
    summary = ""

    for word in words:
       
        if len(summary) + len(word) + 1 <= max_length:
            summary += word + " "
        else:
            break

   
    summary = summary.strip() + "..."
    return summary


summaries = [create_summary(review) for review in reviews]


bad = good_review(negative_words, reviews, counter)
print(f"there are {bad} bad words ")

good = good_review(positive_words, reviews, counter)
print(f"there are {good} good words \n ")

for i, summary in enumerate(summaries):
    print(f"Review {i+1}: {summary}")
