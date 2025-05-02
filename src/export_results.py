import csv

def export_to_csv(incidents, filename="triaged_incidents.csv"):
    headers = ["ID", "Subject", "Category", "Priority", "Team"]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for incident in incidents:
            writer.writerow({
                "ID": incident["id"],
                "Subject": incident["subject"],
                "Category": incident["category"],
                "Priority": incident["priority"],
                "Team": incident["team"]
            })

    print(f"Exported {len(incidents)} incidents to {filename}")
