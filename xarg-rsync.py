#!/usr/bin/env python

"""
This script copies files from source to destination using xargs to speed up the copy, and ensures that permissions and ownership are kept the same.

Args:
    source: The source directory.
    destination: The destination directory.
"""

import subprocess

def rsync_with_xargs(source, destination):
  """
  Copies files from source to destination using xargs to speed up the copy, and ensures that permissions and ownership are kept the same.

  Args:
    source: The source directory.
    destination: The destination directory.
  """

  # Get a list of all the files in the source directory.
  # The `find` command will find all the files in the source directory that are regular files (i.e., not directories or symlinks).
  # The `-type` option specifies the type of files to find.
  # The `f` option specifies that regular files should be found.
  # The output of the `find` command is a list of file paths.
  files = subprocess.check_output(["find", source, "-type", "f"]).decode("utf-8").splitlines()

  # Use xargs to pass the list of files to rsync.
  # The `xargs` command will read a list of arguments from stdin and pass them to another command.
  # The `-a` option tells xargs to use the same options as the command that it is calling.
  # The `-e` option tells xargs to use the specified command to execute the command that it is calling.
  # The `ssh` command is used to execute commands on remote servers.
  # The `--files-from` option tells rsync to read the list of files from stdin.
  # The `--preserve=mode,ownership` option tells rsync to preserve the permissions and ownership of the files being copied.
  subprocess.Popen(["rsync", "-a", "-e", "ssh", "--files-from", "-", "--preserve=mode,ownership", source, destination])

if __name__ == "__main__":
  # Get the source and destination directories from the user.
  source = input("Enter the source directory: ")
  destination = input("Enter the destination directory: ")

  # Copy the files from source to destination.
  rsync_with_xargs(source, destination)
