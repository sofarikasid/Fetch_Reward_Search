import pytest
from mylib.search import (
    search_similar_texts,
)  # Replace with the actual name of your module


def test_search_similar_texts():
    query = "Target"
    model_name = "paraphrase-mpnet-base-v2"
    index_path = "mylib/vector_db"

    offers, scores = search_similar_texts(query, model_name, index_path)

    assert len(offers) == len(scores)


if __name__ == "__main__":
    pytest.main()
