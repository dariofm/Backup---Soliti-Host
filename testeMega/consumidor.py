from mongo import Uteis
from estaticos import ElementosEstaticos
from bson import ObjectId

elementos = ElementosEstaticos()
banco     = Uteis()
database  = banco.conexao



class Consumidor:
    def __init__(self):
        pass



    def Dados():
        Pessoa = database["Pessoas"]

        for dPessoa in Pessoa.find({"_t.1":"Consumidor"}):

            idConsumidor        = dPessoa["_id"]    
            NumeroCasa          = dPessoa["Carteira"]["EnderecoPrincipal"]["Numero"]
            Logradouro          = dPessoa["Carteira"]["EnderecoPrincipal"]["Logradouro"]
            Bairro              = dPessoa["Carteira"]["EnderecoPrincipal"]["Bairro"]
            Cep                 = dPessoa["Carteira"]["EnderecoPrincipal"]["Cep"]
            Municipio           = dPessoa["Carteira"]["EnderecoPrincipal"]["Municipio"]      
              
        consumidor = {
                "_t" : "ConsumidorHistorico",
                "PessoaReferencia" : idConsumidor,
                "Nome" : "Cliente Consumidor",
                "Classificacao" : {
                    "_t" : "NaoContribuinte"
                },
                "EnderecoPrincipal" : {
                    "Numero" : NumeroCasa,
                    "Logradouro" : Logradouro,
                    "Bairro" : Bairro,
                    "Cep" : Cep,
                    "Municipio" : Municipio
                },
                "Cliente" : {
                    "LimiteCredito" : 0.0
                },
                "IndicadorOperacaoConsumidorFinal" : {
                    "_t" : "ConsumidorFinal",
                    "Codigo" : 1,
                    "Descricao" : "Consumidor final"
                },
                "Ie" : "",
                "IndicadorIeDestinatario" : {
                    "_t" : "NaoContribuinte"
                },
                "InformacoesPesquisa" : [ 
                    "cliente", 
                    "consumidor"
                ]
            }
        return consumidor
    
    
    
