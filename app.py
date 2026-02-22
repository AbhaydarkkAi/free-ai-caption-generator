import streamlit as st
from openai import OpenAI
import os
# ==================== API KEY FROM GROQ ====================
API_KEY = os.getenv("GROQ_API_KEY")  # ← yahan apni Groq key daal de (gsk_ se start)


# Groq endpoint (xAI nahi, Groq ka)
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="Mera Free AI Caption Generator", page_icon="🔥")
st.title("Free AI Caption Generator 😎 (Groq Powered)")
st.markdown("*Description daal, free mein mast caption banwa le – Hindi/English mix, hashtags, emoji sab!*")

description = st.text_input(
    "Post ke baare mein bata (Hindi ya English mein)",
    placeholder="jaise: dark background ke liye caption"
)

tone = st.selectbox(
    "Mood kaisa chahiye?",
    ["Normal", "Funny", "Romantic", "Motivational", "Savage/Dark", "Cute", "Attitude"]
)

if st.button("Caption Banao Bhai!", type="primary"):
    if not description.strip():
        st.error("Arre bhai kuch to likho! 😅")
    else:
        with st.spinner("AI ka ghopda soch raha hai... 🚀"):
            try:
                system_prompt = """
                Tu pro Instagram caption writer hai.
                Short, viral jaise caption bana.
                Tone ke hisaab se mood set kar.
                Hindi/English mix kar sakta hai.
                Emoji aur 3-5 hashtags zaroor daal.
                Caption 1-2 line se zyada mat kar.
                """

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",  # Groq pe yeh free aur powerful hai
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Tone: {tone}\nDescription: {description}"}
                    ],
                    max_tokens=100,
                    temperature=0.85
                )

                caption = response.choices[0].message.content.strip()
                st.success("Ye raha tera tadkta vadakta caption:")
                st.markdown(f"*{caption}*")
                st.code(caption, language=None)
                st.caption("Copy kar le bhoii!")

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Bhai, kuch gadbad ho gayi. Thoda try kar fir se ya description thoda badal ke dekh.")

st.markdown("---")
st.caption("Made with ❤️ by Abhay • Free Groq tier pe chal raha • Personal use ke liye hai baatna mat")