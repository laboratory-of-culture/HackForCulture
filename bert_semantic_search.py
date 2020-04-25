from sentence_transformers import SentenceTransformer
import scipy.spatial


def semantic_search(text,corpus,corpus_embeddings,embedder,closest_n):

    queries = [text]
    query_embeddings = embedder.encode([text])
    
    for query, query_embedding in zip([text], query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

    return [(corpus[idx].strip(), (1-distance)) for idx, distance in results[0:closest_n]]