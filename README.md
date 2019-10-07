# EC601-A2 Project Calorie Predictor
Team: Yan Jie Hui, Krishna Palle, Timmy Hoang 

# Our Product
## Product Mission:
-	We are offering a product for anyone who wants to have more control over how many calories they are consuming. Our app will allow a user to easily and quickly  upload pictures of their meals and let them know how many calories they will be eating. 
## User Stories:
-	As a **bodybuilder**, I would like to know my daily calorie intake in order to perform better in my sport.
-	As a very **busy adult**, I would like to easily log my daily calories in order to live a healthier life.
-	As a **researcher**, I would like to provide an easy way for my subjects to log their diets and send me their data in order to perform studies.
## Similar Products
### Food mama
**Pros:**
-	Easy for user to log their food
-	Uses machine learning algorithms to classify the type of food
**Cons:**
-	Hard to accurately predict calories for complex dishes
-	Requires user input for precise results
### My Fitness Pal
**Pros:**
-	Very precise calories, macro and micro nutrient count.
-	Allows barcode scan for processed foods
-	Access to large database of food and restaurant dishes
**Cons:** 
-	Cumbersome to create recipes, and log every food item
-	The user needs to know exactly what he is eating
### Previous study by American University of Beirut:
https://www.aaai.org/ocs/index.php/IAAI/IAAI17/paper/viewFile/14204/13719
## Patent Analysis
TBD
# System Design
![image](https://github.com/yanjh95/ECE601F19A2-CaloriePredictor/blob/master/cpDesign.png)
## MVP
-	A mobile app in IOS or Android
-	Asks the user to select the type of food category(Pizza, Burger, Salads) 
-	Take food image as input
-	Predicts calories using ML
## Major Concerns
-	Labeling of data
-	Finding data
>-	Food 101 Kaggle
>-	FoodDD from University of ottawa
>-	Yelp data set
## Technologies
-	Neural Network options: AlexNet, ResNet
-	PyTorch - beginner friendly, lots of tutorials

