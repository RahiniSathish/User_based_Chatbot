from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from config import (
    API_KEY,
    AZURE_ENDPOINT,
    API_VERSION,
    DEPLOYMENT_ID
)

# Load Azure Chat Model
llm = AzureChatOpenAI(
    model=DEPLOYMENT_ID,
    api_key=API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version=API_VERSION,
    openai_api_type="azure",
    temperature=0
)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question as clearly and accurately as possible:\n\nQuestion: {question}\nAnswer:"
)

# LLM Chain
chain = LLMChain(prompt=prompt, llm=llm)

# Main function to get real answer from Azure LLM
def get_answer(question: str) -> str:
    try:
        print("📡 Calling Azure OpenAI...")
        return chain.run(question)
    except Exception as e:
        return f"[❌ LLM Error]: {str(e)}"
