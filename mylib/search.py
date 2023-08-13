import pandas as pd
from sentence_transformers import SentenceTransformer, util
import faiss

model_name = "paraphrase-mpnet-base-v2"  # Change to the desired Sentence Transformer model
index_path = "mylib/vector_db"
df = pd.read_csv("mylib/combined.csv")

def create_faiss_index(embeddings, index_path):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner Product similarity
    index.add(embeddings)
    faiss.write_index(index, index_path)

def search_similar_texts(query, model_name, index_path, top_k=10):
    # Load the Sentence Transformer model
    model = SentenceTransformer(model_name)
    
    # Load the Faiss index
    index = faiss.read_index(index_path)
    
    # Embed the query using the model
    query_embedding = model.encode([query], convert_to_tensor=True)
    query_embedding = util.normalize_embeddings(query_embedding)
    
    # Search for similar embeddings in the index
    D, indices = index.search(query_embedding.cpu().numpy(), top_k)
    
    # Filter and get the relevant offers and their scores
    relevant_indices = [i for i, score in enumerate(D[0]) if 0.4 <= score <= 1.0]
    relevant_scores = [D[0][i] for i in relevant_indices]
    relevant_offers = [df['OFFER'][indices[0][i]] for i in relevant_indices]
    
    return relevant_offers, relevant_scores

if __name__ == "__main__":
    while True:
        user_query = input("Please enter Retailer, Brand, or Category (type 'exit' to quit): ")
        if user_query == "exit":
            break
        offers, scores = search_similar_texts(user_query, model_name, index_path)
        for text, score in zip(offers, scores):
            print(f"Similarity Score: {score:.4f}\nOffer: {text}\n")
