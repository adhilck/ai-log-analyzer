# 🔍 AI-Powered Log Analysis System

This project is a local AI-powered tool for analyzing system and application logs. It supports parsing multiple log formats, detects anomalies, identifies common patterns, and even generates human-readable incident reports — all without relying on cloud services or third-party APIs.

## 🚀 Features

- ✅ Supports multiple log types (Apache, Nginx, custom app logs)
- 🧠 Anomaly detection using simple heuristics
- 📊 Pattern frequency analysis
- 🧾 CLI chatbot interface to ask questions about your logs
- 🧩 Modular parser/analyzer architecture (MCP tools)
- 📤 Easy to extend for custom log formats

---

## 🗂 Project Structure

```plaintext
ai-log-analyzer/
├── mcp_tools/
│   ├── __init__.py
│   ├── parser.py        # Log parsing functions
│   └── analyzer.py      # Pattern + anomaly detection
├── logs/
│   ├── apache.log       # Sample Apache logs
│   ├── nginx.log        # Sample Nginx logs
│   └── ...              # Add your logs here
├── log_chatbot.py       # CLI chatbot interface
├── .gitignore
└── README.md
