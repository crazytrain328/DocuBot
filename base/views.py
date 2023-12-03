from django.shortcuts import render
import PyPDF2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import io
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

model = SentenceTransformer('all-MiniLM-L6-v2')

def my_model():
    return model

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
 

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    text = ' '.join(filtered_words)
    return text
    
# Function to create embeddings
def create_embeddings(text, model):
    return model.encode(text, show_progress_bar=False)

# Function to handle a query
def handle_query(query, model, embeddings, text_segments):
    # Ensure query_embedding is 2D
    query_embedding = model.encode([query], show_progress_bar=False).reshape(1, -1)
    
    # Ensure embeddings is 2D
    # This depends on how you create and store your embeddings
    embeddings = np.array(embeddings)

    # Calculate cosine similarity
    similarities = cosine_similarity(query_embedding, embeddings)
    most_similar_idx = np.argmax(similarities)
    return text_segments[most_similar_idx]

 
def home(request):
    response = ""
    model = my_model()

    if request.method == "POST":
        if 'pdf' in request.FILES:
            pdf_file = request.FILES['pdf']
            raw_text = extract_text_from_pdf(pdf_file)
            print(raw_text)
            processed_text = preprocess_text(raw_text)
            text_segments = processed_text.split('.')  # Splitting by sentences

            # Initialize the model
            embeddings = create_embeddings(text_segments, model)

            request.session['embeddings'] = embeddings.tolist()
            request.session['text_segments'] = text_segments
        else:
            # Handle chat query
            query = request.POST.get('query', '')
            embeddings = np.array(request.session.get('embeddings', []))
            text_segments = request.session.get('text_segments', [])

            if model and len(embeddings) > 0 and len(text_segments) > 0:
                response = handle_query(query, model, embeddings, text_segments)
                response= process_response(response)
                
            else:
                response = "Please upload a PDF first."

    return render(request, 'base/home.html', {'response': response})

def process_response(response):
    response_list= response.split('\n')
    return response_list
    