'''
This programs takes the dataset named as 'Energy Indicator.xls' and cleans the data.
The issues that I taken care in these dataset were:

  * It removes the header and footer of the dataset
  * It contains '...' when there is any missing data, that is replaced by numpy.NaN
  * Changes some name of the column to get better idea
  * Some country contains old names, which are replaced by their new names, like 
          "Republic of Korea" -> "South Korea",
          "United States of America" -> "United States",
          "United Kingdom of Great Britain and Northern Ireland" -> "United Kingdom",
          "China, Hong Kong Special Administrative Region" > "Hong Kong"
  * Some country name contains digits in it, the digits are removed
 
The file 'After-Cleaning-Energy-Indi.xls' contains the cleaned data
'''
import pandas as pd
import numpy as np
import string

def clean_data():
    raw = pd.ExcelFile('Energy Indicators.xls')
    energy = raw.parse(skiprows=17,skip_footer=(38))
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    # renaming the columns
    energy.rename(columns={'Unnamed: 1':'Country', 'Petajoules':'Energy Supply', 'Gigajoules': 'Energy Supply per Capita', '%':'% Renewable'},
                  inplace=True)
    
    # replacing '...' with np.NaN and converting the column so that the values is treated as numeric
    # DataFrame.apply() method helps to apply a function on all objects and returns the return type 
    # of that object
    energy[['Energy Supply','Energy Supply per Capita','% Renewable']] = energy[['Energy Supply','Energy Supply per Capita','% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    
    # converting the unit of Energy Supply column
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    
    # replacing the given country names
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong',
                                                   'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                                   'Republic of Korea':'South Korea',
                                                   'United States of America':'United States',
                                                   'Iran (Islamic Republic of)':'Iran'})
    
    # editing country names which has digits in it
    # also can use df['Country'].str.replace('\d+','')
    energy['Country'] = energy['Country'].str.rstrip(string.digits) 
    
    # editing country names which has (blah blah) with it
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    return energy
