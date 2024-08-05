# Analysis and Prediction of Unemployment among IT Graduates during the Pandemic

This project involves analyzing and predicting the employment status of IT graduates during the pandemic using various machine learning techniques.

## Implementation Environment

### Data Handling

- **Pandas**: Used for data manipulation and analysis.
- **Warnings**: Used to filter out warnings during data processing.

### Data Visualization

- **Matplotlib**: Used for plotting graphs and visualizing data.
- **Seaborn**: Used for creating statistical graphics.

### Machine Learning

- **Scikit-learn**: Used for model training, including:
  - **Logistic Regression**: For binary classification.
  - **Train-Test Split**: For splitting the dataset into training and testing sets.
  - **Accuracy Score**: For evaluating the model's performance.

## Project Steps

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and normalizing data.
2. **Exploratory Data Analysis (EDA)**: Understanding the data distribution and relationships using visualization tools.
3. **Model Training**: Training the logistic regression model on the preprocessed data.
4. **Model Evaluation**: Evaluating the model's accuracy and performance.
5. **Prediction**: Making predictions on new data and determining the likelihood of employment.

## Project File Structure

The project folder contains the following files:

- **main1.csv**: The dataset used for analysis.
- **analysis.py**: Script for data analysis and preprocessing.
- **model_training.py**: Script for training and evaluating the machine learning model.
- **visualization.py**: Script for creating visualizations and plots.

## How to Run

1. **Install Required Libraries**: Ensure all necessary libraries are installed (pandas, matplotlib, seaborn, scikit-learn).
2. **Run Analysis Script**: Execute the `analysis.py` script to preprocess the data.
3. **Train the Model**: Run `model_training.py` to train and evaluate the machine learning model.
4. **Generate Visualizations**: Use `visualization.py` to create and view data visualizations.

```bash
python analysis.py
python model_training.py
python visualization.py
```
