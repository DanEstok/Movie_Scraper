import subprocess

def is_vpn_connected(vpn_adapter_name):
    try:
        # Check if the VPN is connected by running a command specific to your VPN client
        # For example, if you are using OpenVPN, you can check the status of the TAP adapter
        output = subprocess.check_output(['powershell', '-Command', f'Get-NetAdapter | Where-Object {{ $_.Name -like "{vpn_adapter_name}" }} | Select-Object -ExpandProperty Status']).decode()
        if 'Up' in output:
            return True
    except Exception as e:
        print(f"An error occurred while checking VPN connection: {e}")
    return False
