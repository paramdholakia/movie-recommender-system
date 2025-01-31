import pandas as pd
import  pickle
import streamlit as st


def recommend_movie(movie):
    movie_index = movies[movies_dict['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    reccomendations = []
    for i in movies_list:
        movie_id = i[0]
        reccomendations.append(movies.iloc[i[0]].title)
    return reccomendations

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movies Recommendation System')

