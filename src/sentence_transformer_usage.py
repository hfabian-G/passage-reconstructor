from passage_loader import load_passage
from sentence_transformers import SentenceTransformer
import numpy as np

def encode_string(string: str):
    transformer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    encoded_string = transformer.encode(string)
    return encoded_string

def calculate_similarity(embedding_original: np.array, embedding_2: np.array):
    transformer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return transformer.similarity(embedding_original, embedding_2)

if __name__ == '__main__':
    passage = load_passage('./passages/passage_1.txt')
    encoded_string = encode_string(passage)
    
    semantic_similarity = calculate_similarity(encoded_string,encoded_string)
    print()