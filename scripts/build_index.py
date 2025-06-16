import numpy as np
import faiss
import os

embeddings = np.load("outputs/embeddings.npy")
faiss.normalize_L2(embeddings)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "outputs/faiss.index")

print("ok Index FAISS sauvegardé dans outputs/faiss.index")
