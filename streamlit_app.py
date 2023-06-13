import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV data from the given URL
@st.cache
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Get book recommendations based on selected criteria
def get_recommendations(title, author, genre, height, publisher, data, num_recommendations=5):
    # Filter books based on selected criteria
    filtered_books = data.copy()
    if title:
        filtered_books = filtered_books[filtered_books["title"].str.contains(title, case=False)]
    if author:
        filtered_books = filtered_books[filtered_books["author"].str.contains(author, case=False)]
    if genre:
        filtered_books = filtered_books[filtered_books["genre"].str.contains(genre, case=False)]
    if height:
        filtered_books = filtered_books[(filtered_books["height"] >= height[0]) & (filtered_books["height"] <= height[1])]
    if publisher:
        filtered_books = filtered_books[filtered_books["publisher"].str.contains(publisher, case=False)]

    if len(filtered_books) == 0:
        return None

    # Create a CountVectorizer object to transform book descriptions into a matrix of token counts
    vectorizer = CountVectorizer(stop_words="english")
    book_descriptions = vectorizer.fit_transform(filtered_books["description"].fillna(""))

    # Calculate cosine similarity matrix
    cosine_sim = cosine_similarity(book_descriptions)

    # Get recommendations for the first book in the filtered list
    index = filtered_books.index[0]
    similarity_scores = list(enumerate(cosine_sim[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_books_indices = [i[0] for i in sorted_scores[1:num_recommendations+1]]

    return filtered_books.iloc[top_books_indices]["title"]

def main():
    st.title("Book Recommendation System")

    # Load the CSV data from the URL
    url = "https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/5b9816dfe88e3bd83131be7278e1a13e0cbb0fde/books.csv"
    data = load_data(url)

    if data is not None:
        # User inputs
        st.subheader("User Inputs")
        title = st.text_input("Enter book title (optional):")
        author = st.text_input("Enter author name (optional):")
        genre = st.text_input("Enter genre (optional):")
        height = st.slider("Select book height range (cm):", min_value=0, max_value=400, value=(0, 400))
        publisher = st.text_input("Enter publisher (optional):")

        if st.button("Get Recommendations"):
            recommendations = get_recommendations(title, author, genre, height, publisher, data)

            if recommendations is None:
                st.error("No books found based on selected criteria.")
            else:
                st.success("Recommended Books:")
                st.write(recommendations)

if __name__ == "__main__":
    main()


