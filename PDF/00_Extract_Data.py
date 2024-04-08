import os
import shutil
datapath = r'S:\Project\12090\02_地質資料數化作業\01_數化資料報告書及圖檔'
exclude_folder = r'00_不進行定位及數化之圖檔'
out_folder = r'D:\CECI\TPC\Digitize\07_ExtractData\output'
# 選擇要取出的地質資料類型
prefix = 'ETopo'

# 取出所有報告書中的地質資料
def Extract_Data(datapath, exclude_folder, prefix):
    if not os.path.exists(datapath):
        print(f'資料夾 {datapath} 不存在')
        return
    
    for root, dirs, files in os.walk(datapath):
        if exclude_folder in root.split(os.path.sep):
            continue

        for file in files:
            if file.startswith(prefix):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(out_folder, file)
                shutil.copy2(source_path, dest_path)
                print(f"檔案 '{file}' 已成功複製到目標資料夾中。")

Extract_Data(datapath, exclude_folder, prefix)                