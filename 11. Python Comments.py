#!/usr/bin/env python
# coding: utf-8

# In[1]:


import py


# In[ ]:


#PYTHON COMMENTS
#In this sub-topic, we'll learn how to include comments in Python code.
#Comments are used to document code when necessary.
#There are different types of comments; Block comments, Inline comments, & documentation string.
#Python interpreter ignores comments and interpretes only the code.

#Python BLOCK COMMENT explains the code that follows it. 
# A block comment is started with a single (#) sign follwed by a single space & a sentence string. E.g:
# increase price by 5%
price = price * 1.05

# Python INLINE COMMENT
# When a comment is placed on the same line as statement, it is reffered to as INLINE COMMENT. E.g: 
price = price * 1.05 # increase price by 5%

# Python DOCSTRINGS 
# They are used for functions, modules, and classes.
# There are two forms of Python Docstrings; One-line and Multi-line docstrings. 
# A docstring can be accesed at run-time as obj._doc_ attribute where obj is the name of the function.
# Docstring is used to autonatically generate the code documentation
# Both one-line and Multi-line docstrings start and end with tripple quotes. (""").....(""")
# The following example illustrates a one-line docstring in the quicksort() function:
def quicksort():
""" sort the list using quicksort algorithm """

# The following example shows you how to use multi-line docstrings:
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """
# NB: Python doesn't support multiline comments.  

