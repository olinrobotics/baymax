import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print "Hello, I'm Baymax, your personal healthcare companion"

# Ask the patient for their name
patient_name = raw_input("Who are you? ")
print "Hello, %s!" % patient_name

# Ask the patient how they are
patient_status = raw_input("How are you today?")
print patient_status

#sid = SentimentIntensityAnalyzer()
