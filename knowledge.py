from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import pandas as pd
def get_knowledge():
    def get_chunks(Data):
        titles=Data.columns
        Data = Data.map(lambda x: x.strip() if isinstance(x, str) else x)
        text_data = Data.to_string(index=False)
        text = "".join(text_data)
        document = 'Ω' + text
        for title in titles:
            document = document.replace(title, 'Ω' + title)
        chunk=document.split('Ω')[1:]
        return chunk
    def load_data(path1,path2):
        df1 = pd.read_excel(path1)
        df2 = pd.read_excel(path2)
        embeddings = HuggingFaceEmbeddings()
        chunk1=get_chunks(df1)
        chunk2=get_chunks(df2)
        kb1=FAISS.from_texts(chunk1, embeddings)
        kb2=FAISS.from_texts(chunk2, embeddings)
        kb1.merge_from(kb2)
        return kb1
    return load_data('sheet1.xlsx','sheet2.xlsx')
