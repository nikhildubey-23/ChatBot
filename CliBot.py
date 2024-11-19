from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

print("If you want answer in the form of paragraph use p for that and if you want answer in step by step form use step key word")
print("If you want to exit use iwe in your input feild ")

answer_type = input("Enter your answer type (p/step):-  ")

if answer_type == "iwe":
    exit()

elif answer_type == "p":
    
    template = """Question: {question}

    Answer: In a form of paragraph."""

elif answer_type == None:
    template = """Question: {question}

    Answer: Let's think step by step."""

else:
    template = """Question: {question}

    Answer: Let's think step by step."""


prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model

while   True:
    question = input("Enter your question:-  ")
    

    if question == "iwe":
        exit()
    else:
        answer = chain.invoke({"question":question})
        print(answer)


