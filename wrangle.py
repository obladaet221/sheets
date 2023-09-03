import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self) -> str:
        try:
            with open(self.file_path, 'r') as file:
                file_content = file.read()
                return file_content
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)

    def tickers(self) -> list[str]:
        content = self.read_data()
        first, *others = content.split('.SZ')
        return others

    def extract_pnl(self, list_variable: list[str]) -> list[str]:
        all_pnl = []
        for i in range(len(list_variable)):
            statement = list_variable[i].split('}}')
            pnl = statement[1]
            all_pnl.append(pnl)
        return all_pnl

    def clean_string(self, input_string: str) -> str:
        index = input_string.find("{'Yearend':")
        if index != -1:
            new_string = input_string[index:]
            new_string += "}}"
            return new_string

    def dict_to_df(self, data_list: list) -> pd.DataFrame:
        transformed_dfs = []
        i = 1
        for pnl in data_list:
            df = pd.DataFrame(eval(self.clean_string(pnl)))
            df = df[['Net Income from Continuing & Discontinued Operation', 'Total Revenue']]
            df = df.reset_index()
            value = 'ticker' + str(i)
            df.insert(0, 'Ticker_name', [value] * len(df))
            i += 1
            transformed_dfs.append(df)
        combined_df = pd.concat(transformed_dfs, ignore_index=True)
        return combined_df

    def pivoted_df(self, df: pd.DataFrame) -> pd.DataFrame:
        pivot_df = df.pivot(index='Ticker_name', columns='index')
        new_columns = pd.MultiIndex.from_product([['Net Income from Continuing & Discontinued Operation', 'Total Revenue'],
                                                  ['Current', 'Year1', 'Year2', 'Year3', 'Year4']], names=['Metric', 'Year'])
        new_df = pd.DataFrame(columns=new_columns, index=pivot_df.index)
        for metric in ['Net Income from Continuing & Discontinued Operation', 'Total Revenue']:
            for year in ['Current', 'Year1', 'Year2', 'Year3', 'Year4']:
                new_df[metric, year] = pivot_df[metric, year]
        return new_df

    def sorted_df(self) -> pd.DataFrame:
        tickers_list = self.tickers()
        common_string = "ticker"
        n = len(tickers_list)
        ticker_order = [common_string + str(n) for n in range(1, n + 1)]
        final_df = self.pivoted_df(self.dict_to_df(self.extract_pnl(tickers_list)))
        sorted_data = final_df.loc[ticker_order]
        return sorted_data

    def main(self):
        return self.sorted_df()


# Usage
if __name__ == "__main__":
    file_path = "data_copy.txt"
    processor = DataProcessor(file_path)
    result_df = processor.main()
    print(result_df)
