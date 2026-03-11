from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "I slept"

def get_embeddings(text):
  vector = model.encode(text)
  return vector
