### Dentro do Docker: 1.1.0

_Necessários instalar:_

- nada

### Para fazer modificações, teste-as primeiro dentro de uma _virtualenv_

# - 1ª Etapa: baixar o repositório

#### _Vá para a pasta: projetao-back_

```git pull --all```

```git switch dev```

## - \*Etapa opcional: instalar as dependências (ler observação abaixo)

##### _obs.: o requirements.txt só precisa ser usado enquanto a imagem do docker não as tiverem_

#### _Dentro da pasta: projetao-back_

```pip install -r requirements.txt```

# - 2ª Etapa: rodar e configurar o mariadb

```service mysql start```

```mariadb```

_Na bash do MariaDB (MariaDB [(none)]>):_

```CREATE DATABASE apisemglu;```

```CREATE USER 'administrativo'@'localhost' IDENTIFIED BY 'password';```

```GRANT ALL PRIVILEGES ON apisemglu.\* TO 'administrativo'@'localhost';```

```FLUSH PRIVILEGES;```

_Para sair da bash do MariaDB:_

```exit```

# - 3ª Etapa: adicionar tabelas à database: apisemglu

#### _Vá para a pasta: projetao-back/apisemglu_

_Criando as tabelas do projeto: apisemglu_

```python3 manage.py migrate```

_Criando as tabelas do aplicativo: semglu_

```python3 manage.py makemigrations semglu```

```python3 manage.py migrate```

Obs.: esse mesmo processo deve ser feito quando modificar a pasta models.py

#### Agora é possível realizar o povoamento das tabelas 😎👍

_Para acessar a database "apisemglu" criada_

```mariadb```

_Na bash do MariaDB (MariaDB [(none)]>):_

```use apisemglu```

### Agora temos nossas tabelas criadas, vamos iniciar nosso servidor

# - 4ª Etapa: preparando o HTTPS usando certificado SSL

#### _Baseado no tutorial: https://timonweb.com/django/https-django-development-server-ssl-certificate/_

##### \*Opcional quando o mkcert já estiver instalando no docker:

_Instalando o mkcert_

```brew install mkcert```

_Instalando a autoridade de certificado local no espaço de confiança do sistema:_

```mkcert -install```

#### _Na pasta: projetao-back/apisemglu_

_Gerando o certificado para o domínio: localhost_

```mkcert localhost```

# - 5ª Etapa: iniciando servidor (finalmente 😉)

#### _Na pasta: projetao-back/apisemglu_

_Iniciando o servidor HTTP (usamos esse método na VM do CIn)_

```python3 manage.py runserver 0.0.0.0:8000```

_Iniciando o servidor HTTPS com o certificado e chaves SSL_

```python3 manage.py runserver_plus --cert-file localhost.pem --key-file localhost-key.pem```

### Agora temos nosso servidor da API iniciado, vamos testá-lo

##### - De acordo com a documentação do _curl_, como nosso certificado _"localhost"_ não é público e nem confiável, precisamos mostrar a localização dele com a opção --cacert [PATH]. Referência: https://curl.se/docs/sslcerts.html

##### - _Abra outra instância do mesmo docker e vá para a pasta: /projetao-back/apisemglu_

# - 6ª Etapa: adicionando certificado à pasta de certificados do sistema

#### _Na pasta: projetao-back/apisemglu_

_Copiando o certificado "localhost" para a pasta "/etc/ssl/certs/"_

```cp localhost.pem /etc/ssl/certs/```

# - 7ª Etapa: requisitando a lista de produtos como exemplo

#### _Na pasta: projetao-back/apisemglu_

_Com o certificado "localhost.pem" na mesma pasta (caso não esteja na mesma pasta, colocar o PATH):_

```curl https://localhost:8000/products/ --cacert localhost.pem```
