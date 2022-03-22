This repository aims to archieve the documents for HANTS-GEE, a scalable implimentation of HANTS for time sereis reconstruction in remote sensing on Google Earth Engine platform.
/**********************************************************************
The Harmonic ANalysis of Time Series (HANTS) was proposed by Verheof (1996) and Menenti et al. (1993)
to reconstruct time series of remote sensing products such as NDVI and LAI.
The algorithm had been widely used in the remote sensing community and implemented 
in Fortran, IDL/ENVI, Matlab, C, and Python.   
The script in this file aim to implement the HANTS in GEE, which can avoid 
donwloading large volume dataset to local PC and also make full use of the 
powerfull computation resource of GEE.

Main features:
 - HANTS kernel 
 - Long-term (multiple years) processing for pre-defined area. Each year is
   processed seperately with half of an year overlap.
 - processing result can be export to google drive as well as Assets for 
   further analysis.
 - TO speed up the exporting and downloading, one can choose to export final 
   harmonic coefficient and then construct final image series in local PC. 
   
Attentions:
 - If you want to export the result for large area with high spatial reolution 
   and long-time series, better to seperate the region in different parts and 
   export it one by one. Otherwise, it will take a long time to processing or 
   even failed.
 - The maixum storage space provide by Google Drive with free account is 15 GB,
   please check your left space before exporting result.
   
 Author: Dr. Jie Zhou
Email:zhou.j@ccnu.edu.cn
Central China Normal University, Wuhan, P.R. China
*************************************************************************/
