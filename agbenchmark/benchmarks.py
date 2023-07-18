import shutil
import os
import sys
import subprocess

# Define the correct path based on the OS
venv_path = os.path.join("venv", "Scripts" if os.name == "nt" else "bin")


def setup_virtual_environment():
    # Create a virtual environment only if it doesn't already exist. It should already be created in the ci
    if not os.path.isdir("venv"):
        subprocess.run(["python", "-m", "venv", "venv"], check=True)

        # Activate the virtual environment and install the requirements
        subprocess.run(
            [os.path.join(venv_path, "pip"), "install", "-r", "requirements.txt"],
            check=True,
        )


def run_specific_agent(task: str) -> None:
    # Run the mini-agi command within the virtual environment
    cwd = os.path.join(os.getcwd(), "babycoder")

    subprocess.run(
        [os.path.join(venv_path, "python"), "babycoder.py", task], text=True, cwd=cwd
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <task>")
        sys.exit(1)
    setup_virtual_environment()
    task = sys.argv[1]
    run_specific_agent(task)
