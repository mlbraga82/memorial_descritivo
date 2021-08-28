# memorial_descritivo

![Video](https://img.youtube.com/vi/Mcih2ajWie4/0.jpg)<br>[Video de Demonstração - Youtube](https://youtu.be/Mcih2ajWie4)

Script para geração de Memorial Descritivo a partir de PDF gerado pelo SIGEF do INCRA<br>
Este Scrypt python foi criado para ser executado, incialmente, em ambiente Windows (vamos trabalhar para permitir ser executado também em Linux), necessita da biblioteca <b>tabula</b> para leitura dos dados em PDF, que por sua vez faz uso do JAVA, portanto é necessário acrescentar tanto a biblioteca do python como o o java na máquina.<br>
  Abordaremos como acrescentar apenas a bilbioteca tabula, mas não abordaremos como instalar o Java, que em princípio a sua máquina já deve ter instalado. <br>
A sintaxe para execução é a seguinte: `python memorial.py [código da parcela SIGEF].`
<b><br>Exemplo:</b>

`python memorial.py 84be2b9c-6883-4512-a4c7-03f8b9e494e8`

<br><br>na ausência do `[código da parcela SIGEF]` o script irá procurar no mesmo diretório o arquivo de nome <i>document.pdf</i><br>

## Instalação
  Para instalação da biblioteca tabula é necessário executar o `OSGeo4W Shell` e digitar o seguinte comando:<br>
  `pip install tabula` conforme figura abaixo<br><br>
  ![teste](https://github.com/mlbraga82/memorial_descritivo/blob/b2cae23c33babb97613e98fc0ac4bf9c55aaa235/Imagem_04.png)
 <br>
Baixar o arquivo `memorial.py` disponível neste [LINK](https://github.com/mlbraga82/memorial_descritivo/raw/main/memorial.py) Clique com o botão direito e `"Salvar link como..."`
## Integração com o QGIS
   A fim de facilitar e permitir o script executar integrado ao QGIS, vamos usar a função "Ação de feição", após baixar o SHP (Imóvel Certificado SIGEF Total) no [site do INCRA](https://certificacao.incra.gov.br/csv_shp/export_shp.py) e abrir no QGIS, vamos em "Propriedades da camada" e clicar em ações:
  ![Ações](https://github.com/mlbraga82/memorial_descritivo/blob/b2cae23c33babb97613e98fc0ac4bf9c55aaa235/Imagem_02.png)
  <br>É necessário criar uma ação com os seguintes parâmetros:
  `python [caminho do arquivo]/memorial.py [%parcela_co%]`
  Conforme figura abaixo:<br>
  ![Editar Ação](https://github.com/mlbraga82/memorial_descritivo/blob/b2cae23c33babb97613e98fc0ac4bf9c55aaa235/Imagem_01.png)


## Variável de ambiente PATH precisa acrescentar o seguinte valor (necessário para a biblioteca tabula.read_pdf)
Para que a biblioteca TABULA funcione no QGIS é necessário modificar a variável de ambiente **no QGIS** para isso deve-se clicar no menu `Configurações` e depois em `Opções`. Na Aba `Sistema` procure as variáveis de **ambiente** e acrescente a seguinte linha:<br> `C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath` conforme figura abaixo:<br>
![ambiente](https://github.com/mlbraga82/memorial_descritivo/blob/b2cae23c33babb97613e98fc0ac4bf9c55aaa235/Imagem_03.png)
