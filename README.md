---

# Product Recommendation System

## Overview
This project demonstrates a Product Recommendation System built with Python, leveraging advanced NLP models like Sentence Transformers to provide accurate recommendations based on product descriptions. The system is designed to enhance e-commerce platforms by suggesting relevant products to users based on their search queries.

## Features
- **Sentence Transformers**: Utilizes Sentence Transformers to convert textual data into numerical embeddings.
- **Cosine Similarity**: Calculates the similarity between the user's query and product descriptions to find the most relevant products.
- **Interactive Streamlit App**: Provides a user-friendly interface to input search queries and view recommendations in real-time.
- **Image Fetching**: Fetches product images from Google based on the product name.

## Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- pandas
- sentence-transformers
- requests
- BeautifulSoup4
- Pillow

### Install Required Libraries
```bash
pip install streamlit pandas sentence-transformers requests beautifulsoup4 pillow
```

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/alisufyan143/Product-Recommendation-System.git
   ```

2. **Prepare the Dataset**
   Ensure you have your dataset in the same directory or update the path in the code. For example, a CSV file named `sample-data.csv` with columns `id`, `name`, and `description`.

3. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

   This will start a local server and open the app in your default web browser.

## Example Query
The app allows users to enter a search query, such as "Game Controller" and receive product recommendations based on the descriptions in the dataset.

## Google Colab
Explore the project interactively on Google Colab: https://colab.research.google.com/drive/1W4vrDXWyHRN8dwSgvzUolpSUZDriiYoz?usp=sharing

## Contributing
Feel free to fork this repository, submit issues, and make pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pillow](https://python-pillow.org/)

For any questions or feedback, please open an issue or contact me directly.

---

Thank you for checking out this project! Happy coding! 🚀

---
