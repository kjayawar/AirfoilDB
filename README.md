# AirfoilDB

AirfoilDB is an excel spreadsheet containing airfoil geometric data, Re data, and performance data on a selected subset of [UIUC airfoil database](https://m-selig.ae.illinois.edu/ads.html) airfoils. 

Airfoils selected were from very well-known designers such as Wortmann, Eppler, Althaus, Drela, Hepperle, and Selig.


## Usage

### "Summary" Sheet contains:

- __Basic airfoil details__
![alt text](https://github.com/kjayawar/AirfoilDB/blob/main/geometric_info.png?raw=true)

- __Effect on RE on airfoil drag at 0 alpha.__                                          
__RE@cd=0.01__ for example shows the Reynolds number at which cd reaches __0.01__.            
![alt text](https://github.com/kjayawar/AirfoilDB/blob/main/RE_info.png?raw=true)

- __Performance Data.__                                                                       
These values refer to alfa 0 at minimum cd Reynolds number.                       
__cd*sqrt(RE)__ is used as a Reynolds normalized drag coefficient. 
![alt text](https://github.com/kjayawar/AirfoilDB/blob/main/performance_info.png?raw=true)

### "PLOT" Sheet:

- PLOT sheet is used to observe the behavior of the airfoil throughout the Reynolds number range between 0.5e5 to 3.0e6. When the sheet is selected a macro will plot the graph for filtered airfoils in the "Summary" sheet. 
![alt text](https://github.com/kjayawar/AirfoilDB/blob/main/re_cd.png?raw=true)
 

## Contributing
Pull requests are welcome.   
The method I've used to extract these details are listed in the gen_utils folder with a [dev guide](https://github.com/kjayawar/AirfoilDB/blob/main/gen_utils/dev_doc.md).

## License
[MIT](https://choosealicense.com/licenses/mit/)
