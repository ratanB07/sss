import streamlit as st
import google.generativeai as genai
import os
import pandas as pd

# Initialize Google Generative AI
os.environ["API_KEY"] = 'AIzaSyCyP-Dd4suFMt459CkpXhWTDZXuNcHVVCc'
genai.configure(api_key=os.environ["API_KEY"])

# Example queries
customer_queries = [
    "I have a problem with my Citi credit card. The payment isn't reflected in my account.",
    "I lost my Citi debit card, and I need to block it immediately. Please help!",
    "I was charged twice for a transaction I made at a store. Can you reverse the duplicate charge?",
    # add more queries
]

# Define the instruction
instruction = 'Summarize customer service conversation in 3 lines. This is easily understandable by the agent.'
model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)

# Store the summaries
summaries = []

# Streamlit app layout
st.title("Customer Query Summarizer")
start = st.button("Start Processing Queries")

if start:
    for query in customer_queries:
        st.write(f"Processing: {query}")
        response = model.generate_content(query)
        summary = response.text.strip()  # Get the summary
        summaries.append({'query': query, 'summary': summary})
        st.write(f"Summary: {summary}")
    
    # Save the results to a file
    df = pd.DataFrame(summaries)
    df.to_csv('summarized_queries.csv', index=False)
    st.success("Summaries saved to 'summarized_queries.csv'!")

    # Provide download link
    st.download_button("Download Summary CSV", df.to_csv(index=False).encode('utf-8'), "summarized_queries.csv", "text/csv")

