# -*- coding: utf-8 -*-
"""
@author: snaidove
"""
# pca analysis of fungal community
import matplotlib
# Say, "the default sans-serif font is Helvetica"
matplotlib.rcParams['font.sans-serif'] = "Helvetica"
# Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "sans-serif"

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
params={
    'axes.labelsize': '14',
    'xtick.labelsize':'14',
    'ytick.labelsize':'14',
    'lines.linewidth':1,
    'legend.fontsize': '12'
}
pylab.rcParams.update(params)

import pandas as pd
import numpy as np
import skbio
from scipy.spatial import distance
from plotnine import *
from plotnine.data import *

# read dataframe and check
fungal_otu = pd.read_csv('ITS_OTU_table.csv',header=0,index_col=0)
fungal_otu_transpose=fungal_otu.T
group=pd.read_csv('group1.csv',header=0,index_col=0)
print(fungal_otu_transpose.head())
Ar_dist = distance.squareform(distance.pdist(fungal_otu_transpose, metric="braycurtis")) # (n x n) distance measure
DM_dist = skbio.stats.distance.DistanceMatrix(Ar_dist, ids=fungal_otu_transpose.index)
PCoA_results = skbio.stats.ordination.pcoa(DM_dist)
propotion=PCoA_results.proportion_explained
print(PCoA_results.samples.head())
PCoA_results.write('fungal_otu_pcoa.csv')
samples_fungal=PCoA_results.samples[['PC1','PC2','PC3','PC4']]
samples_fungal['PC4']=group
group_ordering = ['P210','P270','P570','P790','P930','P1060','P1260', 'P1500','P1800','P2500','PQ2500','P3550']
samples_fungal['PC4']=samples_fungal['PC4'].astype('category', categories=group_ordering, ordered=True)

p1 = (ggplot(samples_fungal, aes(x='PC1', y='PC2',color='PC4'))+
	geom_point(size=3.2, shape='^')+ theme_matplotlib()+
	scale_color_manual(values=['#CBD588', '#5F7FC7', '#F5B369','#DA5724',
   '#508578', '#CD9BCD','#AD6F3B', '#673770','#C84248', '#652926',
   '#D14285','#666666','#9BE42C','#EDEDEB','#BA82BD','#3078B3',
   '#C77A30','#7AAB8F','#7A8C73','#C7BAA6','#E3D62E','#DEA196',
   '#879EA6','black', '#8A7C64', '#599861','#8569D5','#D45E1A',
   "#3D6654",'#9C8A1C','#5E738F','#F07D3D','#F5E369','#999999',
   '#FC4F61','#A6732B','#F29999'])+
	labs(color='',x='PCoA1 '+str("%.2f%%" % (propotion[0]*100)),y='PCoA2 '+str("%.2f%%" % (propotion[1]*100)))+
	theme(axis_text=element_text(size=14,color='black',family='sans-serif'),axis_title=element_text(size=14,color='black',family='sans-serif'),legend_text= element_text(size=12,color='black',family='sans-serif'))+
	theme(legend_position=(0.7,0.73),legend_background=element_rect(size=0.5, linetype='solid', colour='#BFBFBF'))+
	guides(color=guide_legend(nrow=6),shape=guide_legend(nrow=6))
	)
p1.save('fungal_pcoa.pdf',width=6, height=5.5)
