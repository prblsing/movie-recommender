import streamlit as st
from mov_recommender import comprehensive_search

# let's call the app movie search assistance 
st.title('Watch What - Movie Recommendation System')

# put your search query here
query = st.text_input('Search for a movie', value="Enter your filter query here")

if st.button('Get Recommendations'):
    # perform the search using the comprehensive search function
    recommendations, release_years = comprehensive_search(query)
    recommendations['Year'] = release_years
    if 'Year' in recommendations.columns:
        recommendations = recommendations.drop(columns=['Year'])
    if recommendations.shape[1] == 6:
        recommendations.columns = ['Title', 'Genre', 'Year', 'Overview', 'Director', 'Lead Actor']
    else:
        st.warning("Unexpected number of columns in the recommendations DataFrame. Displaying as is.")
    st.table(recommendations.reset_index(drop=True))
