import argparse

parser = argparse.ArgumentParser(description="Folder Synchronization")
parser.add_argument("source", type=str, help="Path to the source folder")
parser.add_argument("replica", type=str, help="Path to the replica folder")
parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
parser.add_argument("log_file", type=str, help="Path to the log file")
args = parser.parse_args()

# Output test
print("Source Folder:", args.source)
print("Replica Folder:", args.replica)
print("Interval:", args.interval)
print("Log File:", args.log_file)
