import fitz  # PyMuPDF
import os

def pdf_to_png(input_folder, output_folder):
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有PDF文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename.split('.')[0] + '.png')

            # 打开PDF文件
            pdf_document = fitz.open(pdf_file_path)

            # 逐页将PDF文件转换为PNG图像
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                pixmap = page.get_pixmap(alpha=False)
                pixmap.save(output_file_path,output = 'png')
                #pixmap.save(output_file_path[:-4] + "_page%d" % page_num, output = 'png')                                  

            # 关闭PDF文件
            pdf_document.close()

# 示例用法
input_folder = ".\\input"
output_folder = ".\\output"
pdf_to_png(input_folder, output_folder)
