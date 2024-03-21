import fitz
import glob
import os
#\0 報告書及圖冊
#\1 鑽孔柱狀圖
#\2 地質剖面圖 BGeoP_TA000001_P60
#\3 地物剖面圖 CGeoPhyP_TA000001_P60
#\4 測傾管 DHsta_TA000001_P60
#\5 地形圖 ETopo_TA000001_P60
#\6 地質圖 FGeo_TA000001_P60
#\7 井測資料 GH_TA000001_P60
#\8 地下水位 HWt_TA000001_P60
#\9 位移 IDis_TA000001_P60
#\10 地質試坑J Log_TA000001_P60

#參數設定
file_path = ".\\input"
#serial_num = "TA002350"
#data_type = 8
file_code = "HWt"

# 0 for disparate pages, 1 for consecutive pages
mode = 0
#### consecutive pages ####
multipages = [3,4]
#start_page = 1
#end_page = 1

#### disparate pages ####
#pages = [65,66,67,68,69,70,71]
#pages = [72,73,74,76]
#pages = [16,20,26,33,38,51,55,60,63,67,69,72,75,77,80,82,90,92,94,96,98]
pages = [5,6]
pages = list(map(lambda x: x-1, pages))
rotation = 0  # True = 1, False = 0

input_pdf =  glob.glob(f"{file_path}\\*.pdf")[0]
serial_num = input_pdf.split('\\')[2][:8]
print(f"processing file: {input_pdf}")
output_file = f".\\output\\{file_code}"

def split_pdf(input_pdf, output_file):
    pdf_document = fitz.open(input_pdf)
    #for page_num in range(start_page - 1, end_page):
    if mode == 1:
        for page_num in range(multipages[0]-1,multipages[1]):
            page = pdf_document[page_num]
            if rotation == 1:
                pdf_document[page_num].set_rotation(180)   
            if page_num == multipages[0]-1:
                new_pdf = fitz.open()
                new_pdf.insert_pdf(pdf_document, from_page=multipages[0]-1, to_page=multipages[1]-1)
                output_pdf = f"{output_file}_{serial_num}_P{page_num+1}.pdf"
                if os.path.exists(output_pdf):
                    os.remove(output_pdf)
                new_pdf.save(output_pdf)
                new_pdf.close()
        pdf_document.close()
    else:
        for page_num in pages:
            page = pdf_document[page_num]

            if rotation == 1:
                pdf_document[page_num].set_rotation(180)            

            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

            output_pdf = f"{output_file}_{serial_num}_P{page_num+1}.pdf"
            if os.path.exists(output_pdf):
                os.remove(output_pdf)

            new_pdf.save(output_pdf)
            new_pdf.close()
        pdf_document.close()

if __name__ == "__main__":
    split_pdf(input_pdf, output_file)