import streamlit as st
from config.conf import Config 
from db.ai_sql_agent import AISQLAgent


#---Load configuration
conf=Config()
agent=AISQLAgent(conf.get_db_url(),conf.gemini_api_key)

#---Streamlit UI

st.set_page_config(page_title="AI SQL Sales Agent",layout="wide")
st.title("🤖 AI SQL Sales Query Assistant")
st.caption("Ask questions in natural language. The AI will generate and run SQL on Supabase.")

#---Test DB connection
conn_status=agent.db.test_connection()
if conn_status is not True:
    st.error(conn_status)
else:
    st.success("✅ Connected to Supabase successfully!")

#--User Input

user_question=st.text_area("Enter Your Question:",
                           placeholder="e.g.,Show all reviews with ratings < 3 in Mumbai")     

if st.button("Run Query"):
    if user_question.strip():
        with st.spinner("Generating SQL and Fetching data.."):
            sql_query,df,*_=agent.ask(user_question)
            st.subheader("Generating SQL")
            st.code(sql_query,language="sql") 

        if df is not None and not df.empty:
            st.dataframe(df,use_container_width=True)
            csv=df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results (CSV)",csv,"results.csv","text/csv")
        else:
            st.warning("No result found")              