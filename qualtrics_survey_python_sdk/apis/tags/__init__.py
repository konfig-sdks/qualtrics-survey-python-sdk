# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from qualtrics_survey_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SURVEY_QUOTAS = "Survey Quotas"
    SURVEYS = "Surveys"
    SURVEY_QUESTIONS = "Survey Questions"
    SURVEY_BLOCKS = "Survey Blocks"
    SURVEY_FLOWS = "Survey Flows"
    SURVEY_VERSIONS = "Survey Versions"
    SURVEY_OPTIONS = "Survey Options"
    SURVEY_LANGUAGES = "Survey Languages"
    SURVEY_TRANSLATIONS = "Survey Translations"
    SCHEMAS = "Schemas"
