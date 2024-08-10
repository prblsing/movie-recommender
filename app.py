import streamlit as st
from mov_recommender import comprehensive_search

# let's call the app movie search assistance 
st.title('Watch What - Movie Recommendation System')

# put your search query here
query = st.text_input('Search for a movie', value="Enter your filter query here")

if st.button('Get Recommendations'):
    # perform the search using the comprehensive search function
    recommendations = comprehensive_search(query)
    recommendations.columns = ['Title', 'Genre', 'Year', 'Overview', 'Director', 'Lead Actor']
    st.table(recommendations.reset_index(drop=True))
