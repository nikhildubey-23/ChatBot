

---

# ChatBot

## Overview  
This project provides a chatbot implementation with two modes:  
- **GUI Mode** (via a web browser using Streamlit).  
- **CLI Mode** (for terminal-based interaction).  

Follow the steps below to set up and run the ChatBot.

---

## System Requirements  
To ensure optimal performance, your system should meet the following minimum requirements:  
- **RAM**: 16 GB  
- **Processor**: 4-core CPU  

---

## Installation  

### 1. Install Dependencies  
Run the following command to install all required dependencies:  
```bash
pip install -r requirements.txt
```

### 2. Install Ollama  
Visit the [Ollama website](https://ollama.com) to download and install Ollama for your operating system.  

- **Windows**: [Download for Windows](https://ollama.com/download/windows)  
- **macOS**: [Download for macOS](https://ollama.com/download/mac)  
- **Linux**: Use the following command in your terminal:  
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

### 3. Start Ollama Server  
Once Ollama is installed, start the server using this command:  
```bash
ollama start
```

### 4. Pull Llama Model  
Open a new terminal and pull the Llama model (version 3.1) by running:  
```bash
ollama pull llama3.1
```

---

## Usage  

### GUI Mode  
To run the chatbot with a graphical interface in your browser:  
1. Open `webBot.py`. Modify it as needed for customization.  
2. Run the following command:  
   ```bash
   streamlit run webBot.py
   ```

### CLI Mode  
To run the chatbot in the terminal:  
1. Use the following command:  
   ```bash
   python3 CliBot.py
   ```

---

## Notes  
- Feel free to customize the `webBot.py` file to meet your specific needs.  
- Ensure that the Ollama server is running before executing any chatbot commands.

---

## Troubleshooting  
If you encounter any issues:  
1. Verify that all dependencies are installed.  
2. Ensure that the correct Llama model version is pulled.  
3. Check that the Ollama server is running properly.  

---

Enjoy using the ChatBot! 😊

---
