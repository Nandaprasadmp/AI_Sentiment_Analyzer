from textblob import TextBlob

print("Welcome to AI Sentiment Analyzer! 😊")
print("Type 'quit' to exit.\n")

while True:
    text = input("Enter a sentence: ")
    if text.lower() == "quit":
        print("Goodbye! 👋")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        print("Sentiment: Positive 😊")
    elif polarity < 0:
        print("Sentiment: Negative 😢")
    else:
        print("Sentiment: Neutral 😐")
