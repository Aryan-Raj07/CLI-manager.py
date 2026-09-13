# CLI Password Manager
A lightweight command-line interface (CLI) application built in Python designed to explore file I/O operations and one-way cryptographic hashing concepts.
---
## Features

*Master Password Verification: Hashes the master key using SHA-256 upon initial setup; authenticates future logins by comparing hash digests without saving plaintext master keys.
* Persistent File Storage: Serializes and loads account records locally using structured JSON (`vault.json`).
* Interactive CLI: Simple loop interface to store, look up, and manage service credentials directly from the terminal.
---
## Tech Stack
* Language: Python 3.x
* Core Libraries:** `hashlib` (SHA-256 hashing), `json` (file serialization/deserialization), `os` (filesystem path handling)
---
## Project Structure
```text
├── manager.py          # Core application logic and CLI interface
└── README.md           # Project documentation
