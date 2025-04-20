# utils.py

import re


def mask_pii(text):
    entity_list = []

    def record(match, entity_type):
        value = match.group()

        # Prevent false full_name matches like "My Aadhar"
        if entity_type == "full_name" and value.lower().split()[0] in [
            "my", "your", "the", "this"
        ]:
            return value

        start, end = match.start(), match.end()
        entity_list.append({
            "position": [start, end],
            "classification": entity_type,
            "entity": value
        })
        return f"[{entity_type}]"

    # 1. Full Name (two capitalized words)
    text = re.sub(
        r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",
        lambda m: record(m, "full_name"),
        text
    )

    # 2. Email Address
    text = re.sub(
        r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.\w+\b",
        lambda m: record(m, "email"),
        text
    )

    # 3. Phone Number (10 digits)
    text = re.sub(
        r"\b\d{10}\b",
        lambda m: record(m, "phone_number"),
        text
    )

    # 4. Date of Birth (multiple formats)
    text = re.sub(
        r"\b(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b",
        lambda m: record(m, "dob"),
        text
    )

    # 5. Aadhar Number (12 digits)
    text = re.sub(
        r"\b\d{12}\b",
        lambda m: record(m, "aadhar_num"),
        text
    )

    # 6. Credit/Debit Card Number (16 digits)
    text = re.sub(
        r"\b(?:\d{4}[- ]?){4}\b",
        lambda m: record(m, "credit_debit_no"),
        text
    )

    # 7. CVV (3 digits, not duplicated)
    text = re.sub(
        r"\b\d{3}\b",
        lambda m: record(m, "cvv_no") if m.group() not in [
            e['entity'] for e in entity_list
        ] else m.group(),
        text
    )

    # 8. Expiry Date (MM/YY)
    text = re.sub(
        r"\b(0[1-9]|1[0-2])/\d{2}\b",
        lambda m: record(m, "expiry_no"),
        text
    )

    return text, entity_list
