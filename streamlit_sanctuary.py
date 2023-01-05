import streamlit as st
import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()


def get_response(question, personality):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Answer the question: {} as if you were {}".format(question, personality),
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response.choices[0].text

def get_image_from_response(personality):
    style = "detailed pixel art"
    response = openai.Image.create(
  prompt="A {} of {}".format(style,personality),
  n=1,
  size="512x512"
)   
    return response.data[0].url


def main():
    st.header("Sanctuary®")
    st.markdown('''#### Ask historical figures anything you want, a sanctuary of knowldege.''')
    st.markdown('''###### Powered by [OpenAI](https://openai.com/)''')

    st.write('---')
    science, music, art, economy = st.tabs(["Science", "Music", "Art", "Economy"])

    with science:
        st.header("Science")
        personality=st.selectbox("Choose your science mind", ["Richard Feynmann", "Stephen Hawkins", "Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", "Galileo Galilei","Other"])
        if personality == "Other":
            personality = st.text_input("Enter your music mind", value="eg: Richard Feynmann", max_chars=None, key=None, type='default')
        question = st.text_input('''Ask your question 🪶''', value="eg: What is the meaning of life?", max_chars=None, key=None, type='default')
        if st.button("Ask", key="science"):
            st.write("You asked {} the question: \"{}\"".format(personality, question))
            answer = get_response(question, personality)
            st.markdown('''### Your answer: \n\"{}\"'''.format(answer.strip()))
            url = get_image_from_response(personality)
            st.image(url)
          
    with music:
        st.header("Music")
        personality = st.selectbox("Choose your music mind", ["Jimi Hendrix", "Miles Davis", "John Coltrane", "Beyonce", "Ludwig van Beethoven","Other"])
        if personality == "Other":
            personality = st.text_input("Enter your music mind", value="eg: Ludwig van Beethoven", max_chars=None, key=None, type='default')
        question = st.text_input('''Ask your question 🪶''', value="eg: How did or do you feel when composing?", max_chars=None, key=None, type='default')
        if st.button("Ask", key="music"):
            st.write("You asked {} the question: \"{}\"".format(personality, question))
            answer = get_response(question, personality)
            st.markdown('''### Your answer: \n\"{}\"'''.format(answer.strip()))
            url = get_image_from_response(personality)
            st.image(url)
    with art:
        st.header("Art")
        personality = st.selectbox("Choose your art mind", [ "Leonardo da Vinci", "Michelangelo", "Raphael", "Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Edgar Degas","Other"])
        if personality == "Other":
            personality = st.text_input("Enter your music mind", value="eg: Raphael", max_chars=None, key=None, type='default')
        question = st.text_input('''Ask your question 🪶''', value="eg: Who was your biggest inspiration?", max_chars=None, key=None, type='default')
        if st.button("Ask", key="art"):
            st.write("You asked {} the question: \"{}\"".format(personality, question))
            answer = get_response(question, personality)
            st.markdown('''### Your answer: \n\"{}\"'''.format(answer.strip()))
            url = get_image_from_response(personality)
            st.image(url)
    with economy:
        st.header("Economy")
        personality = st.selectbox("Choose your economy mind", ["Adam Smith", "John Maynard Keynes", "Karl Marx", "John Stuart Mill", "David Ricardo", "Thomas Malthus", "John Locke","Other"])
        if personality == "Other":
            personality = st.text_input("Enter your music mind", value="eg: John Locke", max_chars=None, key=None, type='default')
        question = st.text_input('''Ask your question 🪶''', value="eg: What economic factor do you thinks is worse for inflation?", max_chars=None, key=None, type='default')
        if st.button("Ask", key="economy"):
            st.write("You asked {} the question: \"{}\"".format(personality, question))
            answer = get_response(question, personality)
            st.markdown('''### Your answer: \n\"{}\"'''.format(answer.strip()))
            url = get_image_from_response(personality)
            st.image(url)


if __name__ == "__main__":
    main() 