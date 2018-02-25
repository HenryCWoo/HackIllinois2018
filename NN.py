from keras.models import load_model
import numpy as np

model = load_model('motherModel.h5')
print(model.predict(np.matrix(np.zeros((1, 248)))))