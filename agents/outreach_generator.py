# 📁 early_user_outreach_app/agents/outreach_generator.py
from mistral import generate_with_context
from rag.retriever import retrieve_examples

def generate_outreach_templates(name, description, persona, platforms):
    context = f"Startup: {name}\nWhat we do: {description}\nTarget user: {persona}"
    examples = retrieve_examples(persona)
    outreach = {}
    for platform in platforms:
        prompt = f"""
Use the following startup context and examples to write a personalized outreach message for {platform}:

{context}

Examples:
{examples}
"""
        output = generate_with_context(prompt)
        outreach[platform] = output
    return outreach
