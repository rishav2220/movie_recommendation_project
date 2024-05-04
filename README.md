
## Movie Recommendation Tool

This project is a movie recommendation tool built using Python and hosted [here](https://movie-recommendation-tool-330f5b982b92.herokuapp.com). It leverages machine learning techniques to suggest movies based on user input. The tool processes movie data to generate feature vectors and calculates the similarity between them to recommend movies that are similar to a given input.

Key Features:
- Data Processing: The tool uses Pandas to manipulate and clean movie data for further processing.
- Feature Engineering: Custom transformations, including stemming and vectorization, help generate meaningful features from movie metadata.
- Similarity Calculation: Scikit-learn's cosine similarity function is used to measure the similarity between movies.
- Interactive Interface: The user interface is built with Streamlit, allowing users to select a movie and receive personalized recommendations.
- API Integration: It uses the TMDB API to fetch and display movie posters, enhancing the visual appeal of the recommendations.

**How to Use:**
1. Clone this repository.
2. Ensure you have Python installed, and install the required dependencies from the `requirements.txt`.
3. Launch the Streamlit app using `streamlit run app.py`.
4. Select a movie from the dropdown menu, click "Recommend," and enjoy the suggestions!

### Requirements:
- Python 3.7 or above
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Requests

### How It Works:
1. Data Preprocessing: Movie data is preprocessed to extract relevant features such as genres, cast, and overview.
2. Feature Engineering: The text data is tokenized, stemmed, and vectorized using CountVectorizer.
3. Model Training: A similarity matrix is calculated using cosine similarity.
4. Recommendations: Based on the similarity matrix, the tool recommends movies similar to the user’s input.

