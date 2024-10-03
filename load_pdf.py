import asyncio
from langchain_community.document_loaders import PyPDFLoader

async def load_pdf():
    loader = PyPDFLoader("https://github.com/langchain-ai/langchain/raw/master/libs/community/tests/integration_tests/examples/layout-parser-paper.pdf")
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    #print(f"{pages}\n")
    print(f"{pages[0].metadata}\n")
    print(pages[0].page_content)

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(load_pdf())
