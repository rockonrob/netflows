# -*- coding: utf-8 -*-
"""
William Koehler


--------------------Query tutorial-----------------------
Must install mysql-connector-python to import this
Or install the connector from the mysql website.

create user tempuser at localhost with no password. Privledges, at least SELECT
"""

import mysql.connector
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from timeit import default_timer
from sklearn import svm
from sklearn.preprocessing import scale



cnx = mysql.connector.connect(user='tempuser', password='',
                              host='127.0.0.1',
                              database='traces')
cursor = cnx.cursor()
cnx.close()


#fil = os.path.dirname('C:/Users/William Koehler/Documents/Stats 427/New folder/netflows_all.csv')
start = default_timer()
df = pd.read_csv('C:/Users/William Koehler/Documents/Stats 427/New folder/netflows_50k.csv', header=0)
print('It takes about: {0:2f} seconds to import the entire datasetn\n'.format(default_timer() - start))
print('Head of the dataframe:\n')
print(df.head(n=15))

print('Starting DBSCAN to find outliers on the points')
start = default_timer()
dbs = DBSCAN(eps=10000, min_samples=2)
dbs.fit(df)
print('It takes {0:2f} seconds to fully complete the DBSCAN with eps=.25 and minSamples=10\n It also takes about 4~8gb of memory'.format(default_timer() - start))

from collections import Counter

print('DBSCAN Cluster membership:\n', 25*'-')
for key, val in Counter(dbs.labels_).most_common():
    print('Class {0:2d} has {1:3d} members'.format(key, val))
    
    
    

#of = 0.1 # Expected Outlier Fraction
#nuv = 0.95 * of + 0.05
#svc = svm.OneClassSVM(nu=nuv, kernel="rbf", gamma=0.1)
#svc.fit(df)
#preds = svc.predict(df)
