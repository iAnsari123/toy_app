import streamlit as st
import pickle

st.title("Student Placement Prediction")

st.subheader("Please input data")

# Initialize session state for inputs (separate session keys for resetting)
if "cgpa_value" not in st.session_state:
    st.session_state.cgpa_value = 0.0

if "iq_value" not in st.session_state:
    st.session_state.iq_value = 0


def reset_inputs():
    # Reset the values in session state
    st.session_state.cgpa_value = 0.0
    st.session_state.iq_value = 0


# Input fields for CGPA and IQ
cgpa = st.number_input(
    label="Enter Cumulative Grade Point Average (CGPA)",
    placeholder="e.g., 3.41",
    max_value=4.00,
    value=st.session_state.cgpa_value,  # Use session state for default value
    key="cgpa_input",  # Unique key for this widget
)
iq = st.number_input(
    label="Enter IQ",
    placeholder="e.g., 145",
    max_value=200,
    value=st.session_state.iq_value,  # Use session state for default value
    key="iq_input",  # Unique key for this widget
)

# Predict button
if st.button("Predict", type="primary"):
    try:
        # Load the model
        model = pickle.load(open("model.pkl", "rb"))

        # Predict
        result = model.predict([[cgpa, iq]])[0]

        # Display the result
        st.write(
            "The student is likely :red[**to be placed**]"
            if result == 1
            else "The student is likely :red[**not to be placed**]"
        )
    except FileNotFoundError:
        st.error("Model file not found. Please check 'model.pkl' path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Reset the session state values
    reset_inputs()
