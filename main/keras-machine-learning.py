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
        keras.layers.Dense(128, activation="sigmoid"),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam',
                  loss="mean_squared_error",
                  metrics=['mse'])
    return model

model = create_model()

density = np.load("density.npy")
pressure = np.load("pressure.npy")

#訓練データとしてsin(i)上の点を食わせる
train_datas = density.tolist()
train_labels = pressure.tolist()

#学習段階
model.fit(
    train_datas,train_labels,epochs=100
)

#テスト段階
test_datas = []
for i in range(101):
    test_data = 2.5*i/100
    test_datas.append(test_data)

test_predictions=model.predict(test_datas)


#訓練したモデルにpredictさせたものと正しいデータの比較

plt.plot(train_datas, train_labels, color="blue", marker="o", label="training")
plt.plot(test_datas, test_predictions, color="red", marker="v", label="funapp")
plt.legend()
plt.title("approximation")
plt.show()