from chunks.text_helper import preprocess_text
from chunks.tiktoken_strategy import TiktokenStrategy
from chunks.spacy_strategy import SpacyStrategy
from chunks.sentence_transfomers_strategy import SentenceTransformersStrategy
from chunks.nltk_strategy import NltkStrategy
from chunks.markdown_strategy import MarkdownStrategy

file_path = "../text_to_test.txt"    

def open_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        file_contents = file.read()
        file_contents = preprocess_text(file_contents)
    return file_contents

file_contents = open_file(file_path)

#chunk_splitter = TiktokenStrategy()
chunk_splitter = SpacyStrategy()
#chunk_splitter = SentenceTransformersStrategy()
#chunk_splitter = NltkStrategy()
#chunk_splitter = MarkdownStrategy()

result = chunk_splitter.split(file_contents)

for chunk in result:
    print(chunk)
    print("====================================")