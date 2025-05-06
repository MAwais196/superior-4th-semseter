# hadithbot_logic.py
import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

# Load pre-processed data and models
hadith_df_en = pd.read_csv('cleaned_hadith_data_english.csv')
hadith_df_ar = pd.read_csv('cleaned_hadith_data_arabic.csv')
embeddings_en = np.load('hadith_embeddings_en.npy')
embeddings_ar = np.load('hadith_embeddings_ar.npy')
model_en = SentenceTransformer('paraphrase-MiniLM-L6-v2')
model_ar = SentenceTransformer('bert-base-multilingual-cased')
index_en = faiss.read_index('hadith_faiss_en.index')
index_ar = faiss.read_index('hadith_faiss_ar.index')

def retrieve_similar_hadiths(query, language='english', k=3):
    """Retrieve similar Hadiths based on the query"""
    try:
        if language.lower() == 'arabic':
            model = model_ar
            index = index_ar
            df = hadith_df_ar
            embeddings = embeddings_ar
        else:
            model = model_en
            index = index_en
            df = hadith_df_en
            embeddings = embeddings_en
            
        # Encode the query
        query_embedding = model.encode([query])
        
        # Search the index
        distances, indices = index.search(query_embedding, k)
        
        # Prepare results
        results = []
        for i in range(k):
            idx = indices[0][i]
            hadith = df.iloc[idx]
            results.append({
                'text': hadith['Hadith'],
                'book': hadith['Book_Name'],
                'chapter': hadith['Chapter_Number'],
                'section': hadith['Section_Number'],
                'number': hadith['Hadith_number'],
                'grade': hadith['English_Grade'] if language == 'english' else hadith['Arabic_Grade'],
                'distance': float(distances[0][i])
            })
            
        return results
        
    except Exception as e:
        print(f"Error retrieving Hadith: {str(e)}")
        return []

def process_hadith_message(message):
    """Process user message and return appropriate response"""
    if not message or not isinstance(message, str):
        return "Could you please repeat your question about Hadith?"
    
    message = message.lower()
    
    # Simple keyword matching for greetings
    if any(w in message for w in ["hi", "hello", "hey", "assalam"]):
        return "Assalamu alaikum! I can help you find relevant Hadith. Please ask your question."
    elif "arabic" in message:
        # Extract the actual query (remove "arabic" keyword)
        query = message.replace("arabic", "").strip()
        results = retrieve_similar_hadiths(query, language='arabic')
        return format_hadith_response(results, arabic=True)
    else:
        # Default to English search
        results = retrieve_similar_hadiths(message)
        return format_hadith_response(results)

def format_hadith_response(results, arabic=False):
    """Format the retrieved Hadiths into a response string"""
    if not results:
        return "I couldn't find relevant Hadith for your query. Could you try rephrasing?"
    
    response = "Here are some relevant Hadith:\n\n"
    for i, hadith in enumerate(results, 1):
        response += f"{i}. {hadith['text']}\n"
        response += f"   - Source: {hadith['book']}, Book {hadith['chapter']}, Section {hadith['section']}, Hadith {hadith['number']}\n"
        response += f"   - Grade: {hadith['grade']}\n\n"
    
    if arabic:
        response += "\nNote: The above Hadith are in Arabic as requested."
    else:
        response += "\nNote: The above are English translations of the Hadith."
    
    return response