import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def main():
    st.title("Calories Burnt Predictor")
    st.write("Fill your details and get an estimated calories burnt value.")

    # ---- User Input Form ----
    with st.form("user_input_form"):
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["male", "female"])
            age = st.number_input("Age (years)", min_value=10, max_value=80, value=25)
            height = st.number_input("Height (cm)", min_value=100, max_value=220, value=170)
            weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

        with col2:
            duration = st.number_input("Exercise Duration (minutes)", min_value=1, max_value=300, value=30)
            heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=220, value=110)
            body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=38.0, step=0.1)

        submitted = st.form_submit_button("Predict Calories 🔍")

    # ---- Prediction ----
    if submitted:
        user_df = pd.DataFrame([{
            "Gender": gender,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Duration": duration,
            "Heart_Rate": heart_rate,
            "Body_Temp": body_temp
        }])

        # Load and prepare FULL training data
        exercise = pd.read_csv("exercise.csv")
        calories = pd.read_csv("calories.csv")

        # Merge on User_ID
        df = exercise.merge(calories, on="User_ID")

        # Remove duplicate users
        df = df.drop_duplicates(subset=["User_ID"], keep="first")

        # Drop User_ID
        df = df.drop(columns=["User_ID"])

        # 3) One-hot encode training data
        df_enc = pd.get_dummies(df, drop_first=True)

        # Split into X (features) and y (target)
        X = df_enc.drop(columns="Calories")
        y = df_enc["Calories"]

        # Train model on FULL data
        model = RandomForestRegressor(
            n_estimators=500,
            max_depth=8,
            random_state=42
        )
        model.fit(X, y)

        # Preprocess user input
        user_enc = pd.get_dummies(user_df, drop_first=True)
        user_enc = user_enc.reindex(columns=X.columns, fill_value=0)

        # Predict
        pred_calories = model.predict(user_enc)[0]

        st.success(f"Estimated Calories Burnt: **{pred_calories:.2f} kcal**")


if __name__ == "__main__":
    main()
