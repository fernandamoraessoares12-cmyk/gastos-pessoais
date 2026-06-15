# 💰 Gastos Pessoais

Aplicação para controle de gastos pessoais com persistência de dados na nuvem.

## 🚀 Deploy

Aplicação disponível em: https://replit.com/@fernandamoraess/gastos-pessoais

## 🛠️ Tecnologias

- Python
- Supabase (PostgreSQL na nuvem)
- pytest
- GitHub Actions (CI/CD)

## 🗄️ Banco de Dados

Este projeto usa **Supabase** (PostgreSQL na nuvem) para salvar os gastos.

### Configuração local

1. Crie um projeto gratuito em [supabase.com](https://supabase.com)
2. Crie a tabela `gastos` no SQL Editor:
```sql
CREATE TABLE gastos (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  descricao TEXT NOT NULL,
  valor NUMERIC(10, 2) NOT NULL,
  categoria TEXT NOT NULL DEFAULT 'outros',
  data DATE NOT NULL DEFAULT CURRENT_DATE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```
3. Crie um arquivo `.env` na raiz com:
4. ## ▶️ Como rodar localmente

```bash
pip install supabase python-dotenv pytest
pytest tests/ -v
```

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Fernanda Moraes Soares | [@fernandamoraessoares12-cmyk](https://github.com/fernandamoraessoares12-cmyk) |
| Mary Fernanda | [@maryfernandasdn](https://github.com/maryfernandasdn) |
