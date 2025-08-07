# ATS-Resume-Expert

An intelligent Applicant Tracking System (ATS) Resume Expert built with Streamlit and Google Gemini AI. Upload your resume (PDF) and job description to get professional evaluations,
match percentages, keyword analysis, and detailed feedback tailored for tech roles such as Data Science, Full Stack Development, DevOps, AI/ML Engineering, and more.

---

## Features

- Upload your resume in PDF format for automated parsing using PyMuPDF
- Provide a job description to evaluate candidate-job fit
- Get an HR-like professional review highlighting strengths and weaknesses
- Receive percentage match, missing keywords, and final thoughts using Google's generative AI
- Seamless and interactive UI powered by Streamlit

---

## Technologies & Libraries Used

- [Streamlit](https://streamlit.io/) — For creating the interactive web app
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) — For PDF parsing and rendering
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/) — To manage API keys securely with `.env` files
- [google-generativeai](https://developers.generativeai.google/) — Google Gemini AI for natural language generation and resume evaluation

---

## Setup Instructions
1. **Clone the repository**
  git clone https://github.com/Bhutani63/ATS-Resume-Expert.git
  cd ATS-Resume-Expert
2. **Create and activate your virtual environment**

    Windows CMD:
    python -m venv venv
    .\venv\Scripts\activate
   
    macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate


3. **Install dependencies**

    pip install -r requirements.txt


4. **Prepare your `.env` file**

  Create a `.env` file in the root of the project and add your Google API key:
    GOOGLE_API_KEY=your_google_api_key_here


5. **Run the Streamlit app**
  streamlit run app.py


---

## Usage

- Open the app in your browser.
- Enter the job description in the provided text area.
- Upload a candidate's resume in PDF format.
- Click the evaluation buttons to get professional HR insights or match percentages against the job description.

---

## Notes

- Make sure your Google API key has access to the generative AI services.
- The app currently supports tech roles (e.g., Data Science, AI/ML, Web Development).
- For any issues or feature requests, please open an issue on the repository.

---

## License

MIT License © 2025

---

## Contact

For questions or collaborations, feel free to reach out!


1. **Clone the repository**

