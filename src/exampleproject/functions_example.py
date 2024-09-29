import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def printTest():
    print("Hello World")

def generateData():
    data = np.random.rand(10, 4)
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
    return df

def plotData(df):
    df.plot()
    plt.show()

if __name__ == "__main__":

    printTest()
    df = generateData()
    plotData(df)
    print("The data is:", df)
