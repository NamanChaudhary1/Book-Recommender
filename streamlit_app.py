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

    # Select options
    options = st.multiselect("Select options:", data.columns)

    # Filter the data based on selected options
    filtered_data = data[options]

    # Show the filtered data
    st.write(filtered_data)

if __name__ == "__main__":
    main()

