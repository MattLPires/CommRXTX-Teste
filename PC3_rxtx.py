import serial

# Criando a comunicação
rxtxpc2 = serial.Serial("/dev/pts/15")
rxtxpc4 = serial.Serial("/dev/pts/17")

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
  while pc_des not in ("PC1","PC2","PC4"):
    pc_des = (str(input("Mensagem para qual PC? Exemplo: PC1> ")).strip()).upper()
  
  msg = str(input("Qual a mensagem? > "))
  
  msgenv =  pc_des+"|"+ msg +"\n"
  
  if   pc_des == "PC4":
    rxtxpc4.write(msgenv.encode())
  else:
    rxtxpc2.write(msgenv.encode())

else:

  msg = rxtxpc2.readline() # Retirar comentário quando for receber do PC2 
  #msg = rxtxpc4.readline() # Retirar comentário quando for receber do PC4 
  
  div_string = (msg.decode()).split(sep="|")

  if   div_string[0] == "PC4":
    rxtxpc4.write(msg)
    print("Mensagem enviada ao PC4!")
    
  elif div_string[0] in ("PC1","PC2"):
    rxtxpc2.write(msg)
    print("Mensagem enviada ao PC2!")
    
  else:
    print("Mensagem recebida: ", div_string[1])