# 🔐 Random Password Generator

A sleek, modern web application that generates secure, random 10-character passwords. It features a FastAPI backend and a dark-themed, responsive HTML/CSS/JavaScript frontend.

---

## 📸 App Preview

![Application Screenshot](https://github.com/saqib783/password-generator-in-python/blob/50b556647596b5502c1cf31fbf3be02e3b9f3ea4/Screenshot%20(2127).png) 


---

## ⚡ Features

- **Instant Generation**: Highly secure 10-character passwords including letters, digits, and symbols.
- **FastAPI Backend**: Clean and efficient routing with CORS setup.
- **Dark Mode UI**: Minimalist, eye-friendly design centered perfectly on the screen.
- **Error Handling**: Notifies the user on-screen if the server is offline.

---

## 🚀 How to Run the Project

Follow these steps to set up and run the application locally.

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 2. Project Directory Setup
Ensure your project files are structured like this:
```text
your-project-folder/
│
├── main.py                 # Paste your FastAPI code here
├── screenshot.png          # Place your application screenshot here
└── frontend_template/
    ├── index.html          # Place your HTML inside here
    ├── style.css           # Place your CSS code here
    └── script.js           # Place your JS code here
```

### 3. Install Dependencies
Open your terminal inside the project directory and install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn
```

### 4. Start the Server
Run the following command to start the backend:
```bash
uvicorn main:app --reload
```

### 5. Open the Web App
Once the server starts, open your browser and navigate to:
```text
http://127.0.0.1:8000
```

---

## 🛠️ Built With

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
