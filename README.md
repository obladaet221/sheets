
# JSON to Google Sheets Converter


## Overview

This project automates the process of converting JSON-like data from a text file into a tabular format in Google Sheets using Python and Google APIs.

## Getting Started

### Prerequisites : <br>
- Python 3.9
- PyCharm (I used 2022.2 Community Edition)

### Installation
1. Install Python 3.9.
2. Install PyCharm (I used version 2022.2 Community Edition).

3. Create a virtual environment using PyCharm, this shall create a `venv` folder in the current repository.

    For those who haven't done this before, you can learn setting up a virtual environment in PyCharm from this [link](https://www.youtube.com/watch?v=2P30W3TN4nI&t=16s).

4. For the required Python packages, run the following commands within your virtual environment:

```bash
pip install pandas
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Setting Up Google Sheets API

5. Set up Credentials for GoogleSheets API - follow [Google's documentation](https://developers.google.com/sheets/api/quickstart/python) for same or You can watch [this](https://www.youtube.com/watch?v=4ssigWmExak&t=607s) video that has explained in detail how to do it
6. When a connection is set up using the above, a new file containing the keys will be downloaded automatically, move that to the `venv` folder

## Writing the logic

7. Create wrangle.py in venv repository created in Pycharm projects. This is where your data wrangling/transformation logic is.
8. Add quickstart.py file in the same repository - I took this code from [here](https://developers.google.com/sheets/api/quickstart/python) and tweaked it as per the requirement.
9. Add data.txt file too

## Running the project

10. Run the quickstart.py file from terminal in venv from within PyCharm using
    ```bash
     python quickstart.py
    ```
## Screenshot

A Successful execution should look like [this](https://github.com/Mansi242401/text_df_googlesheet/blob/main/Screen%20Shot%202023-09-02%20at%206.20.31%20PM.png) in the terminal.

Here's a [sample]() of input data (JSON) 

Here's a [sample]() of output data (Tabular)



