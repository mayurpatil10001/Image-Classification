import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load the trained model
model = tf.keras.models.load_model('cifar10_model.h5')
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def load_and_preprocess_image(file_path):
    # Load image with OpenCV
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = cv2.resize(img, (32, 32))  # Resize to match model input
    img = img / 255.0  # Normalize
    return img

def predict_image(file_path):
    img = load_and_preprocess_image(file_path)
    img_array = np.expand_dims(img, axis=0)  # Add batch dimension
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return predicted_class, confidence, img

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display image
        img = Image.open(file_path)
        img = img.resize((200, 200))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Predict class
        predicted_class, confidence, processed_img = predict_image(file_path)
        result_label.config(text=f'Prediction: {predicted_class} ({confidence:.2%})')

        # Show processed image (32x32) using Matplotlib
        plt.figure(figsize=(3,3))
        plt.imshow(processed_img)
        plt.title(f'Processed Image (32x32)\nPredicted: {predicted_class}')
        plt.axis('off')
        plt.show()

# Create GUI
root = tk.Tk()
root.title('Image Classifier')
root.geometry('400x400')

# Widgets
open_button = tk.Button(root, text='Load Image', command=open_image)
open_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

result_label = tk.Label(root, text='Prediction: None')
result_label.pack(pady=10)

# Start GUI
root.mainloop()