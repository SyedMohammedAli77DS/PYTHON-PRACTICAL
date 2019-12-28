
# coding: utf-8

# In[12]:


# sum of two numbers
def sum(a,b):
    '''sum of two number'''
    c=a+b
    return c


# In[17]:


# substraction of two numbers
def sub(a,b):
    ''' substaraction of two numbers'''
    c=a-b
    return c


# In[18]:


# multiplaction of two numbers
def mul(a,b):
    ''' Multiplaction of two numbers'''
    c=a*b
    return c


# In[19]:


# division of two numbers
def div(a,b):
    '''division of two numbers'''
    c=a/b
    return c


# In[20]:


# percentage of two numbers
def per(a,b):
    ''' Percentage of two numbers'''
    c=(a*b)/100
    return c


# In[21]:


# modules of two numbers
def mod(a,b):
    ''' modules of two numbers'''
    c=a%b
    return c


# In[78]:





# In[79]:


# area of circle
def acircle(r):
    ''' area of circle'''
    ar=((3.141592653589793)*(r**2))
    return ar


# In[15]:


# area of square
def asquare(a):
    ''' area of square'''
    s=(a**2)
    return s


# In[32]:


# area of rectangle
def arec(a,b):
    ''' area of rectangle'''
    c=a*b
    return c


# In[33]:


# area of polygon
def poly(a,p):
    ''' pass the area and the sum of six sides of polygon'''
    c=0.5*(a*p)
    return c


# In[36]:


# area of hexagon
def hexa(a):
    ''' enter the a value i.e length of one side'''
    b=(3/2)*math.sqrt(3)
    c=b*(a**2)
    return c


# In[44]:


# conversion of killometer to meter
def kmtomi(a):
    b=a*0.621371
    return b


# In[50]:


mitokm(2)


# In[49]:


# conversion of meter to killometer
def mitokm(a):
    b=a*1.60934
    return b


# In[70]:


# conversion of celsius to fahrenheit
def cetofa(a):
    b=(a*(9/5))+32
    return b


# In[73]:


cetofa(36)


# In[62]:


# conversion of fahrenheit to celsius
def fatoce(a):
    b=(a-32)*5/9
    return b


# In[72]:


fatoce(96.8)

