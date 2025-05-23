from tensorflow.keras.models import load_model
import numpy as np
import os
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Ensure the model path is correct
MODEL_PATH = r"C:\Users\Luchitha\Documents\Python\BDD\Backend\model\eeg_model.h5"  # Replace with the correct model path

# Check if the model exists
if not os.path.exists(MODEL_PATH):
    print(f"Model file not found at {MODEL_PATH}")
    exit()

# Try loading the model
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()


# Route for predicting EEG input
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from POST request
        data = request.get_json()

        # Extract EEG data from the input (Assuming it's a list of features)
        eeg_data = data.get("eeg_data")

        if eeg_data is None:
            return jsonify({"error": "No EEG data provided"}), 400

        # Ensure input data is formatted correctly
        input_data = np.array(eeg_data)  # Convert input to numpy array

        # Reshape input to match model's expected input shape (e.g., [1, num_features])
        input_data = input_data.reshape(
            1, -1
        )  # Adjust depending on your model's input shape

        # Make the prediction
        prediction = model.predict(input_data)

        # Use threshold to classify as 'Yes' or 'No'
        threshold = 0.5  # Adjust this threshold based on your model's output
        result = "Yes" if prediction[0] > 0.7 else "No"

        # Return the prediction as Yes/No
        return jsonify({"prediction": result})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": f"Failed to get prediction from the model: {e}"}), 500


if __name__ == "__main__":
    # Run the app
    app.run(debug=True)
