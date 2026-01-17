
import streamlit as st
from qiskit import QuantumCircuit, execute, IBMQ
import os

# Função para conectar ao hardware da IBM
def rodar_no_quantum_real(api_token):
    if not IBMQ.active_account():
        IBMQ.save_account(api_token, overwrite=True)
        IBMQ.load_account()
    
    provider = IBMQ.get_provider(hub='ibm-q')
    # Usando o simulador quântico da IBM ou o chip de menor fila
    backend = provider.get_backend('ibmq_qasm_simulator') 
    
    qc = QuantumCircuit(1, 1)
    qc.h(0) # Superposição
    qc.measure(0, 0) # Colapso
    
    job = execute(qc, backend, shots=1)
    return job.result().get_counts()

# Interface Streamlit
st.title("Manifestação via Hardware Quântico")
token = st.text_input("Insira seu IBM Quantum Token:", type="password")

if st.button("Colapsar Realidade via Chip IBM"):
    if token:
        with st.spinner("Enviando intenção para o chip criogênico..."):
            resultado = rodar_no_quantum_real(token)
            st.write(f"O bit quântico colapsou em: {resultado}")
            st.success("Ação fantasmagórica concluída com sucesso no Agora.")
    else:
        st.error("O código precisa da chave para acessar o vácuo quântico.")
