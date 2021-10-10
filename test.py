from src import *

some_data = gettingData()
check = input("Choose:")
if check:
    curName = input(" Currency name:")
    scrapper = getRequest(curName)
    for i in scrapper:
        print(i)
