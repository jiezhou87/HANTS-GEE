###With HANTS method, the cloud contaminated NDVI time series from earth observation can be reconstructed. 
#The HANTS had been implemented on GEE, and coeficients of harminics can be retrived from GEE. After donloaded,
#these images of haimonic coeficients needed to be further processed to produce time series of NDVI images with 
#given intevals by users.
#this processing is defined to generate NDVI images based on given images of harmonic coeficients.
import rasterio as rio
import concurrent.futures
import numpy as np
#import matplotlib.pyplot as plt
def tranform(coefArr,ts):
    
    # coefArr = params[0]
    #ts = params[1]
    print(typeof(params))
    print(params[1].shape)
    nHarms = int((coefArr.shape[0]-1)/2.0)
    ni = len(ts)
    
    mat = 2*np.pi*np.r_[np.arange(nHarms-1)+1,[0.5]].reshape(nHarms,1)*ts.reshape(1,ni)/(ni)
    #ind=np.array([i for i in zip(np.arange(nHarms),np.arange(nHarms)+nHarms)]).reshape(2*nHarms)
    
    cosMat = np.cos(mat)
    sinMat = np.sin(mat)
    mat1 = np.vstack((cosMat,sinMat))#[ind,:]
    mat1 = np.vstack((np.ones(ni),mat1))
    result = mat1.T.dot(coefArr.reshape(nHarms*2+1,coefArr.shape[1]*coefArr.shape[2])).reshape(ni,coefArr.shape[1],coefArr.shape[2])
    
    return (result*10000).astype(np.int16)
    
    
    
def COEF2Final(coefFile, outfile, intervals, date):
    num_workers = 4
    with rio.Env():
        with rio.open(coefFile) as src:
            #harmCoef = src.read(1)
            
            period = 365.0
            ts = np.arange(0,period//interval+1)
            profile = src.profile
            profile.update(blockxsize=512, blockysize=512, tiled=True,count = len(ts),dtype = "int16")
            
            nHarms = int((src.count-1)/2.0)
            ni = len(ts)

            mat = 2*np.pi*np.r_[np.arange(nHarms-1)+1,[0.5]].reshape(nHarms,1)*ts.reshape(1,ni)/(ni)
            #ind=np.array([i for i in zip(np.arange(nHarms),np.arange(nHarms)+nHarms)]).reshape(2*nHarms)

            cosMat = np.cos(mat)
            sinMat = np.sin(mat)
            mat1 = np.vstack((cosMat,sinMat))#[ind,:]
            mat1 = np.vstack((np.ones(ni),mat1))
            

            

            with rio.open(outfile, "w", **profile) as dst:
                windows = [window for ij, window in dst.block_windows()]
                data_gen = (src.read(window=window) for window in windows)
                
                for window in windows:
                    coefArr = next(data_gen)
                    result = mat1.T.dot(coefArr.reshape(nHarms*2+1,coefArr.shape[1]*coefArr.shape[2])).reshape(ni,coefArr.shape[1],coefArr.shape[2])
                    result = (result*10000).astype(np.int16)
                    dst.write(result, window=window)
            #print(next(data_gen).shape)
            
            
harmCoefFile = "China_MODIS_NDVI_5kmm_2014_COEF1.tif"
outfile = "Global_2014_5km_hants_daily.tif"
interval = 1
date ='2014-01-01'
#COEF2Final(harmCoefFile,outfile,interval,date)
harmCoefFile=input("Enter the HANTS coeficent file:")
print(harmCoefFile)
outfile=input("Enter the fullpath of output file:")
print(outfile)
interval=input("Enter the interval(days) of output:")
print(outfile)
date=input("Enter the start date of output (YYYY-MM-DD):")
print(outfile)
COEF2Final(harmCoefFile,outfile,interval,date)
