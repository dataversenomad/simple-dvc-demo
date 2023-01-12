import os

# folders needed

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"

]

# create directories
for dir_ in dirs:
    os.makedirs(dir_, exist_ok = True)
    # create for each directory a file for git
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass

# acting as a remote resource
os.makedirs("data_given")