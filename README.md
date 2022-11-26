# teste-tecnico-back-end

## Uma interface web que aceita upload do um arquivo CNAB, normaliza os dados e armazena em um banco de dados relacional e exibe essas informações tratadas em tela.

### Antes de tudo algumas configurações talvez sejam nacessarias então vamos verificar 
#### Primeiramente no arquivo [Back end > _project > settings > CORS_ALLOWED_ORIGINS] verifique se algum dos end points corresponde com qual você utiliza normalmente no front end, caso não basta acrescentar o seu end Point
![Screenshot_5](https://user-images.githubusercontent.com/67373130/204097611-96145f0b-5eaf-4b1c-b501-02976466656f.png)
##### Essa configuração se faz necessaria para o CORS liberar o acesso ao end Point para fazer requisições

#### Logo em seguida vamos verficar no arquivo [Front end > src > App.js] se o onde point localizado no axios corresponde com o end point utilizado pelo seu servidor local no back end
![Screenshot_6](https://user-images.githubusercontent.com/67373130/204097763-22a33238-0845-4ae4-b8de-76d756abb252.png)
##### Essa configuração so se faz necessario caso utilize algum servidor local diferente do padrão já pre configurado 


### #Agora vamos para as configurações de execução dos arquivos de Back e Front end

#### Primeiramente clonamos o respositorio e logo partimos para as configurações específicas

### #Para o Back end vamos serquir os seguintes passos.
#### Primeiro vamos criar um ambiente virtual para podermos rodar nossos codigos sem interferencias externas com o seguinte comando [python -m venv venv] 
#### Logo depois vamos entrar nesse ambiente virtual com o seguinte comando para Linux [source venv/bin/activate], para Windows [venv/Scripts/activate]
#### Agora podemos rodar o comando para instalar as dependencias útilizadas no projeto [pip install -r requirements.txt]
#### E para finalizar podemos usar o comando para rodar nosso projeto [python ./manage.py runserver]

### #Para o Front end vamos serquir os seguintes passos.
#### Primeiro vamos abrir o arquivo e instalar as dependencias com o comando [yarn ou npm]
#### Logo em seguida já podemos rodar nossa aplicação com o comando [yarn start ou npm start]
