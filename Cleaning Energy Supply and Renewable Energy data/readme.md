The file '*Energy Indicators.xls*' contains the raw data, which is a list of indicators of energy supply and renewable electricity production 
from the United Nations for the year 2013, and should be put into a `DataFrame` with the variable name of energy. It contains some mess, the
python code I have written filters this dataset and creat a processable data stored in a `pandas.DataFrame` object. 

The issues I have noted and fixed are as follows:
+ The column names are not informative about the data it contains, I have changed the column names as follows:
    `Unnamed: 1` to `Country`, changed `Petajoules` to `Energy Supply`, changed `Gigajoules` to `Energy Supply per Capita`, changed `%` to 
    `% Renewable`. It better reflects the information each column stores.
    
+ Some country names were too long and will takes lots of space to store(those are repeated multiple times), I have changed those to shorter name. That represents the same 
country but takes less amount of space in memory. Eg: "Republic of Korea" replaced by "South Korea", "United States of America" is replaced by
"United States", "United Kingdom of Great Britain and Northern Ireland" is replaced by "United Kingdom", "China, Hong Kong Special Administrative
Region" is replaced by "Hong Kong".

+ Missing datums were containg `...`, those are replaced by `numpy.NaN`

+ Some country names were containg digits in it, like `Switzerland17`. The digits are removed from those country names. 

