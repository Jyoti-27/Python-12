#!/usr/bin/env python
# coding: utf-8

# 
# - In Python
#  -1.Create a Class
#  -2.Define An Attributes:a) Class Atrributes    b) Instance Attributes
#  -3. Define Methods
#  -4. Create an Instances

# - Create a Class whose name is Cars
# - Define the Attributes such as color, cc
# - Create 2 or 3 instance of the CARS

# In[3]:


class Cars:  # class is a keyword
    
    # Create the Atributes
    def __init__(self,color,cc):    # init is a constructor and it has double underscore mandetory.
        self.color = color      
        self.cc = cc
    
    # Craete the instances of the class Cars
car1 = Cars('red',1000)
print(car1.cc)
print(car1.color)
car1.color


# - Create of class of Humans
# - Assign to instant variables sex and height
# - Then create two instance of the class Humans with the namee Male and Female

# In[9]:


class Humans:  # class is a keyword
    
    # Create the Atributes
    def __init__(self,sex,height):    # init is a constructor and it has double underscore mandetory.
        self.sex = sex      
        self.height = height
    
    # Craete the instances of the class Cars
h1 = Humans('male',6)
h2 = Humans('female',5.5)
print("Instance 1",h1.sex,h1.height)
print("Instance 2",h2.sex,h2.height)


# In[12]:


class Humans:  # class is a keyword
    
    # Create the Atributes
    def __init__(self,sex,height):    # init is a constructor and it has double underscore mandetory.
        self.sex = sex      
        self.height = height
    
    # Craete the instances of the class Cars
hmn = Humans('male','6')
print(hmn.sex)
print(hmn.height)
hmnf = Humans('female','5.5')
print(hmnf.sex)
print(hmnf.height)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




