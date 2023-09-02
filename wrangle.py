import pandas as pd
import json

def read_data(path: str) -> str:
    """
    Read data from a file.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    try:
        with open(path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def tickers(file_path: str) -> list[str]:
    """
    Extract ticker data from a file.

    Args:
        file_path (str): The path to the file containing ticker data.

    Returns:
        list[str]: A list of ticker data.
    """
    content = read_data(file_path)
    first, *others = content.split('.SZ')
    return others

def extract_pnl(list_variable: list[str]) -> list[str]:
    """
    Extract P&L (Profit and Loss) data from a list of ticker data.

    Args:
        list_variable (list[str]): A list of ticker data.

    Returns:
        list[str]: A list of extracted P&L data.
    """
    all_pnl = []
    for i in range(len(list_variable)):
        statement = list_variable[i].split('}}')
        pnl = statement[1]
        all_pnl.append(pnl)
    return all_pnl

def clean_string(input_string: str) -> str:
    """
    Clean an input string by extracting a specific substring.

    Args:
        input_string (str): The input string to be cleaned.

    Returns:
        str: The cleaned substring.
    """
    index = input_string.find("{'Yearend':")
    if index != -1:
        new_string = input_string[index:]  # Extract the substring starting from "Yearend:"
        new_string += "}}"   # Add '}}' at the end
        return new_string

def dict_to_df(data_list: list) -> pd.DataFrame:
    """
    Convert a list of data into a Pandas DataFrame.

    Args:
        data_list (list): A list of data.

    Returns:
        pd.DataFrame: A Pandas DataFrame.
    """
    transformed_dfs = []
    i = 1
    for pnl in data_list:
        df = pd.DataFrame(eval(clean_string(pnl)))
        df = df[['Net Income from Continuing & Discontinued Operation', 'Total Revenue']]
        df = df.reset_index()
        value = 'ticker' + str(i)
        df.insert(0, 'Ticker_name', [value] * len(df))
        i += 1
        transformed_dfs.append(df)
    combined_df = pd.concat(transformed_dfs, ignore_index=True)
    return combined_df

def pivoted_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot a Pandas DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame to be pivoted.

    Returns:
        pd.DataFrame: The pivoted DataFrame.
    """
    pivot_df = df.pivot(index='Ticker_name', columns='index')  # changing ticker_name to an index
    new_columns = pd.MultiIndex.from_product([['Net Income from Continuing & Discontinued Operation', 'Total Revenue'],
                                             ['Current', 'Year1', 'Year2', 'Year3', 'Year4']], names=['Metric', 'Year'])
    new_df = pd.DataFrame(columns=new_columns, index=pivot_df.index)
    for metric in ['Net Income from Continuing & Discontinued Operation', 'Total Revenue']:
        for year in ['Current', 'Year1', 'Year2', 'Year3', 'Year4']:
            new_df[metric, year] = pivot_df[metric, year]
    return new_df

def sorted_df(df: pd.DataFrame, tickers: list[str]) -> pd.DataFrame:
    """
    Sort a DataFrame based on a list of tickers.

    Args:
        df (pd.DataFrame): The input DataFrame to be sorted.
        tickers (list[str]): A list of tickers.

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """
    common_string = "ticker"
    n = len(tickers)
    ticker_order = [common_string + str(n) for n in range(1, n+1)]
    sorted_data = df.loc[ticker_order]
    return sorted_data

def main(file_path: str):
    """
    Main function to process data and return the final DataFrame.

    Args:
        file_path (str): The path to the data file.

    Returns:
        pd.DataFrame: The final processed DataFrame.
    """
    final_df = sorted_df(pivoted_df(dict_to_df(extract_pnl(tickers(file_path)))), tickers(file_path))
    return final_df
