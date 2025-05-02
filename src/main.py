import argparse
from load_incidents import load_incidents, display_incidents

def main():
    parser = argparse.ArgumentParser(description="Smart Incident Triage CLI")
    parser.add_argument(
        "--input", "-i",
        type=str,
        default="../data/sample_incidents.json",
        help="Path to input incident JSON file"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="triaged_incidents.csv",
        help="Filename for the output CSV"
    )

    args = parser.parse_args()
    incidents = load_incidents(args.input)
    display_incidents(incidents, output_filename=args.output)

if __name__ == "__main__":
    main()
