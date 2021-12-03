# Fraud Detection

![AI in Finance](https://github.com/chirathlv/project2/blob/chirath/Images/AIinfinance.jpeg)

# Table of Contents

1. [Introduction - Machine Learning and Risk mitigation in Finance](#intro)
2. [Data, Technology and Coding Standards](#para1)
   1. [Data Sources](#subpara1)
   2. [Technologies](#subpara2)
   3. [Coding Standards](#subpara3)
3. [Basic Statistical Analysis](#para2)
4. [Machine Learning Analysis and procedures](#para3)
   1. [Machine Learning Pipeline](#subpara4)
   2. [Data Preparation](#para4)
      1. [Data Ingestion](#subpara5)
      2. [Data Wrangling](#subpara6)
      3. [Feature Engineering](#subpara7)
   3. [Model Training](#para5)
   4. [Model Deployment](#para6)
5. [References](#para7)

## Introduction - Machine Learning and Risk mitigation in Finance <a name="intro"></a>

The financial sector in which operates throughout the world as we know, is arguably the most predominant and most influential industry throughout.

As in any industry and any society, no matter how advanced or behind, there is always ways and opportunities to cheat the system, and gain and leverage mis-information or poor security & operations, in order for financial gain.

As the world evolves and technology advances, we see more and more cases of fraud and data theft within the financial sector each year, costing businesses, individuals, and the economy billions of dollars.

The Purpose of this project is to use and develope machine learning models to prove the importance and the effectiveness of this technology in the industry, and how it should be implemented across the board.

## Data, Technology and Coding Standards <a name="para1"></a>

### Data Sources <a name="subpara1"></a>

1.  Credit Card Data For ML model (Kaggle)

    The Data Set used for the machine learning model is a Credit Card transactions data set. This Data set has no obfuscation as it has more then 24 million transactions generated from a virtual world simulation.The Data covers 2000 synthetic consumer residents in the US, who travel the world. For this analysis, only 2019 data has been extracted due to missing fradulant data in some years.

2.  Fraud Statistics
    1. The Ascent
    2. Federal Trade Commision

### Technology stack <a name="subpara2"></a>

- Google Colab
- python 3.8.3
- pandas 1.0.5
- numpy 1.18.5
- requests 2.24.0
- json 2.0.9
- panel 0.9.7
- plotly 5.3.1
- hvplot 0.7.3
- seaborn 0.10.1
- matplotlib 3.2.2
- scikit-learn 1.0.0 (NOTE scikit-learn 1.0.1 will not work!)
- imblearn 0.8.1
- xgboost 1.5.1
- jupyter lab 2.1.5

### Coding Standards <a name="subpara3"></a>

Following rules have been applied during code development and testing:

1. All variables must reflect their purpose. Underscore to be used as and when required.
2. Each step of the code must contain comments to explain the purpose of the code.
3. A git hub repository called project2 must be set up with branches for each developer.
4. Each developer must use their own git hub branch to code and unit test developed code.
5. Lead developer must review code prior to merge.
6. Lead developer is responsible for merging all code.
7. Each developer must download the most recent code from main branch before commencing code changes.
8. Each release must provide a brief message on changes made prior to committing the code.

## Basic Statistical Analysis <a name="para2"></a>

The largest amount of fradulent transaction is 1244 and the largest refund fradulent transaction is -475, this suggests that the fraudsters are able to issue refund request and also make fradulent transactions. This however requires further investigation to pin point.
Overall, according to the box plot, fraudulent transactions exhibit higher average amount (79.42 vs 42.21) per transaction with greater degree of deviation (143 vs 80)

![SA](https://github.com/chirathlv/project2/blob/chirath/Images/boxplot.png)

## Machine Learning Model Procedure / Analysis <a name="para3"></a>

### Machine Learning Pipeline <a name="subpara4"></a>

![ML Pipeline](https://github.com/chirathlv/project2/blob/chirath/Images/ML-Pipeline.png)

## Data Preparation <a name="para4"></a>

### Data Ingestion <a name="subpara5"></a>

Extracted data is from Kaggle platform (Refer to the reference for more details) as a CSV files which was about 24 Million data samples that include Fradulant and non-fradulant transaction details. However, due to limited capacity of processing large amount of data, decision being made to extract subsect of the original dataset. To avoid the selection bias, yearly based data (Year 2019 Data) extracted without loosing any information. Excel and python used as tools to manipulate data which made it ready for the analysis.

### Data Wrangling <a name="subpara6"></a>

Following Data cleansing techniques used to process the data before going further.

    1. Drop Duplicates
    2. Handling Missing Values
    3. Correct the data types
    4. Drop unwanted columns

### Feature Engineering <a name="subpara7"></a>

Next, following Feature Engineering techniques applied to get a better sense of the data and to choose most relavent features from the raw data for the Machine Learning model.

    1. Feature Transformation
    2. Feature Splitting
    3. Feature Encoding
    4. Feature Scaling

## Model Training <a name="para5"></a>

Before trainig the data, split the data into 60% for Training and 40% for Testing. Then, feed the training data into the Machine Learning Algorithms. Next, validate the predctions against metrics and imporve further by tuning hyper-parameters. This is an iterative process which continues until model train well enough reducing the cost while increasing the accuracy. Since it is a Fraud detection use cases in financial domain, further forcus on reducing False Negatives as opposed to purely rely on accuracy.

    1. Logistic Regression

<p align="center"><b>Confusion Matrix</b></p>
<p align="center">
  <img width="460" height="300" src="https://github.com/chirathlv/project2/blob/chirath/Images/cm_lr_clf.png">
</p>
<p align="center"><b>Classification Report</b></p>
<p align="center">
  <img src="https://github.com/chirathlv/project2/blob/chirath/Images/cr_lr.PNG">
</p>

    2. Easy Ensemble Classifier

<p align="center"><b>Confusion Matrix</b></p>
<p align="center">
  <img width="460" height="300" src="https://github.com/chirathlv/project2/blob/chirath/Images/cm_easy_ensemble_clf.png">
</p>
<p align="center"><b>Classification Report</b></p>
<p align="center">
  <img src="https://github.com/chirathlv/project2/blob/chirath/Images/cr_eeasy_ensemble_clf.PNG">
</p>

    3. XGBoost Classifier

<p align="center"><b>Confusion Matrix</b></p>
<p align="center">
  <img width="460" height="300" src="https://github.com/chirathlv/project2/blob/chirath/Images/cm_xgboost_clf.png">
</p>
<p align="center"><b>Classification Report</b></p>
<p align="center">
  <img src="https://github.com/chirathlv/project2/blob/chirath/Images/cr_xgboost.PNG">
</p>

    4. Random Forest Classifier

<p align="center"><b>Confusion Matrix</b></p>
<p align="center">
  <img width="460" height="300" src="https://github.com/chirathlv/project2/blob/chirath/Images/cm_rf.png">
</p>
<p align="center"><b>Classification Report</b></p>
<p align="center">
  <img src="https://github.com/chirathlv/project2/blob/chirath/Images/cr_rf.PNG">
</p>

## Model Deployment <a name="para6"></a>

Google colab has been chosen as the desired cloud based platform for model deployment due to following reasons

    1. Cost effectiveness
    2. Reliability
    3. No infrastructure overhead
    4. Usability and accessibility

Hosted files can be found in below links

    https://drive.google.com/file/d/1GRwbiNPk_BRxBJpy5GpH7GHHIuS-t5-5/view?usp=sharing

    https://drive.google.com/file/d/1CRn9pSCsjJ5W0YZcEpq6Sslk-JdbGVig/view?usp=sharing

    https://drive.google.com/file/d/1X\*-51IZRfOtzNyUspLVn-6dY8ggUzCFh/view?usp=sharing

## References <a name="para7"></a>

https://www.kaggle.com/ealtman2019/credit-card-transactions

https://www.ftc.gov/

https://www.fool.com/the-ascent/research/identity-theft-credit-card-fraud-statistics/

https://aws.amazon.com/blogs/machine-learning/architect-and-build-the-full-machine-learning-lifecycle-with-amazon-sagemaker/

https://www.projectpro.io/article/8-feature-engineering-techniques-for-machine-learning/423
