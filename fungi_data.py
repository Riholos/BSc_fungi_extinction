import pandas as pd

# Turning all the Red List files of different countries to different dataframes
df_GER=pd.DataFrame(pd.read_excel('redlist_fungi_GER.xlsx'))
df_DEN=pd.DataFrame(pd.read_excel('Danish_RL_2019.xlsx'))
df_SWE=pd.DataFrame(pd.read_csv('Swedish Red List 2015.csv'))
df_CZ=pd.DataFrame(pd.read_excel('Czech_RL.xlsx'))

extinct_species=[]

# Adding all the extinct species in dataframes to a list
extinct_species = (df_DEN[df_DEN['redlistCategory.category'] == 'RE']['speciesInformation.scientificName'].tolist())+(df_GER[df_GER['Red list catergorie Germany'] == '0']['species name'].tolist())+(df_GER[df_GER['Red list catergorie Austria'] == '0']['species name'].tolist())+(df_SWE[df_SWE['RLCateg'] == 'RE']['TaxonName'].tolist())+(df_CZ[df_CZ['kategorie ohrožení/category of threat'] == '?EX']['TaxonName'].tolist())

# Finding out if a species has gone extinct in more than one country
for species in extinct_species:
    if_double = extinct_species.count(species)
    if if_double >= 2:
        print(species)
# Turning the 'extinct_species' list to a dataframe and exporting it as a '.csv' file
extinct_species_df = pd.DataFrame({'ExtinctSpecies': extinct_species})
extinct_species_df.to_csv('Europe_RE.csv', index=False)
