# Product Recommendation System

## Overview
This project demonstrates a Product Recommendation System built with Python, leveraging TF-IDF and cosine similarity to provide accurate recommendations based on product descriptions. The system is designed to enhance e-commerce platforms by suggesting relevant products to users based on their search queries.

## Features
- **TF-IDF Vectorization**: Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) to convert textual data into numerical values.
- **Cosine Similarity**: Calculates the similarity between the user's query and product descriptions to find the most relevant products.
- **Interactive Streamlit App**: Provides a user-friendly interface to input search queries and view recommendations in real-time.

## Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- pandas
- scikit-learn
- NLTK

### Install Required Libraries
```bash
pip install streamlit pandas scikit-learn nltk
```

### NLTK Stopwords
Ensure you have the NLTK stopwords downloaded:
```python
import nltk
nltk.download('stopwords')
```

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/alisufyan143/Product-Recommendation-System.git
   ```

2. **Prepare the Dataset**
   Ensure you have your dataset in the same directory or update the path in the code. For example, a CSV file named `sample-data.csv` with a column `description` containing product descriptions.

3. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

   This will start a local server and open the app in your default web browser.

## Example Query
The app allows users to enter a search query, such as "bra," and receive product recommendations based on the descriptions in the dataset.

## Google Colab
Explore the project interactively on Google Colab: [Google Colab Notebook Link]

## Contributing
Feel free to fork this repository, submit issues, and make pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License.

## Acknowledgments
- [NLTK](https://www.nltk.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)

For any questions or feedback, please open an issue or contact me directly.

---

Thank you for checking out this project! Happy coding! 🚀
