from glob import glob
import re

file_list = glob('gdes_dumps/*.output')


def extract_details(file_name):
	text = open(file_name).read()
	file_name = file_name.replace('.output', '').replace('gdes_dumps\\', '')
	print file_name,
	thickness_line = re.findall('Max thickness =.*', text)[0]
	camber_line    = re.findall('Max camber    =.*', text)[0]
	le_line        = re.findall('New LE radius = .*', text)

	max_tc, x_tc = map(float, re.findall('\d.\d+', thickness_line))
	max_camb, x_camb = map(float, re.findall('\d.\d+', camber_line))
	le_radius = float(re.findall('\d.\d+', le_line[0])[0])
	return max_tc, x_tc, max_camb, x_camb, le_radius

for filename in file_list:
	print extract_details(filename)