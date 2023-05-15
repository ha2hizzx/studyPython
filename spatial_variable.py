#!/usr/bin/env python
# coding: utf-8

# <h1>python 공간변수</h1>

# In[5]:


a = 1
b = "python"
c = [1,2,3]
#다른 프로그래밍 언어인 c나 Java는 변수를 만들때 자료형의 타입을 지정해줘야 하지만 python은 자동으로 지정해 준다.


# In[6]:


a = [1,2,3] #이렇게 a의 변수를 지정하였을 때 이 리스트 데이터(객체)가 자동으로 메모리에 생성이 되고 a는 [1,2,3]이 저장된 메모리의 주소를 가리킨다.
id(a) #id는 변수가 가리키고 있는 객체의 주소 값을 리턴한다.


# In[10]:


a = [1,2,3]
b = a[:] #a가 가리키고있는 내용을 새로 [1,2,3]을 만들어 그것과 연결하는것
c = [1,2,3]


# In[11]:


id(a)


# In[8]:


id(b)


# In[9]:


id(c) 


# In[12]:


#메모리 공간이 다르기에 값또한 달라진다.


# In[14]:


from copy import copy #파이썬 모듈
a = [1,2,3]
b = copy(a) #a가 가르키고있던 [1,2,3]을 복사한것을 가르킨다.


# In[15]:


a is b #False가 나온다.


# In[17]:


a = [1,2,3]
b = a.copy()


# In[19]:


a is b #똑같이 False가 나온다.


# In[21]:


a, b = ['hello', 'python'] #튜플로 a, b에 값을 대입할수 있다.


# In[22]:


a


# In[23]:


b


# In[24]:


[a, b] = ['hello', 'python']


# In[25]:


a


# In[26]:


b


# In[27]:


a, b = 'hello', 'python'


# In[28]:


a


# In[29]:


b


# In[30]:


a = b = 'hello' #a의 값을 b에 b의 값을 a에 넣는다.


# In[31]:


a


# In[32]:


b


# In[33]:


a = 'hello'
b = 'python'


# In[34]:


a


# In[35]:


b


# In[36]:


a,b = b,a #서로의 값을 바꿀수도 있다.


# In[37]:


a


# In[38]:


b

