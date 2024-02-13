import subprocess
import platform
import logging

# Set up logging
logging.basicConfig(filename='vpn_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_vpn_connected(vpn_adapter_name):
    try:
        if platform.system() == 'Windows':
            # Check if the VPN is connected by running a command specific to Windows
            output = subprocess.check_output(['powershell', '-Command', f'Get-NetAdapter | Where-Object {{ $_.Name -like "{vpn_adapter_name}" }} | Select-Object -ExpandProperty Status']).decode().strip()
            if 'Up' in output:
                return True
            else:
                return False
        else:
            logging.warning("VPN connection check is not implemented for this platform.")
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking VPN connection: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred while checking VPN connection: {e}")
        return False
