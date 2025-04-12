import streamlit as st
import openai

# Set your OpenAI API key
# openai.api_key = "your-api-key-here"

def explain_code(code):
    prompt = f"Explain the following code in simple terms:\n\n{code}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use gpt-3.5-turbo-instruct or your preferred engine
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )
    
    return response.choices[0].text.strip()

# Streamlit UI
st.set_page_config(page_title="AI Code Explainer", page_icon="💡")
st.title("💡 AI-Powered Code Explainer")
st.markdown("Paste your code below and get a plain-English explanation.")

# Input Area
code_input = st.text_area("📝 Paste your code here", height=300)

if st.button("Explain Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Thinking... 🤔"):
            explanation = explain_code(code_input)
        st.success("Here's the explanation:")
        st.markdown(f"```markdown\n{explanation}\n```")