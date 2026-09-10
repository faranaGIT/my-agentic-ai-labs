from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
# used to run multiple chains in parallel
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

#prompt1 and prompt2 will run in parallel and then the output of both will be passed to prompt3 
# to generate a final output
prompt1 = PromptTemplate(
    template="""
    Write a beginner friendly article on {topic}
    """,
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="""
    Generate a professional Linkedin post with a strong hook on below mentioned topic: \n topic: {topic}
    """,
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="""
    Merge the provided article and LinkedIn post into a single document \n {article} and LinkedIn post {post}
    """,
    input_variables=["article", "post"]
)

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
#here is the parallel chain that will run prompt1 and prompt2 in parallel and
#then the output of both will be passed to prompt3 to generate a final output
parellel_chain = RunnableParallel(
    {
        'article': prompt1 | model | StrOutputParser(),
        'post': prompt2 | model | StrOutputParser()
    }
)

# this chain will take the output of the parallel chain and pass it to prompt3 to generate a final output
document_chain = prompt3 | model | StrOutputParser()

chain = parellel_chain | document_chain

# this shows the graph of the chain and how the chains are connected to each other. It is useful for debugging and understanding the flow of the chain

print(chain.get_graph().draw_ascii())

# output of the parallel chain is passed to the document_chain and based on the output of the parallel chain, 
# the document_chain is executed.
print(chain.invoke({'topic': 'AI disruption in IT'}))