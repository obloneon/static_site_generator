import os
import shutil


# Copies all the contents from a source directory to a destination directory.
def copy_directory(source_dir, target_dir):
    if not source_dir.startswith("./"):
        source_dir = f"./{source_dir}"
    if not target_dir.startswith("./"):
        target_dir = f"./{target_dir}"
    if not os.path.exists(source_dir):
        raise ValueError(f"{source_dir} does not exist")
    if not os.path.exists(target_dir):
        raise ValueError(f"{target_dir} does not exist")
    print(f"cleaning target dir at: {target_dir}")
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    recursive_copy(source_dir, target_dir)


def recursive_copy(src, dst):
    src_list = os.listdir(src)
    if len(src_list) == 0:
        print("reached empty directory")
        return
    for entry in src_list:
        path = os.path.join(src, entry)
        if os.path.isfile(path):
            print(f"copied {path} to {shutil.copy(path, dst)}")
        else:
            dir_copy_path = os.path.join(dst, entry)
            print(f"copying directory {path} to {dir_copy_path}")
            os.mkdir(dir_copy_path)
            recursive_copy(path, dir_copy_path)
