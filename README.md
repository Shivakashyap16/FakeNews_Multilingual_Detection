# Multilingual Fake News Detection 📰🤖

Welcome to the **Multilingual Fake News Detection** project!  
This is an AI-powered web application designed to detect whether a given news article is **FAKE** or **REAL** using **Text Mining and Machine Learning** techniques. The system supports **English, Hindi, and Telugu** languages and provides results through a **modern and interactive web interface** built using Flask, HTML, and CSS.

The project uses **TF-IDF feature extraction** and **Naïve Bayes classification**, making it a practical and beginner-friendly implementation suitable for academic mini-projects in **Data Warehousing and Data Mining (DWDM)**.

---

# 🛠️ Setup Instructions

Follow these steps to run the project on your local machine.


## Prerequisites

- Python **3.8 or above** installed on your system  
- Basic knowledge of Python and command-line usage  
- A modern web browser (Chrome / Edge / Firefox)


## Steps

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FakeNews_Multilingual_Detection.git
````

### 2️⃣ Navigate to the Project Directory

```bash
cd FakeNews_Multilingual_Detection
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Machine Learning Model

```bash
python -m src.train_model
```

> This step generates the trained model and TF-IDF vectorizer files inside the `models/` folder.

### 5️⃣ Start the Flask Web Application

```bash
python app.py
```

### 6️⃣ Open the Application in Browser

```
http://127.0.0.1:5000
```

---

# 🖼️ Web Interface

The application provides a clean and modern user interface where users can:

* Enter news text in **English, Hindi, or Telugu**
* Analyze the content using the **Analyze News** button
* View detected language and classification result
* Clear the text using the **Clear Text** button for new analysis

📸 *(Add screenshots of the web interface here for better presentation)*

---

# ✨ Features

* 🌐 Multilingual support (English, Hindi, Telugu)
* 🧠 Machine Learning–based fake news detection
* 📊 TF-IDF feature extraction
* ⚡ Fast prediction using Naïve Bayes classifier
* 🎨 Modern UI with animations and clarity-focused design
* 🔁 Text persistence and clear input functionality

---

# 🔧 Customization

You can easily customize the project:

* Modify **`src/train_model.py`** to experiment with different ML algorithms
* Update **`templates/index.html`** to enhance UI layout
* Edit **`static/style.css`** to change colors, animations, or typography
* Expand the dataset in **`cleaned_data.csv`** to improve model accuracy

---

# 🎓 Academic Use

This project is ideal for:

* DWDM mini-projects
* Machine Learning demonstrations
* NLP and Text Mining assignments
* Web-based AI application showcases

---

# 📌 Conclusion

The **Multilingual Fake News Detection** system demonstrates how text mining and machine learning techniques can be effectively combined with a web interface to solve real-world problems. The project emphasizes usability, clarity, and academic relevance while maintaining a professional and modern appearance.








