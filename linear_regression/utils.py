import numpy as np

# mount gdrive with this code
from google.colab import drive
drive.mount('/content/drive')
#below where the file is in gdrive, change with your
#data_path = "/content/drive/My Drive/linear_regression"
#yearsBase, meanBase = np.loadtxt(data_path + 'file.csv', delimiter=',')

def load_data():
    data = np.loadtxt("/content/drive/My Drive/linear_regression/data/ex1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("/content/drive/My Drive/linear_regression/data/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
