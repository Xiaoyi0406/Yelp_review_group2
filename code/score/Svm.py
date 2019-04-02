# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:00:23 2019

@author: 74293
"""

from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.metrics import classification_report

import pickle

def svm_train_model(X_train, Y_train):
    '''
    print("Fitting the classifier to the training set")
    #t0 = time()
    param_grid = {'C': [1,10, 100, 500, 1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(svm.SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(pca.X_train, pca.Y_train)
    #print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    #本例中最好的参数为c = 500， cache_size = 200, gamma = 0.01, degree = 3, kernel = 'rbf', tol = 0.001
    print(clf.best_estimator_)
    print(clf.best_estimator_.n_support_)
    '''
    svc = svm.SVC(kernel = 'rbf',C=500, gamma = 0.01).fit(X_train, Y_train)
    s=pickle.dumps(svc)
    f=open('svm.txt','wb')
    f.write(s)
    f.close()
    return svc

def svm_predict_model(X_text, svc):
    
   # label_pr = svc.predict(pca.X_train)
    label_pr2 = svc.predict(pca.X_test)
    #最后的正确率为89%
    print(classification_report(Y_test, label_pr2))

