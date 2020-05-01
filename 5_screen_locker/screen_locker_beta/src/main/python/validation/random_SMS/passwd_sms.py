from sms_lib import *

client = AcsClient('LTAI4GK1N2v5jNdoBfsKWvk5', 'S2FD2Tk2Dtx6s9HlWvov37RQz2hLn5', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https')  # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "18957571829")
request.add_query_param('SignName', "Michael宣")
request.add_query_param('TemplateCode', "SMS_189025392")
request.add_query_param('TemplateParam', '{"code": "helloworld"}')

response = client.do_action(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
