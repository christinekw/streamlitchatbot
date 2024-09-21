from langchain_groq import ChatGroq
import AIchatbot.appraisalprompt as appraisalprompt
import AIchatbot.systemmsg as systemmsg
from langchain_core.prompts import ChatPromptTemplate



class Model(object):
    def __init__(self):
        # Load the model
        self.llm_appraisal = ChatGroq(model="llama3-70b-8192",temperature=0.7,presence_penalty=0.5,
                            api_key="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")
        self.llm_response = ChatGroq(model="llama3-70b-8192",temperature=0.7,presence_penalty=0.5,
                            api_key="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")
        self.llm_summarize = ChatGroq(model="llama3-70b-8192",temperature=0.3,presence_penalty=0.3,
                            api_key="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")
        
        self.appraisalprompt = appraisalprompt.appra_prompt
        self.responsesystemprompt= ("system",systemmsg.sys)
        
        
    def generate_response(self, message):
        return self.llm.generate_response(message)
   