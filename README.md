# ai-tool-agent

Created by: Shriyans Ayalasomayajula

This is a lightweight AI agent built in Python that will take a user input and automatically route the user to the correct tool- such as using a calculator tool if asked to calculate an expression, using a weather tool if asked for the weather in a region, using a file reader tool if asked to read a file, and redirecting users to an Opsera search link with their given prompt (if they ask for information regarding Opsera.)

Features:
- Local LLM-powered natural language understanding using LLaMA3
- Dummy calculator tool
- Dummy weather tool
- Dummy file reader tool
- Opsera docs search using live URL queries
- Modular design which allows for easily adding new tools

How to run:
1. Clone the repo
    '''bash
    git clone https://github.com/shriyans-a/ai-tool-agent.git
    cd ai-tool-agent

2. Create and activate a virtual environment (in terminal)
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies (in terminal)
    pip install -r requirements.txt

4. Run the agent (in terminal)
    python main.py
