from colorama import Fore
from pathlib import Path
import sys

tab = '   '

def write_file_name(name):
    print(f"{Fore.BLUE} {name}")

def write_folder_name(name):
    print(f"{Fore.YELLOW} {name}")

def write_dir_infos(path):
    try:
        directory = Path(path)

        if not directory.exists():
            print('directory not exists')
            return

        write_dir_info(directory, tab)

    except:
        print('general exception')

def write_dir_info(directory, tabs):
    write_folder_name(f'{tabs}{directory.name}/')

    for path in directory.iterdir():
        if path.is_dir():
            write_dir_info(path, f'{tab}{tabs}')
        else:
            write_file_name(f'{tabs}{tab}{path.name}')

def main():
    if len(sys.argv) > 1:
        write_dir_infos(sys.argv[1])
    else:
        print('please add path to folder')

if __name__ == "__main__":
    main()

# command : python main.py ./folder1