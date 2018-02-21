import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pickle

def usage():
    print("Usage:")
    print("python %s <data_dir>" % sys.argv[0])

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['pos', 'neg']

    # Read the data
    train_data = []
    train_labels = []
    
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                train_data.append(content)
                train_labels.append(curr_class)
    # Create feature vectors
    
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 stop_words='english',
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    # test_vectors = vectorizer.transform(test_data)


    # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()
    
    classifier_liblinear.fit(train_vectors, train_labels)
    # temp_test = vectorizer.transform(["This is the worst place i have ever seen in my life"])
    # prediction_liblinear = classifier_liblinear.predict(temp_test)
    # # print(prediction_liblinear)
    def predict_sentiment(sentence = None):
        if sentence is not None:
            vector_input = vectorizer.transform(sentence)
            prediction = classifier_liblinear.predict(vector_input)
            for i in range(0,len(sentence)):
                print("-------")
                print("{} | sentiment={}".format(sentence[i],prediction[i]))
                print("-------")

    while True:
    
        print("Please enter a choice you wanna use\n1. Predict the Sentiment of a sentence \n2. Exit")
        choice = int(input("Your choice: "))
        if choice==1:
            sentences = list()
            number = int(input("Number of Sentences - "))
            if isinstance(number,int):
                for i in range(0,number):
                    data = input("%d. "%(i+1))
                    sentences.append(data)
                predict_sentiment(sentence=sentences)   
            else:
                continue
            
        else:
            sys.exit(1)


    
    


    
    
    
    # t2 = time.time()
    # time_liblinear_train = t1-t0
    # time_liblinear_predict = t2-t1

    # Print results in a nice table
    print("Results for SVC(kernel=rbf)")
    print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    print(classification_report(test_labels, prediction_rbf))
    # print("Results for SVC(kernel=linear)")
    # print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    # print(classification_report(test_labels, prediction_linear))
    # print("Results for LinearSVC()")
    # print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    # print(classification_report(test_labels, prediction_liblinear))
    