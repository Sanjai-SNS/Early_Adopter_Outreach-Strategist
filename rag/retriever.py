# 📁 early_user_outreach_app/rag/retriever.py
import random

def retrieve_examples(persona):
    persona = persona.lower()
    samples = {
        "developer": [
            "Hey [name], I saw you're working on X. We're building a tool for devs like you to save time with [feature]. Mind trying it out?",
            "We’re launching a beta for [tool], a productivity booster for coders. Thought you might want early access."
        ],
        "designer": [
            "Hey, we’re creating a new way to prototype without Figma. Interested in being our first user?",
            "We’re testing a design system generator for busy UX teams — want to try?"
        ],
        "startup": [
            "We’re YC-backed and looking for alpha users for our startup discovery tool. Want in?",
            "Would love feedback from other founders on our MVP — up for a 5-min chat?"
        ]
    }
    for key in samples:
        if key in persona:
            return "\n".join(random.sample(samples[key], 2))
    return "\n".join(random.sample(samples["startup"], 2))
