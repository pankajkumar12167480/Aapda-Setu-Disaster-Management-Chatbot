# chatbot.py
import json
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import pickle
import os

lemmatizer = WordNetLemmatizer()

# load intents and model artifacts
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

model = load_model('model/chatbot_model.h5')
with open('model/words.pkl', 'rb') as f:
    words = pickle.load(f)
with open('model/classes.pkl', 'rb') as f:
    classes = pickle.load(f)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence, threshold=0.25):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]), verbose=0)[0]
    results = []
    for i, r in enumerate(res):
        if r > threshold:
            results.append({"intent": classes[i], "probability": float(r)})
    results.sort(key=lambda x: x["probability"], reverse=True)
    return results

def get_response(intents_list, intents_json):
    if not intents_list:
        return "Sorry, I didn’t understand that. Could you please rephrase?"
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "Sorry, I didn't get that."

def chatbot_response(msg):
    ints = predict_class(msg)
    resp = get_response(ints, intents)
    return resp

# quick manual test if run directly
if __name__ == "__main__":
    print("Aapda Setu Chatbot (local test). Type 'quit' to exit.")
    while True:
        text = input("You: ")
        if text.lower() in ("quit", "exit"):
            break
        print("Bot:", chatbot_response(text))
