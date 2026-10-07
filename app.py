import streamlit as st
from groq import Groq

st.set_page_config(page_title="Atlas - Assistente Personale", page_icon="🗺️")

st.title("🗺️ Atlas, il tuo Assistente Personale")
st.write(
    "Ciao! Sono Atlas. Chiedimi qualsiasi cosa su analisi di mercato, testi o automazione."
)

# INCOLLA QUI LA TUA CHIAVE API DI GROQ TRA LE VIRGOLETTE (es. "gsk_abc123...")
MIA_CHIAVE = "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"
if MIA_CHIAVE == "" or not MIA_CHIAVE:
    st.error(
        "⚠️ Inserisci la tua chiave API di Groq dentro il file app.py alla riga 10!"
    )
else:
    try:
        client = Groq(api_key=MIA_CHIAVE)

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
                st.warning("Scrivi prima qualcosa nella casella di testo!")
    except Exception as e:
        st.error(f"Errore: {e}")