import pandas as pd
import numpy as np
import ast
import math
import re

from .sentiment import get_emotion_scores
from .visualization import get_palette_for_emotion

# Load data once
movies_df = pd.read_csv("Movies_Data.csv")
def clean_and_parse_array(s):
    # Remove 'array([[...]]' wrapper if present
    s_clean = re.sub(r'^array\(\[\[|\]\]\)$', '', s.strip())
    # Remove any redundant whitespace
    s_clean = re.sub(r'\s+', ', ', s_clean)
    return np.array(ast.literal_eval(f"[{s_clean}]"))

movies_df['vector'] = movies_df['vector'].apply(clean_and_parse_array)


def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def similarity_percentage(dominant_colors, palette, threshold=60):
    matches = 0
    for color in dominant_colors:
        if any(color_distance(color, p_color) < threshold for p_color in palette):
            matches += 1
    return (matches / len(dominant_colors)) * 100

def recommend_movie(user_text, user_scores):
    emotions = [
    'Happy', 'Sad', 'Angry', 'Calm', 'Nostalgic', 'Anxious', 'Depressed',
    'Moody', 'Elated', 'Relaxed', 'Joyful', 'Disappointed', 'Relief',
    'Gratitude', 'Bored', 'Pride', 'Jealous', 'Optimistic', 'Passion'
    ]
    user_vector = pd.DataFrame(user_scores)[emotions].values[0]

    top10 = movies_df.loc[
        movies_df['vector']
        .apply(lambda x: np.linalg.norm(x - user_vector))
        .nsmallest(10)
        .index
    ]

    top1_emotion = sorted(user_scores[0].items(), key=lambda x: x[1], reverse=True)[0][0]
    top2_emotion = sorted(user_scores[0].items(), key=lambda x: x[1], reverse=True)[1][0]

    user_palette_emotion1 = get_palette_for_emotion(top1_emotion)
    user_palette_emotion2 = get_palette_for_emotion(top2_emotion)

    results = []

    for index, row in top10.iterrows():
        palette_movie = ast.literal_eval(row['dominant_colors'])
        sim1 = similarity_percentage(palette_movie, user_palette_emotion1)
        sim2 = similarity_percentage(palette_movie, user_palette_emotion2)
        combined = sim1 + sim2

        results.append({
            'movie': row,
            'combined_similarity': combined,
            'rating': row['rating']
        })

    results_df = pd.DataFrame(results)
    best_row = results_df.loc[results_df['combined_similarity'].idxmax()]
    best_movie = best_row['movie']

    collage_urls = ast.literal_eval(best_movie['backdrop_urls'])

    return best_movie, collage_urls
