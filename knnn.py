import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from statistics import mode


def kNearestNeighbors(x, y, k, data):
    # if constracints doesnt match return 0
    # else prepare dataframe form data
    # train the model for data without price value
    # find k neighbours for x, y using trained model
    # for those k neighbours get the price and find most common price
    #
    if (k > len(data)):
        return 0

    if (x > 1000):
        return 0

    if (y > 1000):
        return 0

    names = ['x', 'y', 'price']
    train_data = pd.DataFrame(data)
    train_data.columns = names
    print(train_data)
    price_val = train_data['price']
    train_data.drop('price', axis=1)
    print(train_data)
    train = pd.DataFrame()
    train['x'] = train_data['x']
    train['y'] = train_data['y']
    train.head()

    model = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(train)
    distances, indices = model.kneighbors(train)

    newdata = [[x, y]]
    dist, index = model.kneighbors(newdata)
    most_common_P = []

    for i in index:
        for j in i:
            most_common_P.append(price_val[j])

    return max(set(most_common_P), key=most_common_P.count)










