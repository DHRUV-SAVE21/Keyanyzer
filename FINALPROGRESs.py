import requests #url 
from bs4 import BeautifulSoup
from collections import Counter
import re

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
    return None

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from HTML body
    text = soup.get_text(separator=' ')
    return text

def analyze_keywords(text):
    # Split text into words and count frequencies
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)
    return word_freq

def main():
    url = input("Enter URL to analyze: ").strip()
    html = fetch_page(url)
    if html:
        text = extract_text(html)
        word_freq = analyze_keywords(text)
        print("Keyword frequencies:")
        for word, freq in word_freq.most_common(10):  # Print top 10 most frequent words
            print(f"{word}: {freq}")
    else:
        print("Failed to fetch or analyze the page.")

if __name__ == "__main__":   #This is a module into another script and call the main function useful for organizing and separting code 
    #the above give me the premission to reuse the code  
    main()














# When we talk about analyzing text for keyword frequencies, it typically involves using software tools or scripts .
#     it retrive web pages,text,document.and after the present the result in structured format.

# The purpose of analyzing text in this way is to gain insights into the content without relying on manual reading or 
# interpretation. This method is efficient for processing large volumes of text quickly and objectively.
# It's particularly useful in fields like Search Engine Optimization, content analysis, sentiment analysis, and data mining, 
# where understanding the distribution and importance of keywords can inform decision-making and strategy.

#in his human can also play a role in insights and keyword frequencies 
