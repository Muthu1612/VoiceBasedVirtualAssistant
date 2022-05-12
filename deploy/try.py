from intent_classifier import *
from keras.models import load_model

model = load_model("../models/intent_classification.h5")


def infer_intent(text):
    # from keras.models import load_model
    # model = load_model("../models/intent_classification.h5")
    """ Takes as input an utterance an outputs a dictionary of intent probabilities """
    # Making sure that my text is a string
    string_text = re.sub(r"[^ a-z A-Z 0-9]", " ", text)

    # Converting to Keras form
    keras_text = token.texts_to_sequences(string_text)

    # Check for and remove unknown words - [] indicates that word is unknown
    if [] in keras_text:
        # Filtering out
        keras_text = list(filter(None, keras_text))
    keras_text = np.array(keras_text).reshape(1, len(keras_text))
    x = pad_tweets(keras_text, max_token_length)


    # Generate class probability predictions
    # You're using the overfit model to predict!
    intent_predictions = np.array(model.predict(x)[0])

    # Match probability predictions with intents
    pairs = list(zip(unique_intents, intent_predictions))
    dict_pairs = dict(pairs)

    # Output dictionary
    output = {
        k: v
        for k, v in sorted(dict_pairs.items(), key=lambda item: item[1], reverse=True)
    }

    return string_text, output

while True:
    x=str(input("Enter : "))
    string_text, conf_dict = infer_intent(x)
    print(f"You: {string_text}")
    print(f"Eve: \nIntents:{conf_dict}")
    check=input("Continue?")
    check=check.lower()
    n=['no','nope','nah']
    if check in n:
        break