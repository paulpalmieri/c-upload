# c-upload
Automates and speeds up the upload of documents on the public printer service of Concordia University. 
Run a single command and do something else while all the documents get uploaded.
Uses `Selenium` to automate Chrome dynamically. 

## Requirements
* Python 3 (use `brew install python` if you don't have python3)
* Pip and Setuptools (they should come bundled with python3)
* Chrome Browser
* Chrome Driver (executable available at http://chromedriver.chromium.org/downloads)

## Installation
1. Clone the repository and move the folder where you'd like
2. Get the most recent version of ChromeDriver and put the executable in the driver folder
3. Put your information in the `credentials.json` file
4. Open terminal and navigate to the cloned folder
5. Run `pip install -e cupload` 

## Running instructions
You can chose which printer you want to use by running:
* `cupload bw` for black and white printers
* `cupload color` for color printers   

Or simply run `cupload` from anywhere, default is black and white.
The documents in the `upload_queue` folder will be uploaded one by one.


## Uploading documents
You can create a shortcut/alias of the `upload_queue` folder and put it where you'd like.  
Simply drag and drop the documents into it, then run `cupload` to start the process.

### Notes
Tested on OSX only.
