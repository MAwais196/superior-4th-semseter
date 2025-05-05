# Knn_digits.py
import cv2
import numpy as np

def load_training_data():
    digits = cv2.imread("digits.png", cv2.IMREAD_GRAYSCALE)
    rows = np.vsplit(digits, 50)
    
    cells = []
    for row in rows:
        elem = np.hsplit(row, 50)
        for i in elem:
            i = i.flatten()
            cells.append(i)
    
    cells = np.array(cells, dtype=np.float32)
    k = np.arange(10)
    cells_labels = np.repeat(k, 250)
    
    return cells, cells_labels

def train_knn():
    cells, cells_labels = load_training_data()
    knn = cv2.ml.KNearest_create()
    knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)
    return knn

def predict_digit(knn, image):
    # Preprocess the image to match training data format
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (20, 20))
    gray = gray.flatten()
    gray = np.array([gray], dtype=np.float32)
    
    ret, result, neighbours, dist = knn.findNearest(gray, k=3)
    return int(result[0][0])