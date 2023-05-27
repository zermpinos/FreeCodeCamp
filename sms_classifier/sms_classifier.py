import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

print(tf.__version__)

# get data files
train_file_path = "train-data.tsv"
test_file_path = "valid-data.tsv"


'''
Preprocess the data:
Load the data from the provided TSV files and convert it into a format suitable for training a text classification model
Tokenize the text and convert the labels to binary values.
'''


def load_data(file_path):
    data = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'text'])
    text = data['text'].tolist()
    labels = (data['label'] == 'ham').astype(int).tolist()
    return text, labels


train_text, train_labels = load_data(train_file_path)
test_text, test_labels = load_data(test_file_path)

'''
Text preprocessing:
Tokenize the text and convert all characters to lowercase. Pad the sequences to have the same length.
'''
tokenizer = Tokenizer(num_words=20000)
tokenizer.fit_on_texts(train_text)
train_sequences = tokenizer.texts_to_sequences(train_text)
train_padded = pad_sequences(train_sequences, maxlen=100)
test_sequences = tokenizer.texts_to_sequences(test_text)
test_padded = pad_sequences(test_sequences, maxlen=100)

'''
Create the model:
Use a simple LSTM model with an embedding layer, followed by an LSTM layer and a dense output layer.
'''
model = Sequential([Embedding(10000, 128, input_length=100), LSTM(128, return_sequences=True), LSTM(128),
                    Dense(1, activation='sigmoid')])

'''
Compile and train the model:
Compile the model using binary crossentropy loss and an optimizer (e.g., Adam). 
Train the model using the preprocessed train data.
'''
train_labels = np.array(train_labels)
test_labels = np.array(test_labels)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_padded, train_labels, epochs=500, validation_data=(test_padded, test_labels))


'''
Define the predict_message function:
Use the trained model to predict the probability of a message being "ham" or "spam" and return the probability
along with the predicted label.
'''


def predict_message(pred_text):
    """
    Run this cell to test your function and model. Do not modify contents.
    """
    pred_text = tokenizer.texts_to_sequences([pred_text])
    pred_padded = pad_sequences(pred_text, maxlen=100)
    prediction = model.predict(pred_padded)
    prediction_prob = np.round(prediction[0][0])
    return (prediction_prob, 'ham' if prediction_prob > 0.5 else 'spam')


def test_predictions():
    test_messages = [
        "how are you doing today",
        "sale today! to stop texts call 98912460324",
        "i dont want to go. can we try it a different day? available sat",
        "our new mobile video service is live. just install on your phone to start watching.",
        "you have won £1000 cash! call to claim your prize.",
        "i'll bring it tomorrow. don't forget the milk.",
        "wow, is your arm alright. that happened to me one time too"
    ]

    test_answers = ["ham", "spam", "ham", "spam", "spam", "ham", "ham"]
    passed = True

    for msg, ans in zip(test_messages, test_answers):
        prediction = predict_message(msg)
        if prediction[1] != ans:
            passed = False

    if passed:
        print("You passed the challenge. Great job!")
    else:
        print("You haven't passed yet. Keep trying.")


test_predictions()
