import streamlit as st
from groq import Groq

st.set_page_config(page_title="Atlas - Assistente Personale", page_icon="🗺️")

st.title("🗺️ Atlas, il tuo Assistente Personale")
st.write(
    "Ciao! Sono Atlas. Chiedimi qualsiasi cosa su analisi di mercato, testi o automazione."
)

# Recupera la chiave dai Secrets di Streamlit oppure inseriscila qui sotto tra le virgolette per i test locali
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "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")

# Se usi il computer o vuoi testarlo ovunque senza configurare i secrets,
# puoi anche incollare la chiave direttamente qui sotto al posto di "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"
if (
    not GROQ_API_KEY
    or GROQ_API_KEY == "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"
    or GROQ_API_KEY.startswith("INCOLLA")
):
    st.warning(
        "⚠️ Nessuna chiave API trovata. Inseriscila nei Secrets di Streamlit oppure direttamente nel codice."
    )
else:
    try:
        client = Groq(api_key=GROQ_API_KEY)

        user_input = st.text_area(
            "Scrivi il tuo comando o la tua richiesta per Atlas:"
        )

        if st.button("Chiedi ad Atlas"):
            if user_input:
                with st.spinner("Atlas sta elaborando la risposta..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "Ti chiami Atlas, sei un assistente personale avanzato, brillante e diretto, specializzato in finanza, automazione e gestione del telefono.",
                            },
                            {"role": "user", "content": user_input},
                        ],
                        model="llama-3.3-70b-versatile",
                    )
                    risposta = chat_completion.choices[0].message.content
                    st.success("Risposta di Atlas:")
                    st.write(risposta)
            else:
                st.error("Per favore, inserisci un comando per Atlas.")
    except Exception as e:
        st.error(f"Errore di connessione con le API di Groq: {e}")