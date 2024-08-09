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

    # Add debug information to see column names
    st.write("Columns in the recommendations DataFrame:", recommendations.columns)

    # Attempt to access columns based on actual names in the DataFrame
    try:
        # Add the release years to the recommendations DataFrame
        recommendations['Year'] = release_years

        # Rename the columns to be more user-friendly and correctly aligned
        recommendations = recommendations[['Series_Title', 'Genre', 'Year', 'Overview', 'Director', 'Star1', 'IMDB_Rating']]
        recommendations.columns = ['Title', 'Genre', 'Year', 'Overview', 'Director', 'Lead Actor', 'IMDb Rating']

        # Display the results in a table format with the index starting from 1
        st.table(recommendations.reset_index(drop=True))
    except KeyError as e:
        st.error(f"KeyError: {e}. Available columns: {recommendations.columns}")

