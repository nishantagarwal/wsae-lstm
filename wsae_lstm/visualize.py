import faulthandler; faulthandler.enable()
# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
import copy
import pickle

import sys
sys.path.append('../')  

##Visualization/plotting imports
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

import pywt
from pywt import wavedec, waverec
from scipy import signal
from statsmodels.robust import mad

# Internal Imports
from wsae_lstm.utils import dictmap_load,pickle_load,pickle_save
from wsae_lstm.models.wavelet import denoise_periods

dict_dataframes_index=pickle_load(path_filename="../data/interim/cdii_tvt_split.pickle")
ddi_scaled=pickle_load(path_filename="../data/interim/cdii_tvt_split_scaled.pickle")
ddi_denoised=pickle_load(path_filename="../data/interim/cdii_tvt_split_scaled_denoised.pickle")

def tvt_display(ddi_denoised):
    for key, index_name in enumerate(ddi_denoised):
        fpath = "../reports"
        pdf = PdfPages('{}/{} tvt split scale denoise visual.pdf'.format(fpath,index_name))
        for index,value in enumerate(dict_dataframes_index[index_name]): 
            fig, axes= plt.subplots(1, 3,constrained_layout=False,figsize=(12,4))
            fig.suptitle('{}, period: {}'.format(index_name,value))
            fig.subplots_adjust(top=0.88)
            
            axes[0].set_title('Train')
            axes[0].plot(ddi_denoised[index_name][value][1],label='denoised train data')
            #axes[0].plot(ddi_scaled[index_name][value][1].values,alpha=0.5, label='train data')

            axes[1].set_title('Validate')
            axes[1].plot(ddi_denoised[index_name][value][2],label='denoised validate data')
            #axes[1].plot(ddi_scaled[index_name][value][2].values,alpha=0.5,label='validate data')

            axes[2].set_title('Test')
            axes[2].plot(ddi_denoised[index_name][value][3],label='denoised test data')
            #axes[2].plot(ddi_scaled[index_name][value][3].values,alpha=0.5,label='test data')
            
#             handles, labels = plt.gca().get_legend_handles_labels()
#             by_label = OrderedDict(zip(labels, handles))
#             plt.legend(by_label.values(), by_label.keys())

            #plt.tight_layout()
            #plt.show()
            pdf.savefig(fig)
            plt.close()
        pdf.close()    
tvt_display(ddi_denoised)    