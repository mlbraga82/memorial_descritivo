#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from tabula import read_pdf
import numpy as np
import requests
import io
import sys
import os
cwd=os.getcwd()
print ('Diretorio Atual: ',cwd)

print ('Início do Script')
arg = sys.argv[1]
if len(arg)>0:
    url='https://sigef.incra.gov.br/geo/parcela/memorial/'+arg+'/'
    print('Argumento Recebido:',arg)
else:
    url=''
# In[ ]:


#url='https://sigef.incra.gov.br/geo/parcela/memorial/ac1fc569-4b93-49ef-beb1-f98254292140/'
try:
    r=requests.get(url,timeout=60,verify=False)
    arquivo=io.BytesIO(r.content)
    print('Arquivo baixado!')
except:
    print('Erro na requisição!')
    arquivo='document.pdf'
    print('Verifique sua conexão com a internet.')
    exit()

# In[ ]:

print('lendo arquivo...')
#df = read_pdf('document.pdf',output_format='dataframe',pages="all",stream=True)
try:
    df = read_pdf(arquivo,output_format='dataframe',pages="all",stream=True)
    print('leitura do arquivo feita com sucesso!')
except:
    print('Erro na leitura do arquivo.')
    exit()

# In[ ]:


data=pd.DataFrame(df[0])


# In[ ]:


colunas = ['Código',
 'Longitude','Latitude',
 'Altitude (m)',
 'Código',
 'Azimute',
 'Dist. (m)',
 'Confrontações','NaN']    


# In[ ]:


try:
    data.columns=colunas
except:
    colunas = ['Código',
 'Longitude','Latitude',
 'Altitude (m)',
 'Código',
 'Azimute',
 'Dist. (m)',
 'Confrontações']
    data.columns=colunas


# In[ ]:


data=data.drop(0,axis=0)


# In[ ]:


try:
    data=data.drop('NaN',axis=1)
except:
    pass


# In[ ]:


mask=data['Latitude'].isnull()


# In[ ]:


for k,v in data[mask].iterrows():
    linha=data.loc[k,'Longitude']
    lon,lat=linha.split(' ')
    data.loc[k,'Longitude']=lon
    data.loc[k,'Latitude']=lat


# In[ ]:


data


# In[ ]:


#list(data.columns)


# In[ ]:


memorial = 'Inicia-se a descrição deste perímetro no vértice '
for k,v in data.iterrows():
    if k==1:
        memorial=memorial+v[0]+', georreferenciado no Sistema Geodésico Brasileiro, DATUM - SIRGAS 2000,'+' de coordenadas (Longitude:'+v[1]+', Latitude:'+v[2]+')de altitude '+v[3]+' m; deste segue confrontando com a propriedade de '+v[7]+' com os seguintes azimutes e distâncias: '+v[5]+' e '+v[6]+' m até o vértice '+v[4]
    if k>1:
        memorial=memorial+', de coordenadas (Longitude:'+v[1]+', Latitude:'+v[2]+') de altitude '+v[3]+' m; deste segue confrontando com a propriedade de '+v[7]+' com os seguintes azimutes e distâncias:'+v[5]+' e '+v[6]+' m até o vértice '+v[4]
memorial = memorial + '.'


# In[ ]:


#print(memorial)
if arg:
    file=arg+'.txt'
else:
    file='output.txt'
with open(file,'w') as text_file:
    text_file.write(memorial)
    text_file.close()
print ('Memorial Descritivo Criado com Sucesso: ',cwd,'\\',file)