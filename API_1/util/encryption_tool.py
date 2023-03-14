import hashlib
import base64


class EncryptionTool:

    def md5(self, data):
        res = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
        return res

    # 加密
    def base64_encode(self, data):
        return base64.b64encode(data.encode('utf-8'))

    # 解密
    def base64_decode(self, data):
        return base64.b64decode(data)


if __name__ == '__main__':
    pwd = "123qwer"
    md5 = EncryptionTool().md5(pwd)
    ba = EncryptionTool().base64_encode(pwd)
    print(md5)
