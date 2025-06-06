import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Linux":
        # Read uptime from /proc/uptime
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return f"System Uptime: {hours} hours, {minutes} minutes"
    elif system == "Windows":
        # Use 'net stats srv' and parse output
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                return f"System Uptime (since): {line.split('since')[1].strip()}"
        return "Could not determine uptime on Windows."
    elif system == "Darwin":
        # macOS: use 'uptime' command
        output = subprocess.check_output("uptime", shell=True, text=True)
        return f"System Uptime: {output.strip()}"
    else:
        return "Unsupported OS for uptime check."

if __name__ == "__main__":
    print(get_uptime())
