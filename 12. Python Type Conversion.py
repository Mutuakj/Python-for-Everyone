#!/usr/bin/env python
# coding: utf-8

# In[1]:


import py


# In[2]:


# PYTHON TYPE CONVERSION
# To get input from users, we use input() function. E.g: 
value = input('Enter a value:')
print(value)


# In[3]:


# The above input() function returns a string and not an integer.
""" The following example prompts you for entering two input values: net price and tax rate.
After that, it calculates the net price and displays the result on the screen:
"""
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = price * tax / 100

print(f'The net price is ${net_price}') # run the program and enter 100 for price & 10% for tax rateS


# In[4]:


# The above error is because the input values are strings, you cannot apply the arithmetic operator (+) to them.


# In[7]:


# To solve the error, you need to convert the strings to numbers before performing calculations.
""" To convert a string to a number, you use the int() function. 
More precisely, the int() function converts a string to an integer. 
"""
# The following example uses the int() function to convert the input strings to numbers:
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}') # run the program and enter 100 for price & 10% for tax rate 


# In[8]:


# Other type conversion functions
# Besides the int(str) functions, Python support other type conversion functions. 
# The following shows the most important ones for now:
 # - float(str) – convert a string to a floating-point number.
 # - bool(val) – convert a value to a boolean value, either True or False.
 # - str(val) – return the string representation of a value.


# In[9]:


# Getting the type of a value
# To get the type of a value, we use the type(value) function. E.g: 
type(100)


# In[10]:


type(8.0)


# In[11]:


type('Hello, World!')


# In[12]:


type(True)


# In[ ]:


# SUMMARY
# We use the input() function to get an input string from a user
# Type conversions functions such as int(), bool(), str(value), and float() are used to convert a value from one type to another
# The type() function is used to get the type of a value.

