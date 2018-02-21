import sys
import pickle
import os
import csv
import time
import preprocessor as pre

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pickle

# creating training and testing data
p = None

def training_and_modeling():
    train_data_neg =[]
    train_label_neg = []
    train_data_pos =[]
    train_label_pos = []

    test_data_neg = []
    test_label_neg = []
    test_data_pos = []
    test_label_pos = []


    with open('analysis/data/negative.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for r in rows:
            train_data_neg.append(pre.clean(r[1]))
            if r[0] =='0':
                train_label_neg.append('negative')
        
        

    with open('analysis/data/positive.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for r in rows:
            train_data_pos.append(pre.clean(r[1]))
            if r[0] =='4':
                train_label_pos.append('postive')

    train_data = train_data_neg + train_data_pos
    train_label = train_label_neg + train_label_pos

    test_data = train_data_neg[0:1000] + train_data_pos[0:1000]
    test_label = test_label_neg[0:1000] + test_label_pos[0:1000]


    vectorizer = TfidfVectorizer(min_df=5,
                                    max_df = 0.8,
                                    stop_words='english',
                                    sublinear_tf=True,
                                    use_idf=True)

    with open('vectorizer.pickle','wb') as obj:
        pickle.dump(vectorizer,obj,protocol=pickle.HIGHEST_PROTOCOL)


    train_vectors = vectorizer.fit_transform(train_data)

    # print(train_vectors)

    classifier_liblinear = svm.LinearSVC()
    #pickle the classifier
    classifierSVC = classifier_liblinear.fit(train_vectors, train_label)

    with open('classifier.pickle','wb') as obj:
        pickle.dump(classifier_liblinear,obj,protocol=pickle.HIGHEST_PROTOCOL)
    
    testing_sentence = ["this idea might work","you are a bad boy"]
    testing_vector = vectorizer.transform(testing_sentence)


    p = classifier_liblinear.predict(testing_vector)

    # print(list(p))

    return classifierSVC, vectorizer


def predict_sentiment(sentence):

    clf, vec = training_and_modeling()


    # with open('./vectorizer.pickle','rb') as vect:
    #     v = pickle.load(vect)
    sent_vec = vec.transform([pre.clean(sentence),])
    
    # with open('./classifier.pickle','rb') as clf:
    #     c = pickle.load(clf)
    #     return list(c.predict(sent_vec))
    return list(clf.predict(sent_vec))


# testing_sentence = ["this idea might work","you are a bad boy"]
# testing_vector = vectorizer.transform(testing_sentence)


# p = classifier_liblinear.predict(testing_vector)

# print(list(p))
