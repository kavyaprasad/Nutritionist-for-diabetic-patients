
import numpy as np
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as sm
from matplotlib import pyplot
from sklearn.cluster import KMeans
from scipy import cluster
from sklearn.cross_validation import train_test_split

dataNutrition = pd.read_csv('Nutrition Dataset.xlxs',usecols=["FoodName","GyclemicIndex","Energywithdietaryfibre(kJ)",
															"Energywithoutdietaryfibre(kJ)", "Protein(g)", 
                                                             "Availablecarbohydrateswithsugaralcohols(g)",
                                                             "Availablecarbohydrateswithoutsugaralcohol(g)",
                                                             "Dietaryfibre(g)", "VitaminAretinolequivalents(g)","Thiamin(B1)(mg)",
															 "Riboflavin(B2)(mg)", "Niacin(B3)(mg)", "Dietaryfolateequivalents(g)",
															 "VitaminB6(mg)", "VitaminB12(g)", "VitaminC(mg)", 
															 "Alpha-tocopherol(mg)", "VitaminE(mg)", "Calcium(Ca)(mg)",
															 "Iodine(I)(g)",	"Iron(Fe)(mg)", "Magnesium(Mg)(mg)", "Phosphorus(P)(mg)",
															 "Potassium(K)(mg)", "Selenium(Se)(g)", "Sodium(Na)(mg)", "Zinc(Zn)(mg)"])
dataNutrition = dataNutrition[dataNutrition["GyclemicIndex"].notnull()]
diabetes_X = dataNutrition.drop('GyclemicIndex', 1)
diabetes_X = diabetes_X.drop('FoodName', 1)
X = np.array(diabetes_X)
diabetes_Y = dataNutrition["GyclemicIndex"]
'''data_train, data_test = train_test_split(diabetes_X, test_size=.2)'''


cluster_array = [cluster.vq.kmeans(diabetes_X, i) for i in range(1,10)]

plt.plot([var for (cent,var) in cluster_array])
plt.show()

'''model = KMeans(n_clusters=2)
model.fit(data_train)
clusassign =model.predict(data_test)
print (clusassign)

print (sm.accuracy_score(diabetes_Y, data_test))
print (sm.confusion_matrix(diabetes_Y, data_test))'''

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
centroid = kmeans.cluster_centers_
labels = kmeans.labels_
print (centroid)
print(labels)

for i in range(3):
    ds = X[np.where(labels==i)]
    pyplot.plot(ds[:,0],ds[:,1],'o')
    lines = pyplot.plot(centroid[i,0],centroid[i,1],'kx')
    pyplot.setp(lines,ms=20.0)
    pyplot.setp(lines,mew=5.0)
pyplot.show()