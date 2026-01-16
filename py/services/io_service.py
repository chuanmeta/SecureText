import os

def makeDir(dirPath):
    fullPath = os.path.abspath(dirPath)
    os.makedirs(fullPath, exist_ok=True)
    return fullPath