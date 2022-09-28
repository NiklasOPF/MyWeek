# week-tracker
This tool is complementary to the dreamlinign template outlined here: https://niklasopf.github.io/
It shifts focus away form the achievement of the long-term overarching goals that you are progressing towards adn redirects it to the small battles we all fight on a daily basis. By tracking your progression along a set of KPIs (Key Performance Indicators), it allows you to: 
* Monitor your progress toward goals that you have set for yourself
* Prioritize more effectively when it comes to where you spend your time

# 1 Initial setup
Whilst the wekly usage of the tool is extremely lightweight and fast, it does require some initial configuration before it can trck your progress.
## 1.1. Defining your goals
Keeping track of and maintaining your high-level objectives is most easily done with the dreamlining template. Once you have a clear view of the goaols you would like to pursue, you need to define KPIs for those goals. I would recomend to track something between 5-10 KPIs per week. A good KPI is:
* Agnostic to external effects
* Easy to measure
* Correlated to the long-term resuts you want to attain

## 1.2. Defining utility functions
The tool uses utility fucntions to score your progress throughout a week. Utility functions need to be defined for the different KPIs that you have specified. 
* The list of available utility functions can be found here: https://niklasopf.atlassian.net/l/cp/Upn7Fx1t

## 1.3. Formating the input file
Once the KPIs and utility functions have been decided on, it is time to specify the input file. The input file has the followign appearance:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/44125052/192748814-67f47138-5f51-495d-ae2e-68e6d2bad263.png">

Note that there are several tabs in the file. 
* Records specifies your performance on a given week by means of the KPIs
* Comments allows you to comment on a particular result. This is not leveraged for any claculations but may be insightful whilst looking back on past record entries
* UtilityFunctions specifies the utility funciton that goes together with a certain KPI
* PerformanceReport contains the output from the tool with all the copring included

### 1.3.1. Specifying the Records tab
The records tab has the following appearance: 
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/44125052/192759235-adc20bfb-b8d2-4ab0-9038-a578a339171d.png">
* The header has the form "Category - KPI"
  * The Category is used to group several KPIs, which involve similar characteristics or that are related to the same goal, together
  * The KPI uniquely identifies the record type
* The entries are numbers
* Attributes that have ben decomissioned over time should not be removed from the file. Instead they should be filled with "-"

### 1.3.2. Specifying the Comments tab
The Comments tab has the following appearance: 
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/44125052/192759634-efe5c8c4-8bd6-42c3-b4af-ac9dea7fea2c.png">


### 1.3.3. Specifying the Configuration tab
The Configuration tab has the following appearance: 
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/44125052/192759688-8c5d3e22-c8a7-4da2-883b-e8f4b7c9a1af.png">


### 1.3.4. Specifying the PerformanceReport tab
The PerformanceReport tab is configured automatically by the tool


# 2. Running the tool
The tool is run by performing the following steps in sequence: 
1. Placing the input file in the "Input" folder
2. Specifying the input parameters at the beginning of the "main.py" script
3. Running the "main.py" script

The result will then be saved to the "Output" folder




