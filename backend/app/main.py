from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["GROQ_API_KEY"] = "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"  # Replace with your real key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

university_data = """
Department of Computer Science offers courses like AI, ML, Data Science, and Cybersecurity.
The Dean of Engineering is Dr. Deepak.
Semester begins on August 1st and ends on December 15th.
All students must maintain 75% attendance to sit for exams.
Library timings are from 8 AM to 10 PM on weekdays.
"""

template = """
You are a helpful assistant for university students.

Here is the university info:
{university_data}

Student Question: {student_question}

Provide a clear and helpful answer.
"""

prompt = PromptTemplate(
    input_variables=["university_data", "student_question"],
    template=template
)

llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.3)
chain = LLMChain(llm=llm, prompt=prompt)

@app.post("/ask")
async def ask_question(q: Question):
    response = chain.run({
        "university_data": university_data,
        "student_question": q.question
    })
    return {"answer": response}