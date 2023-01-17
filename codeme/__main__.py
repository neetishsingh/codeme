import json
import sys
import requests

from requests.structures import CaseInsensitiveDict

def removespaces(codefilename):
    data=writeu(codefilename)
    with open(codefilename) as f:
        prom = f.readlines()
    list=[]
    for i in range(len(data)):
        prom[i]="'''Autobcode By Neetish Singh"+prom[i]+"'''"
    writegg(''.join(prom),codefilename)    
              

def jsong(value):
    #import json

    data = {}
    data['prompt'] = "write a python code for "+value
    data['model']="text-davinci-003"
    data['temperature'] = 0.7
    data['max_tokens']=2300
    if(len(data["prompt"])>=4000):
        data["prompt"]=str(data['prompt'])[0:3900]
    json_data = json.dumps(data).replace(r'\u0000', '')
    return json_data
def getChatGPTResponse(prom):
   
    #
    #writegg(prom,'b.txt')
    #Sprint(prom)
    #if(len(prom)>4000):
    #    prom=prom[0:4000]
    url = "https://api.openai.com/v1/completions"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer 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"
    headers["Content-Type"] = "application/json"
    
    data = jsong(prom)#'{"model": "text-davinci-003","prompt": "'+str(prom)+'", "temperature": 0.7, "max_tokens": 2300}'
    #print(data)
    
    #writegg(data,'c.txt')
    resp = requests.post(url, headers=headers, data=data)
   
    ab=resp.text
    ah=json.loads(ab)
    #print(ab)
    #print(ah['choices'][0]['text'])
    #json_object = json.dumps(ah['choices'][0]['text'], indent=4)
    #writegg(json_object,'a.json')
    writegg(ah['choices'][0]['text'],'tempcode.py')
 
    return resp.text
def writegg(viewer,loca):
    with open(loca, "w") as f:
        #print(viewer.canvas.text_content)
        f.write(viewer)

def writeu(codefilename):
    #codelength=0
    with open(codefilename) as f:
        prom = f.readlines()
    #codelength=len(prom)
    listofcode=[]#format (code, index) 
    if(len(prom)==1 and prom[0].startswith('#')):
        listofcode.append({"code":prom[0],"index":1})   
    for i in range(len(prom)-1):
        print(prom[i].strip())
        if ((prom[i].strip()!='' and prom[i].startswith('#')) and (i==len(prom) or (prom[i+1].strip()==''))):
            #print(prom[i],'<<',i)
            listofcode.append({"code":prom[i],"index":i+1})
        if(i+2==len(prom)):
            print('Oh! this is little tricky but for you i will do it🤩')
            if((prom[i+1].strip()!='' and prom[i+1].startswith('#'))):
                
                listofcode.append({"code":prom[i+1],"index":i+2})
                #print(prom[i+1].strip())
    #print(listofcode)            
    return listofcode    
    #print(prom)

def writecodeinpy(filename,index):
    with open(filename) as f:
        prom = f.readlines()
    with open('tempcode.py') as ftemp:
        promcode = ftemp.readlines()
    flag=0    
    for i in range(len(promcode)):
        if(promcode[i]=='\\n'):
            flag=i+1
        else:
            break
    promcode= promcode[flag:]
    finalprom=prom[0:index]+promcode+prom[index:]
    writegg((''.join(finalprom)),filename)

    
def readandcode(codefilename):
    
    analysecode=writeu(codefilename)
    for i in range(len(analysecode)):
        getChatGPTResponse(analysecode[i]['code'])
        writecodeinpy(codefilename,findnewindex(codefilename,analysecode[i]['code']))
    removespaces(codefilename)    

def findnewindex(filename,text):
    with open(filename) as f:
        prom = f.readlines()
    for i in range(len(prom)):
        if prom[i].startswith(text):
            return i;    


#readandcode()
if __name__ == "__main__":
    readandcode(sys.argv[1])
    print("ah! Finally its completed.")
    import os
    os.remove("tempcode.py")
    #removespaces()
    #SHello(sys.argv[1],sys.argv[2])          



