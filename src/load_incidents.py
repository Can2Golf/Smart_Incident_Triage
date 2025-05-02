import json
from ml_classifier import classify_with_ml
from triage_engine import assign_priority
from routing_engine import assign_team
from export_results import export_to_csv

def load_incidents(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def display_incidents(incidents, output_filename="triaged_incidents.csv"):
    enriched = []

    for i, incident in enumerate(incidents, start=1):
        category = classify_with_ml(incident)
        priority = assign_priority(category)
        team = assign_team(category, priority)

        print(f"\n--- Incident {i} ---")
        print(f"ID: {incident['id']}" if "id" in incident else f"Subject: {incident['subject']}")
        print(f"Subject: {incident['subject']}")
        print(f"Category: {category}")
        print(f"Priority: {priority}")
        print(f"Team: {team}")

        incident["category"] = category
        incident["priority"] = priority
        incident["team"] = team
        enriched.append(incident)

    export_to_csv(enriched, filename=output_filename)
