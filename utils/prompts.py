# 📁 early_user_outreach_app/utils/prompts.py

OUTREACH_PROMPT_TEMPLATE = """
You are an expert startup growth hacker helping founders reach their first 100 users.
Given the following startup info and outreach examples, write a {channel}-friendly personalized outreach message.

Startup:
Name: {name}
Description: {description}
Target Persona: {persona}

Example Outreach Templates:
{examples}

Now generate a new outreach message below.
"""
