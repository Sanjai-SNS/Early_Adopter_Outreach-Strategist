# 🔄 Updated Agentic AI Timing Suggestion with Mistral LLM

# File: agents/timing_suggester.py

import requests
from mistral import generate_with_context
def suggest_outreach_timing(persona, platforms):
    timing = {}
    for platform in platforms:
        if platform == "Reddit":
            timing[platform] = "Post between 8–10am PST"
        elif platform == "Twitter":
            timing[platform] = "Tweet between 11am–1pm or 5–6pm local time"
        elif platform == "IndieHackers":
            timing[platform] = "Weekdays 10am–4pm local time"
    return timing

def parse_timing_json(response):
    # Naively parse JSON-like output to dict (can improve with regex/json.loads)
    try:
        lines = response.strip().split('\n')
        timing_data = {}
        for line in lines:
            if ":" in line:
                key, val = line.split(":", 1)
                timing_data[key.strip().replace('"','')] = val.strip().replace('"','')
        return timing_data
    except Exception as e:
        return {"error": str(e)}
