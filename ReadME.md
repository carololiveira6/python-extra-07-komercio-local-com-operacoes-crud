## **Table of Contents**
- [Extra - Operações Básicas de uma Aplicação Backend](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#e5---rotas-k%C3%A1sicas-%C3%BAltilizando-flask) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f362b6b10)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f362b6b11)
  - [Rota de Listagem](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1eg6l938o6l) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcepvk0)
  - [Rota de Obtenção de um Produto Único](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcepvk1) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcf5ei2)
  - [Rota de Criação de Produto](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcepvk1) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcf5ei2)
  - [Rota de Atualização de um Produto](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcepvk1) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcf5ei2)
  - [Rota de Deleção de um Produto](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcepvk1) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f3bcf5ei2)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1f362b6b12) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_ee_01_komanda-crud.html&ref=master#mcetoc_1eh146n6m3)
# **Extra - Operações Básicas de uma Aplicação Backend**
Nesta entrega você irá criar cinco rotas de operações CRUD
## **Objetivo**
Essa atividade foi elaborada para trabalhar o que você aprendeu sobre requisições com Flask.
## **Preparativos**
Você deve criar um arquivo chamado **app.py,** nele você irá criar as suas rotas.
## **Rota de Listagem**
- **Endpoint da rota:** /products
- **Nome da função da rota:** list\_products()
- **Métodos Aceitos: GET**
- **Status Code: 200 - OK**
- **Retorno da rota:** Uma lista de dicionários de acordo com os produtos cadastrados
### **Exemplo**
![](Aspose.Words.cac39885-482c-46e8-84e8-b0296dfb510e.001.png)


## **Rota de Obtenção de um Produto Único**
- **Endpoint da rota:** **/products/<id>**
- **Nome da função da rota:** get(product\_id: int)
- **Métodos Aceitos: GET**
- **Status Code: 200 - OK**
- **Retorno da rota:** O produto com id idêntico ao solicitado por string param, em formato de dicionário
### **Exemplo**
![](Aspose.Words.cac39885-482c-46e8-84e8-b0296dfb510e.002.png)
## **Rota de Criação de Produto**
- **Endpoint da rota:** **/products/**
- **Nome da função da rota:** create()
- **Métodos Aceitos: POST**
- **Status Code: 201 - CREATED**
- **Retorno da rota:** O produto recém criado, porém, com seu id, em formato de dicionário
### **Exemplo**
![](Aspose.Words.cac39885-482c-46e8-84e8-b0296dfb510e.003.png)


## **Rota de Atualização de um Produto**
- **Endpoint da rota:** **/products/<id>**
- **Nome da função da rota:** update(product\_id: int)
- **Métodos Aceitos: PATCH & PUT**
- **Status Code: 204 - NO CONTENT**
- **Retorno da rota:** Esta rota não tem retorno
### **Exemplo**
![](Aspose.Words.cac39885-482c-46e8-84e8-b0296dfb510e.004.png)


## **Rota de Deleção de um Produto**
- **Endpoint da rota:** **/products/<id>**
- **Nome da função da rota:** delete(product\_id: int)
- **Métodos Aceitos: DELETE**
- **Status Code: 204 - NO CONTENT**
- **Retorno da rota:** Esta rota não tem retorno
### **Exemplo**
![](Aspose.Words.cac39885-482c-46e8-84e8-b0296dfb510e.005.png)



-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **app.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|1|GET - Rota **/products**|Fazer a requisição na rota|Retornar uma lista de dicionários|
|1|GET - Rota **/products/<id>**|Fazer a requisição na rota|Retornar um dicionário com o produto especifico|
|1|POST - Rota **/products**|Fazer a requisição na rota|Criar um produtoRetornar um dicionário representando o produto criado|
|1|DELETE - Rota **/products/<id>**|Fazer a requisição na rota|Retornar um status code 204|
|1|PATCH/PUT - Rota **/products/<id>**|Fazer a requisição na rota|Retornar um status code 204|
**Boa diversão, devs!** 😸










