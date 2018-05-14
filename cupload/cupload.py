import sys
from routine import upload

def main():
    print("Uploading your documents...")
    upload(sys.argv[1:])
