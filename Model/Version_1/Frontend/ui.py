import gradio as gr
import requests

# URL of the Flask API
API_URL = "http://127.0.0.1:5000/predict"  # Replace with your Flask app URL


# Define the function to call the API and get the prediction
def get_prediction(eeg_data):
    try:
        # Prepare data for API request
        data = {"eeg_data": [float(i) for i in eeg_data.split(",")]}

        # Send POST request to the Flask API
        response = requests.post(API_URL, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract prediction from the response
            prediction = response.json().get("prediction", "Error")
            return prediction
        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"


# Create Gradio interface
def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## EEG prediction by BrainSpeak")

        gr.Markdown("### Enter EEG Features (comma-separated):")

        # Input for EEG features
        eeg_input = gr.Textbox(
            label="Enter EEG Features", placeholder="0.5, 0.6, 0.7, ..., 0.08"
        )

        # Button to submit input
        submit_button = gr.Button("Submit")

        # Output for Prediction
        prediction_output = gr.Textbox(label="Prediction", interactive=False)

        # Flagging output (if needed)
        flag_output = gr.Button("Flag")

        # Submit button action
        submit_button.click(
            fn=get_prediction, inputs=eeg_input, outputs=prediction_output
        )

    return demo


# Run the Gradio interface
if __name__ == "__main__":
    ui = create_ui()
    ui.launch(debug=True)
