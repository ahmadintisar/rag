from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from transformers import SentenceTransformer

from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os


#Loading Preprocessed Data Through LangChain Loader
loader = PyPDFLoader("/content/drive/MyDrive/LegalContractsProject/0002-37-1-Kolt.pdf")
data = loader.load()


#Data Step: Split the data into manageable chunks with overlap
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)  #Testing with chunk_size=500
docs=text_splitter.split_documents(data)
len(docs)

#Loading Embeddings Transformer
from sentence_transformers import SentenceTransformer

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

from pinecone import Pinecone

pc = Pinecone(api_key="d72a2ab9-68bb-4aa4-b6d4-bdf174efa908")
index = pc.Index("legal")

from langchain.vectorstores import Pinecone as PineconeStore
from pinecone import Pinecone
from langchain.vectorstores import Pinecone

os.environ["PINECONE_API_KEY"] = "d72a2ab9-68bb-4aa4-b6d4-bdf174efa908"
index_name= "legal"

docsearch=Pinecone.from_texts([t.page_content for t in docs], embeddings, index_name=index_name)

#Semantic Search

query="Role of LLMs in Contract Generation"
search=docsearch.similarity_search(query, k=20)


query="Legal Compliance and Ethical Considerations"
search=docsearch.similarity_search(query, k=20)

from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from huggingface_hub import hf_hub_download
from langchain.chains.question_answering import load_qa_chain
from huggingface_hub import notebook_login
import torch
from langchain import HuggingFacePipeline, PromptTemplate

from langchain.chains import RetrievalQA

#Access to HuggingFace
notebook_login()

#Import LLAMA-2-7b Tokenizer
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True)

#Import LLAMA-2-7b Base Model
from transformers import AutoTokenizer, AutoModelForCausalLM

#model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf").to('cuda') #Cuda==Shift to GPU
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf") ####CRASHING DUE TO LOW SYSTEM RAM ----30-50GB

from transformers import pipeline

pipe = pipeline("text-generation",
                model=model,
                tokenizer= tokenizer,
                torch_dtype=torch.bfloat16, # Use bfloat16 for mixed precision
                device_map="auto",
                max_new_tokens = 512,
                do_sample=True,
                top_k=30,
                num_return_sequences=1,
                eos_token_id=tokenizer.eos_token_id
                )




llm=HuggingFacePipeline(pipeline=pipe, model_kwargs={'temperature':0.3})
prompt = PromptTemplate(template=template, input_variables=["context", "question"])

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  #stuff,experimental, accuracy
    retriever=docsearch.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt},

)
result = qa_chain("Role of LLMs in Contract Generation")
result