# Hospital Manager
Hospital Manager é uma aplicação web que cuidará de exames feitos por pacientes. Para que um exame seja acessado por alguma pessoa, é necessário esta ter o hash do exame.

## Testes
Está sendo usado a biblioteca padrão do python para testar a aplicação. Para rodar os testes pelo terminal use: 
```
$ python3 -m unittest discover -v ./tests -p test_*.py
```

## Documentação da API
### /
retorna "backend operante" e 200
### /create_tables
cria as tabelas no banco de dados.
Retorna 200
