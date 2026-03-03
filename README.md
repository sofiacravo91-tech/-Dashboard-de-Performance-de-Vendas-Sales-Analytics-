# 📊 Sales CRM Dashboard — Sales Operations Analytics

![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Prophet](https://img.shields.io/badge/Forecast-Prophet-FF6B35?style=flat-square)
![Dashboard](https://img.shields.io/badge/Dashboard-HTML%2FJS-00e5a0?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat-square)

> Dashboard completo de análise de CRM simulando o ambiente real de uma operação de vendas B2B — com geração de dados, SQL analítico, previsão de receita com ML e visualização interativa.

---

## 🎯 Objetivo

Demonstrar habilidades práticas em **Sales Operations** e **Revenue Analytics** através de um projeto end-to-end: modelagem de dados relacionais de CRM, análise com SQL avançado, forecast de receita com ML e dashboard interativo.

---

## 🖥️ Dashboard ao Vivo

👉 **[Ver dashboard interativo](https://SEU_USUARIO.github.io/sales-crm-dashboard/dashboard/sales-dashboard.html)**

---

## 📐 Arquitetura do Projeto
```
sales-crm-dashboard/
├── data/
│   ├── generate_data.py      # Geração de dados simulados com Faker
│   ├── deals.csv             # 1.200 negociações
│   ├── reps.csv              # 12 vendedores
│   ├── accounts.csv          # 600 empresas
│   └── activities.csv        # ~8.000 atividades de vendas
├── sql/
│   └── queries.sql           # 12 queries analíticas documentadas
├── forecast/
│   └── forecast_revenue.py   # Modelo Prophet + visualização
└── dashboard/
    └── sales-dashboard.html  # Dashboard interativo
```

---

## 📊 Métricas Analisadas

| Métrica | Descrição |
|---|---|
| **Revenue (MRR)** | Receita mensal realizada vs meta |
| **Pipeline Value** | Valor ponderado por probabilidade de fechamento |
| **Win Rate** | Taxa de ganho por segmento, região e quarter |
| **Conversion Rate** | % de leads que avançam no funil |
| **Average Deal Size** | Ticket médio por segmento |
| **Sales Cycle Length** | Tempo médio de fechamento em dias |
| **Rep Performance** | Leaderboard com quota attainment |
| **Revenue Forecast** | Previsão 6 meses com IC 80%/95% |

---

## 🗃️ Modelo de Dados
```
reps ──────────────┐
                   ├──► deals ◄──── accounts
activities ────────┘
```

**deals** é a tabela central com estágio do funil, valor, segmento, região, ciclo de venda e fonte.

### Segmentos simulados
- **Enterprise** — $80K–$500K, ciclo 55–90 dias  
- **Mid-Market** — $20K–$120K, ciclo 25–55 dias  
- **SMB** — $3K–$30K, ciclo 7–25 dias  

---

## 🔍 Exemplo de Query — Win Rate por Segmento
```sql
SELECT
    segment, quarter,
    ROUND(
        100.0 * SUM(CASE WHEN stage = 'Closed Won' THEN 1 ELSE 0 END)
              / NULLIF(SUM(CASE WHEN stage IN ('Closed Won','Closed Lost')
                           THEN 1 ELSE 0 END), 0), 1
    ) AS win_rate_pct
FROM deals
WHERE stage IN ('Closed Won', 'Closed Lost')
GROUP BY segment, quarter
ORDER BY segment, quarter;
```

---

## 🔮 Forecast de Receita (Prophet)
```python
model = Prophet(
    yearly_seasonality=True,
    seasonality_mode='multiplicative',
    interval_width=0.80,
    changepoint_prior_scale=0.15,
)
model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
model.fit(monthly[['ds', 'y']])
```

---

## ⚙️ Como Rodar
```bash
# 1. Instalar dependências
pip install pandas numpy faker prophet matplotlib

# 2. Gerar os dados
python data/generate_data.py

# 3. Carregar no PostgreSQL e rodar as queries
psql -U usuario -d banco -f sql/queries.sql

# 4. Gerar o forecast
python forecast/forecast_revenue.py

# 5. Abrir o dashboard
open dashboard/sales-dashboard.html
```

---

## 💡 Principais Insights

- Enterprise tem win rate ~18pp acima de SMB, mas ciclo 3× mais longo
- Deals de Referral convertem 40% mais que Outbound com ticket similar
- Reunião Demo é o touchpoint com maior correlação com fechamento
- Receita tem sazonalidade trimestral clara, com pico em dezembro e março
- Forecast aponta crescimento de ~24% nos próximos 2 quarters

---

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Geração de dados | Python, Faker, pandas, numpy |
| Armazenamento | PostgreSQL 14+ / CSV |
| Análise | SQL (CTEs, Window Functions, Views) |
| Forecast | Prophet (Meta) |
| Visualização | HTML5, CSS3, JavaScript, Chart.js |

---

## 👤 Autor

**[Seu Nome]**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/SEU_PERFIL)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/SEU_USUARIO)

*Projeto desenvolvido para portfólio de Sales Operations & Revenue Analytics.*
