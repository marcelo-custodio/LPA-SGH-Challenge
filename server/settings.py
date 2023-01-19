import os

#MONGO_USER = "cafe-com-leite"
#MONGO_PASSWORD = "nw2A9rwx8QxmXmCRkZMrGF38pmuSWsDK"
MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASSWORD = os.environ["MONGO_PWD"] 
""" 
Usuário e senha do MongoDB do desafio

ATENÇÃO: EM PRODUÇÃO OU TRABALHANDO COM DADOS VERÍDICOS, NUNCA COLOQUE SENHAS OU DADOS DE ACESSO DE BANCO DE DADOS NO CÓDIGO FONTE. Essas informações estão sendo salvas aqui apenas para fins educativos, uma vez que o banco de dados do desafio é público e não contém dados sensíveis.
"""

#MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@sgh.6yzqa.mongodb.net/?readOnly=true"
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@lpa-sgh-challenge.hd07rp6.mongodb.net/?retryWrites=true&w=majority"