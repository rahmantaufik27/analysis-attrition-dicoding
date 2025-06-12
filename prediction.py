# Import library
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
from collections import Counter
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# preprocessing terlebih dahulu datanya
## feature selection
df_missing_attrition = df_missing_attrition[fix_selected_features]
column_to_remove = ['PercentSalaryHike', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
numeric_column2 = numeric_columns.difference(column_to_remove)
## encoding
le = LabelEncoder()
df_missing_attrition['OverTime'] = le.fit_transform(df_missing_attrition['OverTime'].astype(str))
## scaling
df_missing_attrition[numeric_column2] = scaler.fit_transform(df_missing_attrition[numeric_column2])

# predict untuk attrition yang null
# load model dari hasil pemodelan di notebook
model_rf = joblib.load('random_forest_model.pkl')
predicted_attrition = model_rf.predict(df_missing_attrition)
df_missing_attrition['Attrition_Predicted'] = predicted_attrition
# cek hasil
# df_missing_attrition.info()
# df_missing_attrition
class_counts = df_missing_attrition['Attrition_Predicted'].value_counts()
print("Distribusi kelas hasil prediksi Attrition:")
print(class_counts)