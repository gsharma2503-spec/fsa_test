import json, sys

with open("report.json") as f:
    data = json.load(f)

if data["status"] == "FAIL":
    print("PR BLOCKED — Issues detected")
    for i in data.get("issues", []):
        if i["severity"] == "CRITICAL":
            print(f"{i['file']}:{i['line']} -> {i['message']}")
    sys.exit(1)

print("Droid review passed")
