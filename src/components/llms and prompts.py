from langchain_community.vectorstores import Chroma
from transformers import T5ForConditionalGeneration, T5Tokenizer
from embeddings import create_embeddings


model_name = "google/flan-t5-large" 
file_path = "E:\\Political analytics\\City profiles of maharastra.pdf"

llm = T5ForConditionalGeneration.from_pretrained(model_name)

tokenizer = T5Tokenizer.from_pretrained(model_name)

def generate_info(file_path,city_name,query):
    if query:    
        
        db = create_embeddings(file_path,city_name)
        
        city_embeddings = db.similarity_search(query=query,k=10)
        #input_text = f"Describe in brief about city of {city_name}: {city_embeddings}" 

        input_text = f"Describe {query} in {city_name}. (Use the information from {city_embeddings} to inform the description)"
        
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        
        outputs = llm.generate(input_ids, max_length=600, num_beams=4, early_stopping=True)
        
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            

        return generated_text
    else:
        return "Please do enter a query"

# def get_solution(file_path,city_name):
#     db = create_embeddings(file_path,city_name)
#     city_embeddings = db.similarity_search(query=f"All about the {city_name}",k=10)

    
print(generate_info(file_path=file_path,city_name="Mumbai",query= "What are the major issues in Mumbai? "))













