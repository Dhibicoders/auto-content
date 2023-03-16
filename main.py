from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the input parameters
    title = request.form['title']
    keywords = request.form['keywords']
    description = request.form['description']

    # Scrape data from Google
    url = f'https://www.google.com/search?q={title} {keywords}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.get_text()

    # Process the data to extract keywords
    keywords = [word.lower() for word in data.split() if word.isalpha() and word.lower() not in keywords.lower().split()]

    # Generate content
    content = f'Title: {title}\nKeywords: {keywords}\nDescription: {description}'

    # Return the result
    return render_template('result.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
