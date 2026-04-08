# 🚀 Workana Job Hunter Bot (macOS)

Um bot de automação desenvolvido em Python para monitorar propostas de alto valor no Workana. O bot filtra projetos que pagam **R$ 1.000 ou mais** ou **pagamentos por hora**, gerando um relatório dinâmico em HTML e notificando diretamente no macOS.

## ✨ Funcionalidades

* **Busca Automática:** Varre a categoria de TI e Programação no Workana.
* **Filtro Inteligente:** * Filtra projetos com valor fixo $\ge 1.000$ (conversão baseada em USD/BRL conforme o site).
    * Detecta automaticamente propostas de pagamento por hora.
* **Relatório HTML:** Gera uma página `propostas_encontradas.html` com cards clicáveis.
* **Notificação Nativa:** Dispara alertas via AppleScript (System Notifications).
* **Abertura Automática:** Abre a aba de resultados no seu navegador padrão caso encontre oportunidades.

## 🛠️ Tecnologias

* **Python 3.9+**
* **BeautifulSoup4:** Para parsing do HTML/JSON.
* **Requests:** Para comunicação com a plataforma.
* **AppleScript:** Para integração com a UI do macOS.

## 🚀 Instalação e Uso

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/workana-job-hunter.git](https://github.com/SEU_USUARIO/workana-job-hunter.git)
    cd workana-job-hunter
    ```

2. **(Opcional) Verifique o Python utilizado:**
    ```bash
    which python3
    # Saída esperada: /usr/bin/python3
    ```

3. **Configure o serviço de inicialização automática (macOS):**
    O arquivo `com.workana.bot.plist` deve ser copiado para a pasta:
   
    ```
    ~/Library/LaunchAgents/
    ```
    Exemplo de comandos:
    ```bash
    # Descarregue o serviço se já estiver carregado
    launchctl unload ~/Library/LaunchAgents/com.workana.bot.plist
    # Copie o arquivo .plist para o local correto
    cp com.workana.bot.plist ~/Library/LaunchAgents/
    # Carregue o serviço
    launchctl load ~/Library/LaunchAgents/com.workana.bot.plist
    # Inicie o serviço manualmente (se necessário)
    launchctl start com.workana.bot
    ```

    > **Atenção:** O arquivo `com.workana.bot.plist` **deve estar em** `~/Library/LaunchAgents/` para que o serviço funcione corretamente no macOS.
