from langchain_openrouter import ChatOpenRouter
# this is dependency for templates, it allows to create a prompt template that can be used
#  to generate prompts for the ChatOpenRouter model.

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
# this is a simple example of how to use templates to generate prompts for the ChatOpenRouter model. 
# The PromptTemplate class allows you to define a template with placeholders that can be filled in with specific values when generating prompts. In this example, we are creating a template that asks the model to write an article on a given topic in 100 words.
template = PromptTemplate(template="Write an article on the concept of {topic} in 100 words")

# before this is how we did it without templates, we had to manually create the prompt for each topic 
# we wanted to ask the model about. With templates, we can easily generate prompts for different topics 
# by simply filling in the placeholder with the desired value.
# prompt1 = template.invoke({'topic':'AI'})
# prompt2 = template.invoke({'topic': 'CyberSecurity'})

# response = model.invoke(prompt1)
# this would only work for prompt1, so if we wanted to ask the model about a different topic, 
# we would have to create a new prompt manually.
# for this we use the str output parser to parse the output of the model and get the content of the response.

# print(response.content)
#this is a simple example of how to use the ChatOpenRouter model to get a response to a question.
# template output is passed to the model and the response is parsed using the StrOutputParser to get the content of
#  the response.
# LCEL stands for LangChain Execution Layer, which is a way to chain together different components of a LangChain application. In this case, we are chaining together the template, model, and output parser to create a complete pipeline for generating prompts and getting responses from the model.
chain = template | model | StrOutputParser() #LCEL

print(chain.invoke({'topic': 'Cyber Security'}))