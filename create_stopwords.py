import pickle
from nltk.corpus import stopwords
import nltk

# Run once to download stopwords
nltk.download("stopwords")

# Get English stopwords
STOP_WORDS = set(stopwords.words("english"))

# Save as pickle
with open("stopwords.pkl", "wb") as f:
    pickle.dump(STOP_WORDS, f)

print("stopwords.pkl created successfully ✅")
