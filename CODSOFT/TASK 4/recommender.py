
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# path of CSV 
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data.csv")
if not os.path.exists(csv_path):
    print(f"ERROR: '{csv_path}' not found. Make sure data.csv is in the same folder as this script.")
    exit()

#  dataset
data = pd.read_csv(csv_path)

#  DESCRIPTION
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['description'])

# Searching similarity matrixes
similarity_matrix = cosine_similarity(tfidf_matrix)

# Searchin for familar title even if badly typed
def match_title(user_text):
    all_titles = data['title'].tolist()
    matches = get_close_matches(user_text, all_titles, n=1, cutoff=0)  # always return something
    return matches[0] if matches else None

# recommending familar item to  user in the same category
def get_recommendations(name, how_many=3):
    idx = data.index[data['title'] == name][0]
    category = data.loc[idx, 'category']

    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    same_type = [(i, s) for i, s in scores if data.loc[i, 'category'] == category and i != idx]
    top_items = [data['title'].iloc[i] for i, _ in same_type[:how_many]]

    return category, top_items

#MAIN FUCTION
if __name__ == "__main__":
    item = input("Type anything movie, book, or product name: ")
    found_title = match_title(item)

    if found_title:
        category, recs = get_recommendations(found_title)
        print(f"\nClosest match found: '{found_title}' ({category})")
        print("You might also like these:")
        for r in recs:
            print("-", r)
    else:
        print("No items found at all. Please check your dataset or try typing something else.")