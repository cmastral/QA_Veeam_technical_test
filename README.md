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
I chose to complete the task in Python because it's the language I'm most comfortable with and have been working with the last few years. I tried to approach this task step by step and testing each part incrementally.

I started by verifying that the script could accept command-line arguments and that logging worked properly, with output both to the console and to the log file. The main synchronization function was built step-by-step to handle copying, updating, and deleting files and folders as needed. I implemented checks to ensure that only new or updated files would be copied, and that extra files in the replica folder would be deleted. I let the logs and the test files in the repository for your reference. Finally, I wrapped the sync function in a loop with time.sleep(interval) to allow for periodic syncing each specified interval.

**Potential Improvements:**

Currently, the script doesn’t take into account issues like file permission errors, network errors, or other unexpected situations. 
Additionally, regarding processing, for large folders with many files, the synchronization could be improved by using multi-threading or asynchronous processing to speed up file management. 


## Personal Note 
Honestly, I’m pretty new to this type of role, but I decided to start the task in Python since it’s the language I’m most comfortable with. I broke the problem down into smaller steps one piece at a time. I tried to figure out each part, like handling the command-line arguments, setting up the logging, and actually syncing the folders. Whenever I came across something I wasn’t sure about, I just looked it up and tried to work it into the solution. Overall, it’s been a great hands on way to get more comfortable with automation and I hope we have the chance to discuss more about it. :) 