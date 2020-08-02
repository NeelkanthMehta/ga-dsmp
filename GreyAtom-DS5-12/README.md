### Project Overview

 The problem statement revolves around the need to predict the forest cover type (the predominant kind of tree cover) from strictly cartographic variables (as opposed to remotely sensed data).

It includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. These areas represent forests with minimal human-caused disturbances, so that existing forest cover types are more a result of ecological processes rather than forest management practices.

The study area includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. Each observation is a 30m x 30m patch. You are asked to predict an integer classification for the forest cover type. The seven types are:

1 - Spruce/Fir 2 - Lodgepole Pine 3 - Ponderosa Pine 4 - Cottonwood/Willow 5 - Aspen 6 - Douglas-fir 7 - Krummholz

**About the Dataset**:

**_Feature_**: **_Description_**
01. Elevation: Elevation in meters
02. Aspect: Aspect in degrees azimuth
03. Slope: Slope in degrees
04. Horizontal Distance To Hydrology: Horz Dist to nearest surface water features
05. Vertical Distance To Hydrology: Vert Dist to nearest surface water features
06. Horizontal Distance To Roadways: Horz Dist to nearest roadway
07. Hillshade_9am (0 to 255 index): Hillshade index at 9am, summer solstice
08. Hillshade_Noon (0 to 255 index): Hillshade index at noon, summer solstice
09. Hillshade_3pm (0 to 255 index): Hillshade index at 3pm, summer solstice
10. Horizontal Distance To Fire Points: Horizontal Dist to nearest wildfire ignition points
11. Wilderness_Area (4 binary columns, 0 = absence or 1 = presence): Wilderness area designation
12. Soil_Type (40 binary columns, 0 = absence or 1 = presence)	Soil Type designation
13. Cover_Type (7 types, integers 1 to 7): Forest Cover Type designation

There are more than 20 features in the dataset. We will be working with this dataset to gather insights and look at the feature importance of each feature contributing towards the target variable. The data is in raw form (not scaled) and contains binary columns of data for qualitative independent variables such as wilderness areas and soil type.


### Learnings from the project

 After completing this project, you will have a better understanding of how feature selection affects the performance of a machine learning model. In this project, we apply the following concepts.

1. How are the features important to our model.
2. How to select the most significant features out of many.
3. How to perform univariate feature selection.
4. How to perform a multivariate feature selection.


### Approach taken to solve the problem

 1, Loaded the data and obtained descreptive statistics for each variable.
2. Conducted exploratory data analysis w.r.t. size, distribution, multicollinearity etc.
3. We took a closer look at variables that weren't significantly correlated with the target variable, before dropping it.
4. Next, we split and standardized the datasets
5. We performed univariate selection to retain only 90 percentile and above correlation scores.
6. Finally, we compared the performance of the model by implementing logistic regression first on full featureset and next on selected featureset.

We observed, there was no drop in performance with the selected featureset.


### Challenges faced

 The standardized syntax of Scikit-Learn library makes it easy and straightforward to implement the code.


### Additional pointers

 None.


