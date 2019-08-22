# -*- coding: utf-8 -*-

from openpyxl import load_workbook
import re;

book = load_workbook('Dados.xlsx')
sheet = book['Respostas ao formulário 1']

d = sheet.dimensions
linhas = len(sheet[d])

for i in range(2, linhas+1):
	name = re.sub(' ', '%20', sheet['B'+str(i)].value)
	sheet['E'+ str(i)] = 'https://chart.googleapis.com/chart?&cht=qr&chs=400x400&chld=L%7C1&chl=' + name


book.save('Dados.xlsx')