import os
import shutil
from pathlib import Path

def move_and_rename_files(src_dir, dest_dir):
    src_path = Path(src_dir)
    dest_path = Path(dest_dir)

   
    dest_path.mkdir(parents=True, exist_ok=True)

    for parent_folder in src_path.iterdir():
        if parent_folder.is_dir():
            country_name = parent_folder.name + "population"

            stats_folder = parent_folder / "STATS"  

            for file in stats_folder.iterdir():
                if file.is_file() and file.name == 'Population.txt':  
                    new_file_name = f"{country_name}{file.suffix}"
                    new_file_path = dest_path / new_file_name
                    shutil.move(file, new_file_path)

if __name__ == "__main__":
    source_directory =  r"C:\Users\44741\Desktop\hmd" 
    destination_directory = r"C:\Users\44741\Desktop\all_countries_death_1x1" 

    move_and_rename_files(source_directory, destination_directory)
