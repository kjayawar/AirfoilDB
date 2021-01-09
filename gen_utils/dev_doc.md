# Workflow documentation on creating additional airfoil data

This document outlines the process I've used to gather additional information in bulk. 


## Process

### Generating Geometric data

In this particular example, the airfoils are stored in a separate folder called "Airfoils"
Relevent GDES commands are stored in the "gdes_template.txt" file. 

```python
import os
from glob import glob
airfoils = glob('./airfoils/*.dat')
template = open('gdes_template.txt').read()

def gen_commands(airfoil):
	with open('commands.txt', 'w') as f:
		f.write(template.format(airfoil))
	os.system('xfoil.exe <commands.txt > {}.output'.format(airfoil))

for airfoil in airfoils:
	gen_commands(airfoil)
```

This will save newly paneled and refined airfoils in the airfoils folder and geometric information in the .output files. One example is shown below

```
Enter approx. new/old LE radius scaling ratio   r>  
Enter blending distance/c from LE   r>   
 Max thickness =     0.062376  at x =   0.250
 Max camber    =     0.020116  at x =   0.327

 New LE radius = 0.00188

.GDES   c>  
```
These data for each file could then be moved to a separate folder ('gdes_dumps') for easy processing. With Regex, the info could easily be extracted. One example output file was left out for clarity

```bash
mv ./airfoils/*.output ../gdes_dumps
cd ../
python extract_gdes_data.py
```

### Generating Performance data

Following almost the same process as before, Reynolds number sweep can be performed for zero alfa. The template file is re_template.txt

```python
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
```

While the Re_sweep there were and will be some mishaps. These files could easily be verified by tailing the last line to see if it's properly terminated. If not these could be removed.

```bash
find -type f -exec bash -c "eval tail -1 {} > {}.verify " \;
grep -L 'XFOIL' *.verify | xargs rm
```

Then the last iteration for each RE can be extracted by

```bash
find -type f -exec bash -c "eval grep OPERv -B 7 {} > {}.extract" \;
```
As an additional benefit, grep -B puts -- on each find which could easily be used as a delimiter in the next step.

Example would be 
```
--
 Side 1 forced transition at x/c =  1.0000   81
 Side 2 forced transition at x/c =  1.0000   81

   3   rms: 0.1375E-05   max: -.8526E-05   D at   86  2
       a =  0.000      CL =  0.1248
      Cm = -0.0244     CD =  0.01286   =>   CDf =  0.00858    CDp =  0.00428

.OPERv   c>  
.OPERv   c>  
--
```

These data then could be directly used generating an excel file with the desired information

```bash
python -i extract_re_sweep.py
```

### Generating RE_Crit data. 

Once the airfoil_db spreadsheet is generated it can be used to further process and get the lower bound of RE data.

```bash
python critical_re.py
```
