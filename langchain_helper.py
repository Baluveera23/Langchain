from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import Google_API_Key

import os
os.environ['GOOGLE_API_KEY']= Google_API_Key

def generate_restaurant_name_and_item(Selected):
    llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="Give me a meaning about the Indian male name that is {cuisine}, describe the name in words seperated by a commas, give the words only as output.")

    name = LLMChain(llm=llm,prompt=prompt_template_name,output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="list 5 male and 5 female Indian names that should give similar meaning to {restaurant_name}, categorized as Boy names and Girl names without the side heading of Boy Names and Girl Names.But the name should given seperately with comma separation, without any extra explanation or content.do not give the random names give accurate names that related to the given name"
    )
    items = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    from langchain.chains import SequentialChain

    chain = SequentialChain(
    chains = [name,items],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items'])
    response = chain({'cuisine':Selected})
    return response

