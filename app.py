from openai import OpenAI
import streamlit as st

# Read the API Key and Setup an OpenAI Client
f = open("keys/.openai_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("AI Code Reviewer 🤖")
st.subheader("Automated Code Review at Your Fingertips! 🚀")

# Take User's Input
prompt = st.text_area('Enter your code here:', height=300)

# If the button is clicked, generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "system", "content": "As an expert in code review, your task is to meticulously find bugs and errors, and provide the corrected code."},
        {"role": "user", "content": prompt}
      ],
      max_tokens=400
    )

    # Print the response on Web App
    st.write(response.choices[0].message.content)