from groq import Groq
import streamlit as st

def parse_with_ollama(dom_chunks, parse_description):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    # Cap at 5 chunks maximum to stay within API limits
    dom_chunks = dom_chunks[:5]
    
    results = []
    for i, chunk in enumerate(dom_chunks):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Extract the following from this content: {parse_description}\n\n"
                        f"Content:\n{chunk}\n\n"
                        "Return only the extracted data, nothing else. "
                        "If the information is not present, say 'Not found'."
                    )
                }
            ],
            max_tokens=1000
        )
        results.append(response.choices[0].message.content)
    return "\n".join(results)
