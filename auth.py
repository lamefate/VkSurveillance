import vk_api


class Auth:
    def __init__(self, params):
        self.v_login = params['Auth']['login']
        self.v_password = params['Auth']['password']
        self.api = self.fa_enabled()

    def fa_enabled(self, api=0):
        fa_status = input('is 2fa enabled [y/n]: ')
        if fa_status.lower() == 'y':
            print('info: authorization method with 2fa')
            api = self.auth_2fa_process()
        elif fa_status.lower() == 'n':
            print('info: authorization method without 2fa')
            api = self.auth_process()
        else:
            print('error: incorrectly entered answer, try again')
            self.fa_enabled()

        response = api.account.getProfileInfo(v=5.124)
        print('info: using account -> {} {}, id{}'.format(response['first_name'], response['last_name'], response['id']))

        return api

    def auth_handler(self):
        # called if 2fa is enabled
        key = input('2fa code: ')
        remember_device = True

        return key, remember_device

    def auth_2fa_process(self):
        # auth with 2fa support
        try:
            vk_session = vk_api.VkApi(self.v_login, self.v_password, auth_handler=self.auth_handler())
            vk_session.auth()
            return vk_session.get_api()
        except vk_api.AuthError as error_msg:
            print(error_msg)

    def auth_process(self):
        # auth without 2fa support
        try:
            vk_session = vk_api.VkApi(self.v_login, self.v_password)
            vk_session.auth()
            return vk_session.get_api()
        except vk_api.AuthError as error_msg:
            print(error_msg)

