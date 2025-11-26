# Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs a complete **Exploratory Data Analysis (EDA)** on the famous Titanic dataset.  
The goal is to understand passenger demographics, survival patterns, correlations, and important factors that influenced survival rates during the tragedy.

---

## 📂 Dataset
The dataset used is **titanic.csv**, which contains passenger information such as:
- Age, Gender, Fare  
- Passenger Class  
- Survival Status  
- Siblings/Spouses, Parents/Children  
- Embarkation Port  

---

## 🛠 Tech Stack
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

---

## 📌 Project Highlights

### ✔ Data Loading & Basic Exploration
- Loaded dataset with `pandas`
- Displayed head, shape, and info
- Checked missing values and data types

### ✔ Data Cleaning
- Handled missing values (Age, Cabin, Embarked)
- Converted data types
- Removed unnecessary columns

### ✔ Data Visualization
Created detailed plots to understand:
- Survival distribution
- Gender-based survival comparison
- Survival vs Passenger class
- Age distribution
- Fare distribution
- Correlation heatmap

### ✔ Key Insights
- **Female survival rate is significantly higher than males**
- **1st Class passengers survived more; 3rd Class the least**
- **Age had moderate influence — children had better chances**
- **Fare showed strong correlation with survival (higher fare → higher survival)**

---

## 📈 Plots Included
- Countplots (Survived vs Gender, Survived vs Class)  
- Histograms (Age, Fare)  
- Heatmap showing correlations  

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/titanic-eda.git
