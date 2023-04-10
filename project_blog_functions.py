import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_heatmap(df):
    '''
    INPUT:
    df - the clean survey dataframe
    
    The function will create a salary heatmap with Years of Programming experience on the y axis and Company Type on the x axis.
    '''
    heatmap_df = df.groupby(['YearsProgram','CompanyType']).mean().Salary.unstack()
    
    reordercolumnslist = [
    'Publicly-traded corporation',
    'Venture-funded startup',
    'Non-profit/non-governmental organization or private school/university',
    'Something else',
    'Government agency or public school/university',
    'Privately-held limited company, not in startup mode',
      'Pre-series A startup',
     'Sole proprietorship or partnership, not in startup mode',
    "I don't know",
    'I prefer not to answer',
    'State-owned company',
]
    
    reorderindexlist = [
    'Less than a year',
    '1 to 2 years',
    '2 to 3 years',
    '3 to 4 years',
    '4 to 5 years',
    '5 to 6 years',
    '6 to 7 years',
    '7 to 8 years',
    '8 to 9 years',
    '9 to 10 years',
    '10 to 11 years',
    '11 to 12 years',
    '12 to 13 years',
    '13 to 14 years',
    '14 to 15 years',
    '15 to 16 years',
    '16 to 17 years',
    '17 to 18 years',
    '18 to 19 years',
    '19 to 20 years',
    '20 or more years'
]
    heatmap_df = heatmap_df.reindex(reorderindexlist)
    
    heatmap_df.columns = reordercolumnslist
    
    sns.heatmap(heatmap_df, cmap=sns.cubehelix_palette(as_cmap=True))
    plt.ylabel('Years of Programming', fontsize=11)
    plt.xlabel('Company Type', fontsize=11)
    plt.title('How does programming experience affect pay at different types of companies?', fontsize=13);