#run this inside virtual environment (venv) then install streamlit

import os
import pickle
import streamlit as st
import requests


# Alternate api key, if the other one has exceeded max tries, use this.
# aa0ea97ddb9585fb3be03f74868c3150
# url = "https://api.themoviedb.org/3/movie/{}?api_key=aa0ea97ddb9585fb3be03f74868c3150&language=en-US".format(movie_id)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=aa0ea97ddb9585fb3be03f74868c3150&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_links = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_links.append(f"https://www.themoviedb.org/movie/{movie_id}")

    return recommended_movie_names, recommended_movie_posters, recommended_movie_links


script_dir = os.path.dirname(os.path.abspath(__file__))

movie_list_path = os.path.join(script_dir, 'movie_list.pkl')
similarity_path = os.path.join(script_dir, 'similarity.pkl')


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_links = recommend(selected_movie)
    num_recommendations = len(recommended_movie_names)
    num_cols = min(num_recommendations, 5)  # Maximum of 5 columns

    # Fetch and display the selected movie poster
    selected_movie_id = movies[movies['title'] == selected_movie]['movie_id'].values[0]
    selected_movie_poster = fetch_poster(selected_movie_id)
    selected_movie_link = f"https://www.themoviedb.org/movie/{selected_movie_id}"
    st.markdown(f"**If you liked:**")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"<a href='{selected_movie_link}' target='_blank'><img src='{selected_movie_poster}' width='100%'></a>", unsafe_allow_html=True)
        st.text(selected_movie)

    st.markdown(f"**You should try out these:**")
    cols = st.columns(num_cols)  # Use st.columns instead of st.beta_columns
    for i in range(num_cols):
        with cols[i]:
            st.markdown(f"<a href='{recommended_movie_links[i]}' target='_blank'><img src='{recommended_movie_posters[i]}' width='100%'></a>", unsafe_allow_html=True)
            st.text(recommended_movie_names[i])