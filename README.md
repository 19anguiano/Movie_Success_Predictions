
# Movie_Success_Predictions

Welcome! Here is a supervised machine learning model that aims to predict the success rate of movies using a dataset sourced from Letterboxd.com. The primary objective of this project is to provide valuable insights and patterns for studios and companies in determining which movies to host, fund, or sponsor.

Movie success rate prediction holds immense significance across various domains, including content recommendation systems, movie streaming platforms, and market analysis. By accurately forecasting the success of a movie, we can enhance user experiences, facilitate personalized recommendations, and empower streaming companies and studios to make informed decisions aligned with audience preferences.


## Our team:
- Brittni Breese (brittnibresee)
- Yash Kansal (yashkansal97)
- Adam Paganini (adampaganini)
- Nicole Campos (payasanicolasa)
- Vanessa Anguiano (19anguiano)
- David Duran (13263952)

## Built with:
- Python
- Numpy
- Pandas
- hvPlot
- matplotlib
- Scikit Learn
- Flask

## To run the app:
- Git clone - https://github.com/19anguiano/Movie_Success_Predictions
- CD into directory - Movie_Success_Predictions
- Start Flask app with app.py
- Visit localhost:5000 in a browser

## Implementation Details
This repository provides a collection of scripts and files that demonstrate the project's key features including:

Process:
1. Read in data with Pandas
2. Performed Exploratory Data Analysis (EDA)
- The various graphs and observations for the EDA on the raw data can be found at this link: https://13263952.github.io/Project-4_Machine-Learning/
3. Cleaned the data:
- Dropped unneeded columns
- Dropped NaN values
- Updated data types
4. Simplified existing features:
- Release Date: Split this in two columns - “Year” and “Month”
  - Used the “Year” column to identify if the movie was released “post-streaming”, i.e., after 2005, or before
- Language: Bundled all foreign languages in a single category, “fl” (foreign languages)
5. Added new features:
- anticipated_vote_rating: Used the “vote average” for every movie to give values to every genre used for that movie, and averaged that “vote average” for every genre over the entire dataset to get an anticipated score based on the genre
- anticipated_popularity: Similar to anticipated_vote_rating, except used “popularity” instead of “vote average”
- target: Created a target column for the model to predict which was either “1” (Successful) based on net positive difference between revenue and budget, or “0” (Unsuccessful), if the difference was negative
6. Working on datasets:
- Used the original dataset with the original “0” and “1” split, 
  - Split the dataset using train_test_split, into train (label counts - 0: 619, 1: 2140) and test sets
  - Normalized it using StandardScaler on the train set
  - And, created a Random Forest Model (Balanced Accuracy Score: 0.50761)
- OverSampled the above dataset
  - New train (label counts - 0: 2140, 1: 2140) and test set
  - Created another Random Forest Model (Balanced Accuracy Score: 0.62580)
- Doubled the original dataset
  - New train (label counts - 0: 1209, 1: 4309) and test set
  - Again, normalized it using StandardScaler on the train set
  - Created another Random Forest Model (Balanced Accuracy Score: 0.53062)
- Finally, oversampled the doubled dataset (Chosen Dataset)
  - New train (label counts - 0: 4309, 1: 4309) and test set
  - Created another Random Forest Model (Balanced Accuracy Score: 0.79461)
7. Model Development
- Random Forest (Chosen)
- Naive Bayes
- Decision Tree
- Random Forest
- Logistic Regression
- Support Vector Machine
8. Compared the Balanced Accuracy Scores:
![image](https://github.com/19anguiano/Movie_Success_Predictions/assets/116750638/ea0aca7b-6e81-4bee-94ad-faf5d2e74aee)


9. Evaluating the performance of the chosen model (Random Forest Classifier) using Confusion Matrix and Classification Report
![image](https://github.com/19anguiano/Movie_Success_Predictions/assets/116750638/edc1c4a0-a5cc-461c-abab-c40da348612a)


10. Understood the importance of the various features:
![image](https://github.com/19anguiano/Movie_Success_Predictions/assets/116750638/b3afc54c-a103-4314-934b-401c9d2cbf3b)


11. Saved the model and deployed it using a flask app



## CREDITS & SOURCES
Kaggle.com
TMDB 
D3.js documentation: https://d3js.org
Plotly.js
