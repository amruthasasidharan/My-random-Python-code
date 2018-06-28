
# coding: utf-8

# In[1]:


import os
import pandas 


# In[2]:


os.chdir("E:\\Python\\Data")


# In[3]:


breast_cancer=pandas.read_table("breast-cancer-wisconsin.data.txt",sep=",",header=-1,names=["ID","Thickness","Size","Shape"
                                                                                            ,"Adhesion","Epithelial Cell Size",
                                                                                           "Bare Nuclei","Bland Chromatin",
                                                                                           "Normal Nucleoli","Mitosis","Class"],
                               index_col=False)
breast_cancer.head()


# In[4]:


breast_cancer.tail(2)


# In[5]:


breast_cancer.shape


# In[6]:


breast_cancer.columns


# In[7]:


breast_cancer.Class[2:5]


# In[8]:


breast_cancer[["Size","Shape","Class"]].head(10)


# In[9]:


breast_cancer.Size.max()


# In[10]:


breast_cancer.describe()


# In[11]:


breast_cancer.Class[breast_cancer.Shape>3].head(10)


# In[31]:


breast_cancer[(breast_cancer.Shape>3)& (breast_cancer.Size>3)].head(3)


# In[12]:


breast_cancer.index


# In[13]:


breast_cancer.set_index("ID").head(4)


# In[15]:


breast_cancer.iloc[:5,5:]


# In[21]:


breast_cancer.loc[:5,"Class"]

