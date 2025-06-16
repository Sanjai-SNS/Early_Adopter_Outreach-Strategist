# 🚀 Project Summary: Early Adopter Outreach Strategist

## 🤩 Problem Statement

Early-stage startups often struggle to find and engage the *right early adopters*. Without specialized outreach strategies, most teams end up:

- Sending generic messages that fail to resonate
- Reaching out on the wrong platforms or at suboptimal times
- Missing crucial feedback that could improve their MVP

## 💡 Solution Overview

We built a **Streamlit-based AI assistant** that:

- Maps user personas to online communities
- Generates personalized outreach messages via **Mistral 7B**
- Suggests optimal timing for outreach
- Recommends strategies to collect feedback

This app helps startups go from *"idea"* to *"first 100 engaged users"* with minimal effort and maximum personalization.

---

## 🧰 Tech Stack Overview

| Component | Tool/Service                  |
| --------- | ----------------------------- |
| UI        | Streamlit                     |
| Backend   | Python                        |
| LLM       | Mistral 7B (via Ollama)       |
| Retrieval | Rule-based, expandable to RAG |

---

## 📃 Code Structure and Functionality

### 1. `app.py` – Main Application (Streamlit)

Handles user input form, triggers agents, and displays outputs:

- Startup name, description, persona, platforms
- Calls 4 agents:
  - `find_communities()` – community suggestions
  - `generate_outreach_templates()` – calls LLM
  - `suggest_outreach_timing()` – timing suggestions
  - `generate_feedback_methods()` – feedback loop ideas

### 2. `mistral.py` – LLM API Connector

Uses local Ollama Mistral server:

```python
url = "http://localhost:11434/api/generate"
```

Streams and decodes response from Mistral:

```python
response = requests.post(url, json={"model": "mistral", "prompt": prompt})
```

### 3. `agents/outreach_generator.py`

Builds few-shot prompts using example messages retrieved by `retrieve_examples()`. Calls `generate_with_context()` from `mistral.py`.

### 4. `rag/retriever.py`

Basic keyword-matching function returning example outreach templates per persona (developer, designer, startup).

### 5. `agents/persona_mapper.py`

Maps target persona to relevant communities like:

- `r/startups`, `Product Hunt`, `IndieHackers`

### 6. `agents/timing_suggester.py`

Suggests ideal posting times:

- Reddit: 8–10am PST
- Twitter: 11am–1pm or 5–6pm
- Email: Tue–Thu at 9am or 2pm

### 7. `agents/feedback_looper.py`

Returns human-centered methods to collect feedback:

- Typeform link
- Calendly 1:1 invite
- Open-ended questions

---

## 🎯 Sample Scenario

**Input:**

- Startup: SnapBuild
- Description: No-code landing page builder for founders
- Persona: Indie hackers with no technical background
- Platforms: Reddit, Twitter DM, IndieHackers

**Output:**

- Communities: `r/startups`, `r/webdev`, IndieHackers
- Twitter Message: *"Hey [name], we just launched SnapBuild for non-coders..."*
- Best time: Twitter – 11am to 1pm
- Feedback: *"Would you test our MVP? Here’s a 3-question Typeform."*

---

## 📊 Future Enhancements

| Feature                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| RAG-enabled retriever  | Swap keyword logic with vector search (e.g., FAISS)          |
| Multi-language support | Expand outreach across global communities                    |
| Feedback ingestion     | Train model on collected feedback for self-improving prompts |

---

## 🗣️ Final Pitch

This app acts as a *growth co-pilot* for early-stage founders. It saves hours of marketing effort, gives them expert-crafted messages, and optimizes timing — all powered by an open-source local LLM (Mistral 7B).

