import argparse
import logging

def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", 
                        handlers=[logging.FileHandler(log_file), logging.StreamHandler()])


parser = argparse.ArgumentParser(description="Folder Synchronization")
parser.add_argument("source", type=str, help="Path to the source folder")
parser.add_argument("replica", type=str, help="Path to the replica folder")
parser.add_argument("interval", type=int, help="Synchronization interval (in seconds)")
parser.add_argument("log_file", type=str, help="Path to the log file")
args = parser.parse_args()

# Output test
print("Source Folder:", args.source)
print("Replica Folder:", args.replica)
print("Sync Interval:", args.interval)
print("Log File:", args.log_file)

setup_logging(args.log_file)
    
# Test logging
logging.info("Logging successful.")