# 🔔 Three-Tier Notification System using Python (SSL Secured)

This project is a Python-based implementation of a **secure client-server notification system** using a **conceptual three-tier architecture**. It demonstrates how clients can communicate securely with a server, send structured commands, and receive real-time notifications, making it ideal for educational use in network programming and secure communication.

---
          
## 📌 Project Overview

The system simulates a structured communication model with the following conceptual tiers:

### 1. Client Tier
- Python client with a basic GUI (Tkinter).
- Allows users to:
  - Connect securely to the server.
  - Choose a nickname.
  - Send and receive messages.
  - Receive command-based notifications.

### 2. Routing Tier *(Logical Layer)*
- Handled inside the server.
- Parses client messages and routes them to appropriate recipients.
- Supports basic command handling like:
  - `COMS`
  - `COMS WA <recipient> <message>`
  - `!DISCONNECT`

### 3. Data Tier
- The server maintains:
  - Active client connections.
  - Associated nicknames.
  - Communication logic for disconnects and routing.

---

## ⚙️ Key Features

- 🔐 **Secure communication** using SSL/TLS with self-signed certificates.
- 👥 **Multi-client support** via multithreading.
- 💬 **Real-time messaging and notification system**.
- 🧠 **Command parsing and routing** handled server-side.
- 🖼 **Client GUI** for interactive use (based on Tkinter).
- 
