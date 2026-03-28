from sentence_transformers import SentenceTransformer

model = None


def get_model():
    global model

    if model is None:
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    return model


def get_embeddings(text):
    model = get_model()
    return model.encode(text)