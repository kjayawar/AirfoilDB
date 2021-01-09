import os
from glob import glob
airfoils = glob('./airfoils/*.dat')
template = open('re_sweep_template.txt').read()

def gen_commands(airfoil):
	with open('commands.txt', 'w') as f:
		f.write(template.format(airfoil))
	os.system('xfoil.exe <commands.txt > {}.re_sweep'.format(airfoil))

for airfoil in airfoils:
	gen_commands(airfoil)