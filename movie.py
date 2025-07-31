import streamlit as st
import pickle
import pandas as pd
import lzma

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended = []
    for i in movie_list :
        titles = movies['title'][i[0]]
        description = movies['tags'][i[0]]
        #r=print(f'🎬 {titles}\n📝 description : {description}\n')
        recommended.append(f'🎬 {titles}\n\n📝 description : {description}\n\n\n')
    return recommended



movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(lzma.open('similarity.pkl.xz','rb'))

options = ['select a movie among those in dropdown menu ⬇⬇ tap the selectbox to see the options '] + list(movies['title'].values)
st.title('Movie recommender system')
selected_movie = st.selectbox('I can suggest you 5 movies similar to your selection,let me know where your interest lies :',
             options)
if st.button('suggest'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
