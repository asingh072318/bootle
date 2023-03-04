import os
import logging
import platform
import psutil
from bootle.models.device import Device


logger = logging.getLogger(__name__)


class UsbService:
    def get_devices(self):
        devices = []
        for partition in psutil.disk_partitions(True):
            if 'sd' in partition.device and "boot" not in partition.mountpoint:
                device_path = partition.device
                total, used, available = self.get_device_space(device_path)
                device_size = {
                    'total': self.get_human_readable_size(total),
                    'used': self.get_human_readable_size(used),
                    'available': self.get_human_readable_size(available)
                }
                devices.append(Device(device_path, device_size, device_path))
        return devices

    def get_device_space(self, path):
        st = os.statvfs(path)
        total = st.f_blocks * st.f_frsize
        available = st.f_bavail * st.f_frsize
        used = total - available
        return total, used, available

    @staticmethod
    def get_human_readable_size(size_in_bytes):
        """
        Convert size from bytes to human-readable format.
        """
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.2f} PB"