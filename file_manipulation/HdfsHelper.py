import pyhdfs


class HdfsHelper(object):
    def __init__(self, host):
        self.fs = pyhdfs.HdfsClient(host)
        print("successfully obtain hdfs client")

    # 删除
    def delFile(self, path):
        fs = self.fs
        fs.delete(path)

    # 上传文件
    def upload(self, localsrc, dest):
        fs = self.fs
        fs.copy_from_local(localsrc, dest)
        print(localsrc+" has been successfully uploaded to "+dest)

    # 下载文件
    def download(self, src, localdest):
        fs = self.fs
        fs.copy_to_local(src, localdest)

    # 新建目录
    def makdir(self, dest):
        fs = self.fs
        if not fs.exists(dest):
            fs.mkdirs(dest)
            return True
        return False

    # 重命名
    def rename(self, srcPath, dstPath):
        fs = self.fs
        if not fs.exists(srcPath):
            return
        fs.rename(srcPath, dstPath)

    def exists(self, path):
        fs = self.fs
        return fs.exists(path)
