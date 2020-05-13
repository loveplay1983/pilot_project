from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from . import md5_gen_valid
from os.path import dirname, join, abspath


class SendSMS:
    """ Send SMS to the specified phone number based on Aliyun cloud service """

    def __init__(self):
        self.access_param = {'access_key': 'LTAI4GK1N2v5jNdoBfsKWvk5',
                             'access_secret': 'S2FD2Tk2Dtx6s9HlWvov37RQz2hLn5',
                             'region_id': 'cn-hangzhou'
                             }

        self.request_param = {'accept_format': 'json',
                              'domain': 'dysmsapi.aliyuncs.com',
                              'method': 'POST',
                              'protocol_type': 'https',
                              'version': '2017-05-25',
                              'action_name': 'SendSms',
                              'region_id': 'cn-hangzhou',
                              'sign_name': 'Michael宣',
                              'template_code': 'SMS_189025392'
                              }

    def access(self):
        client = AcsClient(self.access_param['access_key'], self.access_param['access_secret'], self.access_param['region_id'])
        return client

    @staticmethod
    def gen_valid_code():
        """
        from md5_gen_valid import xxx
        generate validation code in md5 uuid
        save the code to local JSON file

        use the code as the template param to send sms
        """
        file_path = abspath(dirname(__file__))
        pass_path = join(file_path, '../../rand_pass/unlock.json')
        md5_code = md5_gen_valid.GenMd5()
        rand_pass = md5_code.random_pass()
        get_uuid = md5_code.gen_md5(rand_pass)
        unlock_pass = md5_code.gen_random_choice(get_uuid, 6)
        # save md5 code to local json file
        return md5_code.save_to_json(pass_path, unlock_pass)

    def request_send_sms(self, phone_num=None):
        template_para = str(SendSMS.gen_valid_code())
        request = CommonRequest()
        request.set_accept_format(self.request_param['accept_format'])
        request.set_domain(self.request_param['domain'])
        request.set_method(self.request_param['method'])
        request.set_protocol_type(self.request_param['protocol_type'])
        request.set_version(self.request_param['version'])
        request.set_action_name(self.request_param['action_name'])
        request.add_query_param('RegionId', self.request_param['region_id'])
        request.add_query_param('SignName', self.request_param['sign_name'])
        request.add_query_param('PhoneNumbers', phone_num)
        request.add_query_param('TemplateCode', self.request_param['template_code'])
        request.add_query_param('TemplateParam', template_para)
        response = str(self.access().do_action_with_exception(request), encoding='utf-8')
        print(response)
        print(type(template_para), template_para)


if __name__ == '__main__':
    send = SendSMS()
    print(send.request_send_sms())
