#--------------------------------------------------------------------------------------------
# esempio di utilizzo

file = CSVTimeSeriesFile(name='data.csv')
data = file.get_data()
avg = compute_avg_monthly_difference(data, "1949", "1951")
print(avg)