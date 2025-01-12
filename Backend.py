from flask import Flask, request, jsonify
from variables import *
import cohere
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import tweepy
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import feedparser

load_dotenv()

API_KEY = os.getenv('COHERE_API_KEY')
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Initialize Flask app and Cohere client
app = Flask(__name__)
cohere_client = cohere.Client(API_KEY)  # Replace with your Cohere API key
co = cohere.ClientV2()
co1 = cohere.Client()

# EXTRACTING TEXT FROM LINKS AND PDFS

def extract_text_from_link(link):
    """
    Extract text from a link, handling both PDF and HTML formats.

    Args:
    - link (str): The URL of the resource (PDF or webpage).

    Returns:
    - str: Extracted text from the PDF or webpage.
    """
    try:
        # Fetch the content from the link
        html = urlopen(link).read()
        soup = BeautifulSoup(html, features="html.parser")
        
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
            
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text

    except Exception as e:
        return str(e)
    

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

# USING COHERE API TO SUMMARIZE/ANALYZE TEXT

@app.route('/analyze-pdf', methods=['POST'])
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
                    "content": f"Report the environment score and provide the scores for each metric and a brief summary of the data and company environmental missions: {text}"
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
        
@app.route('/analyze-link', methods=['POST'])
def analyze_link():
    print(request.json)  # Printing the incoming JSON request data
    
    """
    Endpoint to analyze content from a provided link.
    """
    if 'link' not in request.json:
        return jsonify({"error": "No link provided"}), 400

    link = request.json['link']  # Get the URL from the request

    try:
        # Extract text from the provided link (could be a PDF or HTML webpage)
        text = extract_text_from_link(link)

       # Use the Chat API for analysis
        response = co.chat(
            model='command-r7b-12-2024',  # Specify the correct model
            messages=[
                {
                    "role": "user",
                    "content": f"Report the environmental score and provide the scores for each metric and a brief summary of the data and company environmental missions: {text}"
                 }
            ]
        )
        
        assistant_message = response.message.content[0].text
        
        print(assistant_message)
        
        return jsonify({"analysis": assistant_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# SELENIUM SCRAPE HEADLINES IN NEWS TAB AFTER SEARCHING [COMPANY] ENVIRONMENTAL REPORT

@app.route('/get-sentiments', methods=['GET'])
def get_sentiments():
    categories = ["climate", "energy", "poverty"]
    data = {}
    for category in categories:
        data[category] = analyze(category)
    return jsonify(data) # i don't remember if this is the correct way to conver to json
        

def analyze(category): # i moved the api call idk how to reorganize these function definitions
    # Function to perform sentiment analysis
    def analyze_sentiment(category):
        links = []
        examples = []
        if category == "climate": # populate variables based on category
            links = CLIMATE_LINKS
            examples = CLIMATE_EXAMPLES
        elif category == "energy":
            links = ENERGY_LINKS
            examples = ENERGY_EXAMPLES
        elif category == "poverty":
            links = POVERTY_LINKS
            examples = POVERTY_EXAMPLES
        
        pages = rss_news(links)
        
        for page in pages: # append the classification to each page array
            response = co1.classify(
                model="embed-english-light-v3.0",
                inputs=[page[0]],
                examples=examples,
            )
            
            for classification in response.classifications:
                page.append(classification.prediction)
        
        return pages

    # def scrape_news(company_name):
    #     # Initialize WebDriver
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #     # Search Google for the environmental report
    #     search_query = f"{company_name} company environmental and sustainability news"
    #     driver.get("https://www.google.com/")

    #     # Find the search bar, type the query, and hit Enter
    #     search_box = driver.find_element(By.NAME, "q")
    #     search_box.send_keys(search_query)
    #     search_box.send_keys(Keys.RETURN)

    #     # Wait for the results to load
    #     time.sleep(2)

    #     # Locate and click the "News" tab
    #     try:
    #         news_tab = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'tbm=nws')]"))
    #         )
    #         news_tab.click()
    #     except Exception as e:
    #         print("News tab not found:", e)
    #         driver.quit()
    #         return []
        
    #     headlines = []
    #     keywords = ["environmental", "sustain", "report", "CO2", "emissions", "carbon", "footprint", "climate", "greenhouse", "gas", "reduction", "energy", "efficiency", "renewable", "waste", "recycling", "conservation", "ecosystem", "protection", "pollution", "ESG", "stewardship", "green", "regulation", "policy", "initiative", "program", "strategy", "target"]
        
    #     # go through two pages of headlines
    #     for i in range(2):
    #         # Wait for headlines to load
    #         time.sleep(1)

    #         # Extract all headlines
    #         try:
    #             articles = driver.find_elements(By.CLASS_NAME, "n0jPhd.ynAwRc.MBeuO.nDgy9d")
    #             for article in articles:
    #                 if any(keyword in article.text for keyword in keywords):
    #                     headlines.append(article.text)
    #         except Exception as e:
    #             print("Error extracting articles:", e)

    #         # Click the "Next" button to navigate to the next page
    #         try:
    #             next_button = WebDriverWait(driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, "//a[@id='pnnext']"))
    #             )
    #             next_button.click()
    #         except Exception as e:
    #             print("Next button not found:", e)
    #             break

    #     # Close the driver after scraping
    #     driver.quit()
        
    #     return headlines
    
    def rss_news(links):
        pages = []
        
        # URL of the RSS feed
        for i in range(len(links)):
            rss_url = links[i]

            # Parse the RSS feed
            feed = feedparser.parse(rss_url)

            # Iterate through the feed entries and print the required information
            for entry in feed.entries:
                title = entry.title
                link = entry.link
                description = entry.description
                
                pages.append([title, description, link])
                
        return pages
    
    # Analyze the sentiment of the headlines
    pages = analyze_sentiment(category)
    
    return pages



if __name__ == '__main__':
    app.run(debug=True)