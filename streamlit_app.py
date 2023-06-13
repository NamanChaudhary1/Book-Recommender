import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/1b98e8f8b9e65f892a8be27a02dc2dc042a1e867/books.csv'
    data = pd.read_csv(url)
    return data

data = load_data()

# Sidebar options
option = st.sidebar.selectbox('Filter by:', ('Author', 'Genre', 'Height', 'Publisher'))

# Filter data based on user selection
if option == 'Author':
    authors = sorted(data['Author'].unique())
    selected_author = st.sidebar.selectbox('Select Author:', authors)
    filtered_data = data[data['Author'] == selected_author]

elif option == 'Genre':
    genres = sorted(data['Genre'].unique())
    selected_genre = st.sidebar.selectbox('Select Genre:', genres)
    filtered_data = data[data['Genre'] == selected_genre]

elif option == 'Height':
    min_height, max_height = st.sidebar.slider('Select Height Range:', 0, 400, (0, 400))
    filtered_data = data[(data['Height'] >= min_height) & (data['Height'] <= max_height)]

else:  # Publisher
    publishers = sorted(data['Publisher'].unique())
    selected_publisher = st.sidebar.selectbox('Select Publisher:', publishers)
    filtered_data = data[data['Publisher'] == selected_publisher]

# Display filtered data
st.dataframe(filtered_data)


