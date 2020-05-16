#### Servidor de fundo DuzzClean

##### Como Funciona:
O servidor fica em modo handler, aguardando requisições. As requisições resultam em retornos, mas não necessariamente é somente GET info. 

##### Serviços:

Os serviços estarão listados no fim deste documento, porém também estão disponíveis pelo [PROJETO](https://github.com/duzzsys/duzz_clean/projects/1), ou pela [ISSUE #3](https://github.com/duzzsys/duzz_clean/issues/3)

##### Requests:

Padrão de requisição:
Separador padrão ','. Entre request e parametro → ';' 
Tipo de request → Entry, or Out

Interface solicitante → Motorista or Client

Requisição → Serviço desejado
Separador → ';'
Parametros

##### Example: 
````
request = 'E,MOT,LIMPEZA,DADOS;data_nascimento,nascimento,km,tipo,'objeto_limpos'
````
###### Tipos de requisição:
'E' → Entrada de dados;
'O' → Saída de dados;

###### Interfaces:
'MOT' → Motorista do veículo
'CLI' → Usuário cliente

###### Serviços:
**Motorista**
_Entradas de dados:_
    
    ->  Request     : 'new_clean' Informar limpeza realizada 
        Parametros  : Placa_carro, data, nascimento('Notificação', 'Agendada', 'Clicada')

    ->  Request     : 'new_clean_man' Informar manutenção realizada
        Parametros  : Placa_carro, data, nascimento('Notificação', 'Agendada', 'Clicada')

    ->  Request     : 'new_refusal' Informar notificação de limpeza ignorada
        Parametros  : Placa_carro, data, quilometragem última limpeza
_Saída de dados:_

    ->  Request     : 'view_rating' Buscar a nota de avaliação do carro
        Parametros  : Placa_carro

    ->  Request     : 'view_descuido' Buscar média de não limpeza quando notificado
    ->  Parametros  : Placa_carro 

**Cliente**
_Entrada de dados:_

    ->  Request     : 'new_feedback' Informar feedback do cliente
    ->  Parametros  : Placa_carro, nota, comentário

_Saída de dados:_

    ->  Request     : 'view_rating' Buscar rating do carro
    ->  Parametros  :  Placa_carro

    ->  Request     : 'view_last_clean' Buscar última limpeza do carro
    ->  Parametros  : Placa_carro


    ->  Request     : 'view_descuido' Buscar média de não limpeza quando notificado
    ->  Parametros  : Placa_carro 