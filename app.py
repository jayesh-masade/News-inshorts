# import streamlit as st
# import requests
# from transformers import pipeline

# API_KEY = 'd3d5f0b1cac34f6bb0e797e5af210804'  # Replace this with your actual News API key
# URL = 'https://newsapi.org/v2/top-headlines?'

# # Initialize the summarization pipeline
# summarizer = pipeline("summarization")

# def get_news(category='general', country='us'):
#     """ Fetch news articles from the API based on category and country. """
#     params = {
#         "category": category,
#         "country": country,
#         "apiKey": API_KEY
#     }
#     response = requests.get(URL, params=params)
#     data = response.json()
#     return data.get('articles', [])

# def summarize_text(text):
#     """ Generate a summary for the given text. """
#     summary_text = summarizer(text, max_length=200, min_length=60, do_sample=False)
#     return summary_text[0].get('summary_text', '')

# def display_news(articles):
#     """ Display the news articles with titles, descriptions, and summaries. """
#     for article in articles:
#         st.subheader(article['title'])
#         st.write(article['description'])
#         if (article['content'] is not None) and  (len(article['content']) > 100):  # Ensure there's enough text to summarize
#             summary = summarize_text(article['content'])
#             st.write( summary)
#         st.markdown(f"[Read more]({article['url']})")
#         st.write("---")

# def main():
#     """ The main function of the app. """
#     st.title("N App")

#     country = st.sidebar.selectbox("Select Country", ['us', 'gb', 'ca', 'au', 'ru', 'fr', 'in'])
#     category = st.sidebar.selectbox(
#         "Select Category",
#         ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
#     )

#     if st.sidebar.button('Fetch News'):
#         st.subheader(f"Top headlines for {category} news in {country.upper()}")
#         articles = get_news(category, country)
#         if articles:
#             display_news(articles)
#         else:
#             st.error("No news articles found. Please try a different category or country.")

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
from transformers import pipeline

API_KEY = 'd3d5f0b1cac34f6bb0e797e5af210804'  # Replace this with your actual News API key
URL = 'https://newsapi.org/v2/top-headlines?'

# Initialize the summarization pipeline
try:
    summarizer = pipeline("summarization")
except Exception as e:
    print(f"Error initializing the summarization pipeline: {str(e)}")

def get_news(category='general', country='us'):
    """ Fetch news articles from the API based on category and country. """
    params = {
        "category": category,
        "country": country,
        "apiKey": API_KEY
    }
    response = requests.get(URL, params=params)
    data = response.json()
    return data.get('articles', [])

def summarize_text(text):
    """ Generate a summary for the given text. """
    summary_text = summarizer(text, max_length=200, min_length=60, do_sample=False)
    return summary_text[0].get('summary_text', '')

def display_news(articles):
    """ Display the news articles with titles, descriptions, and summaries. """
    for article in articles:
        if article['urlToImage']:  # Check if there is an image URL
            st.image(article['urlToImage'], width=300)  # Display the image as a thumbnail
        st.subheader(article['title'])
        st.write(article['description'])
        if (article['content'] is not None) and  (len(article['content']) > 100):  # Ensure there's enough text to summarize
            summary = summarize_text(article['content'])
            st.write(summary)
        st.markdown(f"[Read more]({article['url']})")
        st.write("---")

def main():
    """ The main function of the app. """
    st.title("News App")

    country = st.sidebar.selectbox("Select Country", ['us', 'gb', 'ca', 'au', 'ru', 'fr', 'in'])
    category = st.sidebar.selectbox(
        "Select Category",
        ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    )

    if st.sidebar.button('Fetch News'):
        st.subheader(f"Top headlines for {category} news in {country.upper()}")
        articles = get_news(category, country)
        if articles:
            display_news(articles)
        else:
            st.error("No news articles found. Please try a different category or country.")

if __name__ == "__main__":
    main()
