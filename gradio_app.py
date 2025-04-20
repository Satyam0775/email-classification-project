import gradio as gr
from utils import mask_pii
from models import load_model


# Load your trained classifier
model_path = (
    r'C:\Users\satya\EmailClassifierProject\email-classification'
    r'\saved_models\classifier_model.pkl'
)
model = load_model(model_path)


def classify_email(email_text):
    # 1) Mask PII
    masked_email, entity_list = mask_pii(email_text)

    # 2) Sanitize any stray parentheses in the mask placeholders
    masked_email = masked_email.replace("(", "[").replace(")", "]")

    # 3) Predict category
    category = model.predict([masked_email])[0]

    # 4) Format entities for display, ensuring every label is shown
    formatted_entities = "\n".join(
        f"{e['classification']}: {e['entity']}" for e in entity_list
    )

    return masked_email, formatted_entities, category


# Build Gradio interface
iface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(
        label="Paste Email Here",
        lines=8,
        placeholder="Enter support email..."
    ),
    outputs=[
        gr.Textbox(label="Masked Email"),
        gr.Textbox(label="Extracted Entities"),
        gr.Textbox(label="Predicted Category"),
    ],
    title="Email Classification with PII Masking",
    description=(
        "Mask all PII (name, email, phone, dob, Aadhar, card#, CVV, expiry) "
        "without LLMs, then classify into support categories."
    )
)

if __name__ == "__main__":
    iface.launch()
