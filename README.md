## Mood to Movie Project

**By: Aigerim Zhumagulova and Arooshi Dayal** 

This Streamlit app recommends movies and soothing color palettes based on how you're feeling. 
You write a text, the sentiment analyzer will give you the top two emotions based on it and then you see a colorful palette and movie recommendation! 
It blends sentiment analysis, movie recommendations, and color psychology all in one fun experience!

## Instructions on how to run the code: 
1) Download the folder from the Github Repository: https://github.com/Aigerimkrm/Mood-to-Movies
2) Open Anaconda Prompt/Terminal and navigate to the project folder. It will look something like this:
   
   **"C:\Users\Mood-to-Movies-main\Final_Python_Project\final_project"**

4) Install the required packages:

   **pip install -r requirements.txt**
(This will automatically install all the libraries used in the project)

7) To Launch App, run this final command:

   **streamlit run app.py**
   
9) The website will then open on your browser! 

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

## Areas for Future Exploration and Improvement
All of our design choices were made with the intention of maintaining reasonable speed and analytical adequacy. Nonetheless, the project is open to several directions for future development. A natural extension would be to significantly expand this collection to include tens of thousands of titles, increasing the breadth and diversity of recommendations. While we currently work with 19 emotions, future models could incorporate hundreds of emotional categories. Future work could also increase the number of movies' frames used to explore more sophisticated visual features.


