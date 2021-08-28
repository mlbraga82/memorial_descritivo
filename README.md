# memorial_descritivo
Script para geração de Memorial Descritivo a partir de PDF gerado pelo SIGEF do INCRA<br>
<p>Este Scrypt python foi criado para ser executado, incialmente, em ambiente Windows (vamos trabalhar para permitir ser executado também em Linux), necessita da biblioteca <b>tabula</b> para leitura dos dados em PDF, que por sua vez faz uso do JAVA, portanto é necessário acrescentar tanto a biblioteca do python como o o java na máquina.<br>
  Abordaremos como acrescentar apenas a bilbioteca tabula, mas não abordaremos como instalar o Java, que em princípio a sua máquina já deve ter instalado. <br>
A sintaxe para execução é a seguinte:<br>
<b>python memorial.py [código da parcela SIGEF]<br></b>
<b>Exemplo: <br></b>
python memorial.py 84be2b9c-6883-4512-a4c7-03f8b9e494e8<br><br>
na ausência do [código da parcela SIGEF] o script irá procurar no mesmo diretório o arquivo de nome <i>document.pdf</i><br>
![imagem_01.png](Imagem_01.png)
Esse comando pode ser integrado ao QGIS, usando a função nativa do QGIS "Rodar ação de feição"<br>

  
  
## Link para baixar o shp do SIGEF
Selecionar "Imóvel Certificado SIGEF Total"<br>
https://certificacao.incra.gov.br/csv_shp/export_shp.py

## Criar ação no QGIS PARA ABRIR O PDF (ABRIR URL)
https://sigef.incra.gov.br/geo/parcela/memorial/[%parcela_co%]/
python C:/Users/limab/Downloads/SIGEF/memorial.py [%parcela_co%]

## Variável de ambiente PATH precisa acrescentar o seguinte valor (necessário para a biblioteca tabula.read_pdf
C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath
