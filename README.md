# Fake News Detector
This project consists of the building of a machine learning model capable of detecting fake news. 
The model will be deployed through a web application using Flask.
## Dataset
The corpus for the model training was obtained from the next [article](https://www.researchgate.net/publication/333098973_Detection_of_fake_news_in_a_new_corpus_for_the_Spanish_language).
\
\
Posadas-Durán, J. P., Gómez-Adorno, H., Sidorov, G., & Escobar, J. J. M. (2019). 
Detection of fake news in a new corpus for the Spanish language. Journal of Intelligent & Fuzzy Systems, 36(5), 4869-4876.
\
\
And it is available in this repository: https://github.com/jpposadas/FakeNewsCorpusSpanish

## Preprocessing
First, I have created a preprocessing function for prepare the text before feed the model with it. This function remove punctuation and tokenize the words
of each text. Optionally can remove stopwords and lemmatize the text via parameter. This function will be the first step in the pipeline process. Next
step will be the vectorizer that transform the text words in an array of counts of each word of the corpus, with a vocabulary of 3000 words. After this process
data is prepared for the model.

## Model Building
In order to find the best model for this purpose I have tried several classification models such as Logistic Regression, Support Vector Machine, Random Forest
and Boosting. Also, I have evaluated three different feature representation:
* Bag of words
* N-gram (bigrams and trigrams)
\
\
I have tried all posible combinations of these setups to find the best accuracy on the training test using GridSearchCV from Scikit-Learn python module.

## Results
                        LogReg  SVM   RF    Boosting
    CV Score(Accuracy): 0.82    0.77  0.79  0.80
    
    Test Score (Using LogReg): 0.78 

## Deployment

I used Flask for the web application and Heroku for deploying it.

Available on:
https://fake-news-detector-by-acervero.herokuapp.com/
