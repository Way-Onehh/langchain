#与pdf的清晰度有关
#Tesseract-OCR
#poppler-24.08.0



import fitz  # PyMuPDF 
from pdf2image import convert_from_path 
import pytesseract 
from PIL import Image, ImageFilter 
 
def extract_text_from_pdf(pdf_path):
    """
    从PDF文件中提取文字,包括可编辑文本和图片中的文字。
    :param pdf_path: PDF文件路径 
    :return: 提取的文字内容 
    """
    text = ""
 
    # 1. 提取可编辑文本 
    try:
        doc = fitz.open(pdf_path) 
        for page_num in range(len(doc)):
            page = doc.load_page(page_num) 
            text += page.get_text("text")  + "\n"
    except Exception as e:
        print(f"提取可编辑文本时出错: {e}")
 
    # 2. 提取图片中的文字 
    try:
        # 将PDF转换为图片 
        images = convert_from_path(pdf_path)
 
        for image in images:
            #图片预处理：灰度化、锐化、二值化 
            image = image.convert('L')   # 灰度化 
            image = image.filter(ImageFilter.SHARPEN)   # 锐化 
            image = image.point(lambda  x: 0 if x < 128 else 255, '1')  # 二值化 
 
            # 使用OCR提取文字 
            ocr_text = pytesseract.image_to_string(image,  lang='chi_sim')
            text += ocr_text + "\n"
    except Exception as e:
        print(f"提取图片文字时出错: {e}")
 
    return text 
 
# 示例使用 
if __name__ == "__main__":
    pdf_path = "config/4.pdf"   # 替换为您的PDF文件路径 
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)