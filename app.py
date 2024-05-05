import streamlit as st
import pickle
import requests

similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pickle.load(open("movies.pkl", "rb"))


def fetch_image(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=0de386c4ce9d82fa805d1a1176a8b294&language=en-US".format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_image(movie_id))
    return recommended_movies, recommended_movies_poster


st.title("Movie Recommendation Tool")

option = st.selectbox("Which Movie do you want to", movies["title"].values)

if st.button("Recommend"):
    name, poster = recommend(option)

    columns_per_row = 5

    for i in range(0, min(len(name), 15), columns_per_row):
        cols = st.columns(columns_per_row)
        for j, col in enumerate(cols):
            if i + j < len(name):
                col.text(name[i + j])
                col.image(poster[i + j])

