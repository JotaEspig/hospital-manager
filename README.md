# Hospital Manager
Hospital Manager é uma aplicação web que cuidará de exames feitos por pacientes. Para que um exame seja acessado por alguma pessoa, é necessário esta ter o hash do exame.

## Testes
Está sendo usado a biblioteca padrão do python para testar a aplicação. Para rodar os testes pelo terminal use: 
```
python3 -m unittest discover -v ./tests -p test_*.py
```

## Documentação da API
### /
retorna "backend operante" e 200
### /create_tables
cria as tabelas no banco de dados.
Retorna 200
### /exame/get
Pega o exame por meio do parâmetro "hash" na ULR. Exemplo: http://localhost:5000/exame/get?hash=hash_do_exame
Retorna:
- 200 e JSON com o exame
- 400 (má formação da requisição)
- 404 exame não encontrado
### /exame/get_image
Pega a imagem do exame (caso não exista retorna 404) por meio do parâmetro "hash" na ULR. Exemplo: http://localhost:5000/exame/get_image?hash=hash_do_exame
Retorna:
- 200 e JSON com a imagem do exame
- 404 exame ou imagem não encontrada