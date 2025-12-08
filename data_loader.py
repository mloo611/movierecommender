import pandas as pd

def load_movie_data(path="movie_data.csv"):
    return pd.read_csv(path)
