import csv
import pandas as pd
import numpy as np


listCSV=[]
listCSV.clear
try:
    with open('WP7_training_data.csv', 'r') as f:
      ml_data = csv.reader(f,delimiter=';',skipinitialspace=True)
      listCSV = list(ml_data)
except IOError:
    msg = ("Error with opening CSV training dataset file.")     
    print(msg)    


if len(listCSV)>100:
    print("Training dataset successfully loaded.")
else:
    print("Training dataset was not loaded - it is too short or problem with the file.")


class Container(object):
     pass 
trainDataset = Container()
# target values of the data (0..7)
trainDataset.target=[] 
# tweets
trainDataset.data=[]
# target names according to the values (0..7)
trainDataset.target_names=['happy','neutral','calm','upset','depressed','discouraged','indeterminate']
testDataset = Container()
testDataset.target_names=trainDataset.target_names
testDataset.data=[]
testDataset.target=[]
# dividing the dataset - you can do this as well with sklearn:
# train, test = train_test_split(df, test_size=0.2)
for idx, item in enumerate(listCSV):
    if item[1].strip()!='':
        if idx%14!=0:
            trainDataset.data.append(item[1].strip())
            if item[2].strip()==trainDataset.target_names[0]:
                trainDataset.target.append(0)  
            elif item[2].strip()==trainDataset.target_names[1]:
                trainDataset.target.append(1)                  
            elif item[2].strip()==trainDataset.target_names[2]:
                trainDataset.target.append(2)  
                print(trainDataset.target_names[2])
                print('2')
            elif item[2].strip()==trainDataset.target_names[3]:
                print(trainDataset.target_names[3])
                print('3')
                trainDataset.target.append(3)  
            elif item[2].strip()==trainDataset.target_names[4]:
                print(trainDataset.target_names[4])
                print('4')
                trainDataset.target.append(4)  
            elif item[2].strip()==trainDataset.target_names[5]:
                print(trainDataset.target_names[5])
                print('5')

                trainDataset.target.append(5)
            else:
                trainDataset.target.append(6)
        else:
            testDataset.data.append(item[1].strip())
            if item[2].strip()==testDataset.target_names[0]:
                testDataset.target.append(0)  
            elif item[2].strip()==testDataset.target_names[1]:
                testDataset.target.append(1)  
            elif item[2].strip()==testDataset.target_names[2]:
                testDataset.target.append(2)  
            elif item[2].strip()==testDataset.target_names[3]:
                testDataset.target.append(3)  
            elif item[2].strip()==testDataset.target_names[4]:
                testDataset.target.append(4)  
            elif item[2].strip()==testDataset.target_names[5]:
                testDataset.target.append(5)
            else:
                testDataset.target.append(6)

print("\n\nCharacteristics of the dataset:")
for i in range(0,7):
    print(trainDataset.target_names[trainDataset.target[i]]+" "+str(trainDataset.target[i])+" "+str(trainDataset.target.count(i)));

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(trainDataset.data)
X_train_counts.shape

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, trainDataset.target)

docs_new = testDataset.data

X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

#for doc, category in zip(docs_new, predicted):
#    print('%r => %s' % (doc, trainDataset.target_names[category]))

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ('clf', MultinomialNB()),
])


text_clf = text_clf.fit(trainDataset.data, trainDataset.target)

import numpy as np
docs_test = testDataset.data;
predicted = text_clf.predict(docs_test)
np.mean(predicted == testDataset.target)      

from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)),
])
_ = text_clf.fit(trainDataset.data, trainDataset.target)
predicted = text_clf.predict(docs_test)
np.mean(predicted == testDataset.target)

from sklearn import metrics
from sklearn.metrics import classification_report
print(classification_report(testDataset.target, predicted, target_names=testDataset.target_names))
