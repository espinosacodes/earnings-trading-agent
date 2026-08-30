"""Send pre-computed metrics to DeepSeek and write the Markdown report."""
import json
import os
import re
import sys

import requests
from dotenv import load_dotenv


def generate_report(ticker: str, metrics: dict) -> str:
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY not set in .env")

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
            "temperature": 0.2,
        },
        timeout=300,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def write_outputs(ticker: str, report: str) -> None:
    os.makedirs("reports", exist_ok=True)
    out = os.path.join("reports", f"{ticker}_earnings_report.md")
    with open(out, "w") as f:
        f.write(report)

    signal = re.search(r"```json\s*(\{.*?\})\s*```", report, re.DOTALL)
    if signal:
        with open(os.path.join("reports", f"{ticker}_signal.json"), "w") as f:
            f.write(signal.group(1))
        print(f"wrote {out} + {ticker}_signal.json")
    else:
        print(f"wrote {out} (no JSON signal block found)")


def main():
    ticker = (os.getenv("TICKER") or "PLTR").upper()
    metrics = json.load(sys.stdin)
    write_outputs(ticker, generate_report(ticker, metrics))


if __name__ == "__main__":
    main()
