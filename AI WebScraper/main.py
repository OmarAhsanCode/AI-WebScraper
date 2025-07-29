import streamlit as st
from scrape import (scrape_website, extract_body_content, clean_body_content, split_dom_content)
from parse import parse_with_ollama

st.title('AI Web Scraper')

url = st.text_input('Enter Website URL:')

if st.button('Scrape Site:'):
    st.write('Scraping...')
    result = scrape_website(url)
    body_content = extract_body_content(result) # Extract the body content
    cleaned_content = clean_body_content(body_content) # Clean the body content
    
    st.session_state.dom_content = cleaned_content # Store the cleaned content in the session state

    with st.expander('View DOM Content:'):
        st.text_area('DOM Content:', value=cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse:")

    if st.button('Parse Content:'):
        if parse_description:
            st.write('Parsing...')

            dom_chunks = split_dom_content(st.session_state.dom_content) # Split the content into chunks of 6000 characters
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)

