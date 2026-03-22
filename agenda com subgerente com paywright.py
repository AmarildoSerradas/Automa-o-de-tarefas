#instalar o playwright
#pip install
#playwright install

#abrir um navegador
import time as tm
from playwright.sync_api import sync_playwright
import re

from datetime import datetime, timedelta

import time
# data de hoje
hoje = datetime.today()
DataHoje = hoje.strftime("%Y-%m-%d")  # formata como 2025-10-04

# data de ontem
ontem = hoje - timedelta(days=1)
DataOntem = ontem.strftime("%Y-%m-%d")
DataOntemBR = ontem.strftime("%d/%m/%Y")

resultado = dict()

mensagem_final = []

Lojas = [1, 2, 3, 5, 6, 7]
with sync_playwright() as pw:
    navegador = pw.chromium.launch_persistent_context(user_data_dir="Amarildomtfd" , headless=False)
    pagina = navegador.new_page()

    #ir para o nosso cadastro
    pagina.goto("https://sisvarandas2.com.br/ag")
    tm.sleep(5)

    #selecionar um elemento na tela
    pagina.get_by_role("textbox", name="Nome do Usuário")
    pagina.get_by_role("textbox", name="Nome do Usuário").fill("")
    #selecionar o campo de senha
    pagina.get_by_role("textbox", name="Senha").fill("")
    pagina.get_by_text("Entrar").click()

    #selecionar o campo de busca
    pagina.get_by_role("link", name=" Cadastro ").click()
    pagina.get_by_role("link", name="Tarefas", exact=True).click()

    def campodebusca():
        pagina.get_by_role("button", name="").click()
        pagina.get_by_role("link", name="Busca Avancada").click()
        pagina.locator("#srchOpt_1_Data").click()
        pagina.keyboard.press("ArrowDown")
        pagina.keyboard.press("Enter")
        pagina.get_by_role("textbox", name="Data").click()
        pagina.get_by_role("textbox", name="Data").fill(DataOntem)
        tm.sleep(0.5)
        pagina.get_by_text("Buscar", exact=True).click()
        pagina.keyboard.press("Enter")
        for loja in Lojas:
            pagina.get_by_role("button", name="").click()
            pagina.get_by_role("link", name="Busca Avancada").click()
            pagina.get_by_role("textbox", name="Data").click()
            pagina.get_by_role("textbox", name="Data").clear()
            pagina.get_by_role("textbox", name="Data").fill(DataOntem)
            pagina.get_by_role("textbox", name="Loja").click()
            pagina.get_by_role("textbox", name="Loja").fill(str(loja))
            tm.sleep(0.5)
            pagina.keyboard.press("Enter")
            #localiza o numero de tarefas

            texto = pagina.locator('xpath=//*[@id="form_above-grid_1"]/div/div[2]/span[1]').inner_text()
            match = re.search(r'de (\d+)', texto)
            if match:
                n1 = int(match.group(1))  #N = a numero
            else:
                n1 = 0

            pagina.get_by_role("button", name="").click()
            pagina.get_by_role("link", name="Busca Avancada").click()
            pagina.get_by_role("textbox", name="Data").click()
            pagina.get_by_role("textbox", name="Data").fill(DataHoje)
            pagina.keyboard.press("Enter")

            texto = pagina.locator('xpath=//*[@id="form_above-grid_1"]/div/div[2]/span[1]').inner_text()
            match = re.search(r'de (\d+)', texto)
            if match:
                n2 = int(match.group(1))  #N = a numero
            else:
                n2 = 0
                
            tarefa = n1 - n2
            faltou = 33- tarefa
            mensagem_final.append(f"📅 {DataOntemBR} | Gerente Loja {loja}:  fez {tarefa}, faltou {faltou} para 33.\n")
            

    def campodebusca4():
        pagina2.get_by_role("button", name="").click()
        pagina2.get_by_role("link", name="Busca Avancada").click()
        pagina2.locator("#srchOpt_1_Data").click()
        pagina2.keyboard.press("ArrowDown")
        pagina2.keyboard.press("Enter")
        pagina2.get_by_role("textbox", name="Data").click()
        pagina2.get_by_role("textbox", name="Data").fill(DataOntem)
        pagina2.get_by_text("Buscar", exact=True).click()
        #localiza o numero de tarefas

        # espera o elemento estar disponível
        try:
            pagina2.wait_for_selector('xpath=//*[@id="form_above-grid_1"]/div/div[2]/span[1]')

            # pega o texto visível
            texto2 = pagina2.locator('//*[@id="form_above-grid_1"]/div/div[2]/span[1]').inner_text()

            # regex para pegar número logo depois de "de"
            match2 = re.search(r'de\s+(\d+)', texto2)

            if match2:
                l4_1 = int(match2.group(1))   # número depois de "de"
            else:
                l4_1 = 0
        except:
            l4_1 = 0
        pagina2.get_by_role("button", name="").click()
        pagina2.get_by_role("link", name="Busca Avancada").click()
        pagina2.get_by_role("textbox", name="Data").click()
        pagina2.get_by_role("textbox", name="Data").fill(DataHoje)
        pagina2.keyboard.press("Enter")
        try:
            texto2 = pagina2.locator('//*[@id="form_above-grid_1"]/div/div[2]/span[1]').text_content()
            match2 = re.search(r'de (\d+)', texto2)
            if match2:
                l4_2 = int(match2.group(1))  #N = a numero
            else:
                l4_2 = 0
        except:
            l4_2 = 0
        tarefa4 = l4_1 - l4_2
        faltou = 33- tarefa4
        
        # print(f"Dia: {DataOntemBR} Gerente da Loja 4 fez {tarefa4}, aonde faltou {faltou} para 33.\n")
        mensagem_final.append(f"📅 {DataOntemBR} | Gerente Loja 4 :  fez {tarefa4}, faltou {faltou} para 33.\n")

    def campodebuscasub():
        for lojasub in Lojas:
            tm.sleep(5)
            pagina3.get_by_role("textbox", name="Nome do Usuário").click()
            pagina3.get_by_role("textbox", name="Nome do Usuário").fill(f"loja {lojasub}")
            #selecionar o campo de senha
            pagina3.get_by_role("textbox", name="Senha").click()
            pagina3.get_by_role("textbox", name="Senha").fill("")
            tm.sleep(1)
            pagina3.keyboard.press("Enter")
            pagina3.get_by_role("button", name="").click()
            pagina3.get_by_role("link", name="Busca Avancada").click()
            pagina3.locator("#srchOpt_1_Data").click()
            pagina3.keyboard.press("ArrowDown")
            pagina3.keyboard.press("Enter")
            pagina3.get_by_role("textbox", name="Data").click()
            pagina3.get_by_role("textbox", name="Data").fill(DataOntem)
            pagina3.get_by_text("Buscar", exact=True).click()
            #localiza o numero de tarefas


            # pega o texto visível
            try:
                texto3 = pagina3.locator('//*[@id="form_above-grid_1"]/div/div[2]/span[1]').inner_text()

                # regex para pegar número logo depois de "de"
                match3 = re.search(r'de\s+(\d+)', texto3)

                if match3:
                    lsub = int(match3.group(1))   # número depois de "de"
                else:
                    lsub = 0
            except:
                lsub = 0

            pagina3.get_by_role("button", name="").click()
            pagina3.get_by_role("link", name="Busca Avancada").click()
            pagina3.get_by_role("textbox", name="Data").click()
            pagina3.get_by_role("textbox", name="Data").fill(DataHoje)
            pagina3.keyboard.press("Enter")

            try:
                texto3 = pagina3.locator('//*[@id="form_above-grid_1"]/div/div[2]/span[1]').inner_text()

                # regex para pegar número logo depois de "de"
                match3 = re.search(r'de\s+(\d+)', texto3)

                if match3:
                    lsub2 = int(match3.group(1))   # número depois de "de"
                else:
                    lsub2 = 0
            except:
                lsub2 = 0

            tarefasub = lsub - lsub2
            Faltou = 10 - tarefasub
            resultado[lojasub] = tarefasub
            # print(f"Dia: {DataOntemBR} | Sub da Loja {lojasub} fez {tarefasub}, aonde Faltou {Faltou} para 10.\n")
            mensagem_final.append(f"📅 {DataOntemBR} | Gerente Loja {lojasub}:  fez {tarefasub}, faltou {Faltou} para 33.\n")
            
            pagina3.get_by_role("button", name=" LOJA").click()
            pagina3.get_by_role("link", name="Log Out").click()
            tm.sleep(3)
    mensagem_final.append("Bom dia, segue posições abaixo.")
    mensagem_final.append("Controle Agenda do Gerente:")
    campodebusca()
    pagina2 = navegador.new_page()

    #ir para o nosso cadastro Loja 4
    pagina2.goto("https://sisvarandas2.com.br/agl")
    tm.sleep(8)

    #selecionar um elemento na tela
    pagina2.get_by_role("textbox", name="Nome do Usuário").click()
    pagina2.get_by_role("textbox", name="Nome do Usuário").fill("loja4")
    #selecionar o campo de senha
    pagina2.get_by_role("textbox", name="Senha").click()
    pagina2.get_by_role("textbox", name="Senha").fill("")
    pagina2.keyboard.press("Enter")


    #selecionar o campo de busca
    pagina2.get_by_role("link", name="Cadastros").click()
    pagina2.get_by_role("link", name="Tarefas", exact=True).click()
    mensagem_final.append("Controle Agenda do Gerente Restaurante:")
    campodebusca4()


    pagina3 = navegador.new_page()

    #ir para o nosso cadastro dos subgerentes
    pagina3.goto("https://sisvarandas2.com.br/agsub")
    mensagem_final.append("Controle Agenda do Sub Gerente :")
    pagina3.get_by_role("button", name="").click()
    pagina3.get_by_role("link", name="Log Out").click()
    campodebuscasub()
    print(mensagem_final)
    
    pagina2.goto("https://web.whatsapp.com/")
    time.sleep(5)

    pagina2.get_by_role("tab", name="Grupos").click()
    pagina2.get_by_role("paragraph").fill("PAR")
    pagina2.get_by_text("PAR DEV").click()
    time.sleep(2)

    mensagem_texto = "\n".join(mensagem_final)

    pagina2.locator(
    '//div[@role="textbox" and @contenteditable="true" and contains(@aria-label, "Digitar")]'
).click()
    
    pagina2.locator(
    '//div[@role="textbox" and @contenteditable="true" and contains(@aria-label, "Digitar")]'
).fill(mensagem_texto)
    
    pagina2.locator(
    '//div[@role="textbox" and @contenteditable="true" and contains(@aria-label, "Digitar")]'
).press("Enter")

    time.sleep(3)
    tm.sleep(5)
    navegador.close
    