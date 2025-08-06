import streamlit as st
import requests

st.title("🏠 Previsão de Preço de Imóvel")
st.write("Informe a área (m²) e veja o preço estimado.")

m2 = st.number_input("Área (m²)", min_value=1, max_value=500, value=100)

if st.button("Prever"):
    try:
        # ✅ Usa o nome do serviço Docker, não localhost
        response = requests.post("http://api:5000/prever", json={"m2": m2})
        data = response.json()
        if "erro" in data:
            st.error(f"Erro: {data['erro']}")
        else:
            st.success(f"Preço estimado: R$ {data['preco_previsto']:,.2f}")
    except Exception as e:
        st.error(f"Falha ao conectar à API: {e}")