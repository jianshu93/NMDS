import argparse
import pandas as pd
import numpy as np
import distance
from sklearn import manifold
import scipy.stats
import itertools
from sklearn.decomposition import PCA
import ecopy as ep
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams['font.sans-serif'] = "Helvetica"

matplotlib.rcParams['font.family'] = "sans-serif"

params={
    'axes.labelsize': '12',
    'xtick.labelsize':'11',
    'ytick.labelsize':'11',
    'lines.linewidth':1,
    'legend.fontsize': '12'
}
pylab.rcParams.update(params)

def executePCoA(data, distance_metric, groupfile):
    
    matrix = data.values
    n_features, n_samples = matrix.shape
    print (str(n_features) +' features, ' + str(n_samples) + ' samples')
    
    # compute distance
    if distance_metric == 'Jaccard':
        distance_matrix = distance.Jaccard(matrix.T)
    elif distance_metric == 'BrayCurtis':
        distance_matrix = distance.BrayCurtis(matrix.T)
    
    # execute nmds
    MDS = ep.MDS(distance_matrix, transform='monotone',naxes=3)
    stress=MDS.stress
    print(stress)
    scores=MDS.scores
    scores_df=pd.DataFrame(scores,index=data.columns)
    print(scores_df.head())


# General settings of the canvas
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if groupfile:
        group_names = []
        group2sample = {}
        for line in open(groupfile):
            sample,group = line.rstrip().split()
            if group in group2sample.keys():
                group2sample[group].append(sample)
            else:
                group2sample[group] = [sample]
                group_names.append(group)
        colors = itertools.cycle(["#56B4E9", "#E69F00", "#D55E00", 
              "#009E73", "#F0E442", "#0072B2", "#000000", 
              "#CC79A7","#BE5C2E","#3F725D","#2CE1C9",
              "#944F4A","#666666","#999999","#557DAD", "#CC7AA6", "#8A7C64",
                "#5E738F", "#F07D3D","#F5E369","#999999", "#B3DE8C",
                "#652926", "#C2CCD6","#8569D5", "#D14285","#4AF2A1",
                "#C7BAA6", "#F7CCAD","#599861",
                "#FCFAF0","#AD6F3B","black",
                "#5F7FC7","#F5B369","#DA5724",
                "#508578","#CD9BCD"])
        markers = itertools.cycle(['o','^','s','H','p','D','<','8','>','d','h','v'])
        for i,current_group in enumerate(group_names):
            if len(group2sample[current_group]) == 0:
                continue
            ax.scatter(scores_df.loc[group2sample[current_group],0],
                       scores_df.loc[group2sample[current_group],1], scores_df.loc[group2sample[current_group],2], s=45,
                       marker=next(markers), color=next(colors), label=current_group)
        plt.legend(bbox_to_anchor=(1.02, 0, 1., 1.05),loc=3, ncol=1, borderaxespad=0.) # bbox_to_anchor=(0., 1.01, 1., 1.01),
    else:
        for i,sample_name in enumerate(data.columns):
            ax.annotate(sample_name, xy=(scores[i,0],scores[i,1],scores[i,2]), textcoords='offset points', color='k', fontsize=13)
        ax.scatter(scores[:,0], scores[:,1],scores[:,2], c='k', s=50)
    ax.set_xlabel('NMDS1')
    ax.set_ylabel('NMDS2')
    ax.set_zlabel('NMDS3')
    stress_label='3D stress:'+ str(round(stress,3))
    ax.annotate(stress_label, xy=(0, 0), xytext=(0,0),textcoords='offset points', ha='center', color='k', fontsize=11, rotation=0)

    ### comstmize figure style
    plt.tick_params(direction='in',axis='both', which='major', labelsize=11)
    fig.tight_layout()
    plt.show()
    plt.close()
    fig.savefig('nmds_result_plot_3D11.pdf')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "-f", "--file", action="store", dest="data_file", help="matrix data file. rows are variables, columns are samples.")
    parser.add_argument( "-d", "--distance_metric", action="store", dest="dist", choices=['Jaccard', 'BrayCurtis'], help="choose distance metric used for PCoA.")
    parser.add_argument( "-g", "--grouping_file", action="store", dest="group_file", default=None, help="plot samples by same colors and markers when they belong to the same group. Please indicate Tab-separated 'Samples vs. Group file' ( first columns are sample names, second columns are group names ).")
    args = parser.parse_args()
    
    if args.data_file == None:
        print ("ERROR: requires options")
        parser.print_help()
        quit()
    
    datafile = args.data_file
    distance_metric = args.dist
    groupfile = args.group_file
    
    data = pd.read_table(datafile,index_col=0)
    executePCoA(data, distance_metric, groupfile)
    print ('done.')

