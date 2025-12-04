import os
import re
from typing import Dict, List
import PyPDF2


# ----------- 1. Extract text from PDF -----------
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract and return the full text from a PDF file."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text_chunks = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(text_chunks)


# ----------- 2. Define skill categories -----------
SKILL_KEYWORDS = {
    "Programming Languages": [
        "python", "java", "c++", "c#", "javascript", "typescript"
    ],
    "ML / DL Frameworks": [
        "tensorflow", "pytorch", "keras", "sklearn", "scikit-learn"
    ],
    "Data Engineering / Databases": [
        "sql", "mysql", "postgresql", "snowflake", "mongodb"
    ],
    "Cloud Platforms": [
        "aws", "azure", "gcp", "google cloud", "amazon web services"
    ],
    "Tools / DevOps": [
        "docker", "kubernetes", "git", "jenkins", "linux"
    ],
}


# ----------- 3. Extract skills from text -----------
def extract_skills(text: str) -> Dict[str, List[str]]:
    """Find and categorize skills from resume text."""
    text_lower = text.lower()
    found_skills = {category: [] for category in SKILL_KEYWORDS}

    for category, keywords in SKILL_KEYWORDS.items():
        for skill in keywords:
            if skill in text_lower:
                found_skills[category].append(skill.capitalize())

    return found_skills


# ----------- 4. Save extracted skills -----------
def save_output(filename: str, skills: Dict[str, List[str]], pdf_name: str) -> None:
    """Save extracted skills into a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Resume file: {pdf_name}\n\n")

        for category, items in skills.items():
            f.write(f"{category}:\n")
            if items:
                for skill in items:
                    f.write(f" - {skill}\n")
            else:
                f.write(" - None found\n")
            f.write("\n")


# ----------- 5. Main program loop -----------
if __name__ == "__main__":
    print("\n🔍 Resume Skill Extractor")
    pdf_name = input("Enter resume PDF file name (example: sample_resume.pdf): ").strip()

    try:
        resume_text = extract_text_from_pdf(pdf_name)
        print("\n📄 PDF loaded successfully! Extracting skills...\n")

        skills_found = extract_skills(resume_text)

        output_file = "extracted_skills.txt"
        save_output(output_file, skills_found, pdf_name)

        print(f"✅ Done! Skills saved in: {output_file}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
