import os




dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"]
for di in dirs:
    os.makedirs(di)
    with open(os.path.join(di,".gitkeep"),"w") as f:
        pass
file = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")

]
for file_ in file:
    with open(file_,"w") as f:
        pass