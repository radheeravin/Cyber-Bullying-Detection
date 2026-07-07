
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    try:
        r = requests.get(f"{BASE_URL}/health")
        print(f"Health Check: {r.status_code} {r.json()}")
    except Exception as e:
        print(f"Health Check Failed: {e}")

def test_analyze(text, expected_decision):
    payload = {
        "text": text,
        "url": "http://test.com",
        "dom": "<html><body>Test</body></html>",
        "screenshot": ""
    }
    try:
        r = requests.post(f"{BASE_URL}/analyze", json=payload)
        data = r.json()
        print(f"Analyze '{text[:20]}...':")
        print(f"  Decision: {data.get('decision')}")
        print(f"  Scores: {data.get('scores')}")
        if data.get('decision') == expected_decision:
            print("  [PASS]")
        else:
            print(f"  [FAIL] Expected {expected_decision}, got {data.get('decision')}")
    except Exception as e:
        print(f"Analyze Failed: {e}")

if __name__ == "__main__":
    test_health()
    test_analyze("Hello world, this is a nice day.", "Safe")
    test_analyze("You are a stupid idiot and I hate you.", "Abusive")
