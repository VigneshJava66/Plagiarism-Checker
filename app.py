import string
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)

def get_word_counts(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the text into words and count their occurrences
    word_counts = Counter(text.split())
    
    return word_counts

def compare_texts(text1, text2):
    # Get the word counts for both texts
    text1_word_counts = get_word_counts(text1)
    text2_word_counts = get_word_counts(text2)
    
    # Calculate the Jaccard similarity coefficient
    intersection = set(text1_word_counts.keys()) & set(text2_word_counts.keys())
    union = set(text1_word_counts.keys()) | set(text2_word_counts.keys())
    jaccard_similarity = len(intersection) / len(union)
    
    return jaccard_similarity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    text1 = request.form['text1']
    text2 = request.form['text2']
    
    similarity = compare_texts(text1, text2)
    return render_template('result.html', similarity=similarity)

if __name__ == '__main__':
    app.run(debug=True)
