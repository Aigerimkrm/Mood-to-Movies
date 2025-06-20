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

target_size = (400, 225)
rows, cols = 2, 5

def create_collage(urls):
    """
    Create a collage image from a list of image URLs.
    """
    images = []
    session = requests.Session()

    for url in urls:
        try:
            response = session.get(url, timeout=5)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGB")
            img = img.resize(target_size)
            images.append(img)
        except Exception as e:
            print(f"Failed to load image {url}: {e}")

    collage_width = target_size[0] * cols
    collage_height = target_size[1] * rows
    collage = Image.new("RGB", (collage_width, collage_height))

    for i, img in enumerate(images):
        if i >= rows * cols:
            break  # avoid overflow
        row = i // cols
        col = i % cols
        x = col * target_size[0]
        y = row * target_size[1]
        collage.paste(img, (x, y))

    return collage


def extract_dominant_colors(image, color_count=6):
    """
    Extract dominant colors from a PIL Image using ColorThief.

    Args:
        image (PIL.Image): The collage image.
        color_count (int): Number of dominant colors to extract.

    Returns:
        List of RGB tuples, e.g. [(r, g, b), ...]
    """
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)

    color_thief = ColorThief(buffer)
    palette = color_thief.get_palette(color_count=color_count)
    return palette

# For sentiment analysis
classifier = pipeline("zero-shot-classification", model='facebook/bart-large-mnli')

def get_emotion_scores(sentences, candidate_labels):
    results = classifier(sentences, candidate_labels=candidate_labels)
    return [dict(zip(r['labels'], r['scores'])) for r in results]
