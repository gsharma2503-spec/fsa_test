import json
import csv
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"droid_report_{timestamp}.csv"

with open("report.json") as f:
    data = json.load(f)

with open(output_file, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)

    writer.writerow(["File(Line)","Tool","Severity","Result","Suggested Fix","Code"])

    for i in data.get("issues", []):
        writer.writerow([
            f"{i['file']}:{i['line']}",
            i.get("tool","DROID"),
            i.get("severity","INFO"),
            i.get("result","FAILED"),
            i.get("suggested_fix",""),
            i.get("code","")
        ])

print(f"REPORT_FILE={output_file}")
