from django.conf import settings
import phonenumbers
import requests



class ProceedOTP(object):

    def __init__(self,mobile):
        self.mobile = mobile
        self.access_token = getattr(settings, 'COGNALYS_ACCESS_TOKEN', '')
        self.app_id = getattr(settings, 'COGNALYS_APP_ID', '')
        self.api_version = getattr(settings, 'COGNALYS_API_VERSION', 'v1')


        p = self.mobile.replace("-", "").replace(" ", "")
        z = phonenumbers.parse(p, None)
        
        if not phonenumbers.is_valid_number(z):
            raise ValueError('Mobile Number is Not Valid')

        elif self.access_token == '':
            raise ValueError('Make sure COGNALYS_ACCESS_TOKEN is properly configured in settings.py')

        elif self.app_id == '':
            raise ValueError('Make sure COGNALYS_APP_ID is properly configured in settings.py')

        
        else:
            back = requests.get('https://www.cognalys.com/api/'+self.api_version+'/otp/?access_token='+self.access_token \
                                +'&app_id='+self.app_id+'&mobile='+p,verify=True)


            self.status =  back.json()['status']
            
            if back.json()['status'] == 'failed':
                self.error_messages = back.json()['errors'].values()
                self.error_codes = back.json()['errors'].keys()

            else:
                self.keymatch = back.json()['keymatch']
                self.mobile = back.json()['mobile']
                self.otp_start = back.json()['otp_start']



class ConfirmOTP(object):

    def __init__(self,keymatch,otp):
        self.keymatch = keymatch
        self.otp = otp
        self.access_token = getattr(settings, 'COGNALYS_ACCESS_TOKEN', '')
        self.app_id = getattr(settings, 'COGNALYS_APP_ID', '')
        self.api_version = getattr(settings, 'COGNALYS_API_VERSION', 'v1')



        if self.access_token == '':
            raise ValueError('Make sure COGNALYS_ACCESS_TOKEN is properly configured in settings.py')

        elif self.app_id == '':
            raise ValueError('Make sure COGNALYS_APP_ID is properly configured in settings.py')

        
        else:
            back = requests.get('https://www.cognalys.com/api/'+self.api_version+'/otp/confirm/?access_token='+self.access_token \
                                +'&app_id='+self.app_id+'&keymatch='+self.keymatch+'&otp='+self.otp,verify=True)


            self.status =  back.json()['status']
            
            if back.json()['status'] == 'failed':
                self.error_messages = back.json()['errors'].values()
                self.error_codes = back.json()['errors'].keys()

            else:
                self.mobile = back.json()['mobile']
                self.app_user_id = back.json()['app_user_id']

