import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_data(file_path):
    df = pd.read_csv(file_path)
    print("\nNumber of rows and columns in the data set: ", df.shape)
    return df


def manipulate_data(df):
    # add ones columm for constant coefficient:
    con = [1] * df.shape[0]
    df.insert(0, "con", con, True)
    # normalize charges column
    df['charges'] = df['charges'].apply(lambda x: x / 1000)
    # one-hot encoding:
    df = pd.get_dummies(df)
    return df


print("Enter file path:")
data_frame = read_data(input())
data_frame = manipulate_data(data_frame)
dataMatrix = data_frame.to_numpy()

# permutate the data
dataMatrix = np.random.permutation(dataMatrix)
copieData = np.copy(dataMatrix)
charges = copieData[:, 4]
copieData = np.delete(copieData, 4, 1)

# split the rows into two sets
trainData = copieData[:int(len(copieData) * 0.8)]
testData = copieData[-int(len(copieData) * 0.2):]
trainCharges = charges[:int(len(charges) * 0.8)]
testCharges = charges[-int(len(charges) * 0.2):]

# compute mean squared error for train and test data
print(trainData.shape)
print(trainCharges.shape)
coefficients = np.asarray(np.linalg.lstsq(trainData, trainCharges, 0)[0])
MSEtrain = np.linalg.norm(
    (trainData @ coefficients) - trainCharges) / len(trainData)
MSEtest = np.linalg.norm(
    (testData @ coefficients) - testCharges) / len(testData)

print("abs differnce between MSE of train and test data is:")
print(abs(MSEtrain-MSEtest))

plt.hist(np.absolute((trainData @ coefficients) - trainCharges), 100)
plt.title('\n\ndistribution of absolute test error values', fontweight="bold")
plt.show()
