import csv
from sklearn.neighbors import NearestNeighbors
import numpy as np

with open('horse_colic_test.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    X = np.array(data)
