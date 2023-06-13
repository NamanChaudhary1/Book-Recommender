import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books_new.csv'
    data = pd.read_csv(url)
    return data

# Main function
def main():
    st.title("Book Recommendation System")

    # Load the data
    data = load_data()

    # Sidebar options
    st.sidebar.title("Filter Options")
    option = st.sidebar.selectbox("Select filter:", ('Author', 'Genre', 'Height', 'Publisher'))

    # Filter based on Author
    if option == 'Author':
        authors = sorted(data['Author'].unique())
        selected_author = st.sidebar.selectbox("Select author:", authors)
        filtered_data = data[data['Author'] == selected_author]

    # Filter based on Genre
    elif option == 'Genre':
        genres = sorted(data['Genre'].unique())
        selected_genre = st.sidebar.selectbox("Select genre:", genres)
        filtered_data = data[data['Genre'] == selected_genre]

    # Filter based on Height
    elif option == 'Height':
        min_height = st.sidebar.slider("Select minimum height:", 0, 400, 0)
        max_height = st.sidebar.slider("Select maximum height:", min_height, 400, 400)
        filtered_data = data[(data['Height'] >= min_height) & (data['Height'] <= max_height)]

    # Filter based on Publisher
    elif option == 'Publisher':
        publishers = sorted(data['Publisher'].unique())
        selected_publisher = st.sidebar.selectbox("Select publisher:", publishers)
        filtered_data = data[data['Publisher'] == selected_publisher]

    # Display filtered results
    st.write(filtered_data)

if __name__ == '__main__':
    main()



