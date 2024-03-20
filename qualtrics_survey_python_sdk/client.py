# coding: utf-8
"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

import typing
import inspect
from datetime import date, datetime
from qualtrics_survey_python_sdk.client_custom import ClientCustom
from qualtrics_survey_python_sdk.configuration import Configuration
from qualtrics_survey_python_sdk.api_client import ApiClient
from qualtrics_survey_python_sdk.type_util import copy_signature
from qualtrics_survey_python_sdk.apis.tags.survey_blocks_api import SurveyBlocksApi
from qualtrics_survey_python_sdk.apis.tags.survey_flows_api import SurveyFlowsApi
from qualtrics_survey_python_sdk.apis.tags.survey_languages_api import SurveyLanguagesApi
from qualtrics_survey_python_sdk.apis.tags.survey_options_api import SurveyOptionsApi
from qualtrics_survey_python_sdk.apis.tags.survey_questions_api import SurveyQuestionsApi
from qualtrics_survey_python_sdk.apis.tags.survey_quotas_api import SurveyQuotasApi
from qualtrics_survey_python_sdk.apis.tags.survey_translations_api import SurveyTranslationsApi
from qualtrics_survey_python_sdk.apis.tags.survey_versions_api import SurveyVersionsApi
from qualtrics_survey_python_sdk.apis.tags.surveys_api import SurveysApi



class Qualtrics(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.survey_blocks: SurveyBlocksApi = SurveyBlocksApi(api_client)
        self.survey_flows: SurveyFlowsApi = SurveyFlowsApi(api_client)
        self.survey_languages: SurveyLanguagesApi = SurveyLanguagesApi(api_client)
        self.survey_options: SurveyOptionsApi = SurveyOptionsApi(api_client)
        self.survey_questions: SurveyQuestionsApi = SurveyQuestionsApi(api_client)
        self.survey_quotas: SurveyQuotasApi = SurveyQuotasApi(api_client)
        self.survey_translations: SurveyTranslationsApi = SurveyTranslationsApi(api_client)
        self.survey_versions: SurveyVersionsApi = SurveyVersionsApi(api_client)
        self.surveys: SurveysApi = SurveysApi(api_client)
