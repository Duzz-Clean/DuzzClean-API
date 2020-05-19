#### Servidor de fundo DuzzClean

##### Como Funciona:
O servidor fica em modo handler, aguardando requisições. As requisições resultam em retornos, mas não necessariamente é somente GET info. 

##### Serviços:

Os serviços estarão listados no fim deste documento, porém também estão disponíveis pelo [PROJETO](https://github.com/Duzz-Clean/DuzzClean-API/projects/1), ou pelo [Escopo de Desenvolvimento](https://github.com/Duzz-Clean/DuzzClean-API/issues/1)

##### Rotas::

Rota: "/novo_veiculo" =  encaminhar para fazer o cadastramento de um novo veículo;
Rota: "/novo_usuario" = encaminhar para fazer o cadastramento de um novo usuário;
Rota: "/nova_limpeza" = encaminha para fazer o cadastramento de uma nova limpeza;
Rota: "/nova_avaliacao" = encaminha para fazer o cadastramento de uma nova avaliação;
Rota: "/recusa_notificacao" = encaminha para salvar a recusa de notificação de limpeza do veículo;
Rota: "/grava_envio_notificao" = encaminha para gravar no bd do veículo as notificações que ele recebeu;
Rota: "/solicitar_limpeza" = encaminha o usuário para mandar notificação ao veículo solicitando nova limpeza;
Rota: "/autenticar_usuario" = encaminha onde o usuário será autenticado para entrar no app;
Rota: "/buscar_notificacoes" = encaminha para busca as notificações recebidas;
Rota: "/buscar_limpezas_veiculo" = encaminha para mostrar as limpezas do veículo;
Rota: "/buscar_resumo_veiculo" = encaminha para mostra ao cliente o resumo de um veículo;
Rota: "/buscar_ultima_limpeza_veiculo" = encaminha para mostrar quando foi a última limpeza do veículo.
