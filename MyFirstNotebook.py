
# coding: utf-8

# In[64]:

import re
def extract_rating(input):
    "extract a Credit Rating type string from input "
    
    rc = re.sub('.*', input)
    return rc


# In[65]:

extract_rating('CL.12')


# In[ ]:



