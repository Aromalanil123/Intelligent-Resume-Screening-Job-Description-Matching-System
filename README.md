# 🚀 Intelligent Resume Screening & Job Description Matching System

<p align="center">
  <img src="assets/banner.png" alt="Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge\&logo=flask)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-red?style=for-the-badge\&logo=streamlit)
![NLP](https://img.shields.io/badge/NLP-Resume_Analysis-green?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-TF--IDF-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

<p align="center">
An AI-powered recruitment assistant that automatically analyzes resumes, compares them with job descriptions, extracts relevant skills, and provides an intelligent compatibility score for recruiters.
</p>

---

# 📑 Table of Contents

* Overview
* Features
* System Workflow
* Tech Stack
* Project Structure
* Installation
* Usage
* Future Improvements
* Author

---

# 📌 Overview

Hiring teams often spend hours manually reviewing resumes.

This project automates the initial screening process using **Natural Language Processing (NLP)** and **Machine Learning**, allowing recruiters to quickly identify candidates whose skills and experience best match a given Job Description.

The system extracts text from resumes, preprocesses it, compares it against the provided JD, and generates an overall matching score along with skill-based insights.

---

# ✨ Features

* ✅ Resume Upload (PDF)
* ✅ Automatic Resume Parsing
* ✅ Job Description Analysis
* ✅ NLP Text Cleaning
* ✅ Skill Extraction
* ✅ TF-IDF Vectorization
* ✅ Cosine Similarity Matching
* ✅ Resume Ranking
* ✅ Match Percentage
* ✅ Interactive Dashboard
* ✅ Easy-to-use Interface

---

# ⚙️ System Workflow

```text
          Resume (PDF)
                │
                ▼
        Text Extraction
                │
                ▼
      NLP Preprocessing
                │
                ▼
      Skill Extraction
                │
                ▼
Job Description Processing
                │
                ▼
 TF-IDF Vectorization
                │
                ▼
 Cosine Similarity Score
                │
                ▼
 Resume Match Percentage
```

---

# 🧠 Tech Stack

| Category       | Technologies                   |
| -------------- | ------------------------------ |
| Language       | Python                         |
| Frontend       | Streamlit                      |
| Backend        | Flask                          |
| NLP            | NLTK, SpaCy                    |
| ML             | Scikit-learn                   |
| PDF Processing | PyPDF2                         |
| Database       | SQLite                         |
| ORM            | Flask-SQLAlchemy               |
| Embeddings     | Sentence Transformers (MiniLM) |
| Framework      | LangChain                      |

---

# 📂 Project Structure

```bash
Resume-Screening-System
│
├── app.py
├── requirements.txt
├── resume_parser.py
├── skill_extractor.py
├── similarity.py
├── models/
├── dataset/
├── templates/
├── static/
├── uploads/
├── assets/
│    ├── banner.png
│    └── workflow.png
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Aromalanil123/Intelligent-Resume-Screening-Job-Description-Matching-System.git

cd Intelligent-Resume-Screening-Job-Description-Matching-System
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

or

```bash
python app.py
```

---

# 🎯 Usage

### Step 1

Upload a Resume (PDF)

⬇️

### Step 2

Paste the Job Description

⬇️

### Step 3

Click **Analyze**

⬇️

### Step 4

View:

* Resume Match Score
* Matching Skills
* Missing Skills
* Similarity Percentage
* Candidate Ranking

---

# 📈 Future Improvements

* 🤖 LLM-powered semantic resume matching
* 📚 FAISS vector database integration
* 💬 AI-generated recruiter feedback
* 📂 Multi-resume comparison and ranking
* 📧 Email notifications for shortlisted candidates
* ☁️ Cloud deployment using Docker and Render
* 📊 Recruiter analytics dashboard
* 📈 Skill gap analysis and recommendations

---

# 🌟 Why This Project?

* ✔ Automates manual resume screening
* ✔ Reduces recruiter effort and screening time
* ✔ Improves hiring efficiency through AI-powered matching
* ✔ Provides objective candidate evaluation
* ✔ Demonstrates practical applications of NLP and Machine Learning

---

# 👨‍💻 Author

### **Aromal Anil**

**Aspiring Data Scientist | AI & Machine Learning Enthusiast**

📧 Email: [your-email@example.com](mailto:your-email@example.com)

🔗 GitHub: https://github.com/Aromalanil123

---

<p align="center">
⭐ If you found this project useful, consider giving it a <b>Star</b> on GitHub!
</p>
