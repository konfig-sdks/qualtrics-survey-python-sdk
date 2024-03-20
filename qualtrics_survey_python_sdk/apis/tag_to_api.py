import typing_extensions

from qualtrics_survey_python_sdk.apis.tags import TagValues
from qualtrics_survey_python_sdk.apis.tags.survey_quotas_api import SurveyQuotasApi
from qualtrics_survey_python_sdk.apis.tags.surveys_api import SurveysApi
from qualtrics_survey_python_sdk.apis.tags.survey_questions_api import SurveyQuestionsApi
from qualtrics_survey_python_sdk.apis.tags.survey_blocks_api import SurveyBlocksApi
from qualtrics_survey_python_sdk.apis.tags.survey_flows_api import SurveyFlowsApi
from qualtrics_survey_python_sdk.apis.tags.survey_versions_api import SurveyVersionsApi
from qualtrics_survey_python_sdk.apis.tags.survey_options_api import SurveyOptionsApi
from qualtrics_survey_python_sdk.apis.tags.survey_languages_api import SurveyLanguagesApi
from qualtrics_survey_python_sdk.apis.tags.survey_translations_api import SurveyTranslationsApi
from qualtrics_survey_python_sdk.apis.tags.schemas_api import SchemasApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SURVEY_QUOTAS: SurveyQuotasApi,
        TagValues.SURVEYS: SurveysApi,
        TagValues.SURVEY_QUESTIONS: SurveyQuestionsApi,
        TagValues.SURVEY_BLOCKS: SurveyBlocksApi,
        TagValues.SURVEY_FLOWS: SurveyFlowsApi,
        TagValues.SURVEY_VERSIONS: SurveyVersionsApi,
        TagValues.SURVEY_OPTIONS: SurveyOptionsApi,
        TagValues.SURVEY_LANGUAGES: SurveyLanguagesApi,
        TagValues.SURVEY_TRANSLATIONS: SurveyTranslationsApi,
        TagValues.SCHEMAS: SchemasApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SURVEY_QUOTAS: SurveyQuotasApi,
        TagValues.SURVEYS: SurveysApi,
        TagValues.SURVEY_QUESTIONS: SurveyQuestionsApi,
        TagValues.SURVEY_BLOCKS: SurveyBlocksApi,
        TagValues.SURVEY_FLOWS: SurveyFlowsApi,
        TagValues.SURVEY_VERSIONS: SurveyVersionsApi,
        TagValues.SURVEY_OPTIONS: SurveyOptionsApi,
        TagValues.SURVEY_LANGUAGES: SurveyLanguagesApi,
        TagValues.SURVEY_TRANSLATIONS: SurveyTranslationsApi,
        TagValues.SCHEMAS: SchemasApi,
    }
)
