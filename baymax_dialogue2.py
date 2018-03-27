# Sources:
# http://opensourceforu.com/2016/12/analysing-sentiments-nltk/

# Import and download natural language toolkit
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print "Hello, I'm Baymax, your personal healthcare companion"

# Ask the patient for their name
patient_name = raw_input("Who are you? ")
print "Hello, %s!" % patient_name

# Ask the patient how they are
patient_status = raw_input("How are you today? ")
print patient_status

# Sentiment analysis proof of concept
sid = SentimentIntensityAnalyzer()
patient_sentiment = sid.polarity_scores(patient_status)

if patient_sentiment['pos'] > patient_sentiment['neg']:
    print "That's good!"
else:
    print "Oh no! How can I help?"
