"""Send pre-computed metrics to DeepSeek and write the Markdown report."""
import json
import os
import sys

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    ticker = (os.getenv("TICKER") or "PLTR").upper()

    if not api_key:
        sys.exit("DEEPSEEK_API_KEY not set in .env")

    metrics = json.load(sys.stdin)
    prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "system_prompt.md")
    with open(prompt_path) as f:
        system_prompt = f.read().replace("{TICKER}", ticker)

    resp = requests.post(
        f"{base_url}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(metrics, indent=2)},
            ],
            "temperature": 0.3,
        },
        timeout=300,
    )
    resp.raise_for_status()
    report = resp.json()["choices"][0]["message"]["content"]

    os.makedirs("reports", exist_ok=True)
    out = os.path.join("reports", f"{ticker}_earnings_report.md")
    with open(out, "w") as f:
        f.write(report)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
