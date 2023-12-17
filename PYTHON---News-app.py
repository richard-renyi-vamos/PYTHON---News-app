import requests
import tkinter as tk
from tkinter import messagebox

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
NEWS_API_KEY = 'YOUR_API_KEY'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
COUNTRY_CODE = 'hu'  # Replace with the desired country code

def fetch_news():
    params = {
        'country': COUNTRY_CODE,
        'apiKey': NEWS_API_KEY
    }
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        news_titles = "\n\n".join([f"- {article['title']}" for article in articles])
        show_popup(news_titles)
    else:
        show_popup("Failed to fetch news. Please try again later.")

def show_popup(news):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo("Latest News", news)

    root.mainloop()

if __name__ == "__main__":
    fetch_news()
