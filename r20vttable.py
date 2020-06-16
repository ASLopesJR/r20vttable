#!/bin/python
# Created by Amaro Jr (amarinlopes@hotmail.com)

import textwrap
import random
import string
import os
import sys

def generate_rand_id(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

dir_source=sys.argv[1]
dir_convert=sys.argv[2]

for filename in os.listdir('./'+dir_source):
    file_converted = open ("./"+dir_convert+"/vtt_%s"%filename, "w")

    _id = generate_rand_id(16)

    first = True
    count = 0
    with open("./forja/"+filename) as f:
        for line in f:
            words = textwrap.dedent(line)
            words = words.split(' ')
            if(words[0]=='\"name\":' and first==True):
                file_converted.write("{ \n\
                  \"_id\": \""+_id+"\", \n\
                  \"name\": "+' '.join(words[1:])+"\
                  \"sort\": 100001,\n\
                  \"flags\": {\n\
                    \"better-rolltables\": {},\n\
                    \"exportSource\": {\n\
                      \"world\": \"teste\",\n\
                      \"system\": \"dnd5e\",\n\
                      \"coreVersion\": \"0.6.2\",\n\
                      \"systemVersion\": 0.93\n\
                    }\n\
                  },\n\
                  \"description\": \"tabela de critico mestre\",\n\
                  \"results\": [\n")
                first = False
                count = count + 1
            elif(words[0]=='\"name\":' and count == 1):
                _id = generate_rand_id(16)
                file_converted.write("{\n\
                \"_id\": \""+_id+"\",\n\
                \"flags\": {},\n\
                \"type\": 0,\n\
                \"text\": "+' '.join(words[1:])+",\n\
                \"img\": \"icons/svg/d20-black.svg\",\n\
                \"resultId\": \"\",\n\
                \"weight\": 1,\n\
                \"range\": [\n\
                  1,\n\
                  1\n\
                ],\n\
                \"drawn\": false\n\
                }\n")
                count = count + 1
            elif(words[0]=='\"name\":'):
                _id = generate_rand_id(16)
                file_converted.write(",{\n\
                \"_id\": \""+_id+"\",\n\
                \"flags\": {},\n\
                \"type\": 0,\n\
                \"text\": "+' '.join(words[1:])+",\n\
                \"img\": \"icons/svg/d20-black.svg\",\n\
                \"resultId\": \"\",\n\
                \"weight\": 1,\n\
                \"range\": [\n\
                  %d,\n\
                  %d\n\
                ],\n\
                \"drawn\": false\n\
                }\n"%(count,count))
                count = count + 1

    file_converted.write("],\n\
      \"formula\": \"1d%d\",\n\
      \"replacement\": true,\n\
      \"displayRoll\": true\n\
    }"%(count-1))

    file_converted.close()
    f.close()
