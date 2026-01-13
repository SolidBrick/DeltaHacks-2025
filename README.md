# 🌱 EcoDash
EcoDash is a web platform that aggregates recent climate-related news and evaluates how each article impacts progress toward sustainability goals. By leveraging AI-powered sentiment analysis, EcoDash turns scattered information into an accessible, easy-to-read dashboard that helps users quickly understand global progress toward a more sustainable future.

## Features
- Automated News Aggregation  
  Fetches recent articles using RSS feeds to ensure up-to-date coverage.

- AI-Powered Impact Analysis 
  Uses a fine-tuned Cohere model to classify whether news positively or negatively impacts progress toward sustainability goals.

- Clean, Accessible Interface
  Displays categorized articles in a simple Vue-based frontend for easy comprehension.

## Tech Stack
### Backend
- Flask (Python) – API layer for fetching, processing, and serving data  
- RSS Feeds – Source of real-time news articles  
- Cohere API – Fine-tuned sentiment analysis model

### Frontend
- Vue.js – Interactive and user-friendly interface

## How It Works
1. EcoDash fetches news articles from various RSS feeds.
2. Articles are sent to a Flask backend for processing.
3. The backend calls the Cohere API, where a fine-tuned AI model evaluates each article’s impact on sustainability progress.
4. Results are returned to the Vue frontend and displayed in a clear, categorized format for users.
