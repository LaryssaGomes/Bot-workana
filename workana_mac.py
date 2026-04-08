import requests
from bs4 import BeautifulSoup
import os
import json
import webbrowser
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# --- CONFIGURAÇÃO ---
FILE_PATH = "/Users/laryssagomes/BotWorkana/propostas_encontradas.html"

def create_html_report(projects):
    """Gera uma página HTML simples com os links das propostas"""
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    html_content = f"""
    <html>
    <head>
        <title>Propostas Filtradas - Workana</title>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; padding: 20px; background: #f4f4f9; }}
            .card {{ background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            a {{ color: #007bff; text-decoration: none; font-weight: bold; font-size: 1.1em; }}
            a:hover {{ text-decoration: underline; }}
            .price {{ color: #28a745; font-weight: bold; }}
            .date {{ color: #666; font-size: 0.8em; }}
        </style>
    </head>
    <body>
        <h1>🚀 Novas Propostas Encontradas</h1>
        <p>Última atualização: {now}</p>
        <hr>
    """
    
    for p in projects:
        html_content += f"""
        <div class="card">
            <a href="{p['link']}" target="_blank">{p['title']}</a><br>
            <span class="price">💰 {p['value']}</span>
        </div>
        """
    
    html_content += "</body></html>"
    
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

def notify_mac(count):
    """Dispara a notificação e abre o HTML ao clicar"""
    title = "Workana: Vagas Encontradas!"
    msg = f"Encontrei {count} propostas excelentes para você. Clique para ver a lista."
    # Comando para notificar e abrir o arquivo ao clicar
    cmd = f'display notification "{msg}" with title "{title}" sound name "Glass"'
    os.system(f"osascript -e '{cmd}'")
    
    # Abre o arquivo no navegador padrão do Mac
    webbrowser.open(f"file://{FILE_PATH}")

def check_workana():
    url = "https://www.workana.com/jobs?category=it-programming&has_few_bids=1&language=pt&publication=1d"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Buscando...")
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_tag = soup.find('search')
        
        if not search_tag:
            print("Erro: Estrutura da página não encontrada.")
            return

        data = json.loads(search_tag[':results-initials'])
        projects = data.get('results', [])
        
        matches = []
        for p in projects:
            title = BeautifulSoup(p.get('title', ''), "html.parser").get_text(strip=True)
            value_text = p.get('budget', '0')
            link = f"https://www.workana.com/job/{p.get('slug', '')}"

            # Filtro
            is_hourly = "hora" in value_text.lower()
            numeric_value = ''.join(filter(str.isdigit, value_text.replace('.', '').replace(',', '')))
            value_int = int(numeric_value) if numeric_value else 0

            if is_hourly or value_int >= 1000:
                matches.append({'title': title, 'value': value_text, 'link': link})

        if matches:
            print(f"Sucesso! {len(matches)} matches encontrados.")
            create_html_report(matches)
            notify_mac(len(matches))
        else:
            print("Nenhum projeto novo nos critérios agora.")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    check_workana()