## Sentiment Analysis 

This project aims to use machine learning to predict if a product review text is positive or negative. 

Navigate to the web app: 
https://glau-sentiment-analysis.herokuapp.com/ 

<img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/Demo_Screen_Capture.gif" alt="demo" width="600">

## Amazon Reviews Dataset

The raw Amazon reviews dataset consists of reviews from amazon. The data span a period of 18 years, including ~35 million reviews up to March 2013. Reviews include product and user information, ratings, and a plaintext review. The dataset can be downloaded from [Stanford SNAP's website](https://snap.stanford.edu/data/web-Amazon.html#:~:text=This%20dataset%20consists%20of%20reviews,ratings%2C%20and%20a%20plaintext%20review.&text=gz).

The dataset used in this project is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the above mentioned Amazon review dataset, which can be accessed from Xiang Zhang's [Google Drive](https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M).

The Amazon reviews full score dataset is constructed by randomly taking 600,000 training samples and 130,000 testing samples for each review score from 1 to 5. In total there are 3,000,000 training samples and 650,000 testing samples.

WordCloud plots below highlight the common words in the positive and negative classes of product reviews in the dataset.


#### Figure 1: WordCloud Generated on Top 100 words used in Amazon Product Reviews
(a) Positive Sentiment |  (b) Negative Sentiment
:-------------------------:|:-------------------------:
<img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/plots/Wordcloud%20-%20positive.png" alt="positive-review-wordcloud" width="600"> | <img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/plots/Wordcloud%20-%20negative.png" alt="positive-review-wordcloud" width="600">

## Model Architecture

A CNN architecture was adopted, where pre-processed text was passed to an embedding, followed by a fully-connected layer and pooling and drop-out layers for regularisation. Utilised AWS EC2 GPUs.

The Python code for training and testing the deep learning model is written in a [Jupyter Notebook](https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/amazon-review-rating-v2.ipynb). 

## Model Training and Evaluation

The accuracy on the test set is 83.1%. Convergence is observed at epoch 2.

#### Figure 2: Evaluation of Model on Training and Validation Sets
(a) Accuracy |  (b) Loss
:-------------------------:|:-------------------------:
<img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/plots/Plot%20of%20accuracy%20over%20epoch.png" alt="positive-review-wordcloud" width="300"> | <img src="https://github.com/gabrielle-lau/sentiment-analysis-deep-learning/blob/master/plots/Plot%20of%20loss%20over%20epoch.png" alt="positive-review-wordcloud" width="300">
