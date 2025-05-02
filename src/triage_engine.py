def classify_incident(incident):
    subject = incident["subject"].lower()
    sender = incident["sender"].lower()
    link_count = incident["link_count"]
    attachment = incident["attachment"]

    if "password" in subject or "login" in subject or link_count > 1 or "micros0ft" in sender:
        return "Phishing"
    elif "gift" in subject or "win" in subject:
        return "Spam"
    else:
        return "Benign"

def assign_priority(category):
    if category == "Phishing":
        return "High"
    elif category == "Spam":
        return "Medium"
    else:
        return "Low"
