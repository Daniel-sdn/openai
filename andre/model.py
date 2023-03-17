import requests
import json
import base64
import os 

intentWelcome = ['opa','oi', 'ola', 'olá', 'teste', 'bom dia', 'boa noite', 'boa tarde','menu', 'opções', 'opcoes']
intentBoleto = ['segunda via boleto', 'boleto', 'boletos', 'segunda via de boleto', 'segunda via boletos', 'segunda via']
intentNF = ['nf', 'nro','nota fiscal', 'cópia', 'copia', 'copia nf', 'cópia nf', 'cópia de nf', 'copia de nf','nota']
intentOS = ['consultar ordem de servico', 'consultar ordem de serviço', 'consultar ordem de serviços', 'consultar ordem de servicos','consultar ordens de servico', 'consultar ordens de serviço', 'consultar ordens de serviços', 'consultar ordens de servicos','servico', 'serviço', 'servicos','serviços', 'ordem de servico','ordem de serviço','ordem de serviços','ordem de servicos','ordens','ordem','ordens de servico','ordens de servicos','ordens de serviço','ordens de serviços']
intentRelatorio = ['relatório', 'relatorio', 'relatório de equipamentos', 'relatorio de equipamentos', 'relatório equipamentos', 'relatorio equipamentos','relatório de equipamento', 'relatorio de equipamento', 'relatório equipamento', 'relatorio equipamento', 'equipamento', 'equipamentos']
intentDepartamento = ['falar com um departamento', 'departamento','departamentos','falar departamento','falar departamentos', 'falar com departamento','falar com departamentos']
intentConsultor = ['falar com meu consultor', 'falar consultor', 'falar com consultor','falar meu consultor', 'meu consultor']
jidCadastrados = ['555183082421','555484132623','555591140933', '555196537236', '555193130284', '555194705711', '13059276522', '555496154044']

wdir = os.getcwd()

#Função que identifica o tipo de mensagem recebida


def detectType(wMessage):
    if 'message' in wMessage:
        jid = wMessage['key']['remoteJid']
        parsedJid = jid.split("@")[0]
        if parsedJid in jidCadastrados:
            if 'conversation' in wMessage['message']:
                textMessage(wMessage)
                print('conversa')
            if 'buttonsResponseMessage' in wMessage['message']:
                buttonMessage(wMessage)
                print('botão')
            if 'listResponseMessage' in wMessage['message']:
                listMessage(wMessage)
                print('lista')
        else:
            apiSendMessage(jid, "Desculpe, seu telefone não consta em nosso cadastro.\n\nPara solicitar o seu cadastro acesse o link abaixo:\n\n https://forms.gle/aD9xsevbsGoiqNpm6")

#Função que identifica a mensagem de texto recebida
def textMessage(wMessage):   

    # Mensagem de boas vindas
    if wMessage['message']['conversation'].lower() in intentWelcome:
        jid = wMessage['key']['remoteJid']
        displayText = f"Olá {wMessage['pushName']}, é um prazer atendê-lo, em que posso lhe ajudar?"
        caption = 'Selecione uma opção..'
        buttons = ['Segunda Via de Boleto','Cópia de NF','Consultar Ordens de Serviço', 'Relatório de Equipamentos','Falar com um Departamento', 'Falar com meu Consultor']
        apiSendButton(jid, displayText, caption, buttons)

    # opção segunda via boleto
    elif wMessage['message']['conversation'].lower() in intentBoleto:
        jid = wMessage['key']['remoteJid']
        boletoListBuilder(jid)    

    # opção nota fiscal
    elif wMessage['message']['conversation'].lower() in intentNF:
        jid = wMessage['key']['remoteJid']
        nfListBuilder(jid)

    # opção Ordens de serviço
    elif wMessage['message']['conversation'].lower() in intentOS:
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o tipo da Ordem de Serviço!'
        caption = 'Selecione uma opção..'
        buttons = ['Abertas', 'Fechadas']
        apiSendButton(jid, displayText, caption, buttons)

    # opção de relatorios
    elif wMessage['message']['conversation'].lower() in intentRelatorio:
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o tipo de relatório!'
        caption = 'Selecione uma opção..'
        buttons = ['COLHEITADEIRAS', 'TRATORES', 'PULVERIZADORES']
        apiSendButton(jid, displayText, caption, buttons)
        
    # opção departamentos    
    elif wMessage['message']['conversation'].lower() in intentDepartamento:
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o Departamento desejado!'
        caption = 'Selecione uma opção..'
        buttons = ['Vendas/Pós-Venda', 'Manutenção', 'Financeiro']
        apiSendButton(jid, displayText, caption, buttons)


    # opção de falar com o consultor
    elif wMessage['message']['conversation'].lower() in intentConsultor:
        jid = wMessage['key']['remoteJid']
        message = "*Deixe uma mensagem ou dúvida parar o seu consultor.*\n\nDigite o comando !Duvida e em seguida a sua dúvida ou mensagem.\n\nExemplo:\n _!Duvida - Como faço parar trocar o meu número de telefone no cadastro?_ "
        apiSendMessage(jid, message)

    #opção do comando dúvida
    elif wMessage['message']['conversation'].lower().startswith('!duvida'):
        nProtocolo = 248273
        jid = wMessage['key']['remoteJid']
        duvida = wMessage['message']['conversation']
        message = f"*Protocolo: #{nProtocolo}*\n\n_{duvida}_\n\nObrigado por enviar sua dúvida/mensagem, o seu consultor entrará em contato."
        apiSendMessage(jid, message)
        nProtocolo += 1

    else: 
        jid = wMessage['key']['remoteJid']
        displayText = f"Olá {wMessage['pushName']}, é um prazer atendê-lo, em que posso lhe ajudar?"
        caption = 'Selecione uma opção..'
        buttons = ['Segunda Via de Boleto','Cópia de NF','Consultar Ordens de Serviço', 'Relatório de Equipamentos','Falar com um Departamento', 'Falar com meu Consultor']
        apiSendButton(jid, displayText, caption, buttons)


#Função que identifica a mensagem de botão recebida
def buttonMessage(wMessage):

    #Botão Boleto
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Segunda Via de Boleto':
        jid = wMessage['key']['remoteJid']
        boletoListBuilder(jid) 

    #Botões Ordens de Serviço 
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Consultar Ordens de Serviço':
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o tipo da Ordem de Serviço!'
        caption = 'Selecione uma opção..'
        buttons = ['Abertas', 'Fechadas']
        apiSendButton(jid, displayText, caption, buttons)

    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Abertas':
        jid = wMessage['key']['remoteJid']
        selectedType = "Abertas"
        osListBuilder(jid, selectedType) 

    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Fechadas':
        jid = wMessage['key']['remoteJid']
        selectedType = "Fechadas"
        osListBuilder(jid, selectedType) 


    #Botão NF    
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Cópia de NF':
        jid = wMessage['key']['remoteJid']
        nfListBuilder(jid) 

    #Botões Relatórios
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Relatório de Equipamentos':
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o tipo de Relatório!'
        caption = 'Selecione uma opção..'
        buttons = ['COLHEITADEIRAS', 'TRATORES', 'PULVERIZADORES']
        apiSendButton(jid, displayText, caption, buttons)

    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'COLHEITADEIRAS':
        jid = wMessage['key']['remoteJid']
        tipoRelatorio = 'COLHEITADEIRAS'
        relatoriosByJid(jid, tipoRelatorio)

    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'TRATORES':
        jid = wMessage['key']['remoteJid']
        tipoRelatorio = 'TRATORES'
        relatoriosByJid(jid, tipoRelatorio)
        
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'PULVERIZADORES':
        jid = wMessage['key']['remoteJid']
        tipoRelatorio = 'PULVERIZADORES'
        relatoriosByJid(jid, tipoRelatorio)

    #Botões Falar com Departamento
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Falar com um Departamento':
        jid = wMessage['key']['remoteJid']
        displayText = 'Selecione o Departamento desejado!'
        caption = 'Selecione uma opção..'
        buttons = ['Vendas/Pós-Venda', 'Manutenção', 'Financeiro']
        apiSendButton(jid, displayText, caption, buttons)

    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Vendas/Pós-Venda':
        nProtocolo = 736456
        jid = wMessage['key']['remoteJid']
        message = f"*Protocolo: #{nProtocolo}*\n\nObrigado por entrar em contato, você está sendo transferido para o Departamento:\n\n*Vendas/Pós-Venda*"
        apiSendMessage(jid, message)
        nProtocolo += 1
    
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Manutenção':
        nProtocolo = 465746
        jid = wMessage['key']['remoteJid']
        message = f"*Protocolo: #{nProtocolo}*\n\nObrigado por entrar em contato, você está sendo transferido para o Departamento:\n\n*Manutenção*"
        apiSendMessage(jid, message)
        nProtocolo += 1
    
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Financeiro':
        nProtocolo = 34529
        jid = wMessage['key']['remoteJid']
        message = f"*Protocolo: #{nProtocolo}*\n\nObrigado por entrar em contato, você está sendo transferido para o Departamento:\n\n*Financeiro*"
        apiSendMessage(jid, message)
        nProtocolo += 1


    #Botão Consultor 
    if wMessage['message']['buttonsResponseMessage']['selectedDisplayText'] == 'Falar com meu Consultor':
        jid = wMessage['key']['remoteJid']
        message = "*Deixe uma mensagem ou dúvida parar o seu consultor.*\n\nDigite o comando !Duvida e em seguida a sua dúvida ou mensagem.\n\nExemplo:\n _!Duvida - Como faço parar trocar o meu número de telefone no cadastro?_ "
        apiSendMessage(jid, message)  


#Função que identifica a mensagem de lista recebida
def listMessage(wMessage):
    selectedRowID = wMessage['message']['listResponseMessage']['singleSelectReply']['selectedRowId']

    if selectedRowID.split("-")[0] == 'nf':
        jid = wMessage['key']['remoteJid']
        sendSelectedNF(jid, selectedRowID.split("-")[1])

    if selectedRowID.split("-")[0] == 'boleto':
        jid = wMessage['key']['remoteJid']
        sendSelectedBoleto(jid, selectedRowID.split("-")[1])
    
    if selectedRowID.split("-")[0] == 'ordemAbertas':
        jid = wMessage['key']['remoteJid']
        selectedType = "Abertas"
        sendSelectedOs(jid, selectedRowID.split("-")[1], selectedType)

    if selectedRowID.split("-")[0] == 'ordemFechadas':
        jid = wMessage['key']['remoteJid']
        selectedType = "Fechadas"
        sendSelectedOs(jid, selectedRowID.split("-")[1], selectedType)    
     

# função que envia o relatório selecionado
def relatoriosByJid(jid, tipoRelatorio):
    path = f"{wdir}\\Files\\{tipoRelatorio}"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    fileFound = False 
    for file in dir_list:
        if parsedJid in file:
            filepath = path + '\\' + file
            base64file = pdfToBase64(filepath)
            apiSendFileBase64(jid, base64file, "Relatorio.pdf")
            fileFound = True        
    if fileFound == False:
        apiSendMessage(jid, "Não existem relatórios vinculados a este número de telefone!")

# construtor da lista de Boletos
def boletoListBuilder(jid):
    path = f"{wdir}\\Files\\Boletos"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    fileFound = False
    boletoList = []
    rowsObj = []
    title = "Selecione um Boleto"
    description = "_Selecione seu Boleto para solicitar segunda via_"
    buttonText = "Selecionar Boleto"
    subtitle = "Boletos"
    for file in dir_list:
        if parsedJid in file:
            boletoList.append(file)
            fileFound = True
    for boleto in boletoList:
        boletoID = "boleto-" + boleto.split("_")[1]
        boletoName = boleto.split("_")[1]
        rowsObj.append({
            "title": boletoName,
            "description": f"Boleto: {boletoName}",
            "rowId": boletoID
            })
    print(rowsObj)
    if fileFound == True:
        apiSendList(jid, title, description, buttonText, subtitle, rowsObj)
    else:
        apiSendMessage(jid, "Não existem Boletos vinculados a este número de telefone!")

# construtor da lista de NFs
def nfListBuilder(jid):
    path = f"{wdir}\\Files\\NF"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    fileFound = False
    nfList = []
    rowsObj = []
    title = "Selecione uma NF"
    description = "_Selecione sua NF para solicitar segunda via_"
    buttonText = "Selecionar NF"
    subtitle = "Notas Fiscais"
    for file in dir_list:
        if parsedJid in file:
            nfList.append(file)
            fileFound = True
    for nf in nfList:
        nfID = "nf-" + nf.split("_")[1]
        nfName = nf.split("_")[1]
        rowsObj.append({
            "title": nfName,
            "description": f"Nota Fiscal: {nfName}",
            "rowId": nfID
            })
    print(rowsObj)
    if fileFound == True:
        apiSendList(jid, title, description, buttonText, subtitle, rowsObj)
    else:
        apiSendMessage(jid, "Não existem Notas Fiscais vinculadas a este número de telefone!")


# construtor da lista de Ordens de Serviço
def osListBuilder(jid, selectedType):
    path = f"{wdir}\\Files\\OS\\{selectedType}"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    fileFound = False
    osList = []
    rowsObj = []
    title = "Selecione uma Ordem de Serviço"
    description = "_Selecione sua Ordem de Serviço para solicitar segunda via_"
    buttonText = "Selecionar Ordem de Serviço"
    subtitle = "Ordens de Serviço"
    for file in dir_list:
        if parsedJid in file:
            osList.append(file)
            fileFound = True
    for ordens in osList:
        osID = f"ordem{selectedType}-" + ordens.split("_")[1]
        osName = ordens.split("_")[1]
        rowsObj.append({
            "title": osName,
            "description": f"Ordem de Serviço: {osName}",
            "rowId": osID
            })
    print(rowsObj)
    if fileFound == True:
        apiSendList(jid, title, description, buttonText, subtitle, rowsObj)
    else:
        apiSendMessage(jid, "Não existem Ordens de Serviço vinculadas a este número de telefone!")

def sendSelectedNF(jid, selectedNF):
    path = f"{wdir}\\Files\\NF"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    for file in dir_list:
        if parsedJid in file:
            if selectedNF in file:
                filepath = path + '\\' + file
                base64file = imgToBase64(filepath)
                apiSendFileBase64(jid, base64file, f"{selectedNF}.jpg")

def sendSelectedBoleto(jid, selectedBoleto):
    path = f"{wdir}\\Files\\Boletos"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    for file in dir_list:
        if parsedJid in file:
            if selectedBoleto in file:
                filepath = path + '\\' + file
                base64file = imgToBase64(filepath)
                apiSendFileBase64(jid, base64file, f"{selectedBoleto}.jpg")

def sendSelectedOs(jid, selectedOs, selectedType):
    path = f"{wdir}\\Files\\OS\\{selectedType}"
    dir_list = os.listdir(path)   
    parsedJid = jid.split("@")[0]
    for file in dir_list:
        if parsedJid in file:
            if selectedOs in file:
                filepath = path + '\\' + file
                base64file = imgToBase64(filepath)
                apiSendFileBase64(jid, base64file, f"{selectedOs}.jpg")


def pdfToBase64(filepath):
  image_data = base64.b64encode(open(filepath, "rb").read())
  encoded = image_data.decode()
  base64pdf = 'data:application/pdf;base64,{}'.format(encoded)
  return base64pdf

def imgToBase64(filepath):
  image_data = base64.b64encode(open(filepath, "rb").read())
  encoded = image_data.decode()
  base64img = 'data:image/jpeg;base64,{}'.format(encoded)
  return base64img


########## FUNÇÕES DA MEGA API WHATSAPP ################




def apiSendMessage(jid, message):
    url = "http://api2.megaapi.com.br:15614/sendmessage?token=M_QtGDBOmxRs5DR"

    payload = json.dumps({
    "jid": jid,
    "body": message
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


def apiSendButton(jid, displayText, caption, buttons):
    url = "http://api2.megaapi.com.br:15614/sendbutton?token=M_QtGDBOmxRs5DR"

    payload = json.dumps({
    "jid": jid,
    "type": "text",
    "displayText": displayText,
    "caption": caption,
    "buttons": buttons
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


def apiSendList(jid,title,description,buttonText,subtitle,rowsObj):
    url = "http://api2.megaapi.com.br:15614/sendlist?token=M_QtGDBOmxRs5DR"

    payload = json.dumps({
    "jid": jid,
    "title": title,
    "description": description,
    "buttonText": buttonText,
    "sections": [
        {
        "title": subtitle,
        "rows": rowsObj
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

def apiSendFileBase64(jid, base64file, filename):
    url = "http://api2.megaapi.com.br:15614/sendfilebase64?token=M_QtGDBOmxRs5DR"

    payload = json.dumps({
    "jid": jid,
    "body": base64file,
    "caption": "",
        "filename": filename})
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

