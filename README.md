<img src="https://venturebeat.com/wp-content/uploads/2018/09/natural-language-processing-e1572968977211.jpg" alt="Logo of the project" align="right">

# NLP-Final-Project; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> Final project for 6.8610 (Quantitative Methods for Natural Language Processing)

There have been numerous advancements in the field of natural language processing (NLP) in
recent years that attempt to solve the task of summarization. However, these have generally
focused on summarization for a singular document. While important in its own right, single
document summarization is insufficient when there are thousands of related documents that need
to be aggregated and summarized. Given the ever-growing volume of information in the modern
age, this is an increasingly relevant challenge. Consider the case when we want to summarize
opinions from several different editorials regarding a current event. Or the case when there are
thousands of different reviews for a product that we want to summarize. This is the problem of
multi-document summarization.

This project will work with a dataset of movie reviews. Websites like Rotten Tomatoes have
users that post thousands of reviews on a daily basis. Users looking for movie recommendations
will usually not want to read through all of these. To address this, Rotten Tomatoes has paid
editors that read through, and then write a short summary of these reviews. In our project, we
intend to build and test models that can automate the process of summarizing these reviews. We
also hope that in addition to helping solve the task at hand, insights from our model(s) can be
applied to other similar problems in the realm of multi-document summarization.

## Installing / Getting started

### Cloning the Repository 

Go to a folder and run the following to clone this repository and move into the right file directory

```shell
git clone https://github.com/hesham-nawaz/NLP-Final-Project.git
cd NLP-Final-Project
```

After cloning the repository, manually add the appropriate datasets to the folder NLP-Final-Project

### Getting the Dataset 

Download Kaggle Datasets from [HERE](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset). 
There are two files to place into the `NLP-Final-Project` folder: `rotten_tomatoes_critic_reviews.csv` and `rotten_tomatoes_movies.csv`

## Developing

### Built With
pandas, python, numpy, rouge-score, matplotlib, sumy, nltk, re, heapq

### Prerequisites

The dataset must be donwloaded manually and inserted into the file directory as the datasets are large.

## Licensing

MIT License. Explicit Permission of the Authors Recommended.
