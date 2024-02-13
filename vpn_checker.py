import subprocess

def is_vpn_connected(vpn_adapter_name):
    try:
        # Run PowerShell command to check the status of the VPN adapter
        # The command returns 'Up' if the VPN is connected, 'Down' otherwise
        command = f'Get-NetAdapter | Where-Object {{ $_.Name -like "{vpn_adapter_name}" }} | Select-Object -ExpandProperty Status'
        output = subprocess.check_output(['powershell', '-Command', command]).decode().strip()

        # Return True if VPN status is 'Up', indicating that the VPN is connected
        return output == 'Up'
    except subprocess.CalledProcessError as e:
        print(f"Error: PowerShell command failed with exit code {e.returncode}")
    except Exception as e:
        print(f"An error occurred while checking VPN connection: {e}")
    return False
