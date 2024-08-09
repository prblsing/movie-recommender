import streamlit as st
from mov_recommender import comprehensive_search

# Set the title of the Streamlit app
st.title('Movie Recommendation System')

# Create an input box for the user to enter their movie query
query = st.text_input('Search for a movie', value="Enter your query here")

# Create a button that triggers the recommendation search when clicked
if st.button('Get Recommendations'):
    # Perform the search using the comprehensive search function
    columns, _ = comprehensive_search(query)

    # Display the columns in the DataFrame
    st.write("Columns in the DataFrame:", columns)
