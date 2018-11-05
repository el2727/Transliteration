
# coding: utf-8

# In[158]:


# Korean evaluation

content = open('test_kor.lex', 'r').readlines()
text_list = []
for i in content:
    text_list.append(i.split(' '))


# In[159]:


with open('words_kor.txt', 'w') as file:
    for i in text_list:
        file.write("%s\n" % i[0])
        
# Reference link: https://stackoverflow.com/questions/37629509/write-each-element-of-a-list-on-a-newline-on-a-text-file-in-python


# In[160]:


content_test = open('word_kor.out', 'r').readlines()
test = []
for i in content_test:
    test.append(i.split('\t'))


# In[161]:


correct_answers = []
for i in test:
    for y in text_list:
        if i == y:
            correct_answers.append(i)


# In[162]:


len(text_list)


# In[163]:


len(correct_answers)


# In[164]:


errors = []
for i in test:
    for y in i:
        if 'failed to convert' in y:
            errors.append(i)


# In[165]:


len(errors)


# In[166]:


correct_percent = len(correct_answers)/len(text_list)
print(correct_percent)


# In[167]:


error_percent = len(errors)/len(text_list)
print(error_percent)


# In[169]:


1 - (correct_percent + error_percent)


# In[126]:


print(errors)


# In[129]:


index_list = range(1, len(text_list) + 1)
zipped = list(zip(index_list, text_list))


# In[135]:


print(zipped)


# In[148]:


results_list = []
for i in errors:
    for w in text_list:
        if w in i:
            results_list.append(i)


# In[149]:


print(results_list)


# In[128]:


with open('korean_errors.tsv', 'w') as file:
    for i in errors:
        file.write("%s\n" % i[0])


# In[170]:


# Russian evaluation

content_test = open('word_ru.out', 'r').readlines()
test = []
for i in content_test:
    test.append(i.split('\t'))


# In[171]:


content = open('test_ru.lex', 'r').readlines()
text_list = []
for i in content:
    text_list.append(i.split(' '))


# In[172]:


correct_answers = []
for i in test:
    for y in text_list:
        if i == y:
            correct_answers.append(i)


# In[173]:


len(correct_answers)


# In[174]:


len(text_list)


# In[175]:


errors = []
for i in test:
    for y in i:
        if 'failed to convert' in y:
            errors.append(i)


# In[176]:


print(errors)


# In[177]:


correct_percent = len(correct_answers)/len(text_list)
print(correct_percent)


# In[178]:


error_percent = len(errors)/len(text_list)
print(error_percent)


# In[179]:


1 - (correct_percent + error_percent)


# In[157]:


with open('russian_errors.tsv', 'w') as file:
    for i in errors:
        file.write("%s\n" % i[0])


# In[2]:


import zipfile
zip_ref = zipfile.ZipFile("weighted_folder.zip", 'r')
zip_ref.extractall("weighted/")
zip_ref.close()

# Reference link: https://stackoverflow.com/questions/3451111/unzipping-files-in-python

