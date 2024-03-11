from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
import os
import knowledge
load_dotenv()
api_key=os.environ.get("OPENAI_API_KEY")

def chat(query):
    knowledge_base=knowledge.get_knowledge()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106")
    qa_chain = load_qa_chain(llm, chain_type='stuff')

    def get_response(query):
        system_message = '''You are a financial analyst, Answer based on the context in the most detail as possible. YOU MUST provide the statistic or the inference that is needed '''
        input_message= f"{system_message}\n\n User: {query}"
        docs = knowledge_base.similarity_search(input_message)
        with get_openai_callback() as cost:
            response = qa_chain.run(input_documents= docs, question=input_message)
            return response
        return "I am sorry, try again" 
    return get_response(query)


