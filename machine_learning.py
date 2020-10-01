import tensorflow as tf
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt

class first_model():
    def create_model(self):
        self.feature = [1,2,3,4,5,6]
        self.label = [2,4,6,8,10,12]
        self.epochs = 50
        self.batch_size = 2
        layers = tf.keras.layers.Dense(units=1, input_shape=(1,))
        self.model = tf.keras.models.Sequential(layers)
        self.model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.1), loss='mean_squared_error', metrics=[tf.keras.metrics.RootMeanSquaredError()])
        history = self.model.fit(x=self.feature, y=self.label, epochs=self.epochs, batch_size=self.batch_size)
        df = pd.DataFrame(data=history.history)
        self.loss = df['loss']
        self.rmse = df['root_mean_squared_error']
        self.epoch = history.epoch
        print('prediction_output:', self.model.predict([250]))
        print('weight:', self.model.get_weights()[0])
        print('bias:', self.model.get_weights()[1])



    def plot_model(self):
        style.use('seaborn')
        fig = plt.figure()
        ax1 = fig.add_subplot(311)
        ax2 = fig.add_subplot(312)
        ax3 = fig.add_subplot(313)

        x0 = 0
        y0 = self.model.get_weights()[1]

        ax1.scatter(self.feature, self.label, label='graph of label against feature', color='green')
        scale = ax2.plot(self.epoch, self.loss, color='red', label='loss_curve')
        ax3.plot(self.epoch, self.rmse, color='red', label='rmse_loss_curve')


        plt.legend()
        plt.show()

main = first_model()
main.create_model()
main.plot_model()
