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
