import pandas as pd
df = pd.read_excel('airfoil_db.xlsx', sheet_name = "cd_series")

def find_re_with_given_cd(s_airfoil, cd):
	return df['re_num'].iloc[abs(s_airfoil - cd).idxmin()]

for airfoil in df.columns[1:]:
	s_airfoil = df[airfoil]
	print airfoil, find_re_with_given_cd(s_airfoil, 0.01), find_re_with_given_cd(s_airfoil, 0.02), find_re_with_given_cd(s_airfoil, s_airfoil.min()*3.0)
