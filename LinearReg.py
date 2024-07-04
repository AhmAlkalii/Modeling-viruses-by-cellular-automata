import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def linreg():

    covid = pd.read_csv('USA Data.csv')

    # Predicting Total Infected:

    X = covid[['Total Cases', 'Total Deaths', 'Active Cases', 'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests',
               'Tests/ 1M pop', 'Population', 'Total Infected']]

    y = covid['Recovered per 1M']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=101)

    lm  = LinearRegression()
    lm.fit(X_train, y_train)

    prediction = lm.predict(X_test)
    plt.scatter(y_test, prediction)


    sns.displot((y_test-prediction),bins=50, kde=True)

    print('MAE:', metrics.mean_absolute_error(y_test, prediction))
    print('MSE:', metrics.mean_squared_error(y_test, prediction))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))


    cdf = pd.DataFrame(lm.coef_,X.columns, columns=['Coefficent'])
    print(cdf)

if __name__ == "__main__":
    linreg()
