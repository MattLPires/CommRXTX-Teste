import serial

# Criando a comunicação
txrxpc2 = serial.Serial("/dev/pts/12")

# Declarando as variáveis para os input´s
enviaMsg = ""
pc_des   = ""

# Verificar com o usuário se o PC será para Receber ou Enviar mensagem
enviaMsg = (str(input("Mensagem: 1=Enviar/2=Receber >")).strip()) 

# Laço até que a resposta do usuário seja satisfatória
while enviaMsg not in ("1","2"):
  enviaMsg = (str(input("Mensagem: 1=Enviar/2=Receber >")).strip())

# Se o usuário escolher enviar mesnagem, prepara o envio
if enviaMsg == "1":
  pc_des = (str(input("Mensagem para qual PC? Exemplo: PC1> ")).strip()).upper()
  while pc_des not in ("PC2","PC3","PC4"):
    pc_des = (str(input("Mensagem para qual PC? Exemplo: PC1> ")).strip()).upper()
  
  msg = str(input("Qual a mensagem? > "))
  
  msgenv =  pc_des+"|" + msg +"\n"
  txrxpc2.write(msgenv.encode())
  
else:
  
  msg = txrxpc2.readline()
 
  div_string = (msg.decode()).split(sep="|")
  print("Mensagem recebida: ", div_string[1])

   

