#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
import scipy.stats as stats


# ## One sample t test 
# It tells us wheather means of the sample and the population are different 

# . 

# This test will tell us wheather means of sample and population are different

# Genrating the population data 

# In[50]:


weight_population=list(np.arange(10,100,2))


# In[51]:


weight_mean=np.mean(weight_population)
weight_mean


# To check the one sample t test(2 tail),we have to first consider the null and alternate hypothesis 
# In this situation  the null hypothesis is that there is not difference between the weight_population mean and weight_sample mean and alternate hypothesis state that there is difference between weight_population mean and weight_sample_mean
# 

# Second step 
# we have to determine the siginificance value that is level of significance.
# <br>
# In this question we determine our level of significance 0.05 from both  ends from both ends

# In[36]:


sample_size=30       
age_sample=np.random.choice(weight,sample_size)


# We assume that our sample data follow normal distribution

# In[37]:


age_sample


# t test equals to sample mean minus hypothesized population mean and divided by standard error
# <br>
# <br>
# Standard error equals to standard deviation of sample data divided by square root of sample size of data 
# <br>
# <br>
# In t test we don't know the standard deviation of population data and population mean as we know in z test 

# In[52]:


ttest,p_value=stats.ttest_1samp(age_sample,54)


# p_value is the probability that your sample supports the null hypothesis
# <br>
# Further p_value itself is meaningless,its the significance value that put it into context!

# In[53]:


p_value


# In[54]:


if p_value <0.05:
    print('we are rejecting the null hypothesis')
else:
    print('we are accepting the null hypothesis')

