# vpn_checker.py
import subprocess

def is_vpn_connected():
    try:
        # Check if the VPN is connected by running a command specific to your VPN client
        # For example, if you are using OpenVPN, you can check the status of the TAP adapter
        output = subprocess.check_output(['powershell', '-Command', 'Get-NetAdapter | Where-Object { $_.Name -like "Tap-Windows*" } | Select-Object -ExpandProperty Status']).decode()
        if 'Up' in output:
            return True
    except Exception:
        pass
    return False