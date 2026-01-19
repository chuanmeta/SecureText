import os


def makeDir(path: str):
    fullPath = os.path.abspath(path)
    os.makedirs(fullPath, exist_ok=True)
    return fullPath