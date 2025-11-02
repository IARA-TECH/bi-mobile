# BI Mobile

Projeto que combina **Power BI** para dashboards interativos e **script Python** para automação de autenticação via API.  
O arquivo `.pbix` contém painéis analíticos estratégicos, enquanto o script Python `daily_token.py` permite gerar e salvar **tokens de acesso** para consumir APIs do ecossistema IARA.

---

## 📚 Sumário

- [💡 Sobre o Projeto](#-sobre-o-projeto)
- [⚙️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🧩 Como Executar](#-como-executar)
- [📊 Indicadores e Visualizações](#-indicadores-e-visualizações)
- [🔐 Variáveis de Ambiente](#-variáveis-de-ambiente)
- [👩‍💻 Autor](#-autor)

---

## 💡 Sobre o Projeto

O **BI Mobile IARA** foi desenvolvido para **centralizar dados e métricas operacionais** em dashboards visuais, permitindo análise rápida e decisões baseadas em dados.  

Funcionalidades principais:

- Painéis interativos no Power BI com KPIs e gráficos de tendência.  
- Análise detalhada de produção, desempenho e automações do ecossistema.  
- Segmentação por unidade, área ou projeto.  
- Script Python para **geração automática de tokens de API**, armazenando-os localmente para acesso seguro.

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Ferramentas / Bibliotecas |
| --- | --- |
| **Dashboard** | Power BI Desktop (.pbix) |
| **Automação / API** | Python 3.8+, `requests`, `python-dotenv`, `os`, `datetime` |
| **Banco de Dados / Fontes** | PostgreSQL / Supabase / CSVs / APIs REST |

---

## 🧩 Como Executar

### 1. Dashboard Power BI
1. Baixe e instale o **Power BI Desktop**.  
2. Abra o arquivo `BI_iara.pbix`.  
3. Atualize as credenciais das fontes de dados (PostgreSQL/Supabase ou CSVs).  
4. Clique em **Atualizar** para carregar os dados atuais.  

### 2. Script de Geração de Token (`daily_token.py`)
```bash
# Clone o repositório
git clone https://github.com/IARA-TECH/bi-mobile.git
cd bi-mobile

# Crie e ative o ambiente virtual
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente no arquivo .env
USERNAME_IARA=seu_usuario
PASSWORD_IARA=sua_senha
URL_ENDPOINT=https://sua-api-iara.com/login
PATH_TOKEN=./token.txt

# Execute o script
python daily_token.py

```
O token será gerado e salvo no arquivo definido em PATH_TOKEN.

---
## 📊 Indicadores e Visualizações

O arquivo .pbix contém:

* KPIs e métricas agregadas: totais, médias e tempos médios de execução.
* Gráficos de série temporal: análise mês a mês ou por período específico.
* Tabelas detalhadas com filtros interativos.
* Mapas geográficos, caso haja dados de localização.
* Slicers e segmentações por unidade, área, projeto ou categoria.

O dashboard permite interatividade completa, ajudando a monitorar operações e a performance de processos automatizados.

---

### 🔐 Variáveis de Ambiente

| Variável        | Descrição                                     |
| --------------- | --------------------------------------------- |
| `USERNAME_IARA` | Usuário de autenticação da API                |
| `PASSWORD_IARA` | Senha de autenticação da API                  |
| `URL_ENDPOINT`  | URL do endpoint de login da API               |
| `PATH_TOKEN`    | Caminho do arquivo para salvar o token gerado |


--- 
## 👩‍💻 Autor 

**IARA Tech**

Projeto interdisciplinar para monitoramento, análise e visualização de performance do ecossistema IARA.

📍 São Paulo, Brasil 
📧 iaratech.oficial@gmail.com 
🌐 https://github.com/IARA-TECH