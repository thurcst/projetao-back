## Caso esteja usando a imagem 1.1.0 ou superior do Docker, podes pular para a 4ª Etapa. 😎
## Caso não, podes continuar normalmente a partir da 1ª Etapa. 😀👍
### Dentro do Docker: 1.1.0

_Necessários instalar:_

- nada

### Para fazer modificações, teste-as primeiro dentro de uma _virtualenv_

# - 1ª Etapa: baixar o repositório

#### _Vá para a pasta: projetao-back_

```git pull --all```

```git switch dev```

## - \*Etapa opcional: instalar as dependências (ler observação abaixo)

##### _obs.: o requirements.txt só precisa ser usado enquanto a imagem do docker não as tiverem ou estiver instalando localmente_

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

# - 4ª Etapa: iniciando servidor (finalmente 😉)

#### _Na pasta: projetao-back/apisemglu_

_Iniciando o servidor HTTP (usamos esse método na VM do CIn)_

```python3 manage.py runserver 0.0.0.0:8000```

### Agora temos nosso servidor da API iniciado, vamos testá-lo

# - 5ª Etapa: criando superuser e adquirindo tokens de autenticação

#### _Abra outro terminal e vá para a pasta: /projetao-back/apisemglu_

### Criando superuser

```python3 manage.py createsuperuser```

##### - Insira os dados necessários e guarde-os

### Fazendo login e recebendo refresh token e access token

_Substitua <usuario> e <senha> pelos criados para o superuser_

```curl -X POST http://localhost/api/token/ -H 'Content-Type: application/json' -d '{"username":"<usuario>","password":"<senha>"}'```

##### - Ele retornará um JSON com os tokens de refresh e access, guarde-os

### *Caso o access token expire, crie um novo usando o de refresh
  
_Substitua <token_refresh> pelo recebido no Login_
  
```curl -X POST http://localhost/api/token/refresh/ -H 'Content-Type: application/json' -d '{"refresh":"<token_refresh>"}'```
  
### *Caso o refresh token expire, um novo login precisará ser realizado

# - 6ª Etapa: requisitando a lista de produtos como exemplo

### Usando o token de acesso enquanto ele for válido
_Substitua <token_acesso> pelo access token_

```curl https://localhost:8000/products/ -H 'Authorization: <token_acesso>'```
