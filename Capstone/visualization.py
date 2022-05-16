import numpy as np
import matplotlib.pyplot as plt

def show_histogram(df, col_name):
    plt.hist(df[col_name])
    plt.xticks(rotation=90)
    plt.title(col_name)
    plt.show()

def compare_histogram(df1, df2, col_name, df1_name = 'males', df2_name = 'females'):
    plt.hist(df1[col_name], label = df1_name, histtype = "step", density = True)
    plt.hist(df2[col_name], label = df2_name, histtype = "step", density = True)
    plt.xticks(rotation=90)
    plt.legend()
    plt.title(col_name)
    plt.show()

def show_correlation_matrix(df, size = None):
    
    if size != None:
        prev_size = plt.rcParams['figure.figsize']
        plt.rcParams['figure.figsize'] = size
    
    plt.matshow(df.corr())
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=90)
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
    plt.colorbar()
    
    if size != None:
        plt.rcParams['figure.figsize'] = prev_size

def plot_dictionaries(list_dict, title='chart plot', labels = []):

    fig, axes = plt.subplots(1, len(list_dict), figsize=(15,5))
    fig.suptitle(title)
        
    for i,ax in enumerate(axes):
        d = list_dict[i]
        ax.bar(range(len(d)), list(d.values()), align='center')
        ax.set_title(labels[i])
        if labels[i] != 'Chi2':
            ax.set_yticks(np.arange(0, 0.04, 0.01))
        else:
            ax.set_yticks(np.arange(0, 1, 0.1))
        ax.set_xticks(range(len(d.keys())))
        ax.set_xticklabels(d.keys(), rotation=90)

def plot_horizontal_dictionaries(list_dict, title='chart plot', labels = [], errors = None):

    fig, axes = plt.subplots(1, len(list_dict), figsize=(20,5))
    fig.suptitle(title)
    fig.tight_layout()
        
    for i,ax in enumerate(axes):
        d = list_dict[i]

        if errors == True:
            ax.barh(range(len(d)), [d[k][0] for k in d.keys()], align='center', xerr=[d[k][1] for k in d.keys()])
        else:
            ax.barh(range(len(d)), list(d.values()), align='center')
            
        ax.set_title(labels[i])
        ax.set_xticks(np.arange(-0.2, 0.85, 0.1))
        ax.set_yticks(range(len(d.keys())))
        ax.set_yticklabels([w.replace('_', ' ') for w in d.keys()])
        
    fig.subplots_adjust(wspace=0.55)