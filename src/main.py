import os
import platform
import subprocess
import yaml
import json
from datetime import datetime

def load_config():
    with open('config/settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def get_metrics():
    os_name = platform.system()

    if os_name == "Linux":
        script_path = "src/collectors/linux_metrics.sh"
        os.chmod(script_path, 0o755)
        result = subprocess.run([f"./{script_path}"], capture_output=True, text=True)
    elif os_name == "Windows":
        script_path = "src/collectors/win_metrics.ps1"
        result = subprocess.run(["powershell", "-File", script_path], capture_output=True, text=True)
    else:
        print(f"Unsupported OS: {os_name}")
        return None

    raw_data = result.stdout.strip()
    metrics = {}
    for item in raw_data.split(','):
        key, value = item.split(':')
        metrics[key] = float(value)
    return metrics

def check_alerts(metrics, config):
    alerts = []
    thresholds = config['thresholds']

    if metrics['cpu'] > thresholds['cpu_percent']:
        alerts.append(f"CRITICAL: CPU Usage at {metrics['cpu']}%")
    if metrics['mem'] > thresholds['memory_percent']:
        alerts.append(f"CRITICAL: Memory Usage at {metrics['mem']}%")
    if metrics['disk'] > thresholds['disk_percent']:
        alerts.append(f"CRITICAL: Disk Usage at {metrics['disk']}%")

    return alerts

def generate_report(metrics, alerts, config):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_data = {
        "timestamp": timestamp,
        "metrics": metrics,
        "alerts": alerts,
        "status": "HEALTHY" if not alerts else "WARNING"
    }

    os.makedirs('reports', exist_ok=True)
    filename = f"{config['reporting']['output_path']}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"

    with open(filename, 'w') as f:
        json.dump(report_data, f, indent=4)

    print(f"Report generated: {filename}")

if __name__ == "__main__":
    print("--- System Health Monitor (2025) ---")
    config = load_config()
    metrics = get_metrics()

    if metrics:
        alerts = check_alerts(metrics, config)
        generate_report(metrics, alerts, config)
