import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the book dataset
books_data = pd.read_csv("books.csv")

# Create a CountVectorizer object to transform the book descriptions into a matrix of token counts
vectorizer = CountVectorizer(stop_words="english")
book_descriptions = vectorizer.fit_transform(books_data["description"].fillna(""))

# Calculate the cosine similarity matrix
cosine_sim = cosine_similarity(book_descriptions)

def get_recommendations(title, category, num_recommendations=5):
    # Filter books by category
    filtered_books = books_data[books_data["category"] == category]

    # Get the index of the selected book
    indices = filtered_books.index[filtered_books["title"] == title].tolist()

    if len(indices) == 0:
        return None

    index = indices[0]

    # Calculate the pairwise similarity scores for the selected book
    similarity_scores = list(enumerate(cosine_sim[index]))

    # Sort the books based on similarity scores
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top recommended books
    top_books_indices = [i[0] for i in sorted_scores[1:num_recommendations+1]]

    return filtered_books.iloc[top_books_indices]["title"]

def main():
    st.title("Book Recommendation System")

    # Input fields for user preferences
    title = st.text_input("Enter the book title:")
    category = st.selectbox("Select the book category:", books_data["category"].unique())

    if st.button("Get Recommendations"):
        recommendations = get_recommendations(title, category)

        if recommendations is None:
            st.error("Book not found. Please check the title and category.")
        else:
            st.success("Recommended Books:")
            st.write(recommendations)

if __name__ == "__main__":
    main()

