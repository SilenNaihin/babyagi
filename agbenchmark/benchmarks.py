import os
import sys
import subprocess


def run_specific_agent(task: str) -> None:
    os.environ["LLM_MODEL"] = "gpt-4"

    os.environ["LLAMA_MODEL_PATH"] = ""

    os.environ["OPENAI_TEMPERATURE"] = "0.0"

    os.environ["RESULTS_STORE_NAME"] = "baby-agi-test-table"

    os.environ["INSTANCE_NAME"] = "BabyAGI"
    os.environ["COOPERATIVE_MODE"] = "none"

    # RUN CONFIG
    os.environ["OBJECTIVE"] = task
    os.environ["INITIAL_TASK"] = "Develop a task list"

    # Extensions
    os.environ["DOTENV_EXTENSIONS"] = ""
    os.environ["ENABLE_COMMAND_LINE_ARGS"] = "false"
    subprocess.run(
        ["python", "babyagi.py"], text=True
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <task>")
        sys.exit(1)
    # setup_virtual_environment()
    task = sys.argv[1]
    run_specific_agent(task)
