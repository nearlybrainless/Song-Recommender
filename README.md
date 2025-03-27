# 🎵 Song Recommender

## 📌 Overview
This machine learning project recommends songs similar to a given input by analyzing features such as **acousticness**, **loudness**, and **danceability**. It utilizes the **Spotify Web API** to extract song data and employs clustering techniques to identify patterns and suggest comparable tracks.

## 🛠 Features
- **Data Extraction**: Uses the **Tekore** Python package to interact with the Spotify Web API and retrieve song features.
- **Machine Learning Model**: Implements clustering algorithms to group songs based on their attributes.
- **Recommendation System**: Suggests songs that are similar to the input track by analyzing feature similarities.

## 📂 Files Included
- **`DataExtract.py`**: Script that leverages the Tekore package to fetch song features from the Spotify Web API.
- **`Spotify_Recommender_1.ipynb`**: Jupyter Notebook containing the machine learning model and recommendation system.
- **`data.csv.zip`**: Compressed dataset of songs used for training and evaluation.
- **`newcsv.csv`**: Additional song dataset for analysis.

## 🚀 How to Use
1. **Prerequisites**:
   - Install required Python packages: `tekore`, `pandas`, `numpy`, `sklearn`, etc.
   - Obtain Spotify API credentials and set up access tokens.

2. **Data Extraction**:
   - Run `DataExtract.py` to fetch song features from Spotify and save them to a CSV file.

3. **Model Training & Recommendation**:
   - Open `Spotify_Recommender_1.ipynb` in Jupyter Notebook.
   - Load the dataset and execute the cells to train the clustering model.
   - Input a song name to receive a list of recommended tracks with similar features.

## 🔗 Resources
- **Tekore Documentation**: [https://tekore.readthedocs.io/](https://tekore.readthedocs.io/)
- **Spotify Web API Reference**: [https://developer.spotify.com/documentation/web-api/](https://developer.spotify.com/documentation/web-api/)

## 👤 Author
Mohammed Haneef

---

**Feel free to contribute or reach out for feedback!** 🚀

