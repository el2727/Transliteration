
# coding: utf-8

# Read in text files from folder 

import glob
import re
path = 'weighted/weighted/*'
files = glob.glob(path)
content = []
for name in files:
    with open(name) as f:
        content.append(f.readlines())
        
# Get file names as target English names

file_names = []
for i in os.listdir('weighted/weighted/'):
    file_names.append(i)

# Balinese pre-processing

words_ban = []
for i in content:
    for y in i:
        if "ban_ban" in y:
            words_ban.append(y)


# In[131]:


words_ban_processed = []
for i in words_ban:
    i = re.sub(r'ban_ban', '', i)
    words_ban_processed.append(i)
    
words_ban_finalized = []
for i in words_ban_processed:
    i = re.sub(r'\t', '', i)
    words_ban_finalized.append(i)
    
words_ban_list = []
for i in words_ban_finalized:
    i = re.sub(r'\n', '', i)
    words_ban_list.append(i)


# In[134]:


zipped_ban = list(zip(words_ban_list, file_names))

full_pairs_ban = []
for i in zipped_ban:
    if i[0] != '-':
        full_pairs_ban.append(i)

translit_file_ban = []
for i in full_pairs_ban:
    translit_file_ban.append(i[0] + ' ' + i[1])
    
len(translit_file_ban)

# Train and test 80 and 20 

train_ban = translit_file_ban[:465]
test_ban = translit_file_ban[117:]

with open('train_ban.lex', 'w') as file:
    for i in train_ban:
        file.write(i + '\n')
        
with open('test_ban.lex', 'w') as file:
    for i in test_ban:
        file.write(i + '\n')

# Korean pre-processing

words_kor = []
for i in content:
    for y in i:
        if "kor_1985" in y:
            words_kor.append(y)
            
words_kor_processed = []
for i in words_kor:
    i = re.sub(r'kor_1985', '', i)
    words_kor_processed.append(i)

words_kor_finalized = []
for i in words_kor_processed:
    i = re.sub(r'\t', '', i)
    words_kor_finalized.append(i)

words_kor_list = []
for i in words_kor_finalized:
    i = re.sub(r'\n', '', i)
    words_kor_list.append(i)

zipped_kor = list(zip(words_kor_list, file_names))

full_pairs_kor = []
for i in zipped_kor:
    if i[0] != '-':
        full_pairs_kor.append(i)
            

translit_file_kor = []
for i in full_pairs_kor:
    translit_file_kor.append(i[0] + ' ' + i[1])


len(translit_file_kor)


# Train and test 80 and 20 

train_kor = translit_file_kor[:447]
test_kor = translit_file_kor[112:]

with open('train_kor.lex', 'w') as file:
    for i in train_kor:
        file.write(i + '\n')
        
with open('test_kor.lex', 'w') as file:
    for i in test_kor:
        file.write(i + '\n')


# Russian pre-processing

words_ru = []
for i in content:
    for y in i:
        if "rus_centralasian" in y:
            words_ru.append(y)

words_ru_processed = []
for i in words_ru:
    i = re.sub(r'rus_centralasian', '', i)
    words_ru_processed.append(i)

words_ru_finalized = []
for i in words_ru_processed:
    i = re.sub(r'\t', '', i)
    words_ru_finalized.append(i)

words_ru_list = []
for i in words_ru_finalized:
    i = re.sub(r'\n', '', i)
    words_ru_list.append(i)
    
zipped_ru = list(zip(words_ru_list, file_names))

full_pairs_ru = []
for i in zipped_ru:
    if i[0] != '-':
        full_pairs_ru.append(i)

translit_file_ru = []
for i in full_pairs_ru:
    translit_file_ru.append(i[0] + ' ' + i[1])

len(translit_file_ru)

# Train and test 80 and 20 

train_ru = translit_file_ru[:461]
test_ru = translit_file_ru[116:]


with open('train_ru.lex', 'w') as file:
    for i in train_ru:
        file.write(i + '\n')


with open('test_ru.lex', 'w') as file:
    for i in test_ru:
        file.write(i + '\n')

