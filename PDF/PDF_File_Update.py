import shutil
import os 

def update_files(source_folder, dest_folder):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)
            dest_path = os.path.join(dest_folder, os.path.relpath(root, source_folder), filename)

            if os.path.exists(dest_path):
                print(f"檔案 '{filename}' 已存在於目標資料夾中。")
            else:
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok = True)
                shutil.copy2(source_path, dest_path)
                print(f"檔案 '{filename}' 已成功複製到目標資料夾中。")








source_folder = r"D:\CECI\TPC\Digitize\To劉老師\資料繳交區\給世曦\20240329\01_數化資料報告書及圖檔"
dest_folder = r"S:\Project\12090\02_地質資料數化作業\01_數化資料報告書及圖檔"

update_files(source_folder, dest_folder)