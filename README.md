# Email Classifier with PII Masking

This project classifies support emails into predefined categories (e.g., Billing, Request, Technical) while masking personal information (PII) like names, emails, phone numbers, Aadhar, and card details.

## 🚀 Features
- **Regex-based PII masking** (no LLMs used)
- **TF-IDF + Naive Bayes classifier** for email categorization
- **FastAPI & Gradio interfaces** for local deployment
- **Deployed on Hugging Face Spaces**

## 🔧 Setup Instructions

### 1. Clone the repository and install dependencies:
```bash
git clone https://github.com/Satyam0775/email-classification-project.git
cd email-classification-project
pip install -r requirements.txt

### 2. Run the Gradio Interface Locally:
```bash
python gradio_app.py
3. (Optional) Run the FastAPI Server:
bash
Copy
Edit
uvicorn api:app --reload
This will start a FastAPI server, and the /predict/ endpoint will be available at http://127.0.0.1:8000/predict/.
🧪 Example Input
Test the system by pasting an email to classify and mask PII:
"Hi, my name is Satyam Kumar. My email is Satyam@example.com. My Aadhar number is 123456789012, my phone number is 9876543210, DOB is 2002-06-07. My card is 4111-1111-1111-1111, CVV 123, expiry 07/27.
Expected Output
Masked Email:
Hi, my name is [full_name]. My email is [email]. My Aadhar number is [aadhar_num], my phone number is [phone_number], DOB is [dob]. My card number is [credit_debit_no], CVV [cvv_no], expiry [expiry_no].
Extracted Entities:
ffull_name: Satyam Kumar
email: Satyam@example.com
phone_number: 9876543210
dob: 2002-06-07
aadhar_num: 123456789012
credit_debit_no: 4111-1111-1111-1111
cvv_no: 123
expiry_no: 07/27
Predicted Category:
Request
🌐 Deployment Links
GitHub: https://github.com/Satyam0775/email-classification-project
Hugging Face: https://huggingface.co/spaces/Satyam0077/email-classifier-satyma

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
📦 API Usage with Postman
Once your FastAPI server is running, you can use Postman to send a POST request to the /predict/ endpoint to classify emails and mask PII.

1. Open Postman.
2. Set the request method to POST.
3. Enter the following URL:
http://127.0.0.1:8000/predict/
4. In the Body tab, choose raw and set the type to JSON.
5. Enter the input data in JSON format:
json
{
  "email_body": "Hi, my name is Satyam Kumar. My email is Satyam@example.com. My Aadhar number is 123456789012, my phone number is 9876543210, DOB is 2002-06-07. My card is 4111-1111-1111-1111, CVV 123, expiry 07/27."
}
6. Click Send.
The response will contain the masked email content and extracted entities, as shown in the expected output section.

