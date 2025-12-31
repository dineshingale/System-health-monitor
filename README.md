# 📊 System Health Monitor (2025 Edition)

A multi-platform monitoring tool using Python, Bash, PowerShell, and YAML. It features a modern web dashboard for real-time visualization of system metrics.

## 🚀 Features

-   **Cross-platform Support:** Works on Linux (via Bash) and Windows (via PowerShell).
-   **Config-driven:** Customizable thresholds via `config/settings.yaml`.
-   **Real-time Dashboard:** A modern, responsive UI built with Vite & TailwindCSS.
-   **REST API:** FastAPI backend for easy integration.
-   **JSON Reports:** Automated report generation for historical tracking.

## 📋 Prerequisites

Ensure you have the following installed on your machine:
-   **Python 3.8+**
-   **Node.js 18+** & **npm**

## 🛠️ Installation

### 1. Backend Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/System-health-monitor.git
    cd System-health-monitor
    ```

2.  Create and activate a virtual environment (optional but recommended):
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\Activate.ps1

    # Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Frontend Setup

1.  Navigate to the dashboard directory:
    ```bash
    cd dashboard
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

## 🏃‍♂️ Running the Application

You need to run both the backend API and the frontend dev server.

### Start the Backend API

From the root directory:
```bash
python -m uvicorn src.server:app --reload
```
The API will be available at `http://localhost:8000`.

### Start the Dashboard

From the `dashboard` directory:
```bash
npm run dev
```
The UI will be available at `http://localhost:5173`.

## 📂 Project Structure

```
System-health-monitor/
├── config/                 # Configuration files (settings.yaml)
├── dashboard/              # Frontend (Vite + TailwindCSS)
├── reports/                # Generated JSON reports
├── src/
│   ├── collectors/         # Platform-specific scripts (Bash/PS1)
│   ├── main.py             # Core logic & CLI entry point
│   └── server.py           # FastAPI backend
├── requirements.txt        # Python dependencies
└── README.md
```

## 🤝 Contributing

1.  Create an Issue.
2.  Branch off `master` (`feat/issue-ID-description`).
3.  Commit your changes.
4.  Open a Pull Request.

---
**License**: MIT
