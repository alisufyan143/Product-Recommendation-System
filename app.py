import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import stopwords

# Download stopwords from NLTK
nltk.download('stopwords')

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('/content/sample-data.csv')

data = load_data()

# Initialize TF-IDF Vectorizer with NLTK stopwords
stop_words = list(stopwords.words('english'))
vectorizer = TfidfVectorizer(stop_words=stop_words)

# Fit and transform the descriptions
tfidf_matrix = vectorizer.fit_transform(data['description'])

# Function to get product recommendations based on a query
def get_recommendations(query, tfidf_matrix, data, top_n=5):
    query_vec = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-top_n-1:-1]
    recommendations = data.iloc[related_docs_indices]
    return recommendations

# Streamlit app
st.title("Product Recommendation System")

query = st.text_input("Enter your search query:")
if st.button("Recommend"):
    if query:
        recommendations = get_recommendations(query, tfidf_matrix, data)
        st.write("### Recommendations:")
        st.dataframe(recommendations)
    else:
        st.write("Please enter a query.")

