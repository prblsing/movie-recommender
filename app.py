import streamlit as st
from mov_recommender import comprehensive_search

# Set the title of the Streamlit app
st.title('Movie Recommendation System')

# Create an input box for the user to enter their movie query
query = st.text_input('Search for a movie', value="Enter your filter criteria here")

if st.button('Get Recommendations'):
    # Perform the search using the comprehensive search function
    recommendations, release_years = comprehensive_search(query)
    recommendations['Year'] = release_years
    recommendations = recommendations[['Series_Title', 'Genre', 'Released_Year', 'Overview', 'Director', 'Star1']]
    recommendations.columns = ['Title', 'Genre', 'Year', 'Overview', 'Director', 'Lead Actor']
    st.table(recommendations.reset_index(drop=True))
