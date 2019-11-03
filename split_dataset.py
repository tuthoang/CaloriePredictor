import os
source = "WebScrape/images"
dest = "WebScrape/test"
directories = os.listdir(source)
import shutil
import numpy as np
for d in directories:
    directory = os.path.join(source, d)
    print(directory)
    try:
        files = os.listdir(directory)
        print(files)
        for f in files:
            old_file = os.path.join(directory, f)
            os.makedirs(os.path.join(dest, d), exist_ok=True)
            new_file = os.path.join(dest, d, f)
            if np.random.rand(1) < 0.2:
                shutil.move(old_file, new_file)

    except NotADirectoryError as e:
        f = directory
        if f[-4:] == '.png':
            print("FILE:", f)
            os.makedirs(dest, exist_ok=True)
            new_file = os.path.join(dest, os.path.basename(f))
            print(f, new_file)
            if np.random.rand(1) < 0.2:
                shutil.move(f, new_file)