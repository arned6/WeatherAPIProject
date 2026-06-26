import csv
from datetime import date, timedelta


class ReportingEngine:
    def __init__(self, d1, d2, compare, date, location):
        self.compare = compare
        self.d1 = d1
        self.d2 = d2
        self.date = date
        self.location = location
    def driftdetect(self):
        """Runs a configuration report to show difference between provider A and B and confirm drift if it exists."""
        print("=" * 50)
        print(f"Location: {self.location}")
        print(f"Date: {self.date}")
        print()

        # Header row
        print(f"{'Metric':<22}{'Source A':>10}{'Source B':>12}{'Diff':>10}")
        print("-" * 50)

        # Metrics config: (Label, key, decimals)
        metrics = [
            ("Avg Temp (F)", "avg_temp_f", 1),
            ("Max Temp (F)", "max_temp_f", 1),
            ("Wind Speed (Mph)", "wind_mph", 1),
            ("Precipitation", "precipitation_in", 2),
        ]

        # Rows
        for label, key, decimals in metrics:
            v1 = self.d1.get(key, 0)
            v2 = self.d2.get(key, 0)
            d = self.compare.get(key, 0)
            #Leave decimals in even if they're 0?
            if decimals > 0:
                print(f"{label:<22}{v1:>10.{decimals}f}{v2:>12.{decimals}f}{d:>10.{decimals}f}")
            else:
                print(f"{label:<22}{int(v1):>10}{int(v2):>12}{int(d):>10}")

        print()
        # Status logic (optional)
        #Change THRESHOLD value to accepted drift threshold as needed.
        THRESHOLD = 0
        status = "DRIFT DETECTED" if any(v != THRESHOLD for v in self.compare.values() if isinstance(v, (int, float))) else "OK"
        print(f"Status: {status}")
        print("=" * 50)

    def csvpost(self, filename="outputs/output.csv"):
        """Formats values to a 2 decimal float for readability and posts the content to ../outputs/output.csv"""
        fields = ["location", "avg_temp_f", "wind_mph", "precipitation_in"]
        with open(filename, mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            row = [
                date.today(),
                self.date,
                self.compare.get("location", ""),  # no float
                f"{self.compare.get('avg_temp_f', 0):.2f}",
                f"{self.compare.get('wind_mph', 0):.1f}",
                f"{self.compare.get('precipitation_in', 0):.2f}"
            ]
            writer.writerow(row)

