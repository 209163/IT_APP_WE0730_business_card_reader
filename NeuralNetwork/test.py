import pickle
import os
from nltk.stem.porter import PorterStemmer


def tokenizer(text):
    return text.split()


def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]


if __name__ == '__main__':

    porter = PorterStemmer()

    dest = os.path.join('classifier')
    cur_dir = os.path.dirname(__file__)
    clf = pickle.load(open(os.path.join(cur_dir, dest, 'classifier.pkl'), 'rb'))

    label = {0: 'company', 1: 'email', 2: 'name', 3: 'phone'}

    X = ['LUKASZ KOSUNIAK']
    X2 = ['CONSULTANT BUSINESSMARKETERP']
    X3 = ['Mobil: +49 l520 9084746']
    X4 = ['E-Moil: lronk.dellert@ohleledern.de']

    print('1) Result: %s, Probability: %.2f%%' %\
          (label[clf.predict(X)[0]], clf.predict_proba(X).max()*100))
    print('2) Result: %s, Probability: %.2f%%' % \
          (label[clf.predict(X2)[0]], clf.predict_proba(X2).max() * 100))
    print('3) Result: %s, Probability: %.2f%%' % \
          (label[clf.predict(X3)[0]], clf.predict_proba(X3).max() * 100))
    print('4) Result: %s, Probability: %.2f%%' % \
          (label[clf.predict(X4)[0]], clf.predict_proba(X4).max() * 100))
