import pandas as pd

# Load the sentiment data from the CSV file
df = pd.read_csv('sentiment_BA_reviews.csv')

# Define thresholds for sentiment categories
df['sentiment_category'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Calculate counts for each sentiment category
total_reviews = len(df)
positive_reviews = len(df[df['sentiment_category'] == 'Positive'])
negative_reviews = len(df[df['sentiment_category'] == 'Negative'])
neutral_reviews = len(df[df['sentiment_category'] == 'Neutral'])

# Calculate percentages
positive_percentage = (positive_reviews / total_reviews) * 100
negative_percentage = (negative_reviews / total_reviews) * 100
neutral_percentage = (neutral_reviews / total_reviews) * 100

# Display the results
print("Skytrax Airline Review Analysis Results")
print("=====================================")
print(f"Total Reviews: {total_reviews}")
print(f"Positive: {positive_reviews} ({positive_percentage:.2f}%)")
print(f"Negative: {negative_reviews} ({negative_percentage:.2f}%)")
print(f"Neutral: {neutral_reviews} ({neutral_percentage:.2f}%)")

# Save the results to a text file
with open('review_analysis_results.txt', 'w') as file:
    file.write("Skytrax Airline Review Analysis Results\n")
    file.write("=====================================\n")
    file.write(f"Total Reviews: {total_reviews}\n")
    file.write(f"Positive: {positive_reviews} ({positive_percentage:.2f}%)\n")
    file.write(f"Negative: {negative_reviews} ({negative_percentage:.2f}%)\n")
    file.write(f"Neutral: {neutral_reviews} ({neutral_percentage:.2f}%)\n")

print("Analysis results saved to review_analysis_results.txt")
