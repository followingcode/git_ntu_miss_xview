import pickle

pkl_file_path = '/root/pyskl/tools/data/nturgbd/ntu60_hrnet.pkl'
with open(pkl_file_path, 'rb') as file:
    pkl_data = pickle.load(file)

# 从 pkl 数据中获取 xview_train 和 xview_val 列表
xview_train_list = pkl_data["split"]["xview_train"]
xview_val_list = pkl_data["split"]["xview_val"]

# 从 txt 文件中读取所有文件路径，并提取文件名
txt_file_path = '/root/pyskl/until/xview_train_test_total.list'
with open(txt_file_path, 'r') as file:
    file_lines = file.readlines()

file_names = [line.strip().split('/')[-1].split('.')[0] for line in file_lines if 'Train' in line]

# 找出 file_names 中不存在于 xview_train_list 的项
missing_files = [item for item in file_names if item not in xview_train_list]

# 将不存在的项保存到新的 txt 文件中
missing_files_path = '/root/pyskl/until/xview_train_not_in.txt'
with open(missing_files_path, 'w') as file:
    for item in missing_files:
        file.write(f"{item}\n")

# 从另一个 txt 文件中读取所有文件路径，并提取文件名
val_file_path = '/root/pyskl/until/xview_train_test_total.list'
with open(val_file_path, 'r') as file:
    val_lines = file.readlines()

val_file_names = [line.strip().split('/')[-1].split('.')[0] for line in val_lines if 'Test' in line]

# 找出 val_file_names 中不存在于 xsub_val_list 的项
val_files = [item for item in val_file_names if item not in xview_val_list]

# 将不存在的项保存到新的 txt 文件中
val_not_in_path = '/root/pyskl/until/xview_val_not_in.txt'
with open(val_not_in_path, 'w') as file:
    for item in val_files:
        file.write(f"{item}\n")


