import shutil, os, send2trash, time
from pathlib import Path

p = Path('ADD YOUR DESKTOP DIRECTORY HERE')
screenshots_folder = p / 'Screenshots'

# Ensure 'Screenshots' folder exists
screenshots_folder.mkdir(exist_ok=True)

while True:  # Keep running indefinitely
    items = list(p.glob('*.png'))  # Refresh the file list every loop
    
    for item in items:
        if 'Screenshot' in item.name:
            print('Screenshot found:', item)
            
            # Move the screenshot instead of copying (optional)
            shutil.move(str(item), str(screenshots_folder))  
            
            # Alternative: If you want to copy and then delete
            # shutil.copy(item, screenshots_folder)
            # send2trash.send2trash(item)
    
    time.sleep(10)  # Check for new screenshots every 10 seconds
