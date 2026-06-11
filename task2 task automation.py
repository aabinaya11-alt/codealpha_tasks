# ============================================
# Project: Automatic JPG File Mover
# Author: Internship Project
# Description: This program automatically moves
# all .jpg files from one folder to another.
# ============================================

import os
import shutil

# --- Welcome message ---
print("======================================")
print("      Automatic JPG File Mover        ")
print("======================================")
print()

# --- Ask the user to enter the source folder path ---
# This is the folder where the .jpg files currently are
source_folder = input("Enter the SOURCE folder path (where .jpg files are): ")
print()

# --- Ask the user to enter the destination folder path ---
# This is the folder where we want to move the .jpg files
destination_folder = input("Enter the DESTINATION folder path (where to move files): ")
print()

# --- Check if the source folder actually exists ---
if not os.path.exists(source_folder):
    print("ERROR: The source folder does not exist. Please check the path and try again.")
    exit()   # stop the program if source folder is not found

# --- Check if the source path is actually a folder (not a file) ---
if not os.path.isdir(source_folder):
    print("ERROR: The source path you entered is not a folder.")
    exit()

# --- If destination folder doesn't exist, create it automatically ---
if not os.path.exists(destination_folder):
    print("Destination folder not found. Creating it automatically...")
    os.makedirs(destination_folder)   # this creates the folder
    print("Destination folder created:", destination_folder)
    print()

# --- Get the list of all files inside the source folder ---
all_files = os.listdir(source_folder)

# --- Counter to keep track of how many .jpg files were moved ---
total_moved = 0

print("--------------------------------------")
print("Scanning source folder for .jpg files...")
print("--------------------------------------")
print()

# --- Go through each file one by one ---
for file_name in all_files:

    # --- Check if the file ends with .jpg (case-insensitive check) ---
    if file_name.lower().endswith(".jpg"):

        # --- Build the full path for source and destination ---
        # For example: C:/Photos/image1.jpg
        source_path = os.path.join(source_folder, file_name)

        # For example: C:/Moved/image1.jpg
        destination_path = os.path.join(destination_folder, file_name)

        # --- Check if a file with the same name already exists in destination ---
        if os.path.exists(destination_path):
            print("SKIPPED (already exists):", file_name)
            continue   # skip this file and move to the next one

        # --- Move the file from source to destination ---
        shutil.move(source_path, destination_path)

        # --- Tell the user which file was moved ---
        print("Moved:", file_name)

        # --- Add 1 to our counter ---
        total_moved = total_moved + 1

# --- After the loop, show the final result ---
print()
print("======================================")

# If at least one file was moved, show success message
if total_moved > 0:
    print("SUCCESS! All .jpg files have been moved.")
    print("Total files moved:", total_moved)

# If no .jpg files were found at all
else:
    print("No .jpg files were found in the source folder.")
    print("Total files moved:", total_moved)

print("======================================")
