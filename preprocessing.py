from sklearn.base import BaseEstimator, TransformerMixin
import spacy
import numpy as np
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('./models/es_core_news_sm-2.3.1')

class TextPreprocessing(BaseEstimator, TransformerMixin):
    def __init__(self, remove_punctuation=True, remove_stopwords=True,
                lemmatization=True, lowercase=True):
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords
        self.lemmatization = lemmatization
        self.lowercase = lowercase

    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        X_transformed = []
        for idx, text in enumerate(X):
            prepared_text = ""
            if self.lowercase:
                text = text.lower()
            doc = nlp(text, disable=['tagger','parser', 'ner', 'textcat'])
            for word in doc:
                if self.remove_stopwords and word.is_stop:
                    continue
                if self.remove_punctuation and word.is_punct:
                    continue
                if self.lemmatization:
                    word = word.lemma_
                prepared_text += " " + str(word)
            X_transformed.append(prepared_text)
        return np.array(X_transformed)
