# Email Classifier with PII Masking

This project classifies support emails into predefined categories (like Billing, Request, Technical) while masking personal information (PII) such as names, emails, phone numbers, Aadhar, card info, etc.

## 🚀 Features
- Regex-based PII masking (no LLMs used)
- TF-IDF + Naive Bayes classifier
- FastAPI & Gradio interfaces
- Deployed on Hugging Face Spaces

## 🔧 Setup Instructions

1. **Clone the repository and install dependencies**  
   ```bash
   git clone https://github.com/Satyam0775/email-classification-project.git
   cd email-classification-project
   pip install -r requirements.txt
Run the Gradio interface locally

bash
Copy
Edit
python gradio_app.py
Open your browser at http://127.0.0.1:7860.

(Optional) Run the FastAPI server

bash
Copy
Edit
uvicorn api:app --reload
The /predict/ endpoint will be available at http://127.0.0.1:8000/predict/.

🧪 Example Input
Paste an email to test the system:

text
Copy
Edit
Hi, my name is Rahul Sharma. My email is rahul@example.com. My Aadhar number is 123456789012, my phone number is 9876543210, DOB is 1995-06-25. My card number is 4111-1111-1111-1111, CVV 123, expiry 07/27.
Expected Output
Masked Email:

text
Copy
Edit
Hi, my name is [full_name]. My email is [email]. My Aadhar number is [aadhar_num], my phone number is [phone_number], DOB is [dob]. My card number is [credit_debit_no], CVV [cvv_no], expiry [expiry_no].
Extracted Entities:

yaml
Copy
Edit
full_name: Rahul Sharma
email: rahul@example.com
aadhar_num: 123456789012
phone_number: 9876543210
dob: 1995-06-25
credit_debit_no: 4111-1111-1111-1111
cvv_no: 123
expiry_no: 07/27
Predicted Category:

text
Copy
Edit
Request
🌐 Deployment Links
Hugging Face: [https://huggingface.co/spaces/Satyam0077/email-classifier-satyma](https://huggingface.co/spaces/Satyam0077/email-classifier-satyma)

📝 File Structure
email-classification-project/
├── gradio_app.py          # Launches the Gradio UI
├── api.py                 # FastAPI server with /predict/ endpoint
├── models.py              # load_model() utility
├── utils.py               # mask_pii() utility
├── requirements.txt       # Project dependencies
├── README.md              # This file
├── saved_models/
│   └── classifier_model.pkl
├── notebooks/
│   └── training_pipeline.ipynb
