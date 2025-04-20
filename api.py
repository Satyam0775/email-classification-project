# api.py

from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii
from models import load_model

app = FastAPI()
model = load_model()


class EmailRequest(BaseModel):
    email_body: str


@app.post("/predict/")
def classify_email(request: EmailRequest):
    """
    Accepts an email body, masks PII, predicts category,
    and returns required JSON structure.
    """
    masked_email, entity_list = mask_pii(request.email_body)
    category = model.predict([masked_email])[0]

    return {
        "input_email_body": request.email_body,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
