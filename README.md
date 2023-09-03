
### Converting json data in text file to tabular data in google sheets using python and google APIs

Following are the steps to run this program:

1. Install Python 3.9
2. Install PyCharm (I used 2022.2(Community Edition))

3. Create a virtual environment using PyCharm, this shall create a venv folder in the current repository.(For those who havent done this before, can learn setting up a virtual environment in PyCharm from this [link](https://www.youtube.com/watch?v=2P30W3TN4nI&t=16s)

4. Install all dependencies using Pip, if not already installed running the following in terminal within the virtual environment
   a. ```python
   pip install pandas```
   (I used version 1.5.2 - You can use any latest version)
   b. pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  (This is required for communicating with Google APIs to populate data into google spreadsheet.

6. Set up Credentials for GoogleSheets API - follow Google's documentation for same or You can watch [this](https://www.youtube.com/watch?v=4ssigWmExak&t=607s) video that has explained in detail how to do it

7. Create wrangle.py in venv repository created in Pycharm projects. This is where your data wrangling/transformation logic is.
8. Add quickstart.py file in the same repository - I took this code from [here](https://developers.google.com/sheets/api/quickstart/python) and tweaked it as per the requirement.
9. Add data.txt file too
10. Run the quickstart.py file from terminal in venv from within PyCharm using 

