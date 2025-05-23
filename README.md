# EEG-Based Communication System for Paralyzed Patients 🧠💬
![Conceptual Overview](Documents/resource_images/welcome.png)

## Overview 🌟

This project aims to create a non-invasive EEG-based communication system to empower paralyzed patients, especially those with conditions like locked-in syndrome or quadriplegia, to communicate effectively with caregivers and their environment. By harnessing electroencephalography (EEG) signals, the system translates brain activity into binary "Yes" or "No" responses through an intuitive interface. This repository contains the code, documentation, and resources for two versions of the system, with iterative improvements addressing key challenges. 🚀

> 📄 For detailed information, refer to the Final Report.

## Project Objectives 🎯

* Enable reliable and efficient communication for paralyzed patients using EEG signals. ✅
* Develop a non-invasive, affordable, and scalable solution. 💸
* Enhance patient autonomy and quality of life by bridging the communication gap. 🌈

## System Architecture 🛠️

The system pipeline includes the following components:

### Signal Acquisition 📡

Captures EEG signals using gold cup electrodes placed on the scalp (e.g., forehead, temporal lobes, with ground and reference electrodes).

### Amplification and Filtering 🔊

Utilizes the NeuroSky ThinkGear ASIC module to amplify low-amplitude signals and filter noise (muscular artifacts, electrical interference).

### Classification 🤖

Employs machine learning to classify EEG signals into "Yes" or "No" responses based on predefined brainwave patterns.

### User Interface 🖥️

Displays classified outputs on an intuitive interface with Start/Stop controls for ease of use by caregivers.

### Enclosure 🛡️

Designed using SolidWorks to house components securely and ensure patient comfort.

## Key Hardware Components ⚙️

* **Gold Cup Electrodes 🥇**: High signal fidelity and patient comfort.
* **ADG408 Multiplexer 🔌**: Manages multiple electrode channels.
* **MT3608 Booster Module 🔋**: Provides stable 12V power from a 5V USB source.
* **NeuroSky ThinkGear ASIC Module 🧠**: Handles signal amplification and filtering.
* **ESP32 💻**: Manages signal processing and interfaces with the ML model.

## Model Versions 📚

### Version 1: Supervised 1D Convolutional Neural Network (CNN) 🧠

**Description**: Utilizes a 1D CNN for binary classification of EEG signals into "Yes" or "No". The model includes two Conv1D layers (32 and 64 filters, ReLU activation), MaxPooling1D layers, a Dense layer with dropout (0.5), and a final sigmoid layer. Trained on a motor imagery dataset from Kaggle for 100 epochs with 32 batches.

**Performance**: Achieved \~70% accuracy in binary classification. ⚖️

**Challenges**:

* **Manual Label Creation ❌**: Labels were created by calculating power in frequency bands (Delta, Theta, Alpha, Beta, Gamma) and manually assigning "Yes" or "No", which introduced potential bias and inaccuracy.
* **Single Time Instance ⏰**: Used only one time instance instead of a sequence of time steps, limiting temporal context for classification.

**Dataset**: Sourced from [Kaggle EEG Muse 2 Motor Imagery Dataset](https://www.kaggle.com/datasets/muhammadatefelkaffas/eeg-muse2-motor-imagery-brain-electrical-activity). 📊

**Code**: Available in `eeg-motor-imagery.ipynb`. 💻

### Version 2: Unsupervised K-means Clustering 🌐

**Description**: Transitioned to an unsupervised K-means clustering model to address limitations of the supervised approach. This version clusters EEG signal features without relying on manually created labels, improving robustness and reducing bias.

**Improvements**:

* **Eliminated Manual Labeling ✅**: K-means clustering groups EEG signal patterns naturally, avoiding the bias introduced by manual power-based labeling.
* **Incorporated Time Steps ⏳**: Processes sequences of time steps to capture temporal dynamics, enhancing classification accuracy for real-time applications.

**Status**: The unsupervised model is implemented but yet to be tested in real-world scenarios. 🧪

**Code**: Available in the repository (please specify the filename if uploaded separately). 📂

> ⚠️ Note: Both models are still in the testing phase and require real-world validation to ensure reliability in clinical settings. 🧼
