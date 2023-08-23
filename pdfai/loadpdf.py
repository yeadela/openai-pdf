from langchain.document_loaders import PyPDFLoader


def loadPdf(filePath):
    return PyPDFLoader.load_and_split(filePath)
    