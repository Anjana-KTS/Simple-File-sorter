import os
import shutil

# Define the folder to sort files in (Downloads folder path)
sou_folder = os.path.expanduser("~/Downloads")  # Automatically fetches Downloads folder

# Define destination folders
folders = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".xlsx", ".txt"],
    "Others": []  # Catch-all for undefined types
}

# Create destination folders if they don't exist
for folder in folders.keys():
    os.makedirs(os.path.join(sou_folder, folder), exist_ok=True)

# Function to sort files
def sort_files():
    for filename in os.listdir(sou_folder):
        file_path = os.path.join(sou_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Move file to the appropriate folder
        moved = False
        for folder, extensions in folders.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(sou_folder, folder, filename))
                moved = True
                break
        
        # If no match found, move to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(sou_folder, "Others", filename))

# Run the sorter
if __name__ == "__main__":
    sort_files()
    print("Files sorted successfully!")
