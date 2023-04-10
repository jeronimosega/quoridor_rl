from quoridor_ai import Agent
from quoridor_logic import Quoridor
import tensorflow as tf
import numpy as np

# Define the reward function
def reward_function(state, action):
    if action == 'w':
        return state / 10.0
    else:
        return -state / 10.0

# Define the training loop
env = Quoridor()
agent = Agent()
optimizer = tf.keras.optimizers.Adam()

for i in range(1000):
    state = tf.constant(env.state, dtype=tf.float32)
    with tf.GradientTape() as tape:
        action = agent.act(state)
        reward = reward_function(env.state, action)
        next_state, _, done = env.step(action)
        if done:
            target = reward
        else:
            next_state = tf.constant(next_state, dtype=tf.float32)
            next_action_probs = agent.model(next_state)
            next_action = tf.argmax(next_action_probs)
            next_reward = reward_function(next_state, next_action)
            target = reward + next_reward
        loss = -tf.math.log(action_probs[action]) * (target - tf.reduce_mean(action_probs))
    gradients = tape.gradient(loss, agent.model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, agent.model.trainable_variables))