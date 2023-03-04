import subprocess
import platform
import logging

logger = logging.getLogger(__name__)

class USBFormatterService:
    def __init__(self):
        self.os_name = platform.system()
    
    def format_drive(self, device):
        device_path = device.device
        if self.os_name == 'Linux':
            # Format drive as GPT partition on Linux
            cmd = ['sudo', 'sgdisk', '-Z', device_path]
            subprocess.check_call(cmd)
            logger.info(f"Drive {device_path} formatted as GPT partition.")
            # Name the formatted drive "bootle" on Linux
            cmd = ['sudo', 'mkfs.fat', '-F', '32', '-n', 'bootle', f"{device_path}1"]
            subprocess.check_call(cmd)
            logger.info(f"Drive {device_path} named as 'bootle'.")
        elif self.os_name == 'Darwin':
            # Format drive as GPT partition and name it "bootle" on macOS
            cmd = ['diskutil', 'eraseDisk', 'GPT', 'bootle', device_path]
            subprocess.check_call(cmd)
            logger.info(f"Drive {device_path} formatted as GPT partition and named as 'bootle'.")
        elif self.os_name == 'Windows':
            # Find the disk number based on the device path
            cmd = ['diskpart', '/s']
            path = device_path.split('\\\\')[2]
            stdin_str = f"""list disk
                            select disk
                            {path}  # Select the disk with the corresponding device path
                            clean
                            convert gpt
                            create partition primary
                            format fs=fat32 quick label="bootle"
                            assign letter=f"""
            subprocess.check_call(cmd, input=stdin_str, text=True)
            logger.info(f"Drive {device_path} formatted as GPT partition and named as 'bootle'.")
        else:
            logger.warning("Unsupported operating system.")
