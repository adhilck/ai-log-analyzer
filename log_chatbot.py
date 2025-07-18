from mcp_tools.parser import parse_logs
from mcp_tools.analyzer import analyze_logs
import json

print("🤖 LogBot: Welcome! Type 'exit' to quit.")

log_path = input("📝 Enter log file path (example: logs/apache.log): ").strip()

try:
    logs = parse_logs(log_path)
    result = analyze_logs(logs)
except FileNotFoundError:
    print("❌ Log file not found!")
    exit()

while True:
    question = input("You: ").strip().lower()
    if question == "exit":
        print("👋 Goodbye!")
        break
    elif question == "anomalies":
        print(f"🚨 Anomalies found: {result['anomalies']}")
    elif question == "patterns":
        print("📊 Top Patterns:")
        for pattern, count in result['patterns'].items():
            print(f" - {pattern} : {count} times")
    elif question == "report":
        import json
        print("\n📄 Incident Report:\n")
        print(json.dumps(result, indent=2))
        print()

