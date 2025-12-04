# 🧠 Resume Skill Extractor

A simple and efficient Python automation tool that extracts text from PDF resumes, detects relevant skills (AI, ML, Data, Programming, Cloud, DevOps etc.), and saves them into a clean output file.

Built as part of my **AI Engineer Automation Roadmap**, where I automate small tasks using Python.

---

## 🚀 Features

- ✔️ Extracts raw text from any PDF resume using **PyPDF2**
- ✔️ Identifies skills using pattern matching  
  (Python, ML, DL, SQL, Cloud, DevOps, NLP, etc.)
- ✔️ Saves results into **extracted_skills.txt**
- ✔️ Fully terminal-based — no GUI required
- ✔️ Lightweight, beginner-friendly Python script

---

## 📁 Project Structure

```
resume-skill-extractor/
│
├── resume_skills_extractor.py   # Main Python script
├── sample.pdf                   # Example resume file
└── extracted_skills.txt         # Output file generated after running script
```

---

## 🛠️ Technologies Used

- **Python 3**
- **PyPDF2** — PDF text extraction
- **Regex (re)** — Skill detection
- **OS module** — File handling

---

## ▶️ How to Run

Install required dependency:

```
pip install PyPDF2
```

Run the script from terminal:

```
python resume_skills_extractor.py
```

When prompted, enter:

```
sample.pdf
```

Output will be saved as:

```
extracted_skills.txt
```

---

## 🎯 Purpose

This tool is part of my ongoing journey to build practical automation tools using Python.  
It also serves as a base for future projects such as:

- Resume analyzers  
- Job matching automation  
- AI-based skill extraction systems  
- Agentic AI workflows  

---

## ✨ Author

**Musthaq Ahmed Gaffoor**  
AI/ML Engineer | Python Developer | Automation Enthusiast  
📧 musthaq258@gmail.com  
🔗 https://www.linkedin.com/in/musthaq-ahmed-gaffoor-a249229236/

---

If you like this project, feel free to ⭐ star the repository!
