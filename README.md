# Neuromint

Neuromint is a project meant to serve as a simple library to be used for analysis and expirimentation in neuroscientific contexts. 

### Wave Class
The wave_class function currently takes several arguments: data, wave_lengths, velocities, frequencies, return_extreme, and return_csv. It is used to analyze EEG data metrics and classify wavelengths accordingly. 

- data
data is a required argument that where a dataframe is passed and serves as a store of information used to define the elements of the EEG data. the arguments wave_lengths, velocities, and frequencies should all be columns of this data frame. If one of these three arguments is undefined, the wave_class function will determine the ungiven values by using the wave length equation λ = v/f.

- return_extreme
The return_extreme argument needs to be filled with a boolean value. If true, the wave_class function will return the lowest and highest frequency waves (quantile(0.1), quantile(0.9)).

- return_csv
The return_csv argument needs to be filled with a boolean value. If true, the wave_class fucntion will return a .csv file with all of the analyzed waves. An Example of this can be found in this repository under the wave_classes.csv file. **Please note:** the wave_classes.csv file is NOT real neuroscientific data, but simply filled with randomized values that were input into the wave_class function. 
