# ChatBot_SEVC
A FDP Training @03/07/2025


# Project Setup Guide

This guide explains how to install dependencies, understand the folder structure, and run both the backend (FastAPI) and frontend (React) for your project.

---

## Folder Structure

```
ragcode/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── __init__.py
│   └── requirements.txt
│
└── frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js
        └── index.js
```

---

## Prerequisites

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **Node.js 16+** and **npm** installed ([Download Node.js](https://nodejs.org/))

---

## 1. Backend Setup (FastAPI)

1. **Open a terminal** and navigate to the backend folder:
    ```sh
    cd c:\ragcode\backend
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set your Groq API key**  
   Edit `c:\ragcode\backend\app\main.py` and replace the placeholder with your real key:
    ```python
    os.environ["GROQ_API_KEY"] = "your_real_groq_api_key"
    ```

5. **Run the FastAPI server:**
    ```sh
    uvicorn app.main:app --reload
    ```
   The backend will be available at [http://localhost:8000](http://localhost:8000).

---

## 2. Frontend Setup (React)

1. **Open a new terminal** and navigate to the frontend folder:
    ```sh
    cd c:\ragcode\frontend
    ```

2. **Install Node.js dependencies:**
    ```sh
    npm install
    ```

3. **Start the React development server:**
    ```sh
    npm start
    ```
   The frontend will be available at [http://localhost:3000](http://localhost:3000).

---

## 3. Usage

- Open [http://localhost:3000](http://localhost:3000) in your browser.
- Ask questions using the web interface.
- The frontend will send your question to the backend, which will process it and return an answer.

---

## 4. Troubleshooting

- If you see `'react-scripts' is not recognized`, run:
    ```sh
    npm install react-scripts
    ```
- If you get dependency errors, try deleting `node_modules` and `package-lock.json`, then run `npm install` again:
    ```sh
    rd /s /q node_modules
    del package-lock.json
    npm install
    ```
- Make sure both backend and frontend servers are running in their respective folders.

---

## 5. Useful Commands

- **Stop the server:** Press `Ctrl+C` in the terminal.
- **Reinstall all frontend dependencies:**
    ```sh
    rd /s /q node_modules
    del package-lock.json
    npm install
    ```

---

**Your project is now ready to use!**


for source code 
visit [GitHub Repository](https://github.com/your-repo)
    winget install --id Git.Git -e --source winget
