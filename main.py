
import yfinance

ticker = input('Digite o codigo da ação: ')
dados = yfinance.Ticker(ticker)

print(dados.history())  

tabela = dados.history('6mo')
print(tabela)

fechamento = tabela.Close
print (fechamento)

print(fechamento.plot)

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(maxima)
print(minima)
print(atual)


import pyautogui
import pyperclip

destinatario = 'Gabrielrochads123@gmail.com' #email que deseja enviar o relatorio
assunto = 'Analise Diaria'

mensagem = f'''Bom dia,
Segue abaixo as analises da ação {ticker} dos ultimos seis meses:

Cotação maxima: R${round(maxima, 2)}
Cotação minima: R${round(minima, 2)}
Cotação atual: R${round(minima, 2)}
Atenciosamente,
Gabriel Rocha. 
'''

print(destinatario)
print(assunto)
print(mensagem)

	
#abrir o navegador 

###Automatização do envio###

#configuraçaão de uma pausa de 3segs do pyautogui
pyautogui.PAUSE = 3 

#abrir uma  nova aba
pyautogui.hotkey('ctrl', 't')

#copiar o endereço d gmail para o clipboard
pyperclip.copy('www.gmail.com')

#colar o endereço do gmail e e dar enter
pyautogui.hotkey('ctrl', 'v')       
pyautogui.press('enter')

# abrindo o 'escrever' gmail 
pyautogui.hotkey('c')

#preenchendo o destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

#preenchendo o assunto
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

#preenchendo a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')

#clicando botao enviar
pyautogui.hotkey('ctrl', 'enter')

#fechar aba gmail                                        
pyautogui.hotkey('ctrl', 'f4')

#imprimir mensagem de envio com sucesso
print('E-mail enviado com sucesso!')