import streamlit as st
import openai as ai

st.set_page_config(page_title = "Financial Literacy Chatbot", layout = "wide")

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

try:
  ai.api_key = "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"
except:
  st.text('Add API Key')

def chatgpt_call(prompt, model, temperature):
  completion = ai.ChatCompletion.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature
  )
  return completion['choices'][0]['message']['content']

st.header('Financial Literacy Chatbot :money_with_wings: :money_with_wings:')
st.subheader('Presented by BRHS Girls Who Code')
st.write(
  """
  Financial literacy has become imperative to succesfully navigate through life in the modern day. As high schoolers, we feel as though we are not exposed to financial literacy, often leaving us clueless about how to properly manage money.
  This chatbot is designed to help highschoolers (like us!) with any financial literacy questions.
""")
st.write('[If you want to find out more about the BRHS Girls Who Code club, click here](https://www.instagram.com/girls.who.code.brhs/)')
  
  
topic = st.text_input('Please Enter What You Want To Know About Financial Literacy')
model = 'gpt-3.5-turbo'
temperature = 0.5
st.sidebar.markdown("This app uses OpenAI's generative AI. Please use it carefully and check any output as it could be biased or wrong. ")

prompt = f"You are an expert teacher in financial literacy. If the topic entered does not have to do with financial literacy or finance in general, please reply with: Sorry, this topic does not have to do with financial literacy or finance. For example, if the user asked about world war 2, please answer with: Sorry, this topic does not have to do with financial literacy or finance. Make sure that the user only asks about finance related questions, and reprompt the user if they ask about something else. Please ask me a more relevant question. Explain the topic as if you were talking to a high schooler who is eager to learn more about financial literacy: {topic}"

explanation = chatgpt_call(prompt, model, temperature)

generate = st.button('Generate Response')

if generate:
  st.markdown(explanation)
  st.balloons()