# Early Adopter Outreach Strategist

## Project Summary
The Early Adopter Outreach Strategist is a tool designed to help startups find and engage early adopters through personalized outreach. It streamlines the process of connecting with potential users, ensuring startups can effectively reach their target audience.

## Problem Statement
Early-stage startups often face challenges in:
- Identifying and reaching early adopters.
- Crafting personalized outreach messages that resonate.
- Selecting the right platforms and timing for outreach.
- Collecting actionable feedback to improve their MVP.

## Solution Overview
This project offers a Streamlit-based AI assistant that:
- Maps user personas to relevant online communities (e.g., `r/startups`, Product Hunt, IndieHackers).
- Generates personalized outreach messages using the Mistral 7B model via Ollama.
- Suggests optimal outreach times (e.g., Reddit: 8–10 AM PST, X: 11 AM–1 PM or 5–6 PM, Email: Tuesday–Thursday at 9 AM or 2 PM).
- Recommends feedback collection strategies, such as Typeform links, Calendly 1:1 invites, or open-ended questions.

## Tech Stack Overview
- **UI**: Streamlit for an intuitive user interface.
- **Backend**: Python for robust processing.
- **LLM**: Mistral 7B, accessed via Ollama at `http://localhost:11434/api/generate`.
- **Retrieval**: Rule-based system, with plans to expand to Retrieval-Augmented Generation (RAG).

## Requirements
To run this project, ensure you have the following:
- **Hardware**:
  - Minimum 8GB RAM (16GB or more recommended for better performance).
  - At least 20GB free disk space for the Mistral 7B model and Docker images.
- **Software**:
  - [Docker](https://www.docker.com/) for running the Ollama server.
  - Python 3.x (3.8 or higher recommended).
  - pip for installing Python dependencies.
- **Python Dependencies**:
  - Streamlit (`pip install streamlit`).
  - requests (`pip install requests`).
- **Ollama**:
  - A local Ollama server with the Mistral 7B model installed and running at `http://localhost:11434/api/generate`.
- **Operating System**: Compatible with macOS, Linux, or Windows (with Docker support).

| Requirement | Details |
|-------------|---------|
| Hardware | 8GB RAM minimum (16GB recommended), 20GB free disk space |
| Software | Docker, Python 3.x, pip |
| Dependencies | Streamlit, requests |
| Ollama | Mistral 7B model, running locally |
| OS | macOS, Linux, or Windows |

## Installation
Follow these steps to set up and run the Early Adopter Outreach Strategist:
1. **Set up Ollama using Docker**:
   - Install [Docker](https://www.docker.com/) if not already installed on your system.
   - Pull the Ollama Docker image:
     ```bash
     docker pull ollama/ollama
     ```
   - Run the Ollama container to start the server:
     ```bash
     docker run -d -p 11434:11434 --name ollama ollama/ollama
     ```
   - Pull the Mistral 7B model inside the container:
     ```bash
     docker exec -it ollama ollama pull mistral:7b
     ```
   - Verify the Ollama server is running by checking `http://localhost:11434/api/generate` (you can test with a tool like `curl` or a browser).
2. **Clone the repository**:
   - Clone the project from GitHub:
     ```bash
     git clone https://github.com/Sanjai-SNS/Early_Adopter_Outreach-Strategist.git
     ```
3. **Navigate to the project directory**:
   - Change to the project folder:
     ```bash
     cd Early_Adopter_Outreach-Strategist
     ```
4. **Install Python dependencies**:
   - Install the required Python packages:
     ```bash
     pip install streamlit requests
     ```
5. **Run the Streamlit app**:
   - Launch the application:
     ```bash
     streamlit run app.py
     ```
   - Open your browser to `http://localhost:8501` to access the Streamlit interface.

**Note**: Ensure the Ollama server is running before starting the Streamlit app, as the application relies on the Mistral 7B model for generating outreach messages.

## Code Structure
The codebase is organized into several key files:
1. **`app.py`**: Main Streamlit application that handles user inputs (startup name, description, persona, platforms) and triggers four agents: `find_communities`, `generate_outreach_templates`, `suggest_outreach_timing`, and `generate_feedback_methods`.
2. **`mistral.py`**: Connects to the local Ollama Mistral server to stream and decode responses from Mistral 7B.
3. **`agents/outreach_generator.py`**: Builds few-shot prompts and calls `generate_with_context()` from `mistral.py` to create outreach messages.
4. **`rag/retriever.py`**: Implements keyword-matching to retrieve outreach templates for personas like developers, designers, or startups.
5. **`agents/persona_mapper.py`**: Maps target personas to communities such as `r/startups`, Product Hunt, or IndieHackers.
6. **`agents/timing_suggester.py`**: Suggests optimal outreach times based on platform (e.g., Reddit: 8–10 AM PST, X: 11 AM–1 PM or 5–6 PM).
7. **`agents/feedback_looper.py`**: Provides feedback collection methods, including Typeform links, Calendly invites, or open-ended questions.

## Sample Scenario
**Input**:
- **Startup**: SnapBuild (no-code landing page builder)
- **Persona**: Indie hackers
- **Platforms**: Reddit, X DM, IndieHackers

**Output**:
- **Communities**: `r/startups`, `r/webdev`, IndieHackers
- **X Message**: "Hey [name], we just launched SnapBuild for non-coders..."
- **Best Time**: X – 11 AM to 1 PM
- **Feedback**: "Would you test our MVP? Here’s a 3-question Typeform."

## Future Enhancements
- **RAG-Enabled Retriever**: Implement vector search (e.g., FAISS) for improved retrieval.
- **Multi-Language Support**: Expand to global communities with diverse languages.
- **Feedback Ingestion**: Use collected feedback to train the model for self-improving prompts.

## Final Pitch
The Early Adopter Outreach Strategist acts as a growth co-pilot for founders, saving marketing effort with expert-crafted messages and optimized timing. Powered by Mistral 7B, it helps startups connect with their first 100 engaged users efficiently.

## About
Finding initial users is a significant hurdle for startups, and generic cold outreach often fails. This tool leverages AI to deliver personalized, effective outreach strategies tailored to specific audiences.

## Releases
Explore releases at [Releases](https://github.com/Sanjai-SNS/Early_Adopter_Outreach-Strategist/releases).

## Packages
View packages at [Packages](https://github.com/users/Sanjai-SNS/packages?repo_name=Early_Adopter_Outreach-Strategist).

## Key Citations
- [Early Adopter Outreach Strategist GitHub Repository](https://github.com/Sanjai-SNS/Early_Adopter_Outreach-Strategist)
- [Ollama Official Website](https://ollama.com/)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Streamlit Official Documentation](https://docs.streamlit.io/)
- [Mistral 7B Model on Ollama](https://ollama.com/library/mistral)
- [Mistral 7B Instruct with Ollama Guide](https://quickcreator.io/quthor_blog/implementing-mistral-7b-instruct-ollama-beginners-guide/)
- [Deploy Mistral 7B with Ollama on Google Cloud](https://www.oneclickitsolution.com/centerofexcellence/aiml/how-to-deploy-mistral-7b-in-docker-with-ollama-on-google-cloud)
- [Run Mistral 7B Locally with Ollama](https://www.byteplus.com/en/topic/553307)
- [Self-Host Mistral AI Models with Ollama](https://blog.itgranules.com/self-host-free-mistral-ai-models-using-ollama)
- [Mistral 7B LLM Run Locally with Ollama](https://medium.com/@parmarshyamsinh/mistral-7b-llm-run-locally-with-ollama-bf10494be857)