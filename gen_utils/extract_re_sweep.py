import re
import numpy as np
from glob import glob
import pandas as pd


file_list = glob('./polar_dumps/*.extract')
re_list = [50000, 60000, 70000, 80000, 90000, 100000, 125000, 150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000, 425000, 450000, 475000, 500000, 525000, 550000, 575000, 600000, 625000, 650000, 675000, 700000, 725000, 750000, 775000, 800000, 825000, 850000, 875000, 900000, 925000, 950000, 975000, 1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000, 1550000, 1600000, 1650000, 1700000, 1750000, 1800000, 1850000, 1900000, 1950000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000, 2800000, 2900000, 3000000]


def extract_single_re_data(re_num, re_data):
	if 'Convergence failed' in re_data:
		return re_num, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan
	else:
		xtr_upp, xtr_bot = map(float, re.findall('transition at x/c =.*(\d\.\d+)', re_data))
		cl = float(re.findall('CL =\s*(-?\d\.\d+)', re_data)[0])
		cm = float(re.findall('Cm =\s*(-?\d\.\d+)', re_data)[0])
		cd = float(re.findall('CD =\s*(-?\d\.\d+)', re_data)[0])
		cdf = float(re.findall('CDf =\s*(-?\d\.\d+)', re_data)[0])
		cdp = float(re.findall('CDp =\s*(-?\d\.\d+)', re_data)[0])
		return re_num, cl, cm, cd, cdf, cdp, xtr_upp, xtr_bot


def extract_single_file(filename):
	text = open(filename).read()
	splited = text.split('--')[1:]
	assert len(splited)==len(re_list)
	return np.array([extract_single_re_data(re_list[re_index], re_data) for re_index, re_data in enumerate(splited)])

def clean_np_matrix(np_matrix):
	return np_matrix[~np.isnan(np_matrix).any(axis=1)]

def get_cd_data(np_matrix):
	return np_matrix[:,3]

def get_min_cd_values(np_matrix):
	return np_matrix[np.nanargmin(np_matrix[:,3])]

def get_airfoil_name(filename):
	return filename.replace('.re_sweep.extract', '').replace('./polar_dumps\\', '')

df_summary = pd.DataFrame(columns=['airfoil', 're_num', 'cl', 'cm', 'cd', 'cdf', 'cdp', 'xtr_upp', 'xtr_bot'])
df_cd = pd.DataFrame(columns=['re_num'])
df_cd['re_num'] = re_list


def process_single_file(filename):
	airfoil_name = get_airfoil_name(filename)
	np_matrix= extract_single_file(filename)
	row_data = [airfoil_name] + list(get_min_cd_values(np_matrix))

	cd_series = get_cd_data(np_matrix)

	df_summary.loc[len(df_summary)] = row_data
	df_cd[airfoil_name] = cd_series

for i, filename in enumerate(file_list):
	try:
		process_single_file(filename)
	except:
		print i, filename


# >>> writer = pd.ExcelWriter('airfoil_db', engine='xlsxwriter')
# >>> df_summary.to_excel(writer, sheet_name='cd_summary')
# >>> df_cd.to_excel(writer, sheet_name='cd_series')
# >>> writer.save()