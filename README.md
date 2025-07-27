Image Classification Project - Quick Start Guide
Key Points to Run the Project
Prerequisites

Python: 3.8 or higher
Hardware: CPU (GPU optional for faster training)
Dependencies: Listed in requirements.txt
Files: image_classification.py, image_classifier_gui.py, requirements.txt

Setup

Clone or Download:

Get the project files (e.g., from GitHub or local copy).
Ensure image_classification.py and image_classifier_gui.py are in the same directory.


Install Dependencies:

Save requirements.txt:tensorflow==2.15.0
opencv-python==4.8.0
matplotlib==3.7.1
numpy==1.24.3
pillow==9.5.0


Run:pip install -r requirements.txt




Optional: Virtual Environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows



Running the Project
Step 1: Train the Model

Script: image_classification.py
Purpose: Trains a CNN on CIFAR-10, achieves ~70–80% accuracy, saves cifar10_model.h5 and cifar10_weights.h5.
Run:
Jupyter Notebook (preferred):
Install Jupyter: pip install jupyter
Start: jupyter notebook
Open image_classification.py or copy into a notebook with 5 cells.

Python Script:python image_classification.py


If plots don’t show, add:import matplotlib
matplotlib.use('TkAgg')






Output: Sample images, model summary, accuracy (~70%+), plots, saved files.

Step 2: Use the GUI

Script: image_classifier_gui.py
Purpose: Classifies user-uploaded images using the trained model.
Requirements: cifar10_model.h5 in the same directory.
Run:python image_classifier_gui.py


Usage:
Click "Load Image" to select a .jpg/.png.
View the image, predicted class (e.g., "dog (78%)"), and processed 32x32 image.


Output: Tkinter window with image and prediction, Matplotlib window with processed image.

Troubleshooting

Model Missing: Ensure cifar10_model.h5 is in the directory (run image_classification.py first).
Dependency Issues: Verify TensorFlow 2.15.0 and other packages are installed.
No Plots: Use Jupyter or add matplotlib.use('TkAgg') in scripts.
Low Accuracy: Increase epochs in image_classification.py (Cell 3, e.g., epochs=20).

Notes

Model Files: If large, upload cifar10_model.h5 and cifar10_weights.h5 to Google Drive and download before running GUI.
Training Time: ~5–10 min on CPU.
Date: Instructions valid as of July 27, 2025, 1:58 PM IST.
