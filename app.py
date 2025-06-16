# 📁 early_user_outreach_app/app.py

import streamlit as st
from agents.persona_mapper import find_communities
from agents.outreach_generator import generate_outreach_templates
from agents.timing_suggester import suggest_outreach_timing
from agents.feedback_looper import generate_feedback_methods

st.set_page_config(page_title="Early User Outreach Strategist", layout="centered")
st.title("🚀 Early Adopter Outreach Strategist")

# --- User Inputs ---
with st.form("startup_form"):
    startup_name = st.text_input("Startup Name")
    description = st.text_area("What does your startup do?")
    persona = st.text_input("Target Persona", value="Non-technical founders")
    platforms = st.multiselect("Target Platforms", ["Reddit", "Twitter", "IndieHackers"])
    submitted = st.form_submit_button("Generate Strategy")

if submitted:
    with st.spinner("🎯 Mapping persona to communities..."):
        communities = find_communities(persona)

    with st.spinner("🧠 Generating outreach messages with Mistral 7B..."):
        outreach = generate_outreach_templates(startup_name, description, persona, platforms)

    with st.spinner("⏱ Calculating best outreach timing..."):
        timing = suggest_outreach_timing(persona, platforms)

    with st.spinner("📣 Recommending feedback strategies..."):
        feedback = generate_feedback_methods(persona)

    # --- Output Section ---
    st.subheader("🌐 Suggested Communities")
    st.write(communities)

    st.subheader("✉️ Personalized Outreach Templates")
    for channel, msg in outreach.items():
        st.markdown(f"**{channel}:**")
        st.code(msg, language="markdown")

    st.subheader("📅 Outreach Timing Tips")
    st.json(timing)

    st.subheader("🧪 Feedback Collection Methods")
    st.write(feedback)
