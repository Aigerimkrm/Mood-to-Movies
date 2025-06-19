import streamlit as st
from emotion_palette import predict_emotion_and_palette, generate_gradient_image

st.set_page_config(page_title="🎨 Emotion Color Palette", layout="centered")
st.title("🎭 Sentiment to Color Palette Generator")

user_input = st.text_area("Enter a sentence to analyze:", height=150)

if st.button("Analyze"):
    if user_input.strip():
        emotion, score, palette = predict_emotion_and_palette(user_input)
        st.success(f"**Predicted Emotion:** {emotion}  \n**Confidence:** {score:.2f}")

        st.subheader("Color Palette:")
        st.image(generate_gradient_image(palette), caption=f"{emotion} palette")
    else:
        st.warning("Please enter some text.")
