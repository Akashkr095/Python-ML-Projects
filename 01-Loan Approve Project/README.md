# Loan Approval Prediction 🏦

A machine learning solution to predict loan approvals using classification models. This project implements data analysis, preprocessing, feature engineering, and model comparison to identify the best performing classifier.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Results](#-results)
- [Technical Stack](#-technical-stack)
- [Usage](#-usage)
- [Key Findings](#-key-findings)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

This project implements a machine learning solution to predict loan approvals using classification models. The notebook performs:

- **Data Analysis**: Comprehensive exploratory data analysis (EDA)
- **Preprocessing**: Handling missing values and feature encoding
- **Feature Engineering**: Correlation analysis and feature scaling
- **Model Comparison**: Evaluating Logistic Regression, KNN, and Naive Bayes
- **Best Model Selection**: Identifying the optimal classifier (Naive Bayes)

---

## 📊 Dataset

### Dataset Characteristics

- **Target Variable**: `Loan_Approved` (Binary: Yes/No)
- **Feature Types**: Mix of numerical and categorical variables
- **Handling Missing Data**: 
  - Numerical features: Mean imputation
  - Categorical features: Mode (most frequent) imputation
- **Preprocessing**: 
  - Label encoding for ordinal features
  - One-hot encoding for nominal features

### Key Features

- Applicant Income
- Co-applicant Income
- Credit Score
- DTI Ratio (Debt-to-Income)
- Savings
- Employment Status
- Marital Status
- Loan Purpose
- Property Area
- Gender
- Education Level
- Employer Category

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab
- pip or conda package manager

### Setup

1. **Clone the repository** (or download the project files)
   ```bash
   git clone <repository-url>
   cd 01-Loan\ Approve\ Project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib jupyter
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

---

## 📁 Project Structure

```
01-Loan Approve Project/
├── README.md                                    # This file
├── LOAN_APPROVAL_PROJECT_DOCUMENTATION.md      # Detailed documentation
├── loan_approval_data.csv                       # Dataset
├── loan_approve_minor_project.ipynb             # Main project notebook
├── credit_wise.ipynb                            # Alternative notebook
└── requirements.txt                             # Python dependencies
```

---

## 🔬 Methodology

### Step 1: Data Loading & Exploration
```python
df = pd.read_csv("loan_approval_data.csv")
df.info()
df.isnull().sum()
```

### Step 2: Missing Values Handling

**Numerical Columns** - Mean Imputation:
```python
from sklearn.impute import SimpleImputer
num_imp = SimpleImputer(strategy="mean")
df[numerical_col] = num_imp.fit_transform(df[numerical_col])
```

**Categorical Columns** - Mode Imputation:
```python
cat_imp = SimpleImputer(strategy="most_frequent")
df[categorical_col] = cat_imp.fit_transform(df[categorical_col])
```

### Step 3: Exploratory Data Analysis (EDA)

- **Target Distribution**: Pie chart showing approved vs. rejected loans
- **Demographics**: Gender and education level distributions
- **Financial Analysis**: Income and credit score distributions
- **Outlier Detection**: Box plots for identifying anomalies

### Step 4: Feature Engineering

**Label Encoding** (Ordinal Features):
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Education_Level"] = le.fit_transform(df["Education_Level"])
```

**One-Hot Encoding** (Nominal Features):
```python
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore")
```

### Step 5: Feature Scaling

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Step 6: Model Training & Evaluation

#### Configuration
- **Train-Test Split**: 80-20 split with random_state=42
- **Evaluation Metrics**: Precision, Recall, F1 Score, Accuracy, Confusion Matrix

#### Models Evaluated

1. **Logistic Regression** - Linear classifier using logistic function
2. **K-Nearest Neighbors (KNN)** - Instance-based learning with k=5
3. **Naive Bayes** - Probabilistic classifier based on Bayes' theorem ⭐ BEST MODEL

---

## 📈 Results

### Model Comparison

| Metric | Purpose |
|--------|---------|
| **Precision** | Accuracy of positive predictions (approved loans) |
| **Recall** | Coverage of actual positive cases |
| **F1 Score** | Harmonic mean of precision and recall |
| **Accuracy** | Overall correctness of predictions |
| **Confusion Matrix** | Details of true/false positives/negatives |

### Best Model Selection

**🏆 Winner: Naive Bayes**

**Selection Criteria**: Precision score prioritizes minimizing false positives (incorrect loan approvals)

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **Data Processing** | pandas, numpy |
| **Visualization** | seaborn, matplotlib |
| **Machine Learning** | scikit-learn |
| **Environment** | Jupyter Notebook |

---

## 💻 Usage

### Run the Complete Analysis

1. Open [loan_approve_minor_project.ipynb](loan_approve_minor_project.ipynb) in Jupyter Notebook
2. Execute cells sequentially to:
   - Load and explore the dataset
   - Handle missing values
   - Perform EDA
   - Encode features
   - Analyze correlations
   - Train and evaluate models
   - View comparative results

### Quick Start Example

```python
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('loan_approval_data.csv')

# Prepare features and target
X = df.drop('Loan_Approved', axis=1)
y = df['Loan_Approved']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Naive Bayes model
model = GaussianNB()
model.fit(X_train_scaled, y_train)

# Make predictions
predictions = model.predict(X_test_scaled)
```

---

## 🔍 Key Findings

### Dataset Insights

✅ **Balanced Dataset**: Good distribution of approved vs. rejected loans  
✅ **Feature Quality**: Mix of reliable numerical and categorical predictors  
✅ **Data Completeness**: Successfully handled all missing values  
✅ **Feature Relationships**: Strong correlations identified for model training

### Model Performance Insights

✨ **Naive Bayes Advantages**:
- Probabilistic approach works well for classification
- Handles both numerical and categorical features effectively
- Good precision in predicting loan approvals
- Computationally efficient

📊 **Model Workflow**:
```
Data Loading 
    ↓
Exploratory Data Analysis
    ↓
Missing Values Imputation
    ↓
Feature Encoding
    ↓
Correlation Analysis
    ↓
Train-Test Split & Scaling
    ↓
Model Training & Evaluation
    ↓
Best Model Selection (Naive Bayes)
```

---

## 📝 Project Information

- **Last Updated**: May 6, 2026
- **Project Type**: Machine Learning Classification - Binary Prediction
- **Status**: ✅ Complete with Best Model Identified
- **Python Version**: 3.x
- **License**: MIT

---

## 🤝 Contributing

Contributions are welcome! To improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📧 Contact & Support

For questions or suggestions about this project, feel free to reach out or open an issue on GitHub.

---

**Made with ❤️ for Machine Learning Enthusiasts**
