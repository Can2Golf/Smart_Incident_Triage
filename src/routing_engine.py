def assign_team(category, priority):
    if category == "Phishing" and priority == "High":
        return "Email Security Team"
    elif category == "Spam" or priority == "Medium":
        return "General Triage Team"
    elif priority == "Low":
        return "Auto-Archive"
    else:
        return "Unknown"
