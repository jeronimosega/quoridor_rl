import tensorflow as tf

# Define the RL agent
class Agent:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(12, kernel_size=(3,3), strides=(1,1), padding='same', activation='relu'),
            tf.keras.layers.Conv2D(24, kernel_size=(3,3), strides=(1,1), padding='same', activation='relu'),
            tf.keras.layers.Dense(30, activation='relu'),
            tf.keras.layers.Dense(5, activation='softmax')
        ])

    def act(self, state):
        action_probs = self.model.predict(state)
        return tf.random.categorical(action_probs, 1)[0, 0]
