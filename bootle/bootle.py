import logging
from bootle.models.device import Device
from bootle.services.usb_service import UsbService
from bootle.services.formatter_service import USBFormatterService
from termcolor import colored


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    try:
        usb_service = UsbService()
        devices = usb_service.get_devices()
        logger.info(f"Found {len(devices)} USB device(s):\n")
        for index, device in enumerate(devices):
            logger.info(f"{colored(str(index + 1), 'yellow')}. {colored(device,'green')}")
        logger.info(f"{colored('q', 'yellow')}. Quit")

        while True:
            choice = input("\nSelect a device (enter number or q to quit): ")
            if choice == 'q':
                break
            try:
                selected_device = devices[int(choice) - 1]
                logger.info(f"\nSelected device:\n{selected_device}")
                formatter_service = USBFormatterService()
                formatter_service.format_drive(selected_device.device_path)
                logger.info(f"\nDrive {selected_device} has been formatted and named as 'bootle'.")
                break
            except (IndexError, ValueError):
                logger.warning("Invalid input, please try again.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()