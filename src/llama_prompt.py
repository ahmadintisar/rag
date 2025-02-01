SYSTEM_PROMPT = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer. """

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<>\n", "\n<>\n\n"
SYSTEM_PROMPT = B_SYS + SYSTEM_PROMPT + E_SYS
instruction = """
{context}

Question: {question}
"""
template = B_INST + SYSTEM_PROMPT + instruction + E_INST

template
