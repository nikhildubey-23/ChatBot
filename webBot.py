import sqlite3
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Initialize the database
def init_db():
    conn = sqlite3.connect('user_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert user question and answer into the database
def insert_history(question, answer):
    conn = sqlite3.connect('user_history.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

# Function to retrieve user history from the database
def get_history():
    conn = sqlite3.connect('user_history.db')
    c = conn.cursor()
    c.execute('SELECT question, answer FROM history ORDER BY id ASC')  # Get history in chronological order
    rows = c.fetchall()
    conn.close()
    return rows

# Function to clear user history from the database
def clear_history():
    conn = sqlite3.connect('user_history.db')
    c = conn.cursor()
    c.execute('DELETE FROM history')  # Clear all entries
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Streamlit app
st.title("Flamingo")

template = """Question: {question}

Answer: you are a friendly assistant made for to help people and you are genius and you try to reply in paragraph and in a small paragraph."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model

# Sidebar for user input
question = st.chat_input("Enter your question here")
if question: 
    answer = chain.invoke({"question": question})
    st.write(answer)
    
    # Store question and answer in the database
    insert_history(question, answer)

# Create a row for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Show History"):
        st.subheader("User  History")
        history = get_history()
        for idx, (q, a) in enumerate(history):
            st.write(f"**Q{idx + 1}:** {q}")
            st.write(f"**A{idx + 1}:** {a}")

with col2:
    if st.button("Clear History"):
        clear_history()
        st.success("History cleared!")

with col3:
    if st.button("Minimize History"):
        st.write("History section minimized. Click 'Show History' to view again.")

# Display the latest question and answer at the bottom
if question:
    st.write(f"**Latest Q:** {question}")
    st.write(f"**Latest A:** {answer}")

# Optionally, you can add a separator for clarity
st.markdown("---")
