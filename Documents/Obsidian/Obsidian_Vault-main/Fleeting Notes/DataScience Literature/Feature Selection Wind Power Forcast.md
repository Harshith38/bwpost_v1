FeatureSelectionWindPowerForcast.pdf



This paper describes the 3d CNN to capture the dynamics of the wind contained in NWP data by focusing on tie silces in a certain period. 

With a procedure in section 2 and proposed feature extraction architecture in section 3 and configuration of numerical experiments in section 4, dicussion of evaluation of results in section 5.

**2. Wind power forecasting framework:**
Wind farm is in japan onshore, with 10 seconds power output measured in April 2015- July 2017. The dataset was converted in to per unit system.

*NWP:*  (Spatio-temporal feature maps) the temporal resoultion is 30 minutes to 72 hours ahead. The daver covered in the Thoku Area, and contain forcasted meteorologival variables on a 5 km horizontal grid. We take the zonal and meridional components of wwind speed vectors at 60 meters above sea level. The fig shows the data points around the targeted wind power plant.. 

Wind power forcast
- *feature extraction phase*.. (converted to spatio temporial maps) here to reduce the data dimensionality and automatically derive the important features from the wide area NWP data
- *Power forcasting phase*.-- Here two types of power phases are considered for comparision. 
	- **One**, that uses the low dimensional features obained by feature extraction phase.
	- **two**, uses the features and historical wind power data, is known to key to improve the accuracy of WPF. Historical data within 12 hours is used as input as power predictors.

**Gradient boosting trees regression**
It is used because it ensemble learning algorithm that builds set of decision trees. Advantages are nonparametric models and low computational cost of prediction.

