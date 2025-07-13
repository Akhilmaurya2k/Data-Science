# Enhanciing Search Engine Relavance Using Movie Subtitles

### Introduction

- Users often hear short dialogue clips but cannot identify the corresponding movie or TV show.  
- Existing tools lack the ability to accurately recognize content from brief audio snippets.

### Objective

- Develop an application to:  
  • Record short audio clips  
  • Accurately transcribe speech  
  • Match transcriptions against a large subtitle database  
- Provide precise movie/show titles, release years, and season/episode details when applicable.

### Methodology

- Built a Streamlit web app with in-browser audio recording.  
- Used OpenAI’s Whisper model for speech-to-text transcription.  
- Implemented a Retrieval Augmented Generation (RAG) system:  
  • LangChain for orchestration  
  • Sentence Transformers for text embeddings  
  • ChromaDB for vector similarity search  
- Leveraged GPT models to generate clear, accurate identification results.

### Result

- Delivered a scalable, user-friendly application enabling accurate identification from short audio clips.  
- Returns detailed metadata including titles, release years, and episode information.  
- Improved user experience and search relevance significantly.


## UML Diagram
* https://docs.google.com/presentation/d/1ztyXWKS6mlmJO6Z5T9N--0dEEGsyZBEgRrSkxKsPDQY/edit?usp=sharing
