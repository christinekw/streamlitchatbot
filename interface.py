import os
from AIchatbot.model import Model
import streamlit as st
from AIchatbot.firstmsg import first_meet, not_first_meet


st.title("💬 Chatbot")

chain_of_emotion = []
chain_of_event = []
#TODO: check if it is a new registered user

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": first_meet}]
avatar = {"assistant":"image/bird/703792AF16B6EF4CAA8B303F81D7ED3A.png","user":"😳"}

for msg in st.session_state.messages:
    st.chat_message(msg["role"],avatar=avatar[msg["role"]]).write(msg["content"])

if prompt := st.chat_input():


    llm = Model()
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user",avatar=avatar["user"]).write(prompt)
    chain_of_event.append(prompt)
    history = llm.llm_summarize.invoke([('system','总结玩家在提供的输入中遇到的事件，字数不超过200字。'),('human',str(chain_of_event))])
    if chain_of_emotion != []:
        agent_apresponse = llm.llm_appraisal.invoke(
            [llm.appraisalprompt.format(str(chain_of_emotion)),('human',"玩家的话："+prompt)]
        )
    else:
        agent_apresponse = llm.llm_appraisal.invoke(
            [llm.appraisalprompt.format("这是一场新的对话。玩家是你的新主人，你们第一次见面。"),('human',prompt)]
        )
    
    chain_of_emotion.append(agent_apresponse.content)
    if len(chain_of_emotion) > 10:
        del chain_of_emotion[0]
    
    response_input = '''玩家遇到的事件:{}
                        聊天记录：{}
                        玩家现在说的话:{}
                        你的情绪:{} 
                        请根据以上资料对玩家的话进行回应：'''
    agent_response = llm.llm_response.invoke(
            [llm.responsesystemprompt,('human',response_input.format(history.content,prompt,str(st.session_state.messages),agent_apresponse.content))]
        )
    
    st.session_state.messages.append({"role": "assistant", "content":agent_response.content})
    st.chat_message("assistant",avatar=avatar["assistant"]).write(agent_response.content)