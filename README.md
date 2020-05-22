#### Servidor de fundo DuzzClean

##### Como Funciona:
O servidor fica em modo handler, aguardando requisições. As requisições resultam em retornos, mas não necessariamente é somente GET info. 

##### Serviços:

Os serviços estarão listados no fim deste documento, porém também estão disponíveis pelo [PROJETO](https://github.com/Duzz-Clean/DuzzClean-API/projects/1), ou pelo [Escopo de Desenvolvimento](https://github.com/Duzz-Clean/DuzzClean-API/issues/1)

##### Rotas:

**_Atenção! Para uso das rotas, com excessão do novo usuário e autenticar usuário, é necessário informar as seguintes chaves-valores:_**

    ["Username"] = Nome de usuario ou email,
    ["UserType"] = Tipo do usuário,
    ["Token"] = Token de acesso à aplicação


**_As rotas obrigatórias para as demais estão descritas:_**


*__/novo_veiculo__*
        
    Função : Encaminhar para fazer o cadastramento de um novo veículo
    Método : POST
    Entrada:
        JSON: 
            ["LicensePlate"] = Placa do carro;
            ["Username] = Usuário do motorista;
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/novo_usuario__*

    Função : Encaminhar para fazer o cadastramento de um novo usuário;
    Método : POST
    Entrada:
        JSON:
            ["Username"] = Nome de usuário ou email;
            ["Password"] = Senha digitada pelo usuário
            ["FirstName"] = Primeiro nome do usuário
            ["SecondName"] = Segundo nome do usuário
            ["UserType"] = Tipo de usuário (1, 2, 3)
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/nova_limpeza__*
    
    Função: Encaminha para fazer o cadastramento de uma nova limpeza
    Método: POST
    Entrada:
        JSON:
            ["LicensePlate"] = Placa do carro
            ["Date"] = Data e hora e segundos realização
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro



*__/nova_avaliacao__* 

    Função : Encaminha para fazer o cadastramento de uma nova avaliação;
    Método : POST
    Entrada:
        JSON:
            ["LicensePlate"] = Placa do carro
            ["Rating"] = Nota de 0 a 5
            ["Comment"] = Comentários do usuário
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/recusa_notificacao__* 

    Função : Encaminha para salvar a recusa de notificação de limpeza do veículo;
    Método : POST
    Entrada:
        JSON:
            ["LicensePlate"] = Placa do carro
            ["Date"] = Data hora e segundos da recusa
            ["NotificationId"] = ID da notificação recusada
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/grava_envio_notificao__* 

    Função : Encaminha para gravar no bd do veículo as notificações que ele recebeu;
    Método : POST
    Entrada:
        JSON:
            ["NotificationId"] = ID da notificação enviada
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro
        

*__/solicitar_limpeza__*  
    
    Função : Encaminha o usuário para mandar notificação ao veículo solicitando nova limpeza;
    Método : POST
    Entrada:
        JSON:
            ["LicensePlate"] = Placa do carro
            ["Username"] = Nome de usuário ou email
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/autenticar_usuario__*

    Função : Encaminha onde o usuário será autenticado para entrar no app;
    Método : POST
    Entrada:
        JSON:
            ["Username"] = Nome de usuário ou email
            ["Password"] = Senha digitada pelo usuário
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro

*__/buscar_notificacoes__

    Função : Encaminha para busca as notificações recebidas;
    Método : POST
    Entrada:
        Variável:
            username = Nome de usuário ou email
    Retorno:
        JSON:
            ["Message"] = Chave valor de Notificações ou Descrição de erro

*__/buscar_limpezas_veiculo__*

    Função : Encaminha para mostrar as limpezas do veículo;
    Método : POST
    Entrada:
        Variável:
            license_plate = Placa do carro
    Retorno:
        JSON:
            ["Message"] = Chave valor de limpezas ou Descrição de erro

*__/buscar_resumo_veiculo__*

    Função : Encaminha para mostra ao cliente o resumo de um veículo;
    Método : POST
    Entrada: 
        Variável:
            license_plate = Placa do carro
    Retorno:
        JSON:
            ["Message"] = Chave valor do resumo ou Descrição de erro
*__/buscar_ultima_limpeza_veiculo__*

    Função : Encaminha para mostrar quando foi a última limpeza do veículo.
    Método : POST
    Entrada:
        Variável:
            license_plate = Placa do carro
    Retorno:
        JSON:
            ["Message"] = Chave valor de limpeza ou Descrição de erro

*__/realizar_logoff__*

    Função : Realizar logoff
    Método: POST
    Entrada:
        Variável:
            Username = Nome de usuário ou email
            UserType = Tipo de usuário (1, 2, 3)
    Retorno:
        JSON:
            ["Message"] = "OK" ou Descrição de erro
