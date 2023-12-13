from unidecode import unidecode

def preprocess_text(text:str) -> str:
    text = unidecode(text, errors='ignore')
    #text = text.replace('\n', ' ')
    text = text.lstrip()
    return text
