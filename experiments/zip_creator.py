import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)  # 1st stage
            archive.write(filepath, arcname=filepath.name)#second stage to extract only the file name not the whole apth

if __name__ == "__main__": #to test the function lcally
    make_archive(filepaths=["bonus2.py"], dest_dir="dest")