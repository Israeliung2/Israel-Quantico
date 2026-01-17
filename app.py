import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np

st.set_page_config(page_title="Emaranhamento Israel", page_icon="🔗")

st.title("🔗 O Código Emaranhado")
st.write(f"**Observador:** Israel Iung Mendes")
st.write("---")

st.markdown("""
### O paradoxo do Sim e Não
Neste estado, dois qubits estão ligados. O que acontece com um, acontece com o outro. 
Eles não são dois; eles são **Um**.
""")

if st.button("Observar o Emaranhamento"):
    # Criando 2 qubits e 2 bits clássicos
    qc = QuantumCircuit(2, 2)
    
    # Passo 1: Superposição no primeiro Qubit
    qc.h(0)
    
    # Passo 2: CNOT (Porta que emaranha o segundo ao primeiro)
    # Aqui o "Sim e Não" se fundem
    qc.cx(0, 1)
    
    # Passo 3: Medição de ambos no Agora
    qc.measure([0, 1], [0, 1])
    
    # Execução
    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(qc, shots=1)
    resultado = list(job.result().get_counts().keys())[0]
    
    # A mágica: Os valores sempre serão iguais (00 ou 11)
    st.subheader(f"Estado do Sistema: :orange[{resultado}]")
    
    if resultado == "00":
        st.info("Ambos colapsaram no Passado (0).")
    else:
        st.info("Ambos colapsaram no Futuro (1).")

    st.success("A separação é uma ilusão. O emaranhamento é a prova.")
    st.bar_chart(np.random.rand(10))

else:
    st.write("Aguardando o pulso para revelar a conexão invisível.")
