from flask import Flask, render_template, request
from model import analyze_uploaded_resumes, extract_text_from_pdf
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', error=None)


@app.route('/analyze', methods=['POST'])
def analyze():

    job_descs = []
    
    # Check text input
    job_desc_text = request.form.get('job_desc', '').strip()
    if job_desc_text:
        job_title = request.form.get('job_title', '').strip()
        if not job_title:
            job_title = "Pasted Job Description"
        job_descs.append({"title": job_title, "text": job_desc_text})

    # Check file inputs
    job_desc_files = request.files.getlist('job_desc_file')
    custom_file_title = request.form.get('job_title_file', '').strip()
    
    for jd_file in job_desc_files:
        if jd_file and jd_file.filename:
            if jd_file.filename.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(jd_file)
                if extracted_text.strip():
                    if len(job_desc_files) == 1 and custom_file_title:
                        clean_title = custom_file_title
                    else:
                        clean_title = jd_file.filename[:-4].replace('_', ' ').replace('-', ' ').title()
                    job_descs.append({"title": clean_title, "text": extracted_text})
                else:
                    return render_template('index.html', error=f"Could not extract text from {jd_file.filename}.")
            else:
                return render_template('index.html', error=f"Job Description file {jd_file.filename} must be a PDF.")
            
    if not job_descs:
        return render_template('index.html', error="Please provide at least one Job Description (paste text or upload PDF).")

    uploaded_files = request.files.getlist('resumes')

    if not uploaded_files or uploaded_files[0].filename == '':
        return render_template('index.html', error="Please upload at least one PDF resume.")

    valid_files = []
    for file in uploaded_files:
        if file.filename.lower().endswith('.pdf'):
            valid_files.append(file)
        else:
            return render_template('index.html', error=f"Invalid file type: {file.filename}. Only PDFs are allowed.")

    if not valid_files:
        return render_template('index.html', error="No valid PDF files found.")

    try:
        results = analyze_uploaded_resumes(job_descs, valid_files)
        return render_template('results.html', results=results)
    except Exception as e:
        print(f"Error during analysis: {e}")
        return render_template('index.html', error="An error occurred while analyzing the resumes. Please try again or check your files.")


if __name__ == "__main__":
    app.run(debug=False)