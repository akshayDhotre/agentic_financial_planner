
# AgenticFinancialPlanner Crew

Welcome to the AgenticFinancialPlanner Crew project, powered by [crewAI](https://www.crewai.com/open-source). This project helps you set up a multi-agent AI system for personalized financial planning. Agents collaborate to generate actionable financial advice and reports based on user data and configuration.

Huge shoutout to [Ed Donner](https://www.linkedin.com/in/eddonner/) for his amazing course on [AI Agents](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/).

## Installation

Ensure you have Python >=3.10,<3.14 installed. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

Install uv:

```bash
pip install uv
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

Or use crewAI's CLI:

```bash
crewai install
```

## Configuration & Customization

1. **API Keys**: Add your `OPENAI_API_KEY` and other keys to the `.env` file.
2. **Agents**: Edit `src/agentic_financial_planner/config/agents.yaml` to define agent roles and goals.
3. **Tasks**: Edit `src/agentic_financial_planner/config/tasks.yaml` to define tasks and outputs.
4. **Logic**: Customize `src/agentic_financial_planner/crew.py` for agent/task orchestration and tool integration.
5. **Inputs**: Adjust `src/agentic_financial_planner/main.py` for user data and execution logic.

## Running the Project

To generate a financial plan and advice reports, run:

```bash
python src/agentic_financial_planner/main.py
```

This will create markdown reports in the `output/` directory:

- `summarized_user_data.md`
- `emergency_fund_advice.md`
- `investment_advice.md`
- `insurance_advice.md`
- `financial_plan_report.md`

## Project Structure

- `src/agentic_financial_planner/config/agents.yaml`: Agent definitions
- `src/agentic_financial_planner/config/tasks.yaml`: Task definitions
- `src/agentic_financial_planner/crew.py`: Crew and orchestration logic
- `src/agentic_financial_planner/main.py`: Entry point and user input
- `src/agentic_financial_planner/tools/custom_tool.py`: Example custom tool
- `output/`: Generated reports

## Custom Tools

You can add custom tools for agents in `src/agentic_financial_planner/tools/custom_tool.py`.

## Support

- [crewAI documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with I!
