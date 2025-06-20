import pandas as pd
from utils import get_emotion_scores

movies1000 = pd.read_csv('movies1000.csv')

test_movies_df = movies1000[150:160]
print(test_movies_df)
# emotion_dicts_test = test_movies_df['description'].apply(lambda desc: get_emotion_scores_safe(desc, emotions))
# emotion_df_test = pd.DataFrame(emotion_dicts_test.tolist())
#
# print(emotion_df_test)
# test_movies_df = pd.concat([test_movies_df, emotion_df_test], axis=1)
# test_movies_df['vector'] = test_movies_df[emotions].apply(lambda row: row.values, axis=1)
#
#
# print(test_movies_df)

emotions = [
    'Happy', 'Sad', 'Angry', 'Calm', 'Nostalgic', 'Anxious', 'Depressed',
    'Moody', 'Elated', 'Relaxed', 'Joyful', 'Disappointed', 'Relief',
    'Gratitude', 'Bored', 'Pride', 'Jealous', 'Optimistic', 'Passion'
]

descriptions_test = test_movies_df['description'].tolist()
scores_list_test = get_emotion_scores(descriptions_test, emotions)
emotion_df_test = pd.DataFrame(scores_list_test)
test_movies_df = pd.concat([test_movies_df, emotion_df_test], axis=1)
test_movies_df['vector'] = test_movies_df[emotions].apply(lambda row: row.values, axis=1)

print(test_movies_df)

print('Stage 5 is finished')



