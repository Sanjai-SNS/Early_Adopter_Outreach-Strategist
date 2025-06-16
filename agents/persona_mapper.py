# 📁 early_user_outreach_app/agents/persona_mapper.py
def find_communities(persona):
    persona = persona.lower()
    suggestions = []
    if "developer" in persona:
        suggestions += ["r/webdev", "r/learnprogramming", "IndieHackers dev groups"]
    if "startup" in persona:
        suggestions += ["r/startups", "Product Hunt", "YC Bookface"]
    if "designer" in persona:
        suggestions += ["r/userexperience", "Designer Hangout Slack"]
    return list(set(suggestions))
