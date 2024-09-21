from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from model import Model
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory


def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///memory.db")


def main():
    llm = Model()
    chain_of_emotion = []
    chain_of_event = []
    while True:
        print("INPUT:")
        user_input = input()
        chain_of_event.append(user_input)
        history = llm.llm_summarize.invoke([('system','Summarize the events that the user encountered from the provided user input in no more than 200 words.'),('human',str(chain_of_event))])
        if chain_of_emotion != []:
            agent_apresponse = llm.llm_appraisal.invoke(
                [llm.appraisalprompt.format(str(chain_of_emotion)),('human',"here is the player's words:"+user_input)]
            )
        else :
            agent_apresponse = llm.llm_appraisal.invoke(
                [llm.appraisalprompt.format("new conversation. The player is your new owner."),('human',user_input)]
            )
        
        print("AGENT_APPRAISAL : {}".format(agent_apresponse.content))
        
        chain_of_emotion.append(agent_apresponse.content)
        if len(chain_of_emotion) > 10:
            del chain_of_emotion[0]
        
        response_input = '''Here is the events that the player encountered:{}
                            Here is what player said:{}
                            Here is what you feel:{} '''
        
        agent_response = llm.llm_response.invoke(
            [llm.responsesystemprompt,('human',response_input.format(history.content,user_input,agent_apresponse.content))]
        )
        
        print("AGENT : {}".format(agent_response.content))

main()