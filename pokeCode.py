
# First and foremost, it is needed to import all the necessary libraries to perform a data analisys.
# The Pandas library, powerful data manipulation and analysis tool and one of the most popular. It provides data structures and functions needed to efficiently work with structured data,
# such as tables and time series.
import pandas as pd
# Next one is seaborn library, which is a data visualization library based on matplotlib. Seaborn provides a high-level interface for creating attractive statistical graphics 
# and is particularly useful for creating informative and visually appealing plots.
import seaborn as sns
# Following, pyplot module from the matplotlib library, which is a widely used plotting library in Python. Matplotlib.pyplot provides a simple interface for creating various types 
# of plots charts, and graphs.
import matplotlib.pyplot as plt
# Moving forward the os module, which allows the interaction with the operating system. It provides functions for performing various tasks related to file and directory 
# manipulation, such as listing files, creating directories, and checking file existence.
import os
# In adittion, the combinations class from the itertools module. The itertools module in Python provides a set of fast, memory-efficient tools for working with iterators 
# (sequences of data). The combinations function, in particular, allows to generate all possible combinations of elements from an iterable (e.g., a list or a string) of a 
# specified length.
from itertools import combinations
# Finally, the Counter class from the collections module. The collections module provides various useful data structures beyond the built-in Python data types. 
# The Counter class is a specialized dictionary (subclass of the Python dict) that allows to efficiently count the occurrences of elements in an iterable (e.g., a list or a 
# string) and store them as key-value pairs.
from collections import Counter

# Firstly, is needed the creation of dataframe. "poke_dataframe" will be name for this project.
# pd.read_csv is a pandas function to read the data from a CSV file. In this example it is named 'pokemon_data.csv'.
# The argument for that function will be the complete path where the dataset is stored.This particular example has the data set stored on a local machine.
# The 'r' prefix before the string is called a raw string literal in Python. It is used to specify that the string should be treated as a raw string, often used with file paths to 
# avoid conflicts with backslashes, which are commonly used in file paths.

poke_dataframe = pd.read_csv(r'C:\Users\raul_\OneDrive\Documentos\PythonFolder\DataAnalysiswithJupyter\PokemonProject\pokemon_data.csv')

# Calling the dataframe will show the first 5 and last 5 rows from the dataset, the total number of rows and total number of columns
poke_dataframe

# Data cleaning and data exploration are similar steps performed at the begining of any data analysis project. The reason is to ensure that the collected it is accurate and ready for 
# analysis, including dealing with missing values, outlier detection, and data normalization.
# .describe() is a method provided by pandas to generate descriptive statistics of the dataframe.
poke_dataframe.describe()

# .duplicated() method returns a boolean Series indicating whether each row in the DataFrame is a duplicate of a previous row.
poke_dataframe.duplicated()

# To visualize the actual duplicated values the syntax will be changed to this for: df[df.duplicated].
poke_dataframe[poke_dataframe.duplicated]


# It was confirmed that there doesn't exist duplicated rows
# Following, it is neccessary to explore if there exists null values or not
# isnull() or isna() method indicate whether each element in the original data is null (True) or not null (False).
poke_dataframe.isnull()


# For this step it is not necessary to show the rows who has NaN vallues. A combination of isnull() and sum() will sum all the NaN values from the dataframe and provides a better view
# for those values.
poke_dataframe.isnull().sum()

# To get rid of the NaN values they will be filled with an empty character
# fillna() function is used to fill missing or NaN (Not a Number) values in a DataFrame or Series with specified values. This function allows handle missing data effectively
# either by replacing NaN values with a constant value or by applying various filling methods based on specific requirements.
# For this, the NaN values will be changed with '' (an empty value).
poke_dataframe['Type 2'].fillna('', inplace=True)


# To finish this first exploratory task is needed to determine the type of series of each column. 
# .dtypes attribute is a property in pandas that is used to get the data types of each column in a DataFrame
poke_dataframe.dtypes

# ### TASK 1 Results: 
# * 386 null values exists on the column "Type 2". This is due to not all the pokemon has 2 types. So, it is ok that there appear some NaN values on that column
# * All columns has an specific dtype, which will facilitate the data manipulation
# * No further exploratory commands where performed. Depending on the subsecuent task it will be executed specific exploratory analysis

# # QUESTION 1: How many Pokemons are One Type only?

# To solve this question, an  Type 2 are null, which will translate in pokemon with only type 1. 
# In the exploraty step it was observed that exists 386 rows with a null value. Now, using the syntax if df[df['Type 2'].isnull()] 
# Wraping the commands between square bracktes will show all the records resulting from it.
poke_dataframe[poke_dataframe['Type 2'].isnull()]

# ### ANSWER 1: How many Pokemons are one type only?
# There exists 386 pokemon with only one type 

# # QUESTION 2: What is the most and less repeated Type?

# In order to not repeat the same comment, it will be assume that the very first step for any type of querying it is necessary (or recommended at least) to check the dataframe 
# to visualize which information will be used and the column names to call the proper functions
poke_dataframe

# It is being asked to show what is the most and less repeated type, therefore, it will be considered only Type 1 column, as it is the "Principal" type of a pokemon, it determines
# wether it has a second type or no, the physical appareance mainly, so as the initial/proyected stats and the question asked for "Type", in singular.
#  .value_counts is used to count the occurrences of unique values in a pandas Series. As argument has the column name in which you want to count the occurences, for this question
# it sill be in Type 1 Column
poke_dataframe.value_counts('Type 1')

# ### ANSWER 2: What is the most and less repeated type?
# The most repeated type is Water, the less repeated type is Flying

# # QUESTION 3A: Which is the highest pokemon in HP from each type? (It could be one or two types)
# # QUESTION 3B: Which is the lowest pokemon in Speed from each type? (It could be one or two types)

# According to fandom wiki:
# 
#     It is known as a subtype or second type to a secondary type that a Pokémon species can develop. The subtype normally only affects the type of moves the Pokémon learns, but it also has a minimal impact on its physical appearance.
# 
# So, with that statement, it is interpreted that Type 2 or Secondary type will only affects the type of movements it can learn, the weaknesses and sometimes physical appearence. Therefore, the query will be done with type 1 column only. In adittion, the type 1 or principal type determines most of the time the proyected stats.
# 
# [Source](https://pokemon.fandom.com/es/wiki/Tipos_elementales)

# Check the dataframe to observe which information will be used, and how the filters will be performed
# .head() will return the firsts elements from the dataframe. The argument is always a number and it will determine how many elements will show
poke_dataframe.head(2)

# The first approach for this step will be grouping the dataframe by Type 1.
# .groupby function in pandas is a powerful tool for grouping and aggregating data in a DataFrame. It allows to group rows based on one or more columns and then apply various aggregate 
# functions to those groups to get summary statistics or perform analyses on the grouped data.
# It will be stored on a secondary dataframe that will be used for the next steps.
type_df = poke_dataframe.groupby('Type 1')

# .agg () function in pandas is used to perform multiple aggregation operations on the data grouped by a particular column or set of columns using the .groupby() method. It allows 
# to apply various aggregate functions simultaneously and obtain a customized summary of the grouped data.
# Using the new dataframe type_df the function .agg will be applied with the syntax of a dictionary.
# Selecting as first argument the Column, and secondly the operation. In this case, for the highest is needed a max() function.
type_df.agg({'HP': 'max',
            'Attack' : 'max',
            'Defense' : 'max',
            'Sp. Atk' : 'max',
            'Sp. Def' : 'max',
            'Speed' : 'max'})

# Ok, the past approach,as it was with a dictionary method it is not possible to ask for more information. The question recquires the name of the pokemon too. Therefore, a different
# approach has to be performed.
# Working with indexes might be helpful. In a pandas DataFrame, the index label refers to the unique identifier assigned to each row of the DataFrame. The index label provides a way 
# to access, reference, and identify individual rows based on this unique label.
# The idxmax() function in pandas is a method that is used to find the index label of the first occurrence of the maximum value in a Series. It is commonly applied to a pandas Series 
# to determine the index label where the maximum value occurs.
# Now, is is needed another secondary dataframe to store the indexes values. The data will be grouped by type 1, as type_df used previously. Adding ['HP'] means that the idxmax() 
# function will look into the 'HP' column. In other words, will bring the index of the row with the max value for HP column.
# Similar to idxmax() it exists idxmin(). As te question recquires to show the highest and lowest pokemon it will be used in parallel.
max_hp_indices = poke_dataframe.groupby('Type 1')['HP'].idxmax()
min_speed_indices = poke_dataframe.groupby('Type 1')['Speed'].idxmin()


# The results for the max_hp_indices are the following:
max_hp_indices

# The results for the min_hp_indices are the following:
min_speed_indices

# Awesome! Now, having the index label it can be access to all the values that it has. For such intention the .loc function is needed. 
# .loc attribute in pandas is used for label-based indexing, allowing to access rows and columns of a dataframe using their index labels and column names. 
# The syntax is df.loc[index, 'Column'].
# The result will be stored in another dataframe. This will have the type, the name, and the value of both highest and lowest value.
# To access multiple columns it has to be called as  a list ['Column 1', 'Column 2']
pokemon_max_hp_by_type = poke_dataframe.loc[max_hp_indices, ['Type 1', 'Name', 'HP']]
pokemon_min_speed_by_type = poke_dataframe.loc[min_speed_indices, ['Type 1', 'Name', 'Speed']]

# The results for the highest pokemon for HP, grouped by type are the following:
pokemon_max_hp_by_type

# The results for the lowest pokemon for Speed, grouped by type are the following:
pokemon_min_speed_by_type

# To make a beter visualization a merge between both dataframes is possible, due to the same size of them
# The pd.merge() function in pandas is used to combine two or more DataFrames based on a common column or index. It allows you to perform database-style joins, similar to SQL joins
# to merge the DataFrames horizontally.
# The suffix '_max' '_min' will be added to the column names to make the disctintion.
pokemon_stats_by_type = pd.merge(pokemon_max_hp_by_type, pokemon_min_speed_by_type, on='Type 1', suffixes=('_max', '_min'))

# Finally, the answer for the pokemons with the highest HP and lowest value of Speed are the following:
pokemon_stats_by_type

# ### ANSWER 3A: 
# * Bug:   Yanmega      
# * Dark:   Yveltal     
# * Dragon:    Kyurem     
# * Electric:    Zapdos      
# * Fairy:   Xerneas     
# * Fighting:  Hariyama     
# * Fire:     Entei     
# * Flying:   Noivern      
# * Ghost:  Drifblim     
# * Grass:    Gogoat     
# * Ground: Rhyperior     
# * Ice:   Walrein     
# * Normal:   Blissey     
# * Poison:       Muk     
# * Psychic: Wobbuffet     
# * Rock:   Aurorus     
# * Steel:   Jirachi     
# * Water:   Wailord     

# %% [markdown]
# ### ANSWER 3B:
# * Bug: Shuckle	
# * Dark:		SableyeMega Sableye	
# * Dragon:		Goomy	
# * Electric:		Mareep
# * Fairy:		Cleffa	
# * Fighting:	Makuhita	
# * Fire:		Slugma	
# * Flying:		Noibat	
# * Ghost:		Litwick	
# * Grass:	Ferroseed	
# * Ground:		Trapinch	
# * Ice:		Spheal	
# * Normal:		Munchlax	
# * Poison:	Grimer	
# * Psychic:		Solosis	
# * Rock:		Bonsly	
# * Steel:		Bronzor	
# * Water:	Slowpoke	

# # QUESTION 4A: Which are the top 5 pokemon in Sp. Def from primal type? 
# # QUESTION 4B: Which are the bottom 5 pokemon in Defense from primal type? 

# Print of the main dataframe
poke_dataframe

# As it is asking this time the top 5 and bottom 5 for it is needed to save a secondary dataframe with the characteristic that this time it will be sorted by the stat "Sp. Def".
# .sort_values() is a function used to sort the rows of a DataFrame based on the values of one or more columns. This function allows to rearrange the data in ascending 
# or descending order according to the specified column(s).
# by= can be a single column name (string) or a list of column names (list of strings) by which you want to sort the dataframe.
# ascending = This parameter determines whether the sorting should be in ascending or descending order. If True, the data will be sorted in ascending order; if False, it will be 
# sorted in descending order. The default is True.
sorted_sp_def = poke_dataframe.sort_values(by='Sp. Def', ascending=False)
sorted_defense = poke_dataframe.sort_values(by='Defense')

# Time to check the new dataframe for Sp. Def
sorted_sp_def.head(15)

# New dataframe for Defense
sorted_defense.head(15)

# Now, a mix of function will be performed.
# It was asked the top 5 for primal types: Fire, Water, Grass. So, a filter where type 1 = fire will be neededñ The syntax will be: df['Column'] condition (!=, ==, OR (|), AND(&))
# A head(5) will be added at the end to show the top 5 in Sp. Def
# It will be stored on a secondary dataframe, one for each type_ fire sp def, water sp. def and grass sp.def
# Finally, all 3 secondary fataframes will be concatenated on a single dataframe using the function pd. concat
# pd.concat()  is a function used to concatenate, or join together, two or more pandas objects (such as DataFrames or Series) It allows to combine data from different sources
# either vertically (along rows) or horizontally (along columns), based on the axis specified.
fire_sp_def = sorted_sp_def[sorted_sp_def['Type 1'] == "Fire"].head(5)
water_sp_def = sorted_sp_def[sorted_sp_def['Type 1'] == "Water"].head(5)
grass_sp_def = sorted_sp_def[sorted_sp_def['Type 1'] == "Grass"].head(5)
top_primal_sp_def = pd.concat([fire_sp_def,water_sp_def, grass_sp_def])

# Time to check the result
# As all the other information is not relevant, it will be called only Name, Type 1 and Sp. Def column
top_primal_sp_def[['Name', 'Type 1', 'Sp. Def']]

# Same workaround will be performed for the bottom 5 of defense
fire_defense = sorted_defense[sorted_defense['Type 1'] == "Fire"].head(5)
water_defense = sorted_defense[sorted_defense['Type 1'] == "Water"].head(5)
grass_defense = sorted_defense[sorted_defense['Type 1'] == "Grass"].head(5)
bottom_primal_defense = pd.concat([fire_defense, water_defense, grass_defense])

# Time to check the results
bottom_primal_defense[['Name', 'Type 1', 'Defense']]

# ### ANSWER 4A
# TOP 5 Fire pokemon for Sp. Defense
# 
# *   FIRE
#     * Ho-oh	154
#     * CharizardMega Charizard Y	Fire	115
#     * Flareon		110
#     * Heatran		106
#     * DarmanitanZen Mode		105
# *   WATER
#     * KyogrePrimal Kyogre		160
#     * Kyogre		140
#     * Mantine		140
#     * GyaradosMega Gyarados		130
#     * Milotic		125
# *   GRASS
#     * Virizion		129
#     * VenusaurMega Venusaur		120
#     * Ferrothorn		116
#     * Roserade		105
#     * AbomasnowMega Abomasnow		105

# ### ANSWER 4B
# 
# * FIRE
#     * Magby	Fire	37
#     * Slugma	Fire	40
#     * Fennekin	Fire	40
#     * Torchic	Fire	40
#     * Numel	Fire	40
# * WATER
#     * Carvanha	Water	20
#     * Feebas	Water	20
#     * Lotad	Water	30
#     * Wingull	Water	30
#     * Remoraid	Water	35
# * GRASS
#     * Sunkern	Grass	30
#     * Budew	Grass	35
#     * Treecko	Grass	35
#     * Bellsprout	Grass	35
#     * Hoppip	Grass	40

# # QUESTION 5: Which is the most and the less repeated combination of types?

#  Checking once again the main dataframe
poke_dataframe

# For this question, it is needed to count combination of types, so this time it will be looked up for pokemons with 2 types. In addition, to count the combination it is needed to
# merge both types into one column.
# Now, the easiest form to join the types in a singler column would be just to sum the types together, separated with a comma. For this to work both columns, Type 1 and Type 2 have to 
# strings (str).
# astype(str) is a method used to convert the elements of a pandas Series (or a column in a dataframe) to strings. It is commonly used to change the data type of the 
# elements in a series to the string data type.
poke_dataframe[['Type 1', 'Type 2']] = poke_dataframe[['Type 1', 'Type 2']].astype(str)
# Next step will be a for loop. for x (int) in df.index. This means that this for loop will go through all the numbers that appears in the index column. In this case from 0 - 799
# .loc is a powerful attribute used for label-based indexing, selection, and slicing of data in a DataFrame. It allows access specific rows and columns in a DataFrame using 
# labels (row and column names) instead of numeric indices.
# The label to use for the .loc function is the x declared on the foor loop.
for x in poke_dataframe.index:
    # For each row it's needed to check if it has or no a second type.
    # If the value is different than '' means that this pokemon has 2 types, so the new column will be Type 1, Type 2.
    if poke_dataframe.loc[x,'Type 2'] != '':
        poke_dataframe.loc[x,'Type'] = poke_dataframe.loc[x, 'Type 1'] + ', ' + poke_dataframe.loc[x, 'Type 2']
    # If the value is empty (= '') it means that it doesn't have a second type, so the column "Type" will be the same as Type 1.
    else:
         poke_dataframe.loc[x, 'Type'] = poke_dataframe.loc[x, 'Type 1']

# Check the results of the new type column.
poke_dataframe

# Excellent! Now it can be look through this column to search for the combination.
# Pokemon with only 1 type has to be discarded, as it is needed 2 type pokemon only. For that purpose, a secondary dataframe will be created.
two_types = poke_dataframe[poke_dataframe['Type 2'] != '']

# Time to check the new dataframe.
two_types

# Using the function .value_counts() on the Type column it will show how many combinations exists.
two_types['Type'].value_counts().head(5)

# Now for the less repeated
two_types.Type.value_counts().tail(5)

# ### ANSWER 5: Which is the most and the less repeated combination of types?
# Top 5 Most repeated types:
# * Normal, Flying
# * Grass, Poison
# * Bug, Flying
# * Bug, Posion
# * Ghost, Grass
# 
# Top 5 Less repeated types:
# * Fire, Water
# * Water, Steel
# * Psychic, Grass
# * Grass, Dragon
# * Bug, Water

# # QUESTION 6: How many Mega Pokemon exist?

# Take a look for the principal dataframe
poke_dataframe

# Number 3 and 719 will be useful data. To know a pokemon having a Mega evolution it will be sufficient to look for Mega in the name
# contains() is a method that allows you to check if a specific substring or pattern exists in each element of a pandas Series. It returns a boolean Series that indicates whether the 
# substring or pattern is present in each element or not.
# Before contains() it is needed to specify that the column is a str. 
# As the .contains() returns a boolean, using the df[df['column']] will return the data.
poke_dataframe[poke_dataframe['Name'].str.contains('Mega')]

# Excellent, now adding .count() function will return how many rows exist with "Mega" on the column name.
poke_dataframe[poke_dataframe['Name'].str.contains('Mega')].count()

# ### ANSWER 6: How many Mega Pokemon exist?
# There exists 49 Mega Pokemons

# # QUESTION 7: Which generation has most legendary pokemons?

# Calling the main dataframe
poke_dataframe

# It can be observed there exists a column named 'Legendary'. 
# A filter will be used , to check if the pokemon is Legendary or not.
# If the pokemon results "True" then it will be sumed the column 'Legendary'.
# The results will be shown per generation, so, the data will be grouped by the column 'Generation'
poke_dataframe.groupby('Generation').sum('Legendary' == True)['Legendary']

# ### ANSWER 7: Which generation has most legendary pokemons?
# The generation 3 has more Legendary pokemons

# # QUESTION 8: Which are the most equilibrated pokemons from each generation?

# Same operation to start, remembering our principal dataframe 
poke_dataframe

# Ok, translating the formula here it is what is needed to do:
# A sum of all the statistics and stored them in a new column Sum_Stats.
# With the column Sum_Stats now it can be calculated the population mean and stored them in another column.
# Finally, substitute all the values in the formula.
# In order to make things work, all the stats columns must be integers, so it will be used dtypes one more time.
poke_dataframe.dtypes

# %%
# Great, they are integers, so, the sum column will be as following
# axis=1 represents the columns axis. When an operation is performed with axis=1, it means the operation will be applied along the columns of the dataframe. 
# In this case, as it will be a sum of multiple columns it will be sent as a list
poke_dataframe['Sum_Stats'] = poke_dataframe[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)

# Checking the new column
poke_dataframe

# Perfect, now, to create the mean column it will be just the Sum_Stats column divided in 6, the number of stats each pokemon has.
poke_dataframe['Mean'] = poke_dataframe['Sum_Stats'] / 6


# Calling again the dataframe.
poke_dataframe

# Perfect, now, in order to 
# First, declaring the constants: exponential  = 2 and to represent the square root an exponential of 0.5 
# (NOTE: To make the exponential the syntax is: number**exponential
exp = 2
root = 0.5
# Having everything set up, the first element is (HP - Mean)^2
poke_dataframe['Standard_Deviation'] = ((((poke_dataframe['HP'] - poke_dataframe['Mean'])**exp) + 
 #Next one is (Attack - Mean)^2
 ((poke_dataframe['Attack'] - poke_dataframe['Mean'])**exp) + 
 #Next one is (Defense - Mean)^2
 ((poke_dataframe['Defense'] - poke_dataframe['Mean'])**exp) + 
 #Next one is (Sp. Atk - Mean)^2
 ((poke_dataframe['Sp. Atk'] - poke_dataframe['Mean'])**exp) + 
 #Next one is (Sp. Def - Mean)^2
 ((poke_dataframe['Sp. Def'] - poke_dataframe['Mean'])**exp) + 
 #The final element (Speed - Mean)^2
 # After sum all the previous elements it they will be divided in 6, the number of stats, and to the result an exponential of 0.5 will be applied to finally get the Standard Deviation
 # column.
 ((poke_dataframe['Speed'] - poke_dataframe['Mean'])**exp)) / 6)**root


# Checking the results.
poke_dataframe

# Now, as it is being asked to bring the most equilibrated pokemon from each generation 6 secondary dataframes will be created
first_gen = poke_dataframe[poke_dataframe['Generation'] == 1]
second_gen = poke_dataframe[poke_dataframe['Generation'] == 2]
third_gen = poke_dataframe[poke_dataframe['Generation'] == 3]
fourth_gen = poke_dataframe[poke_dataframe['Generation'] == 4]
fifth_gen = poke_dataframe[poke_dataframe['Generation'] == 5]
sixth_gen = poke_dataframe[poke_dataframe['Generation'] == 6]

# Now, the dataframe will be sorted using standard deviation as parameter to find, as the pokemon theory says, the pokemon with standard deviation closer to 0.
first_gen.sort_values(by='Standard_Deviation').head(3)

# Same for 2nd generation
second_gen.sort_values(by='Standard_Deviation').head(5)

# Moving forward to the 3rd generation
third_gen.sort_values(by='Standard_Deviation').head(7)

# Continuing with 4th generation.
fourth_gen.sort_values(by='Standard_Deviation').head(5)

# Now the 5th generation.
fifth_gen.sort_values(by='Standard_Deviation').head(5)

# And finally the 6th
sixth_gen.sort_values(by='Standard_Deviation').head(3)

# ### ANSWER 8: Which are the most equilibrated pokemons from each generation?
# * Gen 1: Mew, Mewtwo
# * Gen 2: Celebi, Tyrogue, Sunkern
# * Gen 3: Jirachi, Glalie, Snorunt, Castform, Spinda
# * Gen 4: Arceus, Shaymin Land Forme, Manaphy, Phione
# * Gen 5: Victine
# * Gen 6: Theres no pokemon with 0, the closest is Slurpuff with 5.06

# # FINAL TASK: Bring your top 6 Pokemon

# Now, personally, I will bring my 6 favourite pokemons:
# Charizard: The first pokemon I ever liked
# Greninja: His lore is one of the best of the anime, and it is my favorite character in Pokemon Unite game.
# Luxray: The best electric pokemon design.
# Gardevoir: Impossible to think on another psychic pokemon better than Gardevoir.
# Infernape: The first pokemon I got to level 100 so I have an special attachment to it.
# Hydrerigon: It was difficult to choose, but a 3 headed pokemon for a Dragon type is mighty.

# Perfect, now time to search for each pokemon. First Charizard.
poke_dataframe[poke_dataframe.Name == 'Charizard']
# Now look for Greninja
poke_dataframe[poke_dataframe.Name == 'Greninja']
# Time for Luxray
poke_dataframe[poke_dataframe.Name == 'Luxray']
# Next one on the lits: Gardevoir
poke_dataframe[poke_dataframe.Name == 'Gardevoir']
# Turn for Infernape
poke_dataframe[poke_dataframe.Name == 'Infernape']
# Final pokemon. Hydreigon
poke_dataframe[poke_dataframe.Name == 'Hydreigon']



