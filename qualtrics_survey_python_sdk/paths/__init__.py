# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from qualtrics_survey_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SURVEYDEFINITIONS = "/survey-definitions"
    SURVEYDEFINITIONS_SURVEY_ID = "/survey-definitions/{surveyId}"
    SURVEYDEFINITIONS_SURVEY_ID_METADATA = "/survey-definitions/{surveyId}/metadata"
    SURVEYDEFINITIONS_SURVEY_ID_BLOCKS = "/survey-definitions/{surveyId}/blocks"
    SURVEYDEFINITIONS_SURVEY_ID_BLOCKS_BLOCK_ID = "/survey-definitions/{surveyId}/blocks/{blockId}"
    SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS = "/survey-definitions/{surveyId}/questions"
    SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS_QUESTION_ID = "/survey-definitions/{surveyId}/questions/{questionId}"
    SURVEYDEFINITIONS_SURVEY_ID_FLOW = "/survey-definitions/{surveyId}/flow"
    SURVEYDEFINITIONS_SURVEY_ID_FLOW_FLOW_ID = "/survey-definitions/{surveyId}/flow/{flowId}"
    SURVEYDEFINITIONS_SURVEY_ID_OPTIONS = "/survey-definitions/{surveyId}/options"
    SURVEYDEFINITIONS_SURVEY_ID_VERSIONS = "/survey-definitions/{surveyId}/versions"
    SURVEYDEFINITIONS_SURVEY_ID_VERSIONS_VERSION_ID = "/survey-definitions/{surveyId}/versions/{versionId}"
    SURVEYDEFINITIONS_SURVEY_ID_QUOTAS = "/survey-definitions/{surveyId}/quotas"
    SURVEYDEFINITIONS_SURVEY_ID_QUOTAS_QUOTA_ID = "/survey-definitions/{surveyId}/quotas/{quotaId}"
    SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS = "/survey-definitions/{surveyId}/quotagroups"
    SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS_QUOTA_GROUP_ID = "/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}"
    SURVEYS_SURVEY_ID_LANGUAGES = "/surveys/{surveyId}/languages"
    SURVEYS_SURVEY_ID_TRANSLATIONS_LANGUAGE_CODE = "/surveys/{surveyId}/translations/{languageCode}"
