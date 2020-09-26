<p align="center">
  <img width="1600" height="200" src="images/diabetes.png">
</p>


# PROBLEM
 - The intent is to develop an application which guides a diabetic patient whether they are taking the right food or not, taking into consideration their blood sugar level.
- Suggest a better food substitute.

# APROACH
 - This can be achieved using Glycemic index of a particular food.
 - GI rates carbohydrate-containing foods by how much they boost blood sugar.
 - Glycemic Load (GL) is determined by multiplying its glycemic index by the amount of carbohydrate the food contains in each serve and dividing by 100. Thus, GL helps us to determine whether the food taken is appropriate or not.
 ## Other areas where this approach can be applied
This approach can be applied to patients suffering from problems such as:
 - Obesity
 - Thyroid
 - PCOD/PCOS 
It can also be considered as a nutritionist, which helps to check the quantify of food intake and provides healthier food choices.
# Modeling
In order to develop this project, I am using the following techniques:

Linear Regression- for the prediction of GI
K-Nearest Neighbor Algorithm- For searching food substitute.
Case-based Reasoning- For adaptive learning of food substitute.

## Linear Regression
The Regression model helps to predict GI values depending on the food nutrients inputed by the user.
The GI value ranges from 0-100. GI is classified as : 
 - Low GI: 0-55.
 - Medium GI: 56-69.
 - High GI: 70-100.
As the GI has continuous values and for calculation of GL we multiply with GI, we have considered applying linear regression model.

Using GI value and net carbohydrate content we will calculate GL that will in turn help us decide whether food is appropriate for the patient or not. 
Using GI values we will classify foods into low, medium and high glycemic index food that will help us predict better food substitutes for the patient.

## Nearest neighbor algorithm
Food samples from the dataset that have low range of GI value is given as input to the k-NN algorithm.
When the user will input a food item, clustering will be done in a way to have similar nutrients with lower GI index.
The best result will be returned as per the distance. 
## Use of Case Based Reasoning
If the patient agrees to the food item suggested by the system, the combination will be saved in the knowledge base.
If similar case occurs in future, the results will be fetched from the knowledge base.

## How is our approach different?

The root of diabetes is the consumption of food with high glycemic index (processed food)
Our approach provides a solution to the problem, fixing it from its root.
Our application is extremely user friendly, so even a person who is not well-versed with technology can use it. 
One can also use this application on a day-to-day basis to improve one's health.
 