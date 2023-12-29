
# Loan Approval Prediction Project

### Overview

This project focuses on predicting loan approval outcomes using machine learning. The dataset consists of various features such as applicant income, coapplicant income, loan amount, gender, marital status, dependents, education, self-employment status, property area, credit history, and loan amount term.

### Data Preprocessing

The following data preprocessing steps have been applied to prepare the data for machine learning models:

1. **Handling Dependents Column:**
   - Replaced '3+' in the 'Dependents' column with the numeric value 3.

2. **Removing Columns:**
   - Dropped the 'Loan_ID' column from the dataset.

3. **Categorical Columns:**
   - Identified and printed the categorical columns in the dataset.
   - Used these categorical columns for ordinal encoding.

4. **Numerical Columns:**
   - Identified and printed the numerical columns in the dataset.

5. **Train-Test Split:**
   - Split the data into training and testing sets using the `train_test_split` function.

### Machine Learning Models

Three machine learning models have been implemented for loan approval prediction:

1. **Logistic Regression:**
   - Utilized a logistic regression model with balanced class weights.
   - Implemented a pipeline with ordinal encoding.

2. **Naive Bayes:**
   - Implemented a Gaussian Naive Bayes model.
   - Utilized ordinal encoding in a pipeline.

3. **Decision Tree Classifier:**
   - Implemented a decision tree classifier with specified parameters (random_state, max_depth, min_samples_split).
   - Used ordinal encoding in a pipeline.

### Model Evaluation

Evaluated the performance of each model using the following metrics:

- **F1 Score:**
  - Logistic Regression: 0.8132
  - Naive Bayes: 0.8718
  - Decision Tree Classifier: 0.8377

- **Accuracy:**
  - Logistic Regression: 0.7236
  - Naive Bayes: 0.7967
  - Decision Tree Classifier: 0.7480

### Conclusion

The machine learning models have been trained and evaluated for loan approval prediction. Naive Bayes achieved the highest F1 score, indicating good performance in terms of precision and recall. The models can be further fine-tuned, and additional features can be explored to improve predictive accuracy.
