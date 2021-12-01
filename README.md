# Fraud Detection

![AI in Finance](https://github.com/chirathlv/project2/blob/chirath/Images/AIinfinance.jpeg)

# Table of Contents

1. [Introduction - Machine Learning and Risk mitigation in Finance](#intro)
2. [Data, Technology and Coding Standards](#para1)
   1. [Data Sources](#subpara1)
   2. [Technologies](#subpara2)
   3. [Coding Standards](#subpara3)
3. [Data Cleanse and Visualisation](#para2)
   1. [Data Cleanse](#subpara4)
4. [Machine Learning Analysis and procedures](#para3)
5. [Recommendations](#para4)
6. [References](#para5)

## Introduction - Machine Learning and Risk mitigation in Finance

The financial sector in which operates throughout the world as we know, is arguably the most predominant and most influential industry throughout.

As in any industry and any society, no matter how advanced or behind, there is always ways and opportunities to cheat the system, and gain and leverage mis-information or poor security & operations, in order for financial gain.

As the world evolves and technology advances, we see more and more cases of fraud and data theft within the financial sector each year, costing businesses, individuals, and the economy billions of dollars.

The Purpose of this Code and the Assignment Is to use and develope machine learning models to prove the importance and the effectiveness of this technology in the industry, and how it should be implimented across the board.

## Data, Technology and Coding Standards.

### Data Sources

1.  Credit Card Data For ML model. (Kaggle)

    The Data Set used for the machine learning model is a Credit Card transactions data set. This Data set has no obfuscation as it has more then 20 million transactions generated from a virtual world simulation.The Data covers 2000 synthetic consumer residents in the US, who travel the world. For this analysis, only 2019 data has been extracted.

2.  Fraud Statistics.
    1. The Ascent
    2. Federal Trade Commision.

### Technology stack

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

### Coding Standards

Following rules have been applied during code development and testing:

1. All variables must reflect their purpose. Underscore to be used as and when required.
2. Each step of the code must contain comments to explain the purpose of the code.
3. A git hub repository called project2 must be set up with branches for each developer.
4. Each developer must use their own git hub branch to code and unit test developed code.
5. Lead developer must review code prior to merge.
6. Lead developer is responsible for merging all code.
7. Each developer must download the most recent code from main branch before commencing code changes.
8. Each release must provide a brief message on changes made prior to committing the code.

## Data Cleaning and Visualisation

### Data Cleaning

The following Data cleaning procedure has been followed in order to produce accurate representations in our Machine Learning Model.

1. Identify data set is accurate for the ML model and Analysis.
2. Load data into jupyter notebook.
3. Rename Columns to Suit layout and analysis.
4. Basic Cleaning techniques, duplicates and unwanted columns.
5. Check the target variable class Ratio.
6. Check nulls/nans & further inspect.
7. Fill missing data values in Merchant State with 'UNKNOWN'.
8. Split time collumn into hours & minutes, then drop 'Time' column.
9. Re-arrange respective columns.
10. Format appropriate columns and change D-types where needed.
11. Transform 'Merchant Name' columns with label encoder.
12. Save Cleaned Data for use in Machine Learning Algorithm.

## Machine Learning Model Procedure / Analysis

![ML Pipeline](https://github.com/chirathlv/project2/blob/chirath/Images/ML-Pipeline.png)

## References

[https://www.kaggle.com/ealtman2019/credit-card-transactions]()

[https://www.ftc.gov/]()

[https://www.fool.com/the-ascent/research/identity-theft-credit-card-fraud-statistics/]()
