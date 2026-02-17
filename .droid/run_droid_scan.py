import os
import json
import requests
from pathlib import Path

API_KEY = os.environ.get("DROID_API_KEY")
DROID_URL = "https://api.factory.ai/droid/scan"

repo_files = []

# collect .py and .scala files
for file in Path(".").rglob("*"):
    if file.suffix in [".py", ".scala"]:
        try:
            repo_files.append({
                "path": str(file),
                "content": file.read_text(encoding="utf-8", errors="ignore")
            })
        except:
            pass

payload = {
    "policy": Path(".droid/databricks_lakehouse_policy.md").read_text(),
    "files": repo_files
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(DROID_URL, headers=headers, json=payload)

if response.status_code != 200:
    print(response.text)
    raise SystemExit("Droid scan failed")

with open("report.json", "w") as f:
    json.dump(response.json(), f, indent=2)

print("Droid scan completed")
