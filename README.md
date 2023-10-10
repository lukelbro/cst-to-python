# cst to python

This code is for reading the files generated in CST Studio 2023 when exporting parametric Plot Data as ASCII. For example, after performing a parameter sweep and evaluating a 1D curve/line in the results template.


Example file format for input file:
```
#Parameters = {parameter=0.1}
#"Z / mm"	"E-Field (Es)_Abs (Z) [Real Part]"
#-------------------------------------------
-45.000000477954	9.5254719702912
-44.990000477954	9.5314968873529
-44.980000477954	9.5375420931393
-44.970000477954	9.5436018740679
#Parameters = {parameter=0.02; Mesh Pass=3}
#"Z / mm"	"E-Field (Es)_Abs (Z) (parameter=0.02) [Real Part]"
#-------------------------------------------------------
-45.000000477954	0.95254707781736
-44.990000477954	0.95314952183912
-44.980000477954	0.95375412586305
-44.970000477954	0.95436011587716
```

Usage:
```
parameters, arrays = cst_to_python(filename)
```
```
Returns:
tuple: A tuple containing two elements:
    - parameters (numpy.ndarray): An array of parameter values extracted from the file.
    - arrays (list of numpy.ndarray): A list of NumPy arrays containing data from each data block in the file.
```

Instillation: 

Seemed unnecessary. Copy and paste.

