import streamlit as st
from mov_recommender import comprehensive_search

# Set the title of the Streamlit app
st.title('Movie Recommendation System')

# Create an input box for the user to enter their movie query
query = st.text_input('Search for a movie', value="Enter your query here")

# Create a button that triggers the recommendation search when clicked
if st.button('Get Recommendations'):
    # Perform the search using the comprehensive search function
    recommendations, release_years = comprehensive_search(query)

    # Add the release years to the recommendations DataFrame
    recommendations['Year'] = release_years

    # Drop the redundant 'Year' column if it exists
    if 'Year' in recommendations.columns:
        recommendations = recommendations.drop(columns=['Year'])

    # Check the number of columns before renaming
    if recommendations.shape[1] == 6:
        # Rename the columns to be more user-friendly
        recommendations.columns = ['Title', 'Genre', 'Year', 'Overview', 'Director', 'Lead Actor']
    else:
        st.warning("Unexpected number of columns in the recommendations DataFrame. Displaying as is.")

    # Display the results in a table format with the index starting from 1
    st.table(recommendations.reset_index(drop=True))
