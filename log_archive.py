#!/usr/bin/env python3

import os
import sys
import tarfile
from datetime import datetime

def archive_logs(log_directory):
    if not os.path.isdir(log_directory):
        print(f"Error: '{log_directory}' is not a valid directory.")
        sys.exit(1)

    # Create archive directory if it doesn't exist
    archive_dir = os.path.join(os.getcwd(), "archived_logs")
    os.makedirs(archive_dir, exist_ok=True)

    # Create archive name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)

    # Compress the log directory
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname=os.path.basename(log_directory))

    print(f"Archived logs to: {archive_path}")

    # Log the action
    log_entry = f"[{datetime.now().isoformat()}] Archived '{log_directory}' to '{archive_path}'\n"
    with open(os.path.join(archive_dir, "archive_log.txt"), "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)

    log_dir = sys.argv[1]
    archive_logs(log_dir)
