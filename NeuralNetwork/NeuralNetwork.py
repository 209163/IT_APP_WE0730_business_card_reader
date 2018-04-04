import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')


def tokenizer(text):
    return text.split()


def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]


if __name__ == '__main__':

    # ---- downloading set ----
    df = pd.read_csv('trainingSet.txt', header=None)

    data = df.values
    X = data[:, 0]
    y = data[:, -1]

    pd.DataFrame(X)
    pd.DataFrame(y)
    print('Labels:', np.unique(y))

    print(X.shape)
    print(y.shape)

    # ---- dividing set ----
    splits = model_selection.train_test_split(X, y, test_size=.1, random_state=0)

    X_train, X_test, y_train, y_test = splits
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # ---- learning and prediction ----
    # logistic regression with grid search

    stop = stopwords.words('english')  # stopwords like "am, are, is" from english dictionary

    porter = PorterStemmer()  # convert text into stamps

    tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, preprocessor=None)

    param_grid = [{'vect__ngram_range': [(1,1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'clf__penalty': ['l1', 'l2'],
                   'clf__C': [1.0, 10.0, 100.0]},
                  {'vect__ngram_range': [(1,1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'vect__use_idf':[False],
                   'vect__norm':[None],
                   'clf__penalty': ['l1', 'l2'],
                   'clf__C': [1.0, 10.0, 100.0]},
                  ]

    lr_tfidf = Pipeline([('vect', tfidf), ('clf', LogisticRegression(random_state=0))])

    gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid, scoring='accuracy', cv=10, verbose=1, n_jobs=2)

    gs_lr_tfidf.fit(X_train, y_train)

    print('Best parameters: %s ' % gs_lr_tfidf.best_params_)
    print('Cross validation precision: %.3f' % gs_lr_tfidf.best_score_)

    clf = gs_lr_tfidf.best_estimator_
    print('Precision: %.3f' % clf.score(X_test, y_test))


