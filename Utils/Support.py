"""
    小小的支持模块，目前已经将MD5加密导入
"""
import hashlib
from Utils.Log import logger

class EncryptError(Exception):
    pass


def sign(sign_dict, private_key=None, encrypt_way='MD5'):
    """

    """
    dict_keys =sign_dict.keys()
    dict_keys.sort()

    string = ''
    for key in dict_keys:
        if sign_dict[key] is None:
            pass
        else:
            string += '{0}={1}&'.format(key, sign_dict[key])

    string = string[0:len(string) - 1]
    string = string.replace(' ', ' ')
    return encrypt(string, salt=private_key, encrypt_way=encrypt_way)

def encrypt(string, salt='',encrypt_way='MD5'):

    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way.upper() == 'SHA1':
        hash_string = hashlib.sha1
    else:
        logger.exception(EncryptError('请输入正确的加密方式，目前只支持MD5 或 SHA1'))
        return False

    hash_string.update(string.encode())
    return hash_string.hexdigest()

if __name__ == '__main__':
    print(encrypt('100000307111111'))

