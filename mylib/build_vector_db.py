import pandas as pd
from sentence_transformers import SentenceTransformer, util
import faiss


def create_faiss_index(csv_file, column_name, model_name, index_path):
    # Load the Sentence Transformer model
    model = SentenceTransformer(model_name)

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file)

    # Extract the text data from the CSV
    texts = df[column_name].tolist()

    # Embed the text using the Sentence Transformer model
    embeddings = model.encode(texts, convert_to_tensor=True)

    # Normalize embeddings
    embeddings = util.normalize_embeddings(embeddings)

    # Create a Faiss index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner Product similarity

    # Add embeddings to the index
    index.add(embeddings.cpu().numpy())

    # Save the Faiss index
    faiss.write_index(index, index_path)


if __name__ == "__main__":
    # Example usage
    csv_file = "mylib/combined.csv"
    column_name = "combined"
    model_name = (
        "paraphrase-mpnet-base-v2"  # Change to the desired Sentence Transformer model
    )
    index_path = "mylib/vector_db"
    create_faiss_index(csv_file, column_name, model_name, index_path)
    print("Vector database created and indexed.")
