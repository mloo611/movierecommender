import streamlit as st
from data_loader import load_movie_data
from classes.Recommender import Recommender

def main():
    st.title("Movie Recommender")

    df = load_movie_data()

    # Show dataset preview
    st.subheader("Movie Dataset")
    st.dataframe(df.head())

    # Build genre list
    all_genres = sorted({g for row in df["genres"] for g in row.split("|")})

    st.subheader("Select your favorite genres:")
    selected_genres = st.multiselect("Choose genres:", all_genres)

    recommender = Recommender(df)

    if st.button("Recommend"):
        if not selected_genres:
            st.warning("Please select at least one genre!")
        else:
            results = recommender.recommend_by_genre(selected_genres, top_k=5)
            st.subheader("Recommended Movies:")
            for movie in results:
                st.write(f"- **{movie.title}** — {movie.genres}")

if __name__ == "__main__":
    main()
