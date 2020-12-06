from pandas.io.excel import ExcelWriter
import pandas

def cvs_to_xlsx(cvs_file, xlsx_file, sheet_name):
    with ExcelWriter(xlsx_file) as ew:
        pandas.read_csv(cvs_file).to_excel(ew, sheet_name=sheet_name, index=False)
        return xlsx_file

if __name__ == "__main__":
    cvs_file = './tests/final_result.csv'
    xlsx_file = './tests/final_result.xlsx'
    sheet_name = 'daily'
    cvs_to_xlsx(cvs_file, xlsx_file, sheet_name)

# https://stackoverflow.com/questions/39099008/how-to-write-csv-files-into-xlsx-using-python-pandas
# https://www.codegrepper.com/code-examples/r/pandas+to+excel+no+index