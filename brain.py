from imageai.Prediction import ImagePrediction

import os

execution_path = os.getcwd()

prediction = ImagePrediction()

prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath()
prediction.loadModel()
