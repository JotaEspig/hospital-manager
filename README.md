# Hospital Manager
Hospital Manager é uma aplicação web que cuidará de exames feitos por pacientes. Para que um exame seja acessado por alguma pessoa, é necessário esta ter o hash do exame.

## Testes
Está sendo usado a biblioteca padrão do python para testar a aplicação. Para rodar os testes pelo terminal use: 
```
python3 -m unittest discover -v ./tests -p test_*.py
```

## Documentação da API
### /
Retorna "backend operante" e 200

### /create_tables
cria as tabelas no banco de dados.
Retorna 200

### /frontend/\<path_to_file\>
Abre arquivos presentes na pasta frontend

### /login
Faz o login

Recebe (x-www-form-urlencoded):
 - username
 - password

Retorna:
 - 200
 - 400
 - 401

### /signup
Faz o cadastro

Recebe (x-www-form-urlencoded):
 - username
 - password

Retorna:
 - 200
 - 400
 - 409

### /exame/get
Pega o exame por meio do parâmetro "hash" na ULR. Exemplo: http://localhost:5000/exame/get?hash=hash_do_exame
Retorna:
- 200 e JSON com o exame
- 400
- 404

### /exame/get_image
Pega a imagem do exame (caso não exista retorna 404) por meio do parâmetro "hash" na ULR. Exemplo: http://localhost:5000/exame/get_image?hash=hash_do_exame
Retorna:
- 200 e a imagem do exame
- 404

### /exame/add
Adiciona um exame no banco de dados.

Recebe (x-www-form-urlencoded):
 - id
 - nome
 - descricao
 - resultado
 - paciente_id
 - medico_id
 - doenca_id
 - hospital_id

Retorna:
 - 200 e o hash do exame
 - 400

### /exame/save_image
Salva uma imagem relacionada com exames no banco de dados

Recebe:
 - Arquivo

Retorna:
 - 200
 - 500

### /exame/associate_image
Associa uma imagem salva com uma exame

Recebe (x-www-form-urlencoded):
 - hash
 - filename

Retorna:
 - 200
 - 404

### /doenca/get
Pega uma doença de acordo com o id por meio do parâmetro "id" na ULR. Exemplo: http://localhost:5000/doenca/get?id=id_de_doenca

Retorna:
- 200 e JSON da doença
- 404

### /doenca/get_all
Pega todos os doenças do banco de dados

Retorna:
 - 200 e JSON dos doenças

### /hospital/get
Pega um hospital de acordo com o id por meio do parâmetro "id" na ULR. Exemplo: http://localhost:5000/hospital/get?id=id_de_hospital

Retorna:
- 200 e JSON da hospital
- 404

### /hospital/get_all
Pega todos os hospitals do banco de dados

Retorna:
 - 200 e JSON dos hospitals

### /medico/get
Pega um medico de acordo com o id por meio do parâmetro "id" na ULR. Exemplo: http://localhost:5000/medico/get?id=id_de_medico

Retorna:
- 200 e JSON da medico
- 404

### /medico/get_all
Pega todos os medicos do banco de dados

Retorna:
 - 200 e JSON dos medicos

### /paciente/get
Pega um paciente de acordo com o id por meio do parâmetro "id" na ULR. Exemplo: http://localhost:5000/paciente/get?id=id_de_paciente

Retorna:
- 200 e JSON da paciente
- 404

### /paciente/get_all
Pega todos os pacientes do banco de dados

Retorna:
 - 200 e JSON dos pacientes
