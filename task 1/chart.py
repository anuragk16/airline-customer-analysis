import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
import re

# Download the stopwords dataset if not already downloaded
nltk.download('stopwords')

# Load the cleaned reviews from the CSV file
df = pd.read_csv('sentiment_BA_reviews.csv')

# Set of stopwords in English and add custom stopwords
stop_words = set(stopwords.words('english'))
custom_stopwords = set([',', '|', '-', 'get', 'got', 'like', 'also', 'even', 'would', 'could', 'one', 'us', 'go', 'make', 'see', 'still'])
stop_words.update(custom_stopwords)

# Tokenize the words in the cleaned reviews, filter out stopwords, and remove non-alphanumeric characters
all_words = [word for review in df['cleaned_reviews'] 
             for word in re.findall(r'\b\w+\b', review.lower()) if word not in stop_words]

# Count the frequency of each word
word_counts = Counter(all_words)

# Convert to a DataFrame for easy plotting
word_freq_df = pd.DataFrame(word_counts.items(), columns=['word', 'frequency'])

# Sort by frequency in descending order
word_freq_df = word_freq_df.sort_values(by='frequency', ascending=False)

# Plot the top 20 most frequent meaningful words
plt.figure(figsize=(12, 8))
plt.barh(word_freq_df['word'].head(10)[::-1], word_freq_df['frequency'].head(10)[::-1], color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 10 Most Frequent Meaningful Words in BA Reviews')
plt.tight_layout()
plt.savefig("word_frequency_chart_filtered_v2.png")
plt.show()

print("Word frequency chart (filtered v2) saved to word_frequency_chart_filtered_v2.png")
