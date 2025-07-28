Quick Start Guide for the Image Classification Project Important Things to Do Before Starting the Project

3.8 or later for Python Hardware: CPU (GPU is optional for faster training) Dependencies: requirements.txt Files: image_classification.py, image_classifier_gui.py, and requirements.txt

Set Up

Download or Clone:

Get project files, like from GitHub or a copy on your computer. Check that image_classification.py and image_classifier_gui.py are both in same folder.

Install things you need:

Save following to requirements.txt: tensorflow==2.15.0, opencv-python==4.8.0, matplotlib==3.7.1, numpy==1.24.3, and pillow==9.5.0.

run command "pip install -r requirements.txt"

Optional: To set up a virtual environment, type python -m venv venv source venv/bin/activate (for Linux and Mac) or venv\Scripts\activate (for Windows).

Step 1 of the project is to train the model.

Script: image_classification.py Purpose: To train a CNN on CIFAR-10, get about 70–80% accuracy, and save cifar10_model.h5 and cifar10_weights.h5. Run: Jupyter Notebook (the best way to go): Install Jupyter with pip put jupyter on your computer Begin: jupyter notebook Open image_classification.py or copy and paste it into a notebook with five cells.
