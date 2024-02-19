import fitz
import glob
import os
import shutil
import time
folder_path = r".\\TA002350\\0"
folder_name = folder_path.split("\\")[2]

#rename input file
inp_file = glob.glob(f"{folder_path}\\*.pdf")[0]
inp_file_rename = f"{folder_path}\\{folder_name}.pdf"

if not os.path.exists(inp_file_rename):
    shutil.copy(inp_file, inp_file_rename)
    print(f"已複製檔案並重新命名為{folder_name}.pdf")
else:
    print(f"{folder_name}.pdf已存在")
new_filename = f"{folder_path}\\{folder_name}.pdf"

#create output folder
out_type = "6"
out_path = folder_path.split("\\")[0]+"\\"+folder_path.split("\\")[1]+"\\"+folder_path.split("\\")[2]+"\\"+out_type
out_path_output = os.path.join(out_path, "output")
out_path_skipped = os.path.join(out_path, "skipped")

if not os.path.exists(out_path):
    os.makedirs(out_path)
if not os.path.exists(out_path_output):
    os.makedirs(out_path_output)
if not os.path.exists(out_path_skipped):
    os.makedirs(out_path_skipped)


t0 = time.time()
pdf_document = fitz.open(new_filename)

#找出重複十次以上的xref
xref_count = {}
for current_page in range(len(pdf_document)):
    for image in pdf_document.get_page_images(current_page):
        xref = image[0]

        # 更新 xref 的出現次數
        xref_count[xref] = xref_count.get(xref, 0) + 1

# 儲存已處理過的 xref，每個 xref 只需要處理一次
processed_xrefs = set()

for current_page in range(len(pdf_document)):
   for image in pdf_document.get_page_images(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)

        if xref_count[xref] <= 10:
            if pix.n < 5:        # this is GRAY or RGB
               # pix.writePNG("page%s-%s.png" % (current_page, xref))
                pix.save(f"{out_path_output}\\page%s-%s.png" % (current_page+1, xref), output="png")
            else:                # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix.save(f"{out_path_output}\\page%s-%s.png" % (current_page+1, xref), output="png")
                pix1 = None
        elif xref_count[xref] > 10 and xref not in processed_xrefs:
            processed_xrefs.add(xref)
            pix.save(f"{out_path_skipped}\\page%s-%s.png" % (current_page + 1, xref), output="png")
        pix = None
        
pdf_document.close()
t1 = time.time()
execution_time = t1 - t0
print(f"運行時間: {execution_time} 秒")