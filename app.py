import streamlit as st
from groq import Groq

st.set_page_config(page_title="Atlas - Assistente Personale", page_icon="🗺️")

st.title("🗺️ Atlas, il tuo Assistente Personale")
st.write(
    "Ciao! Sono Atlas. Chiedimi qualsiasi cosa su analisi di mercato, testi o automazione."
)

# Inserisci qui la tua chiave API di Groq tra virgolette (oppure usa i Secrets di Streamlit)
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "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")

if not GROQ_API_KEY or GROQ_API_KEY == "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":
    st.warning(
        "⚠️ Inserisci la tua chiave API di Groq nel codice o nei Secrets di Streamlit."
    )
else:
    client = Groq(api_key=GROQ_API_KEY)

    user_input = st.text_area("Scrivi il tuo comando o la tua richiesta per Atlas:")

    if st.button("Chiedi ad Atlas"):
        if user_input:
            with st.spinner("Atlas sta elaborando la risposta..."):
                try:
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
                except Exception as e:
                    st.error(f"Errore durante la richiesta: {e}")
        else:
            st.error("Per favore, inserisci un comando per Atlas.")