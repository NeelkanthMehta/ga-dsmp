The main goal of this problem is to leverage the power of techniques like LSA (Latent Semantic Analysis) and LDA (Latent Dirichlet Allocation) to assign topics to unseen news headlines.

**About the dataset**

The dataset includes the entire corpus of articles published by the ABC website in the given time range. With a volume of 200 articles per day and a good focus on international news, we can be fairly certain that every event of significance has been captured here. In total there are 331100 instances of data available with two columns.

The columns in this dataset are:
1. publish_date: Date of publish of the news headline
2. headline_text: Headline of the news published on that particular date


Solving it will help one apply the following skills:
1. Text preprocessing techniques like tokenization, stopword removal, POS tagging etc.
2. Enhance your data visualization skills
3. Topic modelling with LSA (Latent Semantic Analysis) and LDA (Latent Dirichlet Allocation)
4. Use coherence score to determine the optimum number of topics


The steps involved are as follows:
1. Loading and cleaning the dataset, including removing any non-alphabetic headline titles
2. Finding the mode frequently occurring word in the document by the way of Count Vectorizing
3. Implementing topic modelling with Latent Sementic Analysis (LSA) and Latend Dirichlet Allocation (LDA) models
4. Finally, computing the coherence scores of the models and tune the hyperparameter of optimum number of topics
