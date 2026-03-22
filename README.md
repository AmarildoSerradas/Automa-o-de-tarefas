# 🤖 Automação de Tarefas + Relatório via WhatsApp

Script de automação desenvolvido em Python utilizando Playwright para coleta de dados em sistema web, processamento das informações e envio automático de relatórios via WhatsApp Web.

O objetivo é eliminar tarefas manuais repetitivas, garantindo agilidade, consistência e padronização na geração de relatórios diários.

# ⚙️ Tecnologias utilizadas
Python
Playwright (automação web)
Regex (re) para extração de dados
datetime (manipulação de datas)
# 🚀 Funcionalidades
Login automatizado em múltiplos ambientes (admin, loja e subgerente)
Aplicação de filtros por data e loja
Coleta automática de quantidade de tarefas realizadas
Cálculo de produtividade (realizado vs meta)
Geração de relatório formatado
Envio automático da mensagem via WhatsApp Web
Execução contínua sem intervenção manual
# 🧠 Como funciona

O script acessa o sistema web, realiza login e navega até a área de tarefas.
A partir disso, aplica filtros por data e loja, extrai os dados exibidos na interface e realiza os cálculos necessários.

Com base nessas informações, o sistema monta um relatório estruturado e envia automaticamente para um grupo no WhatsApp.

# ▶️ Como executar
pip install playwright
playwright install
python nome_do_arquivo.py
🔐 Credenciais

As credenciais de acesso ao sistema foram removidas propositalmente deste código por questões de segurança.

Para utilizar o script, você deve inserir suas próprias credenciais nos campos indicados no código.

# ⚠️ Pontos de atenção
Dependente da estrutura do site (mudanças podem quebrar a automação)
Uso de time.sleep() ao invés de waits inteligentes
Código extenso e pouco modular
Dependência de sessão ativa no WhatsApp Web
# 📌 Melhorias futuras
Refatoração em funções e módulos
Implementação de wait_for no Playwright
Tratamento de erros mais robusto
Uso de variáveis de ambiente (.env) para credenciais
Agendamento automático da execução
# 🧾 Exemplo de saída
Bom dia, segue posições abaixo.

Controle Agenda do Gerente:
📅 21/03/2026 | Gerente Loja 1: fez 25, faltou 8 para 33.

Controle Agenda do Gerente Restaurante:
📅 21/03/2026 | Gerente Loja 4: fez 30, faltou 3 para 33.

Controle Agenda do Sub Gerente:
📅 21/03/2026 | Sub Loja 1: fez 8, faltou 2 para 10.
