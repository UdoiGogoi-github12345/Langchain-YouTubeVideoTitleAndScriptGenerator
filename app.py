import os
os.environ['OPENAI_API_KEY']='your api key'
from langchain.llms import OpenAI
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.memory import ConversationBufferMemory

#Loading our OpenAI model
llm=OpenAI(temperature=0.9)

st.title("🦜 YouTube Video Name and Script Generator v1.0.0")
user_input=st.text_input("Please enter your creative Youtube Video Idea here!!!")


 
 #Prompt Template
title_template=PromptTemplate(
    input_variables=['topic'],
    template="Write me a YouTube video title on the topic {topic}"
)
script_template=PromptTemplate(
        input_variables=['topic'],
        template="Write me a script for the Youtube Video on the topic {topic}"
)


#using Chain, In the chain we have specified llm to be used and then the prompt
title_chain=LLMChain(llm=llm,prompt=title_template,verbose=True)
script_chain=LLMChain(llm=llm,prompt=script_template,verbose=True)
#overall_chain=SimpleSequentialChain(chains=[title_chain,script_chain],verbose=True)



if user_input:
    #response=overall_chain.run(user_input)
    #st.write(response)

    title=title_chain.run(user_input)
    script=script_chain.run(user_input)
    st.write("🔥 ")
    st.subheader(title)
    st.write("📜 " + script)






