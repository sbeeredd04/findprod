import os
import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")


def improve_prompt(original_prompt):
    system_message = """You are an expert at improving prompts for language models. Your task is to take the given prompt and enhance it to be more specific, detailed, and effective. The improved prompt should help language models provide better, more accurate, and more relevant responses."""

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Please improve this prompt: '{original_prompt}'"}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content


st.title("Prompt Improvement Tool")

st.write("Enter your original prompt, and our AI will help improve it for better results.")

original_prompt = st.text_area("Enter your original prompt:", height=100)

if st.button("Improve Prompt"):
    if original_prompt:
        with st.spinner("Improving your prompt..."):
            improved_prompt = improve_prompt(original_prompt)

        st.subheader("Improved Prompt:")
        st.write(improved_prompt)
    else:
        st.warning("Please enter a prompt to improve.")

st.markdown("---")
st.write("This tool uses the GroqCloud LLM API to enhance your prompts.")
