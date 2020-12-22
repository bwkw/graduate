import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import math

#モデルの作成
def create_model():
    model = keras.Sequential([
        keras.layers.Dense(1),
        keras.layers.Dense(128, activation="sigmoid"),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam',
                  loss="mean_squared_error",
                  metrics=['mse'])
    return model

model = create_model()

density = np.load("density_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")
pressure = np.load("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")

#訓練データとしてsin(i)上の点を食わせる
train_datas = density.tolist()
train_labels = pressure.tolist()
pressure_max = max(train_labels)
train_labels = [i/pressure_max for i in range(len(train_labels))]

#学習段階
model.fit(
    train_datas,train_labels,epochs=1000
)

#テスト段階
test_datas = []
for i in range(46):
    test_data = i/5
    test_datas.append(test_data)

test_predictions=model.predict(test_datas)


#訓練したモデルにpredictさせたものと正しいデータの比較
fig = plt.figure()
plt.plot(train_datas, train_labels, color="blue", marker="o", label="training")
plt.plot(test_datas, test_predictions, color="red", marker="v", label="funapp")
plt.legend()
plt.title("L6.0-7.0-0.002_L7.0-L25.0-0.036 approximation")
fig.savefig("L6.0-7.0-0.002_L7.0-L25.0-0.036.png")
