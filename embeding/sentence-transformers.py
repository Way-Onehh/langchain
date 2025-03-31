from langchain_huggingface import HuggingFaceEmbeddings 

model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings_model  = HuggingFaceEmbeddings(model_name=model_name)
embeddings=[]
embeddings.append(embeddings_model.embed_query("你是sb"))
embeddings.append(embeddings_model.embed_query("你是帅哥"))
embeddings.append(embeddings_model.embed_query("我是帅哥"))

import numpy as np

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

similarity=[]
similarity.append(cosine_similarity(embeddings[0], embeddings[1]))
similarity.append(cosine_similarity(embeddings[1], embeddings[2]))
similarity.append(cosine_similarity(embeddings[2], embeddings[0]))
print("Cosine Similarity:", similarity[0])
print("Cosine Similarity:", similarity[1])
print("Cosine Similarity:", similarity[2])