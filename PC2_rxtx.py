import serial

# Criando a comunicação
rxtxpc1 = serial.Serial("/dev/pts/13")
rxtxpc3 = serial.Serial("/dev/pts/14")

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
  while pc_des not in ("PC1","PC3","PC4"):
    pc_des = (str(input("Mensagem para qual PC? Exemplo: PC1> ")).strip()).upper()
  
  msg = str(input("Qual a mensagem? > "))
  
  msgenv =  pc_des+"|"+ msg +"\n"
  
  if   pc_des == "PC1":
    rxtxpc1.write(msgenv.encode())
  else:
    rxtxpc3.write(msgenv.encode())

else:

  msg = rxtxpc1.readline() # Retirar comentário quando for receber do PC1 
  #msg = rxtxpc3.readline() # Retirar comentário quando for receber do PC3
  
  div_string = (msg.decode()).split(sep="|")

  if   div_string[0] == "PC1":
    rxtxpc1.write(msg)
    print("Mensagem enviada ao PC1!")
    
  elif div_string[0] in ("PC3","PC4"):
    rxtxpc3.write(msg)
    print("Mensagem enviada ao PC3!")
    
  else:
    print("Mensagem recebida: ", div_string[1])