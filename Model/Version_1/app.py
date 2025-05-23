import gradio as gr
import serial
import threading
import time
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
MODEL_PATH = r"C:\Users\Luchitha\Documents\Python\BDD\Backend\f_model.h5"  # Update the path to your model
model = load_model(MODEL_PATH)

# Serial port settings
SERIAL_PORT = (
    "COM3"  # Replace with your port (e.g., /dev/ttyUSB0 on Linux, COMx on Windows)
)
BAUD_RATE = 9600

# Global variable to store the latest data
latest_data = {"RAW": 0, "Delta": 0, "Theta": 0, "Alpha": 0, "Beta": 0, "Gamma": 0}
prediction_result = "Waiting for data"


# Function to read from the serial port
def read_serial():
    global latest_data
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8").strip()
                try:
                    # Example: Parse CSV or JSON (modify as per your data format)
                    # Assuming CSV format: RAW,Delta,Theta,Alpha,Beta,Gamma
                    raw, delta, theta, alpha, beta, gamma = map(float, line.split(","))
                    latest_data = {
                        "RAW": raw,
                        "Delta": delta,
                        "Theta": theta,
                        "Alpha": alpha,
                        "Beta": beta,
                        "Gamma": gamma,
                    }
                except ValueError:
                    print(f"Error parsing line: {line}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")


# Start the serial reading in a separate thread
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()


# Function to run the ML model on the latest data
def predict():
    global latest_data, prediction_result

    # Prepare input data for the model
    input_data = np.array(
        [
            [
                latest_data["RAW"],
                latest_data["Delta"],
                latest_data["Theta"],
                latest_data["Alpha"],
                latest_data["Beta"],
                latest_data["Gamma"],
            ]
        ]
    )
    # Predict using the loaded model
    prediction = model.predict(input_data)[0][0]  # Assuming binary classification
    prediction_result = "Yes" if prediction > 0.5 else "No"
    return (
        latest_data["RAW"],
        latest_data["Delta"],
        latest_data["Theta"],
        latest_data["Alpha"],
        latest_data["Beta"],
        latest_data["Gamma"],
        prediction_result,
    )


# Gradio Interface
with gr.Blocks() as ui:
    gr.Markdown("### EEG Data and ML Model Prediction")
    raw = gr.Number(label="RAW")
    delta = gr.Number(label="Delta")
    theta = gr.Number(label="Theta")
    alpha = gr.Number(label="Alpha")
    beta = gr.Number(label="Beta")
    gamma = gr.Number(label="Gamma")
    prediction = gr.Textbox(label="Prediction", value="Waiting for data")

    gr.Button("Run Prediction").click(
        predict, [], [raw, delta, theta, alpha, beta, gamma, prediction]
    )

# Run the Gradio app
if __name__ == "__main__":
    ui.launch()
