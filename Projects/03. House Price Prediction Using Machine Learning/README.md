# 🏡 Multiple Linear Regression on Boston House Price Prediction Dataset  

## 🎯 Objective  
The objective of this project is to build and evaluate Multiple Linear Regression (MLR) models using different approaches to predict house prices based on various features in the Boston Housing dataset. The goal is to explore feature selection techniques, residual analysis, and model evaluation to improve model performance.  

## ❓ Problem Statement  
Predicting house prices is a complex task influenced by multiple factors such as location, number of rooms, and economic conditions. This project aims to implement Multiple Linear Regression models using different methodologies to understand the impact of various independent variables on house prices and identify the best modeling approach for accurate predictions.  

## 🚀 Approach  
This project follows multiple approaches to building and evaluating MLR models:  

### 📌 1. Multiple Linear Regression using statsmodels  
✅ Load and explore the data (Exploratory Data Analysis - EDA)  
✅ Data Preparation (Train-Test Split)  
✅ Train the model using `statsmodels`  
✅ Perform manual feature selection based on **p-values** and **Variance Inflation Factor (VIF)**  
   - 🔹 Forward Feature Selection  
   - 🔹 Backward Feature Selection  
✅ Conduct residual analysis on train data  
✅ Make predictions on test data  
✅ Evaluate the model using **📉 Root Mean Squared Error (RMSE)** and **📊 R-squared (R²)**  

### 📌 2. Multiple Linear Regression using sklearn  
✅ Load and explore the data (EDA)  
✅ Data Preparation (Train-Test Split)  
✅ Train the model using `sklearn`  
✅ Perform residual analysis on train data  
✅ Make predictions on test data  
✅ Evaluate the model using **📉 RMSE** and **📊 R²**  

### 📌 3. Feature Selection and Dimensionality Reduction Techniques  
🔹 **Recursive Feature Elimination (RFE):** Automatically selects the most important features  
🔹 **Principal Component Analysis (PCA):** Reduces dimensionality while preserving variance  
🔹 **Lasso Regularization:** Identifies and eliminates less important features using L1 regularization  
🔹 **Feature Importance using Ensembles:** Uses ensemble models to determine the most significant predictors  

## 📌 Conclusion  
📌 The project demonstrates how different techniques impact model performance and interpretability.  
📌 Manual feature selection using **p-values** and **VIF** improves model efficiency by eliminating multicollinearity.  
📌 **RFE, PCA, and Lasso** provide automated methods for feature selection and dimensionality reduction.  
📌 The final model evaluation using **RMSE and R²** helps in assessing predictive accuracy and generalizability.  
📌 These methodologies can be applied to various real-world regression problems beyond house price prediction.  

## 🛠️ Technologies Used  
🔹 Python  
🔹 pandas, numpy (Data Processing)  
🔹 seaborn, matplotlib (Data Visualization)  
🔹 scikit-learn (MLR, Feature Selection, Evaluation)  
🔹 statsmodels (Statistical Modeling and Inference)  
