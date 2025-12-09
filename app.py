import streamlit as st
from data_loader import load_movie_data
from classes.Recommender import Recommender

print("DEBUG: App file loaded")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- NEW CODE ADDED HERE ---
def display_movies(movies):
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create rows of 3 columns
    for i in range(0, len(movies), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(movies):
                movie = movies[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="movie-card">
                        <div class="movie-title">{movie.title}</div>
                        <div class="movie-genres">{movie.genres.replace('|', ' • ')}</div>
                        <div class="movie-description">{movie.description}</div>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    pass