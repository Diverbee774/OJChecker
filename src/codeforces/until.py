import requests
import time
from openpyxl import load_workbook
from urllib.parse import quote

def get_data():
    url = './config/codeforces.xlsx'
    workbook = load_workbook(url)
    sheets = workbook.get_sheet_names()
    bookSheet = workbook.get_sheet_by_name(sheets[0])

    rows = bookSheet.rows
    first = True

    data = {}

    for row in rows:

        if row[0].value is None:
            break
        if first:
            first = False
            continue
        who = row[0].value
        user = row[1].value
        data[who] = str(user)
        #print(who, user)

    return data