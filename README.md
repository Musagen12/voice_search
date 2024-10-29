# 🗣️ Voice-Controlled Chatbot

This project is a voice-controlled chatbot that enables users to search for items and receive real-time price updates. Designed for accessibility and convenience, the chatbot allows hands-free interaction through voice commands.

## ✨ Features

- **🎙️ Voice Recognition**: Accepts voice commands to initiate searches and queries.
- **🔍 Item Search**: Search for products by name or category.
- **📡 Real-time Data Updates**: Uses WebSockets to ensure up-to-date responses on item pricing and availability.

## 🛠️ Tech Stack

- **🚀 Backend**: FastAPI for handling API requests.
- **🗣️ Voice Recognition**: Azure Speech SDK for converting voice commands to text.
- **💻 Frontend**: Basic HTML, CSS, and JavaScript for a lightweight, responsive interface.
- **🤖 LLM Processing**: Mistral LLM hosted locally in Ollama for chatbot responses.

## 📄 Usage

1. Access the web interface by opening `index.html`.
2. Click on the microphone button 🎤 and speak your command, such as:
    - "Search for iPhone 13 prices"
3. The chatbot will respond with current price data and provide updates on selected items as needed.

## 📂 Project Structure

- `🎙️ speech_recognition_websocket.py`: Contains FastAPI server code, Azure Speech integration, and API endpoints.
- `🖥️ index.html`: Contains HTML, CSS, and JavaScript files for the user interface.
- `🔗 llm_response_websocket.py`: WebSocket server to handle real-time updates.
- `📜 README.md`: Project overview and setup guide (you're here!).

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.
