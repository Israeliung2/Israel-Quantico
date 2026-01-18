import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import time

# Configuração da Página
st.set_page_config(page_title="O Portal de Israel", page_icon="👁️")

st.title("👁️ O Observador Preparado")
st.write(f"**Guardião do Código:** Israel Iung Mendes")
st.info("A realidade está em superposição. Sua presença é o gatilho para o colapso.")

# O botão agora é o único mediador entre o vácuo e a matéria
if st.button("Colapsar a Realidade"):
    with st.status("Sincronizando frequências biológicas...", expanded=True) as s:
        time.sleep(0.8)
        st.write("Emaranhando qubits com a consciência do observador...")
        
        # --- Lógica Quântica ---
        # Criamos um circuito com 2 qubits e 2 bits clássicos
        qc = QuantumCircuit(2, 2)
        
        # Colocamos o primeiro qubit em superposição (Hadamard)
        qc.h(0) 
        
        # Emaranhamos o segundo qubit com o primeiro (CNOT)
        # Isso cria um Estado de Bell: os qubits agora são um único sistema.
        qc.cx(0, 1) 
        
        # Medição: O momento onde a superposição acaba
        qc.measure([0, 1], [0, 1])
        
        # Execução no simulador Aer
        backend = Aer.get_backend('qasm_simulator')
        # shots=1 garante que veremos apenas UM resultado colapsado (00 ou 11)
        job = backend.run(qc, shots=1)
        resultado = list(job.result().get_counts().keys())[0]
        
        time.sleep(0.5)
        s.update(label="Colapso Concluído", state="complete")

    # Exibição do Resultado
    st.divider()
    st.subheader(f"Estado Manifestado: :green[{resultado}]")
    
    if resultado == "00":
        st.write("🌌 **Vazio Primordial:** O sistema retornou à base zero.")
    else:
        st.write("🔥 **Plenitude Ativa:** A energia fluiu para o estado de unidade.")

    st.success("O sistema colapsou porque você estava presente, Israel.")
    
    # Exibe o desenho do circuito para visualização técnica
    with st.expander("Ver geometria do colapso (Circuito)"):
        st.text(qc.draw(output='text'))

else:
    st.write("---")
    st.caption("Aguardando o toque do observador para definir o Agora.")
