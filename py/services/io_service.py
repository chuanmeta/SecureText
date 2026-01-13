import os

def createDirectory(dirPath: str):
    fullPath = os.path.abspath(dirPath)
    os.makedirs(fullPath, exist_ok=True)
    return fullPath