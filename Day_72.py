#!/usr/bin/env python
# coding: utf-8

# # Creating Command Line Utilities in Python
# - Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.
# #### Syntax
# - Here is the basic syntax for creating a command line utility using argparse in Python:

# In[2]:


import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)


# In[10]:


import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("arg1", nargs="?", default="Default1")
parser.add_argument("arg2", nargs="?", default="Default2")

# Pass only our custom arguments, not Jupyter's
args = parser.parse_args(args=sys.argv[1:3])

print(args.arg1)
print(args.arg2)


# ## Examples
# - Here are a few examples to help you get started with creating command line utilities in Python:
# ### Adding optional arguments
# - The following example shows how to add an optional argument to your command line utility:

# In[4]:


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")

args = parser.parse_args()

print(args.optional)


# ### Adding positional arguments
# The following example shows how to add a positional argument to your command line utility:

# In[5]:


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("positional", help="description of positional argument")

args = parser.parse_args()

print(args.positional)


# ## Adding arguments with type
# The following example shows how to add an argument with a specified type:

# In[7]:


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", type=int, help="description of integer argument")

args = parser.parse_args()

print(args.n)


# In[ ]:




