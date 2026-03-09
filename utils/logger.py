import logging
import os
import platform

def get_logger(name="mag-diff"):
    """
    Returns a configured logger that writes to both console and a file.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create handlers
        c_handler = logging.StreamHandler()
        
        # Ensure the logs directory exists
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        f_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
        
        # Create formatters and add it to handlers
        os_type = platform.system()
        c_format = logging.Formatter(f'%(name)s - %(levelname)s - [{os_type}] - %(message)s')
        f_format = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - [{os_type}] - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        
        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
    return logger
