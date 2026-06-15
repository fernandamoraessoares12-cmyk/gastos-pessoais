import os
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")


def get_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def listar_gastos():
    supabase = get_client()
    response = supabase.table("gastos").select("*").order("created_at", desc=True).execute()
    return response.data


def adicionar_gasto(descricao, valor, categoria, data):
    supabase = get_client()
    response = supabase.table("gastos").insert({
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }).execute()
    return response.data[0] if response.data else {}


def deletar_gasto(gasto_id):
    supabase = get_client()
    response = supabase.table("gastos").delete().eq("id", gasto_id).execute()
    return len(response.data) > 0
