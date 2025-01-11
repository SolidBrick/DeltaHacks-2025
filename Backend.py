from flask import Flask, request, jsonify
import cohere
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('COHERE_API_KEY')

# Initialize Flask app and Cohere client
app = Flask(__name__)
cohere_client = cohere.Client(API_KEY)  # Replace with your Cohere API key
co = cohere.ClientV2()

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/analyze', methods=['POST'])
def analyze_pdf():
    print(request.files)
    """
    Endpoint to analyze the uploaded PDF.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # Save the uploaded file
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)

    try:
        # Extract text from the PDF
        text = extract_text_from_pdf(file_path)

        # Use the Chat API for analysis
        response = co.chat(
            model='command-r7b-12-2024',  # Specify the correct model
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze the following text: {text}"
                 }
            ]
        )
        
        assistant_message = response.message.content[0].text
        
        print(assistant_message)
        
        return jsonify({"analysis": assistant_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Clean up the saved file
        os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)
