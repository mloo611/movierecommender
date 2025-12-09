import streamlit as st
from data_loader import load_movie_data
from classes.Recommender import Recommender

print("DEBUG: App file loaded")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    pass  # We will add the main function later