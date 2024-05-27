====
HANTS-GEE
====
This repository aims to introduce the `HANTS-GEE <https://code.earthengine.google.com/fcd8dc8d40a68b3c47af140f17da5dd7>`_ (Latest update: 27/05/2024) package, **a scalable implimentation of HANTS for time sereis reconstruction in remote sensing on Google Earth Engine platform**.

The **Harmonic ANalysis of Time Series (HANTS)** was proposed by Verheof (1996) and Menenti et al. (1993)
to reconstruct time series of remote sensing products such as NDVI and LAI.
The algorithm had been widely used in the remote sensing community and implemented 
in Fortran, IDL/ENVI, Matlab, C, and Python.   
The script in this file aim to implement the HANTS in GEE, which can avoid 
donwloading large volume dataset to local PC and also make full use of the 
powerfull computation resource of GEE.

Main features:
 - Complete HANTS kernel implementation
 - Scalable reconstrction tasks (spatiotemporal extent & resolution).
 - Processing result can be export to google drive as well as Assets for 
   further analysis.
 - TO speed up the exporting and downloading, one can choose to export final 
   harmonic coefficient and then construct final image series in local PC. 
.. figure:: figures/GUI.png
  :width: 800
  :alt: Grapical User Interface  for HANTS-GEE
  :class: with-border
  
  *Figure 1. Grapical User Interface  for HANTS-GEE*

.. figure:: figures/sample_case1.png
  :width: 800
  :alt: A reconstrction case with HANTS-GEE
  :class: with-border
  
  *Figure 2. Pixel-level time series reconstruciton with HANTS-GEE. Gray dots represent quality assessment (QA) value for observation (MODIS-NDVI: 0- Good Data, 1- Marginal Data, 2- Snow/Ice, 3- Cloudy. Red squres indicate valid observations identified by HANTS-GEE and other observations are outliers.*

Attentions:
 - If you want to export the result for large area with high spatial reolution 
   and long-time series, better to seperate the region in different parts and 
   export it one by one. Otherwise, it will take a long time to processing or 
   even failed.
 - The maixum storage space provide by Google Drive with free account is 15 GB,
   please check your left space before exporting result.
   

****
Usage of the packages
****

The HANTS-GEE package is freely avaliable  `here <https://code.earthengine.google.com/5ab9bde3c258a2b9c5046c4305e76186>`_ (Latest update: 19/12/2023).

Contact: Dr. Jie Zhou (zhou.j@ccnu.edu.cn), Central China Normal University, Wuhan, P.R. China

****
Usefull references
****

[1]	Menenti, M, S Azzali, W Verhoef, and R Van Swol. 1993. “Mapping Agroecological Zones and Time Lag in Vegetation Growth by Means of Fourier Analysis of Time Series of NDVI Images.” Advances in Space Research 13 (5). Elsevier: 233–237.

[2]	Roerink, GJ, Massimo Menenti, and Wout Verhoef. 2000. “Reconstructing Cloudfree NDVI Composites Using Fourier Analysis of Time Series.” International Journal of Remote Sensing 21 (9). Taylor & Francis: 1911–1917.

[3]	Verhoef, W. 1996. Application of Harmonic Analysis of NDVI Time Series (HANTS). Fourier Analysis of Temporal NDVI in the Southern African and American Continents. DLO Winand Staring Centre, Wageningen, The Netherlands.

[4]	Zhou, Jie, Li Jia, and Massimo Menenti. 2015. “Reconstruction of Global MODIS NDVI Time Series: Performance of Harmonic ANalysis of Time Series (HANTS).” Remote Sensing of Environment 163. Elsevier: 217–228.

[5] Zhou, Jie, Li Jia, Massimo Menenti, and Ben Gorte. 2016. “On the Performance of Remote Sensing Time Series Reconstruction Methods–A Spatial Comparison.” Remote Sensing of Environment 187: 367–384.

[6]	Zhou, Jie, Li Jia, Massimo Menenti, and Xuan Liu. 2021. “Optimal Estimate of Global Biome—Specific Parameter Settings to Reconstruct NDVI Time Series with the Harmonic ANalysis of Time Series (HANTS) Method.” Remote Sensing 13 (21). Multidisciplinary Digital Publishing Institute: 4251.

[7]	Zhou, J., Menenti, M., Jia, L., Gao, B., Zhao, F., Cui, Y., Xiong, X., Liu, X. and Li, D., 2023. A scalable software package for time series reconstruction of remote sensing datasets on the Google Earth Engine platform. International Journal of Digital Earth, 16(1), pp.988-1007. `https://doi.org/10.1080/17538947.2023.2192004 <https://doi.org/10.1080/17538947.2023.2192004>`_
