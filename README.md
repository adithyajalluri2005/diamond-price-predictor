# Diamond Price Predictor 💎

An open-source machine learning application to predict diamond prices based on key attributes such as carat, cut, color, clarity, and dimensions. This project blends data preprocessing, model training, and a Flask web app for real-time prediction.

---

## 🚀 Features

- **Data Ingestion & Preprocessing**  
  Load and clean Kaggle's diamonds dataset—remove outliers, handle missing values, scale numerical features, and encode categorical ones.

- **Exploratory Data Analysis**  
  Understand feature relationships with scatterplots, correlation matrices, and violin plots.

- **Model Training & Comparison**  
  Train and evaluate multiple regressors: LinearRegression, Ridge, Lasso, DecisionTree, RandomForest, KNeighbors, GradientBoosting, XGBRegressor. Use metrics like MAE, RMSE, and R² to pick the best model.

- **Feature Importance**  
  XGBRegressor yields actionable insights—carat is most important, followed by 'y' dimension, clarity, and color.

- **Web App Deployment**  
  Powered by Flask with a simple front-end (HTML forms + Bootstrap), this interface allows users to input diamond specs and receive predicted price instantly.

---

## 📂 Project Structure

```
diamond-price-predictor/
├── application.py        # Flask back-end
├── requirements.txt      # Python dependencies
├── notebooks/            # EDA & modeling notebooks
├── src/                  # Data preprocessing & training modules
├── templates/            # HTML front-end
├── artifacts/            # Trained models, scalers, metadata
├── setup.py              # Packaging script
└── README.md             # Project overview
```




---

## 🛠 Installation

### Requirements

- Python 3.7+
- `git`
- (Optional) Virtual environment (`venv`, `conda`)

### Steps

git clone https://github.com/adithyajalluri2005/diamond-price-predictor.git
cd diamond-price-predictor

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

---

## 🎯 Usage


### Train models or directly use existing ones from artifacts/.

### Run the web app:

python application.py
Open your browser at http://127.0.0.1:5000/.

Input diamond attributes—carat, cut, color, clarity, depth, table, x, y, z.

Click Predict to view the estimated price.

---

## 🧪 Model Training & Inference


### Data: Uses Kaggle's diamonds dataset with ~54,000 entries and ten core features.

### Preprocessing:

Remove outliers (e.g., extreme depth or dimension values).

Encode categorical features (cut, color, clarity).

Scale numeric columns.

### Modeling:

Compare regressors (Linear, Ridge, Lasso, DecisionTree, RandomForest, KNN, XGB, etc.).

Evaluate via R², RMSE, MAE.

XGBoost consistently delivers top performance (~98–99% R²).

### Deployment: Serve the best model using Flask for real-time predictions.
