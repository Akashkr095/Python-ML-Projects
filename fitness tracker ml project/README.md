
🔥 Calories Burnt Prediction Web App

A machine-learning powered web application that predicts the number of calories burned during exercise based on user-entered health and workout parameters. Built using Python, Scikit-Learn, Pandas, and Streamlit.

📌 Project Overview

This project predicts how many calories a person burns during physical activity using user inputs such as:

 	 Age

    Gender

    Height

    Weight

    Exercise Duration

    Heart Rate

    Body Temperature

The backend uses a Random Forest Regression model, trained on combined exercise and calorie datasets. The frontend is built using Streamlit, allowing users to get instant calorie predictions in a clean and interactive interface.

🎯 Problem Statement

Manually tracking calories burned during exercise is inaccurate and often unavailable without fitness devices.
This app provides an ML-based estimation system that gives instant calorie predictions from simple user inputs.

🧠 Machine Learning Approach
✔ Dataset Used

	Two CSV files are used:

  	exercise.csv

  	calories.csv

	Both share the common column User_ID.

	✔ Steps:

  	Load Datasets

  	Merge Using User_ID

  	Clean Data

  	Remove duplicates

  	Drop User_ID

  	Feature Engineering

  	Gender encoding

  	One-Hot Encode Categorical Variables

  	Prepare Feature Matrix (X) and Labels (y)

  	Train Random Forest Regressor on Full Dataset

  	Predict Calories for New User Inputs

🏗️ Project Workflow
Import Libraries → Load CSV Files → Merge → Clean → 
Feature Engineering → Encode → Train RF Model →
Build Streamlit Form → Take User Input → Preprocess →
Align Columns → Predict → Display Result

🖥️ Streamlit Web App

	The user-friendly interface includes:

  	Drop-down for gender

  	Number inputs for age, height, weight

  	Inputs for duration, heart rate, and body temperature

  	A prediction button

Real-time output display
