#!pip install seaborn

# Import needed packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process.kernels import RBF
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

path = "AfricanCrisis.csv"
df = pd.read_csv(path)


# specify the names of the features (i.e. band names) and label
# feature names used to extract out features and define what bands

feature_names = ['year', 'systemic_crisis', 'exch_usd', 'domestic_debt_in_default', 
                 'sovereign_external_debt_default', 'gdp_weighted_default', 'inflation_annual_cpi', 'independence', 
                 'currency_crises', 'inflation_crises']

label = "banking_crisis"


# get the features and labels into separate variables
X = df[feature_names]
Y = df[label]


## Resampling
#!pip install imblearn
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from numpy import where

over = SMOTE()
under = RandomUnderSampler()
steps = [('o', over), ('u', under)]
pipeline = Pipeline(steps=steps)

# transform the dataset
X, Y = pipeline.fit_resample(X, Y)
# summarize the new class distribution
counter = Counter(Y)
print(counter)

# Split features and target into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1, stratify=Y)


# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier(5)))
models.append(('CART', DecisionTreeClassifier(max_depth=5)))
models.append(('RF', RandomForestClassifier(max_depth=5, n_estimators=10)))
models.append(('SVC I', SVC(kernel="linear", C=0.025)))
models.append(('SVM II', SVC(gamma=2, C=1)))
models.append(('MP', MLPClassifier(alpha=1, max_iter=1000)))
models.append(('Ada', AdaBoostClassifier()))
models.append(('QDA', QuadraticDiscriminantAnalysis()))

# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'

for name, model in models:
	kfold = model_selection.KFold(n_splits=10)
	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
    
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# Instantiate and fit the model
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, Y_train)


# Make predictions for the test set
Y_pred_test = model.predict(X_test)


# View accuracy score
accuracy_score(Y_test, Y_pred_test)


# View confusion matrix for test data and predictions
confusion_matrix(Y_test, Y_pred_test)


# Get and reshape confusion matrix data
matrix = confusion_matrix(Y_test, Y_pred_test)
matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]
# Build the plot
plt.figure(figsize=(20, 10))
sns.set(font_scale=1.4)
sns.heatmap(matrix, annot=True, annot_kws={'size':10}, cmap=plt.cm.Greens, linewidths=0.2)

# Add labels to the plot
class_names = ['crisis', 'no_crisis']

tick_marks = np.arange(len(class_names))
tick_marks2 = tick_marks + 0.5
plt.xticks(tick_marks, class_names, rotation=25)
plt.yticks(tick_marks2, class_names, rotation=0)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for Random Forest Model')
plt.show()


import pickle
import joblib
 
# Save the trained model as a pickle string.
joblib.dump(model, "one")