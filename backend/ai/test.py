# from embeddings import get_embeddings

# text = "I slept"

# vector = get_embeddings(text)

# print("Vector length:", len(vector))
# print("First numbers:", vector[:5])

from embeddings import get_embeddings
from sklearn.metrics.pairwise import cosine_similarity

s1 = "sleep"
s2 = "slept"
s3 = "grocery"

v1 = get_embeddings(s1)
v2 = get_embeddings(s2)
v3 = get_embeddings(s3)

sim1 = cosine_similarity([v1],[v2])
sim2 = cosine_similarity([v1],[v3])

print("sleep vs slept:", sim1)
print("sleep vs grocery:", sim2)