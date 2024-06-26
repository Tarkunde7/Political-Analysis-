from data_ingestion import extract_city_data
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

CHROMA_DATA_PATH = "E:\Political analytics\src\data_embeddings"

file_path = "E:\\Political analytics\\City profiles of maharastra.pdf"

def create_embeddings(file_path,city_name):
    # client = chromadb.PersistentClient("E:\Political analytics\src\data_embeddings")

    # embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # collection_name = "city_descriptions"
    # collection = client.create_collection(collection_name,embedding_function=embedding_function)

    # city_embeddings = {}  

    # for city, description in data.items():
    #     embedding = embedding_function.embed_documents(description)
    #     city_embeddings[city] = embedding


    # collection.add(list(city_embeddings.keys()), list(city_embeddings.values()))
    # return city_embeddings,collection

    embedding = SentenceTransformerEmbeddings(model_name = "all-MiniLM-L6-v2")

    text = extract_city_data(file_path).get(city_name)

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=100,
        chunk_overlap=20,
        length_function=len)
    
    chunks = text_splitter.split_text(text)

    db = Chroma.from_texts(chunks,embedding)

    return db


# city_embeddings = create_embeddings(extract_city_data(file_path=file_path),city_name="Mumbai")
# query = "All about Mumbai"
# docs = city_embeddings.similarity_search(query,k=5)
# print(docs)