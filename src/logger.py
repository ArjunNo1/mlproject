import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_path = os.path.join(os.getcwd(),"logs",log_file)
log_file_path = os.path.join(log_path,log_file)
os.makedirs(log_path,exist_ok = True)
logging.basicConfig(filename =log_file_path,
                    level=logging.INFO,
                     format = '[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s')

# if __name__=='__main__':
#     logging.info("Logging Works !")