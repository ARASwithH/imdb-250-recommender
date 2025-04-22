# 🎬 IMDb 250 Movie Recommender Based on Plot Summaries

## 📌 Project Overview
This project scrapes plot summaries of the Top 250 movies on IMDb using BeautifulSoup4, processes the text data using NLP techniques, and builds a content-based recommendation engine. By entering a plot summary, the system returns the 5 most similar movies from the IMDb Top 250 using TF-IDF vectorization and cosine similarity.

## 🔍 Features
- Web scraping using BeautifulSoup4
- Plot summary cleaning (punctuation removal, stop word filtering, stemming)
- TF-IDF vectorization
- Cosine similarity and KNN for finding similar movies
- Command-line interface for interactive recommendations

## 🛠️ Technologies Used
- Python
- BeautifulSoup4
- NLTK
- NumPy
- scikit-learn (optional)
- CSV for storing scraped data

## 🧠 How It Works
1. Scraping IMDb Top 250 movie plot summaries
2. Text preprocessing with NLTK (stopwords, stemming)
3. TF-IDF vectorization of cleaned text
4. Cosine similarity/KNN to compare user input with movies
5. Return 5 most similar IMDb Top 250 movies

## 🚀 Getting Started

1. Install dependencies:
   pip install beautifulsoup4 nltk numpy

2. Run the program:
   python main.py

3. Input a plot summary when prompted to get movie recommendations.

## 📂 Project Structure
- dirty_datas.csv       # Scraped data: {title: plot summary}
- getting plot summery.py  # Script to scrape plot summaries
- main.py               # Main recommendation script

## ✨ Sample Input/Output

Input:
Enter your plot summary: A skilled thief leads a team into dreams to steal corporate secrets.

Output:
Top 5 similar movies:
1. Inception : 0.913
2. The Matrix : 0.881
3. Interstellar : 0.843
4. Fight Club : 0.812
5. The Prestige : 0.785

## 📌 Future Improvements
- Add a web UI for easier interaction
- Use BERT or Word2Vec for semantic similarity
- Add filters (e.g., genre, year)
- Explain why each movie was recommended
