## Sentiment Analysis 

This project aims to use machine learning to predict if a product review text is positive or negative. 

Navigate to the web app: 
https://glau-sentiment-analysis.herokuapp.com/ 

<img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/Demo_Screen_Capture.gif" alt="demo" width="600">

## Amazon Reviews Dataset

The raw Amazon reviews dataset consists of reviews from amazon. The data span a period of 18 years, including ~35 million reviews up to March 2013. Reviews include product and user information, ratings, and a plaintext review. The dataset can be downloaded from [Stanford SNAP's website](https://snap.stanford.edu/data/web-Amazon.html#:~:text=This%20dataset%20consists%20of%20reviews,ratings%2C%20and%20a%20plaintext%20review.&text=gz).

The dataset used in this project is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the above mentioned Amazon review dataset, which can be accessed from Xiang Zhang's [Google Drive](https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M).

The Amazon reviews full score dataset is constructed by randomly taking 600,000 training samples and 130,000 testing samples for each review score from 1 to 5. In total there are 3,000,000 trainig samples and 650,000 testing samples.

## Model
The Python code for training and testing the deep learning model is written in a [Jupyter Notebook](https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/amazon-review-rating-v2.ipynb). The test accuracy is >83%. 

