# na_l3_ecoregions

Identify l3 ecoregions in North America using Python

## Data

Ecoregions dataset from:
https://gaftp.epa.gov/EPADataCommons/ORD/Ecoregions/cec_na/NA_CEC_Eco_Level3.zip

## Installation

clone to python path

e.g.
```
> cd /usr/lib/python3/dist-packages
> git clone https://github.com/rogerlew/na_l3_ecoregions/
```

## Usage

```python
> import na_l3_ecoregions
> na_l3_ecoregions.identify(-117, 47)
{'60': {'NA_L3CODE (String)': '10.1.2',
  'NA_L3NAME (String)': 'Columbia Plateau',
  'NA_L2CODE (String)': 10.1,
  'NA_L2NAME (String)': 'COLD DESERTS',
  'NA_L1CODE (String)': 10.0,
  'NA_L1NAME (String)': 'NORTH AMERICAN DESERTS',
  'NA_L3KEY (String)': '10.1.2  Columbia Plateau',
  'NA_L2KEY (String)': '10.1  COLD DESERTS',
  'NA_L1KEY (String)': '10  NORTH AMERICAN DESERTS',
  'Shape_Leng (Real)': 2889543.18764,
  'Shape_Area (Real)': 81830013715.6}}
```

