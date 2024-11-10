# Veeam Technical Test: Folder Synchronization Task

This task is a Python script that aims to synchronize two folders: source and replica. The script was designed to ensure the replica folder is a one-way synchronized copy of the source folder, run the synchronization at a standard interval, so that any new changes in source will be reflected in replica and track possible actions (file copies, updates, deletions) in both a log file and the console.
 
## How it works 
The script takes four (command line) **arguments**:

- **source**: Path to the source folder (target)
- **replica**: Path to the replica folder (copy) 
- **interval**: Number of seconds between each sync of folders
- **log_file**: Path to the file where the logs are saved

**Synchronization:**

The script iterates through each file and folder in the source folder and compares it with the replica.
- **Copied or Updated Files**: If a file is missing in the replica folder or it is modified (checked using timestamps), we copy it or update it respectively in replica folder. 
- **Removing Files**: Files or folders in replica that are not in the source folder are removed, so the folders are in sync. 
- **Logging feature**: Every action is logged both to the console and the log file.

The script runs in a loop with a time.sleep(interval) pause, updating the replica each specified interval. It continues to run until manually stopped.

## Usage 

To run the script, you can use:

```bash
python main.py /path/to/source/folder /path/to/replica/folder 10 /path/to/logs.txt
```

I used a 10 seconds internval between each sync for quicker testing but it can be set based on the task. 

## Process and Potential Improvements 

## Personal Note 