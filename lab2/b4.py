date_in_MM_DD_YYYY = input("Date in MM/DD/YYYY format: ")
date_in_DD_MM_YYYY = f'{date_in_MM_DD_YYYY[3:5]}/{date_in_MM_DD_YYYY[0:2]}/{date_in_MM_DD_YYYY[6:10]}'
print(f'Date in DD/MM/YYYY format: {date_in_DD_MM_YYYY}')
