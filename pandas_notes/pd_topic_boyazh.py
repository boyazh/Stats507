#!/usr/bin/env python
# coding: utf-8

# # Question 0

# ## Introduction to Python Idioms  
#   
# Boya Zhang (boyazh@umich.edu)  
# 
# 10.16.21
# 

# ## Overview  
#   
# 1. if-then/if-then-else
# 2. splitting
# 3. building criteria

# ## 1. if-then/ if-then-else 
# 
# 1.1 You can use if-then to select specific elements on one column, and add assignments to another one or more columns: 
#         

# In[21]:


import pandas as pd
df = pd.DataFrame({"A": [1, 3, 5, 7, 9], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df


# * To assign to one or more column:

# In[22]:


df.loc[df.A > 5, 'B'] = '> 5'
df


# * or

# In[23]:


df.loc[df.A > 5, ['B','C']] = '> 5'
df


# * You can add another line with different logic, to do the ”-else“

# In[25]:


df.loc[df.A <= 5, ['B','C']] = '< 5'
df


# 1.2 You can also apply "if-then-else" using Numpy's where( ) function

# In[28]:


import numpy as np
import pandas as pd

df = pd.DataFrame({"A": [1, 3, 5, 7, 9], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df['new'] = np.where(df['A'] > 5, '> 5', '< 5')
df


# ## 2. Splitting a frame with a boolean criterion

# You can split a data frame with a boolean criterion

# In[38]:


import numpy as np
import pandas as pd

df = pd.DataFrame({"A": [1, 3, 5, 7, 9], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df


# In[39]:


df[df['A'] > 5]


# In[40]:


df[df['A'] <= 5]


# ## 3. Building criteria 
# You can build your own selection criteria using "**and**" or "**or**".  
# 
# 3.1 "... and"

# In[49]:


import numpy as np
import pandas as pd

df = pd.DataFrame({"A": [1, 3, 5, 7, 9], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df


# * ...and

# In[50]:


df.loc[(df["B"] < 25) & (df["C"] >= 20), "A"]


# * ...or

# In[51]:


df.loc[(df["B"] < 25) | (df["C"] >= 40), "A"]


# * you can also assign new value to a existing column using this method

# In[52]:


df.loc[(df["B"] > 40) | (df["C"] >= 300), "A"] = 'new'
df


# ## Takeaways  
# There are a few python idioms that can help speeding up your data managemet.  
# * "if-then-else" allows you easily change the current column or add additional new columns based on the value of a specific column
# * "Splitting" allows you quickly select specific rows based on the value of a specific column
# * "Building criteria" allows you select specific data from one column or assign new values to one column based on the criteria you set up on other columns

# In[ ]:




