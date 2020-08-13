**Problem Statement**

Given are the references to news pages collected from an web aggregator in the period from 10-March-2014 to 10-August-2014. The resources are grouped into categories that represent pages discussing the same story. News categories included in this dataset include business(b); science and technology(t); entertainment(e); and health(h). 
The goal is to predict which class a particular resource belongs to given the title of the resource.

**About the dataset**

This dataset comes from the UCI Machine Learning Repository. In total there are 422937 resources available in the dataset. The columns included in this dataset are:

• **ID**: the numeric ID of the article
• **TITLE**: the headline of the article
• **URL**: the URL of the article
• **PUBLISHER**: the publisher of the article
• **CATEGORY**: the category of the news item; one of:  b:business, t:science and technology, e: entertainment and m:health
• **STORY**: alphanumeric ID of the news story that the article discusses
• **HOSTNAME**: hostname where the article was posted
• **TIMESTAMP**: approximate timestamp of the article's publication, given in Unix time (seconds since midnight on Jan 1, 1970)


**Learning Objectives**:

Solving it will reinforce the following concepts of text analytics:

• Preprocess text data with tokenization, stopword removal etc
• Vectorize data using Bag-of-words and TF-IDF approaches
• Apply classifiers (Logistic and Multinomial Naive Bayes) to perform multi-class classification


**The Approach**:

The following approach was taken to solve the problem

1. Loading and cleaning the dataset before extracting just the relevant features for this exercise, i.e., TITLE (X feature set) and CATEGORY (y target).
2. Cleaning the data by:
a. Filtering our all the non-alphabetic words; for they have little predicting power in NLP
b. Turning the words into lower case; since, the algorithms applied here are case sensitive.
c. Eliminating stopwords
3. Pre-processing by:
a. Splitting into training and test datasets
b. Count-Vectorizing the dataset (a process of converting each word instance in an observation, to a feature - similar to OneHot Encoding)
c. Tf-IDF-vectorizing; which is another way to vectorize the text data. This approach normalizes the no. of repetitions and assigns weights per inverse proportion of its popularity in the dataset.
4. Fitting model: we fitted Naïve Bayes algorithm, which assigns conditional probability score of document being of a particular CATEGORY given each word feature. Another model that could've been implemented in given use case is Support Vector Classifier; for it is effective in handling high dimensional features set.
Conventional dimensionality reduction techniques viz., feature selection, decomposition proves to be ineffective in case of NLP problems.


**Challenges Faced**:

The directions provided to solve the problem were straightforward; plus the NLTK and Scikit-Learn libraries are well documented. This ensured the implementation went smoothly.
