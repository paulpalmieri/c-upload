from driver.uploader import upload
import sys

def main():
    print("Uploading your documents...")
    upload(sys.argv[1:])