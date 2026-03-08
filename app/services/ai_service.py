import requests

API_URL = "https://router.huggingface.co/hf-inference/models/codellama/CodeLlama-7b-hf"

API_TOKEN = "hf_your_token_here"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

SYSTEM_PROMPT = """
Rewrite the given code with the same logic.
Change variable names and structure.
Improve readability.
Return only the rewritten code.
"""

def refine_code(code):

    prompt = f"{SYSTEM_PROMPT}\n\nCode:\n{code}"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    result = response.json()

    if isinstance(result, list):
        return result[0].get("generated_text", "No output generated")

    if "error" in result:
        return result["error"]

    return "Unexpected API response"