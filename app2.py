import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from rapidfuzz import process, fuzz
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        df_filtered = df[['id', 'name', 'description']].dropna()
        df_filtered['combined'] = df_filtered['name'] + " " + df_filtered['description']
        return df_filtered
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

@st.cache_resource
def compute_embeddings(df_filtered):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df_filtered['combined'].tolist(), convert_to_tensor=True)
    return model, embeddings

def recommend_products(query, model, embeddings, df_filtered, top_n=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    sim_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    product_indices = sim_scores.argsort(descending=True)[:top_n].cpu().numpy()
    return df_filtered.iloc[product_indices][['id', 'name', 'description']]

def fetch_product_image(product_name):
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={product_name.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    if img_tags:
        img_url = img_tags[1].get('src')
        return img_url
    return None

def main():
    st.title('Product Recommendation System')
    query = st.text_input('Enter your query:')
    if st.button('Search'):
        if query:
            df_filtered = load_data('/content/Product Dataset.csv')
            if df_filtered is not None:
                model, embeddings = compute_embeddings(df_filtered)
                recommendations = recommend_products(query, model, embeddings, df_filtered)
                for _, row in recommendations.iterrows():
                    st.subheader(row['name'])
                    img_url = fetch_product_image(row['name'])
                    if img_url:
                        try:
                            image_response = requests.get(img_url)
                            image = Image.open(BytesIO(image_response.content))
                            st.image(image, caption=row['name'])
                        except Exception as e:
                            st.write(f"Could not load image for {row['name']}")
                    else:
                        st.write(f"No image found for {row['name']}")
                    st.write(row['description'])
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
