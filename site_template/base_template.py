import abc


class BaseTemplate(abc):
    @abc.abstractmethod
    def get_item(self, url, browser):
        '''
        :param url:
        :param browser:
        :return:
        '''