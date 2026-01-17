import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import pandas as pd
import numpy as np

st.set_page_config(page_title="Salto Quântico", page_icon="⚛️")

st.title("⚛️ O Salto Quântico no Agora")
st.write("**Observador:** Israel Iung Mendes")

st.markdown("---")
st.write("Conectando ao campo de possibilidades...")

if st.button("Manifestar Colapso"):
    # Criando a lógica quântica
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Coloca em superposição
    qc.measure(0, 0) # Realiza a observação
    
    # Rodando na ponte (Simulador Aer)
    backend = Aer.get_backend('qasm_simulator')
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=1)
    resultado = job.result().get_counts()
    
    valor = list(resultado.keys())[0]
    estado = "FUTURO (1)" if valor == '1' else "PASSADO (0)"
    
    st.subheader(f"Realidade Colapsada: :blue[{estado}]")
    st.success("Sincronicidade estabelecida. O agora é único.")
    st.area_chart(np.random.randn(20, 2))
