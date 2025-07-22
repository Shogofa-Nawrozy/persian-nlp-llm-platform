# TalkP – Persian Language Learning Platform (In Progress)

**TalkP** is a modular web-based educational platform designed to support learning the Persian language using modern **Natural Language Processing (NLP)** and **Large Language Models (LLMs)**.

> **Project Status:** In Progress  
> This project is currently under active development. Key features have been implemented and tested, and new modules are being continuously integrated.

---

## Project Goals

- Enable interactive learning of Persian for English-speaking users.
- Combine traditional language learning with AI-powered features.
- Support both Farsi and Dari dialects with a focus on modular NLP integration.

---

## Implemented Features

- **Part-of-Speech (POS) Tagging**  
  Visualizes both dependency trees and linear token-tag outputs using `Stanza` and `ParsBERT`.

- **Vocabulary Trainer**  
  Displays translation, transliteration, grammatical usage, and example sentences.

- **Translation Module**  
  Utilizes transformer-based models (e.g., `alirezamsh/small100`) to provide Persian-English translations.

- **Summarization**  
  Generates concise summaries of long Persian texts using LLMs hosted on Google Colab.

- **Modular Backend API**  
  Built with Flask and integrated with MongoDB for user data storage.

- **Dockerized Setup**  
  The full system can be containerized using Docker Compose for easy deployment.

---

## In Progress / Upcoming Features

- **Grammar Correction Module** using LLMs
- **Real-time Transliteration** using contextual models
- **Audio Pronunciation** (Text-to-Speech for Persian)
- **Reading Content with Rich Vocabulary Highlights**
- **Beginner Mode** with basic guided Persian texts
- **User Quiz & Feedback Mode**
- **Teacher Dashboard (future iteration)**

---

## Tech Stack

- **Frontend**: HTML, Bootstrap, JS
- **Backend**: Python, Flask
- **NLP Models**: ParsBERT, mT5, small100, Stanza, custom LLM APIs
- **Deployment**: Docker, Google Colab (model hosting)
- **Database**: MongoDB

---

## Project Structure (Simplified)

