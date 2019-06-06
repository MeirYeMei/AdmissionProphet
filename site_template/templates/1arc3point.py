from selenium import webdriver
from pymongo import MongoClient
from site_template.base_template import BaseTemplate

class OneArc3PointTemplate(BaseTemplate):
    def __init__(self):
        super().__init__("oneArcThreePoint", proxy=False)
        self.root_url = [
            'https://www.1point3acres.com/bbs/thread-471012-1-1.html'
        ]
        driver = self.get_driver_instance()
        driver.get("http://www.1point3acres.com")
        cookie = {‘name’: ‘foo’, ‘value’: ‘bar’}
        driver.add_cookie(cookie)




    def get_available_applicants_list(self):
        """
        Get the url of all available applicants for the entire site, through checking walking over the category hierarchy.

        @return: [string] - a list of all the applicants urls
        @raise crawlerError: CrawlerException
        """

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