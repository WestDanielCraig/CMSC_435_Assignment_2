# Load the pandas libraries with alias 'pd'
import pandas as pd
# Load the numpy libraries with alias 'np'
import numpy as np

# Read data from file 'dataset_missing05.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv
data_05 = pd.read_csv("dataset_missing05.csv")

data_20 = pd.read_csv("dataset_missing20.csv")

data_complete = pd.read_csv("dataset_complete(1).csv")

# Converts object to data frame
df_05 = pd.DataFrame(data_05)

df_20 = pd.DataFrame(data_20)

df_complete = pd.DataFrame(data_complete)

# Replace all ? with a NaN value to calculate the mean
dfr_05 = df_05.replace('?', np.nan)

dfr_20 = df_20.replace('?', np.nan)

# Converts all column data types to floats
dfr_05['F1'] = dfr_05['F1'].astype(float)
dfr_05['F2'] = dfr_05['F2'].astype(float)
dfr_05['F3'] = dfr_05['F3'].astype(float)
dfr_05['F4'] = dfr_05['F4'].astype(float)
dfr_05['F5'] = dfr_05['F5'].astype(float)
dfr_05['F6'] = dfr_05['F6'].astype(float)
dfr_05['F7'] = dfr_05['F7'].astype(float)
dfr_05['F8'] = dfr_05['F8'].astype(float)

dfr_20['F1'] = dfr_20['F1'].astype(float)
dfr_20['F2'] = dfr_20['F2'].astype(float)
dfr_20['F3'] = dfr_20['F3'].astype(float)
dfr_20['F4'] = dfr_20['F4'].astype(float)
dfr_20['F5'] = dfr_20['F5'].astype(float)
dfr_20['F6'] = dfr_20['F6'].astype(float)
dfr_20['F7'] = dfr_20['F7'].astype(float)
dfr_20['F8'] = dfr_20['F8'].astype(float)

missing_values_05 = dfr_05.isnull().sum().sum()

missing_values_20 = dfr_20.isnull().sum().sum()

# Fill in imputed values with mean of columns for 5% missing
dfr_05_imputed = dfr_05.fillna(dfr_05.mean())
export_dfr_05_imputed = dfr_05_imputed.to_csv(r'/Users/westdc/Desktop/CMSC 435/Assignment 2/00844444_missing05_imputed_mean.csv', index = None, header=True)

# Fill in imputed values with mean of columns for 20% missing
dfr_20_imputed = dfr_20.fillna(dfr_20.mean())
export_dfr_20_imputed = dfr_20_imputed.to_csv(r'/Users/westdc/Desktop/CMSC 435/Assignment 2/00844444_missing20_imputed_mean.csv', index = None, header=True)


##### Algorithm 2 Starts here, data is split up as yes and no #####
dfr_05_yes = dfr_05.loc[(dfr_05['Class']=="Yes"), ['F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'Class']]
dfr_05_no = dfr_05.loc[(dfr_05['Class']=="No"), ['F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'Class']]

dfr_05_imputed_yes = dfr_05_yes.fillna(dfr_05_yes.mean())
dfr_05_imputed_no = dfr_05_no.fillna(dfr_05_no.mean())
dfr_05_concat = pd.concat([dfr_05_imputed_yes, dfr_05_imputed_no])
export_dfr_05_imputed_concat = dfr_05_concat.to_csv(r'/Users/westdc/Desktop/CMSC 435/Assignment 2/00844444_missing05_imputed_mean_conditional.csv', index = None, header=True)


dfr_20_yes = dfr_20.loc[(dfr_20['Class']=="Yes"), ['F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'Class']]
dfr_20_no = dfr_20.loc[(dfr_20['Class']=="No"), ['F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'Class']]

dfr_20_imputed_yes = dfr_20_yes.fillna(dfr_20_yes.mean())
dfr_20_imputed_no = dfr_20_no.fillna(dfr_20_no.mean())
dfr_20_concat = pd.concat([dfr_20_imputed_yes, dfr_20_imputed_no])
export_dfr_20_imputed_concat = dfr_20_concat.to_csv(r'/Users/westdc/Desktop/CMSC 435/Assignment 2/00844444_missing20_imputed_mean_conditional.csv', index = None, header=True)


##### Algorithm 3 Starts Here

    ### Unable to finish in time.

##### Algorithm 4 Starts Here

    ### Unable to finish in time.

#####################################

def mae_calculator(dataset, missing):

    df_complete['F1Difference'] = np.where(dataset.F1 == df_complete.F1, '0', dataset.F1 - df_complete.F1)
    df_complete['F2Difference'] = np.where(dataset.F2 == df_complete.F2, '0', dataset.F2 - df_complete.F2)
    df_complete['F3Difference'] = np.where(dataset.F3 == df_complete.F3, '0', dataset.F3 - df_complete.F3)
    df_complete['F4Difference'] = np.where(dataset.F4 == df_complete.F4, '0', dataset.F4 - df_complete.F4)
    df_complete['F5Difference'] = np.where(dataset.F5 == df_complete.F5, '0', dataset.F5 - df_complete.F5)
    df_complete['F6Difference'] = np.where(dataset.F6 == df_complete.F6, '0', dataset.F6 - df_complete.F6)
    df_complete['F7Difference'] = np.where(dataset.F7 == df_complete.F7, '0', dataset.F7 - df_complete.F7)
    df_complete['F8Difference'] = np.where(dataset.F8 == df_complete.F8, '0', dataset.F8 - df_complete.F8)

    df_complete['F1Difference'] = df_complete['F1Difference'].astype(float)
    df_complete['F2Difference'] = df_complete['F2Difference'].astype(float)
    df_complete['F3Difference'] = df_complete['F3Difference'].astype(float)
    df_complete['F4Difference'] = df_complete['F4Difference'].astype(float)
    df_complete['F5Difference'] = df_complete['F5Difference'].astype(float)
    df_complete['F6Difference'] = df_complete['F6Difference'].astype(float)
    df_complete['F7Difference'] = df_complete['F7Difference'].astype(float)
    df_complete['F8Difference'] = df_complete['F8Difference'].astype(float)

    df_complete['F1Difference'] = df_complete['F1Difference'].abs()
    df_complete['F2Difference'] = df_complete['F2Difference'].abs()
    df_complete['F3Difference'] = df_complete['F3Difference'].abs()
    df_complete['F4Difference'] = df_complete['F4Difference'].abs()
    df_complete['F5Difference'] = df_complete['F5Difference'].abs()
    df_complete['F6Difference'] = df_complete['F6Difference'].abs()
    df_complete['F7Difference'] = df_complete['F7Difference'].abs()
    df_complete['F8Difference'] = df_complete['F8Difference'].abs()

    total1 = df_complete['F1Difference'].sum()
    total2 = df_complete['F2Difference'].sum()
    total3 = df_complete['F3Difference'].sum()
    total4 = df_complete['F4Difference'].sum()
    total5 = df_complete['F5Difference'].sum()
    total6 = df_complete['F6Difference'].sum()
    total7 = df_complete['F7Difference'].sum()
    total8 = df_complete['F8Difference'].sum()

    final_total = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8

    mae = 1/missing * final_total
    return round(mae, 4);

print("MAE_05_mean = ", mae_calculator(dfr_05_imputed, missing_values_05))
print("MAE_05_mean_conditional = ", mae_calculator(dfr_05_concat, missing_values_05), '\n')

print("MAE_20_mean = ", mae_calculator(dfr_20_imputed, missing_values_20))
print("MAE_20_mean_conditional = ", mae_calculator(dfr_20_concat, missing_values_20), '\n')

