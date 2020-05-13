from .md5_lib import *


class GenMd5:
    """ Generate md5 code from current time which utilized uuid and random passwords """

    @staticmethod
    def remove_char(target=None, remove=None):
        """ remove particular pattern from the target string """
        return target.translate(str.maketrans('', '', remove))

    @staticmethod
    def get_cur_time():
        """ return the current time from timestamp"""
        return str(datetime.fromtimestamp(time()))

    @staticmethod
    def random_pass_(length=12, symbols='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$^_+&', salt=None):
        """
        generate random password
        To-Do: fix IndexError: string index out of range
        """
        symbols = symbols + salt
        passwd = []
        for each in map(lambda x: int(len(symbols) * x / 255.0), urandom(length)):
            passwd.append(symbols[each])
        return ''.join(passwd)

    @staticmethod
    def random_pass():
        try:
            return GenMd5.random_pass_(salt=GenMd5.get_cur_time())
        except IndexError:
            return GenMd5.random_pass_(salt=GenMd5.get_cur_time())

    @staticmethod
    def gen_uuid(name=None, is_dash=True):
        """ generate uuid from random password with salt process"""
        if is_dash:
            return GenMd5.remove_char(str(uuid3(uuid.NAMESPACE_DNS, name)), '-')
        return str(uuid3(uuid.NAMESPACE_DNS, name))

    @staticmethod
    def gen_md5(uuid_str):
        """ generate md5 code from uuid outcome which produce extremely high security """
        md5 = hashlib.md5()
        md5.update(uuid_str.encode('utf-8'))
        return md5.hexdigest()

    @staticmethod
    def gen_random_choice(target, num_items):
        """ randomly choose some times from the generated md5 code"""
        random_choice = sample(target, num_items)
        return ''.join(each for each in random_choice)

    @staticmethod
    def save_to_json(file_path, rand_pass):
        """ save the generated random md5 code to local file """
        passwd = {'code': rand_pass}
        dump(passwd, open(file_path, 'w'))
        return str(passwd)
