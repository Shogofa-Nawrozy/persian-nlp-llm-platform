import subprocess

def generate_with_mistral(prompt: str) -> str:
    try:
        ollama_path = r"C:\Users\dell\AppData\Local\Programs\Ollama\ollama.exe"

        result = subprocess.run(
            [ollama_path, "run", "mistral"],
            input=prompt.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120
        )

        if result.returncode != 0:
            return f"Ollama error: {result.stderr.decode('utf-8')}"

        return result.stdout.decode('utf-8').strip()

    except FileNotFoundError:
        return "Error: Could not find Ollama. Make sure the path is correct."
    except Exception as e:
        return f"Error: {e}"
