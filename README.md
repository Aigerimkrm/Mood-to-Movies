## Emotion-Based Movie and Color Palette Recommender

**By: Aigerim Zhumagulova and Arooshi Dayal** 

This Streamlit app recommends movies and soothing color palettes based on how you're feeling. 
Just type a sentence describing your mood (or any sentence you want!) and the app will analyze your sentiment and identify your top two emotions. Then it shows:

- Two emotion-driven color palettes

- A personalized movie recommendation

- A visual collage from the movie scenes

It’s a fun blend of sentiment analysis, color psychology, and movie discovery. 

## Instructions on how to run the code: 
We recommend using Python 3.12.x (e.g., 3.12.7) for this project.
The code has been tested on Python 3.12 and all required packages are fully compatible with this version.
Using earlier or later versions may result in compatibility issues or unexpected errors.

1) Download the folder from the Github Repository: https://github.com/Aigerimkrm/Mood-to-Movies
2) Open Anaconda Prompt/Terminal and navigate to the `final_project` folder, i.e. use the similar looking command `cd "C:\Users\PythonProjects\Mood-to-Movies-main\Final_Python_Project\final_project"`
3) Install the required packages by using the command `pip install -r requirements.txt` (This will automatically install all the libraries used in the project)
4) To Launch App, run this final command: `streamlit run app.py`
5) The website will then open on your browser! 

## Dataset Generation

While the Streamlit application utilizes our pre-compiled CSV file containing 2,000 movies, we also provide the full source code required to generate this dataset from scratch. The movie information was retrieved from [The Movie Database (TMDB)](https://www.themoviedb.org/) using their public API. Access to the API required personal API keys, which were employed to extract the most relevant metadata for each movie.

Most notably, the dataset includes:
1) **Movie descriptions**, which were used for text-based sentiment analysis using models from the transformers package. This step allowed for a richer understanding of each movie’s thematic tone.
2) **A sample of 10 random frames from movies**, from which we extracted dominant color palettes. These color features are intended to capture the visual aesthetic associated with each film.

## Matching Algorithm
To determine which movies align most closely with the emotional content of a user’s input text, we applied the following methodology:
1)	**Sentiment Vectorization**

The user’s input text is processed by a pre-trained sentiment model to produce a 19-dimensional emotion vector, with each dimension corresponding to the intensity of a specific emotion. Each movie in the dataset is also represented as a 19-dimensional vector, derived from its description. To identify the most relevant movies, we compute Euclidean distances between the user’s vector and those of all movies in the database.

2)	**Aesthetic Refinement via Color Matching**

Rather than selecting only the single closest match, we retain the 10 nearest movies based on emotion-space distance. From this subset, we evaluate aesthetic similarity by comparing the dominant color palettes of these movies with a predefined color palette representing the user’s top emotional states. 


This dual-stage filtering process aims to provide recommendations that not only align with the emotional content of the user's input, but also visually resonate with the conveyed mood.
We view this approach as a certain trade-off between the robustness of language-based vector analysis and our curiosity-driven exploration of aesthetic dimensions. 

## Illustrative Example
Here is an example of what you should achieve after following our instructions:

![Streamlit output photo 1 ](https://github.com/user-attachments/assets/5c2a6658-a60f-4299-ae52-0557028afe63)

Some users might initially find it unusual that the system recommends a sad movie in response to a sad mood. While it may seem peculiar at first, we believe that watching a movie that resonates emotionally can be both comforting and validating. 

## Areas for Future Exploration and Improvement
All of our design choices were made with the intention of maintaining reasonable speed and analytical adequacy. Nonetheless, the project is open to several directions for future development. A natural extension would be to significantly expand this collection to include tens of thousands of titles, increasing the breadth and diversity of recommendations. While we currently work with 19 emotions, future models could incorporate hundreds of emotional categories. Future work could also increase the number of movies' frames used to explore more sophisticated visual features.


