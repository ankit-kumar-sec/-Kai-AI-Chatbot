import os
from datetime import datetime
from uuid import uuid4

import streamlit as st
from dotenv import load_dotenv
from groq import AuthenticationError as GroqAuthenticationError
from groq import NotFoundError as GroqNotFoundError
from openai import AuthenticationError as OpenAIAuthenticationError
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


load_dotenv()

st.set_page_config(
    page_title="Kai | AI workspace",
    page_icon=":material/auto_awesome:",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    :root { --kai-cyan: #54e7e3; --kai-ink: #071013; --kai-muted: #90a5a8; }
    .stApp { background: radial-gradient(circle at 75% 8%, #16383c 0, transparent 28%), linear-gradient(135deg, #071013 0%, #0b171a 52%, #101d20 100%); }
    .stApp:before { content: ''; position: fixed; inset: 0; pointer-events: none; opacity: .22; background-image: linear-gradient(rgba(84,231,227,.08) 1px, transparent 1px), linear-gradient(90deg, rgba(84,231,227,.08) 1px, transparent 1px); background-size: 42px 42px; mask-image: linear-gradient(to bottom, black, transparent 85%); }
    h1, h2, h3, p, label, [data-testid='stChatMessage'] { font-family: 'Space Grotesk', sans-serif; }
    .kai-header { padding: 1.2rem 0 1.8rem; border-bottom: 1px solid rgba(84,231,227,.18); margin-bottom: 1.3rem; }
    .kai-mark { color: var(--kai-cyan); font: 500 .72rem 'DM Mono', monospace; letter-spacing: .18em; text-transform: uppercase; }
    .kai-header h1 { margin: .25rem 0 .35rem; font-size: clamp(2.2rem, 5vw, 4.6rem); letter-spacing: -.06em; color: #f1fbf9; }
    .kai-header p { color: var(--kai-muted); margin: 0; max-width: 42rem; }
    .kai-welcome { display: grid; grid-template-columns: repeat(3, 1fr); gap: .8rem; margin: 2rem 0 1rem; }
    .kai-feature { padding: 1rem; min-height: 7rem; border: 1px solid rgba(84,231,227,.14); border-radius: 12px; background: rgba(13, 31, 34, .52); }
    .kai-feature strong { display: block; color: #f1fbf9; margin: .45rem 0 .35rem; }
    .kai-feature span { color: var(--kai-muted); font-size: .84rem; line-height: 1.4; }
    .kai-icon { color: var(--kai-cyan); font-size: 1.25rem; }
    [data-testid='stSidebar'] { background: rgba(5, 14, 16, .78); border-right: 1px solid rgba(84,231,227,.15); }
    .kai-brand { padding: .8rem 0 1.25rem; }
    .kai-brand-title { color: #f1fbf9; font: 700 2.25rem/1 'Space Grotesk', sans-serif; letter-spacing: -.07em; }
    .kai-brand-subtitle { color: var(--kai-cyan); font: 500 .68rem 'DM Mono', monospace; letter-spacing: .14em; margin-top: .55rem; text-transform: uppercase; }
    [data-testid='stSidebar'] h2 { color: #f1fbf9; font-size: 1rem; }
    [data-testid='stChatMessage'] { border: 1px solid rgba(84,231,227,.11); border-radius: 12px; background: rgba(13, 31, 34, .62); margin-bottom: .8rem; }
    [data-testid='stChatMessage'][data-testid*='user'] { background: rgba(20, 47, 49, .62); }
    .stButton button, .stTextInput input, .stSelectbox div[data-baseweb='select'] { border-radius: 8px; }
    .stButton button { border-color: rgba(84,231,227,.3); }
    .kai-status { color: var(--kai-muted); font: 400 .76rem 'DM Mono', monospace; letter-spacing: .03em; }
    </style>
    """,
    unsafe_allow_html=True,
)


def secret_value(name):
    try:
        value = st.secrets.get(name)
    except FileNotFoundError:
        value = None
    return value or os.getenv(name)


def clean_key(value):
    return value.strip().strip('"').strip("'") if value else ""


def new_conversation():
    conversation_id = str(uuid4())
    st.session_state.conversations[conversation_id] = {
        "title": "New transmission",
        "messages": [],
        "created": datetime.now().strftime("%H:%M"),
    }
    st.session_state.active_conversation = conversation_id


def get_model(provider, model_name, api_key):
    if provider == "Groq":
        return ChatGroq(model=model_name, temperature=0.7, api_key=api_key)
    return ChatOpenAI(model=model_name, temperature=0.7, api_key=api_key)


st.session_state.setdefault("conversations", {})
st.session_state.setdefault("active_conversation", None)
if not st.session_state.conversations:
    new_conversation()

with st.sidebar:
    st.markdown(
        """
        <div class="kai-brand">
          <div class="kai-brand-title">Kai</div>
          <div class="kai-brand-subtitle">Your personal AI companion</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("New conversation", icon=":material/add:", width="stretch"):
        new_conversation()
        st.rerun()

    st.markdown("### History")
    for conversation_id, conversation in reversed(list(st.session_state.conversations.items())):
        label = conversation["title"][:28]
        if st.button(
            f":material/chat_bubble_outline: {label}",
            key=f"conversation_{conversation_id}",
            width="stretch",
            type="primary" if conversation_id == st.session_state.active_conversation else "secondary",
        ):
            st.session_state.active_conversation = conversation_id
            st.rerun()

    st.markdown("### Model control")
    provider = st.selectbox("Provider", ["Groq", "OpenAI"], key="provider")
    model_options = {
        "Groq": ["qwen/qwen3.8-27b", "llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
        "OpenAI": ["gpt-4o-mini", "gpt-4.1-mini", "gpt-4o"],
    }
    model_name = st.selectbox("Model", model_options[provider], key=f"model_{provider}")
    env_key_name = "GROQ_API_KEY" if provider == "Groq" else "OPENAI_API_KEY"
    api_key = clean_key(secret_value(env_key_name))

active = st.session_state.conversations[st.session_state.active_conversation]
st.markdown(
    f"""
    <div class="kai-header">
      <div class="kai-mark">KAI / COGNITIVE INTERFACE</div>
            <h1>Hi, I'm your personal chatbot.</h1>
            <p>Thoughtful answers, quick ideas, and a calm place to get things done.</p>
    </div>
    <div class="kai-status">SESSION {st.session_state.active_conversation[:8].upper()} &nbsp;·&nbsp; {provider} / {model_name}</div>
    """,
    unsafe_allow_html=True,
)

for message in active["messages"]:
    avatar = ":material/auto_awesome:" if message["role"] == "assistant" else ":material/person:"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if not active["messages"]:
    st.markdown(
        """
        <div class="kai-welcome">
          <div class="kai-feature"><div class="kai-icon">:material/lightbulb:</div><strong>Think with me</strong><span>Turn rough ideas into clear next steps.</span></div>
          <div class="kai-feature"><div class="kai-icon">:material/bolt:</div><strong>Move faster</strong><span>Draft, explain, summarize, or solve in seconds.</span></div>
          <div class="kai-feature"><div class="kai-icon">:material/tune:</div><strong>Make it yours</strong><span>Switch models anytime from the control panel.</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if not api_key:
        st.warning("Kai is waiting for a backend API key. Add it to your .env file, then restart the app.", icon=":material/key:")

prompt = st.chat_input("Transmit a message to Kai", disabled=not bool(api_key), submit_mode="disable")
if prompt:
    active["messages"].append({"role": "user", "content": prompt})
    if active["title"] == "New transmission":
        active["title"] = prompt.strip().replace("\n", " ")[:34] or "New transmission"
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(prompt)

    history = []
    for message in active["messages"]:
        message_type = HumanMessage if message["role"] == "user" else AIMessage
        history.append(message_type(content=message["content"]))

    with st.chat_message("assistant", avatar=":material/auto_awesome:"):
        try:
            model = get_model(provider, model_name, api_key)
            response = st.write_stream(model.stream(history))
        except (GroqAuthenticationError, OpenAIAuthenticationError):
            response = None
            st.error(f"{provider} rejected the backend API key. Check your .env or secrets.toml and try again.", icon=":material/error:")
        except GroqNotFoundError:
            response = None
            st.error(f"The {provider} model `{model_name}` is unavailable for this key.", icon=":material/error:")
        except Exception as error:
            response = None
            st.error(f"Kai could not complete that request: {error}", icon=":material/error:")

    if response:
        active["messages"].append({"role": "assistant", "content": response})
