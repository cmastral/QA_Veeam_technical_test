import argparse
import logging
import shutil 
import os
import time

def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", 
                        handlers=[logging.FileHandler(log_file), logging.StreamHandler()])

def sync_folder(source, replica):
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)

        # Create the same directories in replica folder
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info(f"Created directory: {replica_root}")

        # Copy files from source to replica folder
        for file_name in files:
            source_file = os.path.join(root, file_name)
            replica_file = os.path.join(replica_root, file_name)
            if not os.path.exists(replica_file):
                shutil.copy2(source_file, replica_file)
                logging.info(f"Copied file: {replica_file}")

        for root, dirs, files in os.walk(replica, topdown=False):
            rel_path = os.path.relpath(root, replica)
            source_root = os.path.join(source, rel_path)

            # Remove files
            for file_name in files:
                replica_file = os.path.join(root, file_name)
                source_file = os.path.join(source_root, file_name)
                if not os.path.exists(source_file):
                    os.remove(replica_file)
                    logging.info(f"Removed file: {replica_file}")

            # Remove directories
            for dir_name in dirs:
                replica_dir = os.path.join(root, dir_name)
                source_dir = os.path.join(source_root, dir_name)
                if not os.path.exists(source_dir):
                    shutil.rmtree(replica_dir)
                    logging.info(f"Removed directory: {replica_dir}")

def periodic_synchronization(source, replica, interval):
    while True:
        sync_folder(source, replica)
        time.sleep(interval)    

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
periodic_synchronization(args.source, args.replica, args.interval)