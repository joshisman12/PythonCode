import fitz  # PyMuPDF
import glob

def merge_pdfs(pdf_paths, output_path):
    # 创建一个新的PDF文件对象
    merged_pdf = fitz.open()

    # 遍历每个PDF文件路径
    for pdf_path in pdf_paths:
        # 打开当前PDF文件
        pdf_document = fitz.open(pdf_path)
        merged_pdf.insert_pdf(pdf_document)
        pdf_document.close()

    # 保存合并后的PDF文件
    merged_pdf.save(output_path)
    merged_pdf.close()

    print("PDF files merged successfully!")

# 要合并的PDF文件列表
pdf_paths = glob.glob(".\\input\\*.pdf")

# 合并后的PDF文件路径
output_pdf_path = ".\\output\\merged_pdf.pdf"

# 调用合并函数
merge_pdfs(pdf_paths, output_pdf_path)
