# Importa o módulo de cliente Twilio
from twilio.rest import Client

# Adiciona o Account SID - substitua 'AC0fd3d178c3efabf8110a95c89e1a5bcd' pelo seu Account SID
account_sid = 'account_sid'

# Adiciona o Auth Token - substitua 'fc6c433184d9fa0f2a00e591713eb3b3' pelo seu Auth Token
auth_token = 'auth_token'

# Cria um cliente com as credenciais fornecidas
client = Client(account_sid, auth_token)

# Cria uma mensagem com o texto 'Olá, isso é um teste da api de sms do TWILIO',
# 'from' número do Twilio e 'to' número do destinatário
message = client.messages.create(
    body = "Olá, isso é um teste da api de sms do TWILIO",
    from_='+111111111111',  # Substitua pelo seu número Twilio
    to='+111111111111'  # Substitua pelo número do destinatário
)

# Imprime a ID da mensagem
print(message.sid)



