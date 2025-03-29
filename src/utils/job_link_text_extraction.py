import requests
import os
from bs4 import BeautifulSoup
def extract_text_from_url(url):
    """Extracts text content from a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs])
        print(text)
        return text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
        return None