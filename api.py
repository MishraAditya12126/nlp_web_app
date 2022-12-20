import paralleldots
API_key="ly8MIDL9xMF3NtcZitayne3kq3Fk8R7Z4HxzRaUNBY4"
paralleldots.set_api_key(API_key)

def ner(text):
    ner=paralleldots.ner(text)
    return ner

def sentiment(text):
    snt = paralleldots.sentiment(text)
    return snt

def abusive(text):
    abus = paralleldots.abuse(text)
    return abus



