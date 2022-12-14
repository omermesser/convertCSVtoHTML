import csv, os
current_path = os.path.dirname(__file__)
file_name = input('Enter file name (with extension) -> name.csv\n')
with open(f'{current_path}\\{file_name}', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open(f'{current_path}\\result.html', 'w') as html_file:
        #writing the start of the HTML
        html_file.write('''<style>
	td{
		border: 1px black solid;
	}
</style>
<table style="border-collapse:collapse">
''')
        #writing the table
        for thead in next(csv_reader):
            html_file.write(f'\t<th>{thead}</th>\n')
        for row in csv_reader:
            html_file.write('\t<tr>\n')
            for data in row:
                html_file.write(f'\t\t<td>{data}</td>\n')
            html_file.write('\t</tr>\n')
        html_file.write('</table>')
print(f'Done')