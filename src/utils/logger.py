import logging
import os

def setup_logger():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger('SystemHealthMonitor')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f'{log_dir}/system_monitor.log')
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

monitor_log = setup_logger()
