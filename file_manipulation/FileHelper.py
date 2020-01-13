import json
import os
import zipfile


# 若不存在文件夹则创建文件夹
def create_directory_if_not_exist(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


# 默认文件的母目录必须存在
# 文件存在则删除，然后新创建文件存储数据
def store_data_to_file(data, file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, "w") as fd:
        json.dump(data, fd)


# 默认path有效
# 删除该目录或者文件
def remove_dir_or_file(path):
    if os.path.isfile(path):
        # 如果是文件则删除该文件
        os.remove(path)
    else:
        # 如果是目录
        # 先删除目录里的内容
        for i in os.listdir(path):  # os.listdir(path) 取path下的所有文件及目录
            path_file = os.path.join(path, i)  # 取文件绝对路径
            remove_dir_or_file(path_file)
        # 删除该目录
        os.removedirs(path)


# 压缩文件为zip，目标文件名称"xxx.zip"
def compress_directory_by_zip(src_dir, dst_filename):
    # 如果已经有压缩过的文件, 则删除
    remove_dir_or_file(dst_filename)
    z = zipfile.ZipFile(dst_filename, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(src_dir):
        # 绝对路径变相对路径
        f_path = dir_path.replace(src_dir, '') + os.sep
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()

