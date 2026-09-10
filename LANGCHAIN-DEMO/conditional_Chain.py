from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
# runnable branch is a way to create a conditional chain that can execute different branches 
# based on the output of the previous chain. It allows you to create a chain that
#  can handle different scenarios and execute different logic based on the output of the previous chain.

from langchain_core.runnables import RunnableBranch
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal
import os

# use case : Conditional Chain - feedback about product and classify it into positive or negative and then send a thank you email for positive feedback and apology email for negative feedback.

load_dotenv()

class Feedback(BaseModel):
    customer_name: str =Field(description="Name of the customer")
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

# predefined class allows to pass pydantic model to the output parser and get the output in the form of pydantic model. 
# This is useful when we want to get the output in a structured format and use it for further processing.
# format instructions are used to tell the model how to format the output. In this case,
# we are telling the model to output the sentiment in a structured format that can be parsed by the PydanticOutputParser.
# pydantic library to define models in this case we use to define the structure of the output that we want 
# to get from the model. The PydanticOutputParser allows us to parse the output of the model 
# and convert it into a Pydantic model that can be used for further processing.
# we are specifying the structure of the output that we want to get from the model.
# In this case, we want to get the sentiment of the feedback in a structured format that can be parsed by the PydanticOutputParser.
pyparser = PydanticOutputParser(pydantic_object=Feedback)

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

prompt1 = PromptTemplate(template="""
Analyze the sentiment of the following feedback and classify it into positive or negative \n {feedback} \n {format_instructions}
""", input_variables=["feedback"], validate_template=True, partial_variables={'format_instructions': pyparser.get_format_instructions()})

chain1 = prompt1 | model | pyparser

positive_email_prompt = PromptTemplate(
    template="""
    Write a thank you email to the customer for giving a positive feedback about his recent purchase of IPhone 16.
    \n {feedback}
    """,
    input_variables=["feedback"]
)


negative_email_prompt = PromptTemplate(
    template="""
    Write an apology email to the customer for giving a negative feedback about his recent purchase of IPhone 16.
    \n {feedback}
    """,
    input_variables=["feedback"]
)

# Writing the conditional chain
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_email_prompt | model | StrOutputParser()),
    (lambda x:x.sentiment == 'negative', negative_email_prompt | model | StrOutputParser()),
    (lambda x: "Not able to analyze the feedback")
)
# output of the first chain is passed to the second chain and based on the output of the first chain, the second chain is executed.

chain = chain1 | branch_chain

# this shows the graph of the chain and how the chains are connected to each other. It is useful for debugging and understanding the flow of the chain.
print(chain.get_graph().draw_ascii())

# option of positive and negative feedback is given to the model to classify the feedback into positive or negative.

# print(chain.invoke({'feedback': 'The phone is really good and it is meeting my expectations. I am really happy. Name - Dhiraj'}))
print(chain.invoke({'feedback': 'The phone is really bad and it is not meeting my expectations. I am really disappointed. Name - Dhiraj'}))
