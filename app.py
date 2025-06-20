import streamlit as st
import pandas as pd
import numpy as np
from utils.sentiment import get_emotion_scores
from utils.recommend import recommend_movie
from utils.visualization import display_gradient_palette, create_collage_from_urls

st.set_page_config(page_title="Emotion-Based Movie Recommender 🎬")

st.title("🎭 Emotion-Based Movie & Color Recommender")
user_input = st.text_input("Type a sentence describing your mood:", "")

if user_input:
    st.markdown("### 🔍 Analyzing Sentiment...")
    emotions = ['Happy', 'Sad', 'Angry', 'Calm', 'Nostalgic', 'Anxious', 'Depressed', 'Moody', 'Elated', 'Relaxed', 'Joyful', 'Disappointed', 'Relief',
    'Gratitude', 'Bored', 'Pride', 'Jealous', 'Optimistic', 'Passion']
    emotion_scores = get_emotion_scores(user_input, emotions)
    
    top_emotions = sorted(emotion_scores[0].items(), key=lambda x: x[1], reverse=True)[:2]
    top1, top2 = top_emotions[0], top_emotions[1]
    
    st.markdown(f"**Top Emotion:** {top1[0]} ({top1[1]:.2f})")
    st.markdown(f"**Second Emotion:** {top2[0]} ({top2[1]:.2f})")

    st.markdown("### 🎨 Emotion Color Palette")
    palette1 = display_gradient_palette(top1[0])
    palette2 = display_gradient_palette(top2[0])

    st.image(palette1, caption=f"Palette for {top1[0]}", use_column_width=False)
    st.image(palette2, caption=f"Palette for {top2[0]}", use_column_width=False)

    st.markdown("### 🎬 Recommended Movie:")
    best_movie, collage_urls = recommend_movie(user_input, emotion_scores)
    
    st.markdown(f"**Title:** {best_movie['title']}")
    st.markdown(f"**Description:** {best_movie['description']}")
    st.markdown(f"⭐ **Rating:** {best_movie['rating']}")

    collage = create_collage_from_urls(collage_urls)
    st.image(collage)
