import numpy as np
import matplotlib.pyplot as plt 
from tabulate import tabulate
#--------------------------------------------------------------------------------------------#
#FINDING AN OPTIMAL HUBBLE CONSTANT
#--------------------------------------------------------------------------------------------#
# Creating a list of potential Hubble Constants 
Hubble_Constant_List=np.arange(17.0,30.1,0.1)

#Finding the difference between the line of best fit and the expected value for each Hubble Constant. Omega Matter = 0.3 , Omega Dark Energy = 0.7

Model_Data_Difference_List=[24.62,23.48,22.38,21.32,20.3,19.31,
                           18.36,17.45,16.57,15.72,14.91,14.12,13.37,12.65,11.96,11.29,
                           10.65,10.04,9.45,8.89,8.36,7.84,7.35,6.88,6.44,6.01,5.61,5.23,4.86,4.51,
                           4.19,3.88,3.59,3.31,3.05,2.81,2.58,2.37,2.18,2,1.83,1.67,1.53,1.4,1.29,1.19,
                           1.1,1.02,.95,.89,.84,.81,.78,.77,.76,.77,.78,.8,.83,.87,.91,0.97,1.03,
                           1.1,1.18,1.27,1.36,1.46,1.56,1.67,1.79,1.91,2.04,2.18,2.32,2.47,2.62,2.78,
                           2.94,3.11,3.28,3.46,3.64,3.83,4.02,4.21,4.41,4.61,4.82,5.03,5.24,5.46,5.68,5.9,
                           6.13,6.36,6.59,6.83,7.07,7.31,7.55,7.8,8.05,8.3,8.56,8.81,9.07,9.33,9.6,9.86,10.13,
                           10.4,10.67,10.94,11.22,11.5,11.77,12.05,12.34,12.62,12.9,13.19,13.47,13.76,14.05,
                           14.34,14.63,14.93,15.22,15.52,15.81]
                          
print(tabulate({"Hubble Constant":Hubble_Constant_List ,
               "Model-Data Difference":Model_Data_Difference_List}, headers="keys",
               tablefmt='fancy_grid'))
plt.figure(figsize=(20,10))
plt.plot(Hubble_Constant_List,Model_Data_Difference_List)
plt.axhline(y=0.76,color='r',label="Lowest Model-Data Difference=0.76")
plt.scatter(Hubble_Constant_List,Model_Data_Difference_List)
plt.xticks(np.arange(min(Hubble_Constant_List), max(Hubble_Constant_List)+0.1, 1))
plt.xlabel("Hubble Constant",size=20)
plt.ylabel("Model-Data Difference",size=20)
plt.grid()
plt.title(" Model-Data Difference vs. Hubble Constant",size=20)
plt.legend(fontsize=15)

mask=np.min(Model_Data_Difference_List)
dmin = np.min(Model_Data_Difference_List)
mask = np.array(Model_Data_Difference_List) == dmin
fin = np.where(mask)
print(fin[0])
# 54th data entry is the value of the minimum

np.round(Hubble_Constant_List[54],1) # This is the ideal Hubble Constant for our universe

#--------------------------------------------------------------------------------------------#
# FINDING AN OPTIMAL MATTER DENSITY 
#--------------------------------------------------------------------------------------------#


fixed_density_matter_values_1=np.arange(0.1,1.1,0.1)
fixed_density_matter_values_2=np.arange(0.21,.39,0.01)
fixed_density_model_difference_values_1=[2.97,1.15,0.76,1.12,1.89,2.91,4.08,5.35,6.67,8.01]
fixed_density_model_difference_values_2=[1.06,.99,.92,.87,.83,.8,.78,.77,.76,.76,.77,
                                        .79,.81,.84,.87,.91,.95,1]


plt.figure(figsize=(20,10))
plt.plot(fixed_density_matter_values_1,fixed_density_model_difference_values_1,label='Matter Density 0.1 - 1.0')
plt.axhline(y=0.76,color='r',label="Lowest Model-Data Difference=0.76")
plt.scatter(fixed_density_matter_values_2,fixed_density_model_difference_values_2,label='Matter Density 0.21 - 0.39', color='black')
plt.xlabel("Matter Density",size=20)
plt.ylabel("Model-Data Difference",size=20)
plt.grid()
plt.title(" Model-Data Difference vs. Matter Density",size=20)
plt.legend(fontsize=15)

mask1=np.min(fixed_density_model_difference_values_2)
dmin1 = np.min(fixed_density_model_difference_values_2)
mask1 = np.array(fixed_density_model_difference_values_2) == dmin1
fin1 = np.where(mask1)
print(fin1[0])
# 8,9th data entry is the value of the minimum
np.round(fixed_density_matter_values_2[8:9],1)
#0.3 is the ideal Matter Density
#--------------------------------------------------------------------------------------------#
#FINDING A MODEL EQUATION IN TERMS OF MATTER DENSITY AND DARK ENERGY DENSITY
#--------------------------------------------------------------------------------------------#
plt.figure(figsize=(20,10))
plt.scatter(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated,color='r')
plt.plot(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated)
plt.xticks(np.arange(min(Best_Fit_Dark_Updated), max(Best_Fit_Dark_Updated)+0.1, 0.1))
plt.yticks(np.arange(min(Best_Fit_Matter_Updated), max(Best_Fit_Matter_Updated)+0.1, 0.1))
plt.xlabel("Dark Energy Density Fraction- Best-Fit",size=20)
plt.ylabel("Matter Density Fraction- Best-Fit",size=20)
plt.grid()
plt.title("Matter Density Fraction- Best-Fit vs. Dark Energy Density Fraction- Best-Fit",size=20)

# On the 9th iteration, we find four near optimal solutions.... 
Case1_Matter_Fraction_List_9=[]
Case1_Matter_Fraction_List_10=[]
Case1_Matter_Fraction_List_11=[]
Case1_Matter_Fraction_List_12=[]

for i in Best_Fit_Dark_Updated:
    Case1_Matter_Fraction_List_9.append(i-0.3)
    Case1_Matter_Fraction_List_10.append(i-0.4)
    Case1_Matter_Fraction_List_11.append(i-0.5)
    Case1_Matter_Fraction_List_12.append(i-0.6)

plt.figure(figsize=(20,10))
plt.scatter(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated,color='r')
plt.plot(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated,label="Data")
plt.plot(Best_Fit_Dark_Updated,Case1_Matter_Fraction_List_9,label="Case 1, constant =0.3")
plt.plot(Best_Fit_Dark_Updated,Case1_Matter_Fraction_List_10,label="Case 1, constant =0.4")
plt.plot(Best_Fit_Dark_Updated,Case1_Matter_Fraction_List_11,label="Case 1, constant =0.5")
plt.plot(Best_Fit_Dark_Updated,Case1_Matter_Fraction_List_12,label="Case 1, constant =0.6")


plt.xticks(np.arange(min(Best_Fit_Dark_Updated), max(Best_Fit_Dark_Updated)+0.1, 0.1))
plt.yticks(np.arange(min(Best_Fit_Matter_Updated), max(Best_Fit_Matter_Updated)+0.1, 0.1))
plt.xlabel("Dark Energy Density Fraction- Best-Fit",size=20)
plt.ylabel("Matter Density Fraction- Best-Fit",size=20)
plt.grid()
plt.title("Matter Density Fraction- Best-Fit vs. Dark Energy Density Fraction- Best-Fit",size=20)
plt.legend(fontsize=15,loc='lower right')

#--------------------------------------------------------------------------------------------#
# PROVING THE EQUATION  (density fraction of dark energy) + (density fraction of matter) = (0.4) IS VALID
#--------------------------------------------------------------------------------------------#

plt.figure(figsize=(20,10))
plt.scatter(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated,color='r')
plt.plot(Best_Fit_Dark_Updated,Best_Fit_Matter_Updated,label="Data")
plt.plot(Best_Fit_Dark_Updated,Case1_Matter_Fraction_List_6,label="Case 2, constant =0.4")



plt.xticks(np.arange(min(Best_Fit_Dark_Updated), max(Best_Fit_Dark_Updated)+0.1, 0.1))
plt.yticks(np.arange(min(Best_Fit_Matter_Updated), max(Best_Fit_Matter_Updated)+0.1, 0.1))
plt.xlabel("Dark Energy Density Fraction- Best-Fit",size=20)
plt.ylabel("Matter Density Fraction- Best-Fit",size=20)
plt.grid()
plt.title("Matter Density Fraction- Best-Fit vs. Dark Energy Density Fraction- Best-Fit",size=20)
plt.legend(fontsize=15,loc='lower right')

print(Best_Fit_Dark_Updated-Best_Fit_Matter_Updated)

# We can see that the value of C=0.4 is acceptable
