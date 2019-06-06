import abc
import os
from selenium import webdriver

class BaseTemplate(abc):
    def __int__(self, site_identifier: str, proxy = False):
        '''
        :param site_identifier: the id of the site being crawled.
        :param proxy: if use proxy to crawl website
        '''
        self.resource_dir = "./data/" + self.site_identifier
        self.proxy = proxy
        if proxy:
            self.crawler_proxy = proxy.CrawlerProxy()
        if not os.path.exists(self.resource_dir):
            os.makedirs(self.resource_dir, exist_ok=True)


    @abc.abstractmethod
    def get_item(self, url, browser):
        '''
        :param url: url of an applicant's result table
        :param browser: default = firefox
        :return: [
         'application_year': int ,
         'application_semester':int,
         'major': string,
         'program_name': string,
         'degree': string,
         'scholarship': string,
         'submission_time': string,
         'application_result': string,
         'target_school_name':string,
         'reply_time': string,
        'personal_other_info':string,
        'undergrad_school_level': string,
        'undergrad_school_name': string,
        'undergrad_major': string,
        'undergrad_GPA_Ranking':string,
        'grad_school_level': string,
        'grad_school_name': string,
        'grad_school_major':string,
        'grad_school_GPA_Ranking': string,
        'toefl': string,
        'gre': string,
        'gre_sub': string,
        'intern_or_refer': string,
        'result_country': string,
        'receiving_status_method': string
        ]
        '''
        raise Exception("Implement in sub-class")

    def get_driver_instance(self):
        """
        Get a driver instance.

        @return: webdriver - a selenium web driver object
        """
        if self.proxy:
            return webdriver.Firefox(proxy=self.crawler_proxy.get_random_proxy())
        else:
            return webdriver.Firefox()

    @abc.abstractmethod
    def get_available_applicants_list(self):
        """
        Get the url of all available applicants for the entire site, through checking walking over the category hierarchy.

        @return: [string] - a list of all the applicants urls
        @raise crawlerError: CrawlerException
        """
