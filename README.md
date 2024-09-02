Machine Learning Pipeline Design to Predict Status of a Loan 
==============================
This project is a loan prediction pipeline designed to predict the status of loan applications. 
It utilizes the LightGBM model, known for its efficiency and performance in handling large datasets. The pipeline includes data loading, preprocessing, feature encoding, and model training stages. The LightGBM model is saved for integrated into the prototype for user testing.The prototype, built with Gradio, provides an interactive interface for testing and improving the model's performance.

Directory Structure
-------------------
- `data` Dataset used in the project.
- `models` The LightGBM model is save here for integration into the prototype.
- `Loan` Python script of data training, model development, and experimentation.
- `app.py` Python script for the Gradio user interface or testing.

Pipeline Overview:
-------------------
Pipeline Overview:

1. Data Loading and Preprocessing:

Data Loading:
The pipeline starts by loading data from a CSV file using the loadData function. This function handles potential errors, such as file not found or other loading issues.

Data Display:
The displayData function is used to preview the first few rows of the dataset and provide information on the number of rows and columns.

Data Summary:
Summary statistics for numerical and categorical features are computed using describe and displayed.
Histograms and bar plots are generated to visualize the distribution of numerical and categorical features respectively.

2. Data Cleaning:

Check for Duplicates:
The checkDuplicateData function identifies any duplicate loanId values.

Remove Null Values:
The removenullValue function removes rows with missing values in selected columns, reducing the dataset to only relevant columns.

3. Data Encoding and Splitting:

Encoding:
Categorical variables are encoded using LabelEncoder to convert them into numerical format. This includes encoding the loanStatus, payFrequency, leadType, and fpStatus columns.
Data Splitting:
The dataset is split into training and testing sets using train_test_split, with 20% of the data reserved for testing.

4. Model Building and Training:

Model Initialization:
A LightGBM classifier is initialized with specific hyperparameters.

Model Training:
The model is trained on the training data (x_train and y_train) and then saved using joblib.

Evaluation:
The model’s performance is evaluated using accuracy and a classification report. These metrics provide insights into how well the model can classify loan statuses.

5. Model Saving:

The trained LightGBM model is saved to a file (LightGBM_model.pkl) for future use in testing or deployment.

6. Visualization:

Histograms:
Histograms of numerical features are plotted to visualize their distributions.

Bar Plots:
Bar plots for categorical features are displayed to show the frequency of each category.

Download Dataset
------------
Open the data folder, and given the link to download the .csv dataset in kaggle, Download the dataset and put into the data folder. 

Installation (Terminal)
------------
pip install pandas scikit-learn lightgbm matplotlib joblib gradio

Make sure to install the necessary libraries and modules before running the project.

==============================

The Gradio Prototype
------------
![image](https://github.com/user-attachments/assets/e70c413f-77da-4bf9-a62d-86e03af2e075)
