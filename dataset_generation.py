import requests
from bs4 import BeautifulSoup as bs
import json
from PIL import Image
from io import BytesIO
from colorthief import ColorThief
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from transformers import pipeline

# custom function:
from utils import create_collage, extract_dominant_colors, get_emotion_scores

api_key = "3039136bdade60a401af3af4c8024a39"
params = {"api_key": api_key}
headers = {"accept": "application/json"}

top_movies = []
page = 1
session = requests.Session()

while len(top_movies) < 1000:
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
        'api_key': api_key,
        'page': page
    }

    try:
        response = session.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Request failed on page {page}: {e}")
        break

    results = data.get('results', [])
    if not results:
        print("No more results.")
        break

    top_movies.extend(results)
    page += 1

print('Stage 1 is finished')

movies_data = []

for movie in top_movies:
    movie_id = movie.get('id')

    try:
        response = session.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}/images',
            params={'api_key': api_key},
            timeout=5
        )
        response.raise_for_status()
        backdrops = response.json().get('backdrops', [])
    except requests.RequestException as e:
        print(f"Error fetching images for movie ID {movie_id}: {e}")
        backdrops = []

    selected_backdrops = random.sample(backdrops, min(10, len(backdrops)))
    backdrop_urls = [f"https://image.tmdb.org/t/p/w1280{img['file_path']}" for img in selected_backdrops]

    movies_data.append({
        'id': movie_id,
        'title': movie.get('title', ''),
        'description': movie.get('overview', ''),
        'rating': movie.get('vote_average'),
        'poster_url': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else None,
        'backdrop_urls': backdrop_urls
    })

movies_df = pd.DataFrame(movies_data)
print('Stage 2 is finished')

# Account for NA values:
movies_df = movies_df.dropna().reset_index(drop=True)

target_size = (400, 225)
rows, cols = 2, 5

movies_df['collage'] = movies_df['backdrop_urls'].apply(create_collage)
print('Stage 3 is finished')

movies_df['dominant_colors'] = movies_df['collage'].apply(extract_dominant_colors)
print('Stage 4 is finished')

# A small section to add vectors representing sentiment analysis of the movies' descriptions:
emotions = [
    'Happy', 'Sad', 'Angry', 'Calm', 'Nostalgic', 'Anxious', 'Depressed',
    'Moody', 'Elated', 'Relaxed', 'Joyful', 'Disappointed', 'Relief',
    'Gratitude', 'Bored', 'Pride', 'Jealous', 'Optimistic', 'Passion'
]

descriptions = movies_df['description'].tolist()
scores_list = get_emotion_scores(descriptions, emotions)
emotion_df = pd.DataFrame(scores_list)
movies_df = pd.concat([movies_df, emotion_df], axis=1)
movies_df['vector'] = movies_df[emotions].apply(lambda row: row.values, axis=1)

print('Stage 5 is finished')