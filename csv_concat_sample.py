from cmath import log
import pandas as pd
import os

log_filepath = r"\\172.27.21.41\disk1\PJ7_製造技術員室\0_工場IoT\08_ソフトウェアサポート_pgmTeam\ビックデータ解析\20220412\CPD81Analog2"
# フォルダ内のファイルリスト取得
log_lists = os.listdir(log_filepath)
# print(log_lists)
# 空のdf作成
log_all_df = pd.DataFrame()
# csvを入れるリスト
csv_all_list = []
# csvを読み込む
for log_list in log_lists:
    # ファイルのパス作成
    log_list_path = log_filepath + "\\" + log_list
    # csvのリスト作成
    csv_all_list.append(pd.read_csv(log_list_path, engine='python', encoding="cp932", header=1))
    # csvファイルを縦に結合
    log_all_df = pd.concat(csv_all_list, axis=0, sort=True)
# print(log_all_df)    
# csvファイルの作成
log_all_df.to_csv(log_filepath + "\\" + "test.csv")
