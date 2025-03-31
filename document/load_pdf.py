from langchain_community.document_loaders  import PyPDFLoader 
import asyncio 
 
async def load_pdf():
    # 使用原始字符串避免转义问题 
    loader = PyPDFLoader(r"config\[啊哈！算法].啊哈磊.扫描版.pdf")
    pages = []
    async for page in loader.alazy_load(): 
        pages.append(page) 
    return pages 
 
# 调用异步函数 
pages = asyncio.run(load_pdf()) 
for page in pages:
    print(page.page_content)