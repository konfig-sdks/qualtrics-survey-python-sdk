import typing_extensions

from qualtrics_survey_python_sdk.paths import PathValues
from qualtrics_survey_python_sdk.apis.paths.survey_definitions import SurveyDefinitions
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id import SurveyDefinitionsSurveyId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_metadata import SurveyDefinitionsSurveyIdMetadata
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_blocks import SurveyDefinitionsSurveyIdBlocks
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_blocks_block_id import SurveyDefinitionsSurveyIdBlocksBlockId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_questions import SurveyDefinitionsSurveyIdQuestions
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_questions_question_id import SurveyDefinitionsSurveyIdQuestionsQuestionId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_flow import SurveyDefinitionsSurveyIdFlow
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_flow_flow_id import SurveyDefinitionsSurveyIdFlowFlowId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_options import SurveyDefinitionsSurveyIdOptions
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_versions import SurveyDefinitionsSurveyIdVersions
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_versions_version_id import SurveyDefinitionsSurveyIdVersionsVersionId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_quotas import SurveyDefinitionsSurveyIdQuotas
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_quotas_quota_id import SurveyDefinitionsSurveyIdQuotasQuotaId
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_quotagroups import SurveyDefinitionsSurveyIdQuotagroups
from qualtrics_survey_python_sdk.apis.paths.survey_definitions_survey_id_quotagroups_quota_group_id import SurveyDefinitionsSurveyIdQuotagroupsQuotaGroupId
from qualtrics_survey_python_sdk.apis.paths.surveys_survey_id_languages import SurveysSurveyIdLanguages
from qualtrics_survey_python_sdk.apis.paths.surveys_survey_id_translations_language_code import SurveysSurveyIdTranslationsLanguageCode

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SURVEYDEFINITIONS: SurveyDefinitions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID: SurveyDefinitionsSurveyId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_METADATA: SurveyDefinitionsSurveyIdMetadata,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_BLOCKS: SurveyDefinitionsSurveyIdBlocks,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_BLOCKS_BLOCK_ID: SurveyDefinitionsSurveyIdBlocksBlockId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS: SurveyDefinitionsSurveyIdQuestions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS_QUESTION_ID: SurveyDefinitionsSurveyIdQuestionsQuestionId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_FLOW: SurveyDefinitionsSurveyIdFlow,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_FLOW_FLOW_ID: SurveyDefinitionsSurveyIdFlowFlowId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_OPTIONS: SurveyDefinitionsSurveyIdOptions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_VERSIONS: SurveyDefinitionsSurveyIdVersions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_VERSIONS_VERSION_ID: SurveyDefinitionsSurveyIdVersionsVersionId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAS: SurveyDefinitionsSurveyIdQuotas,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAS_QUOTA_ID: SurveyDefinitionsSurveyIdQuotasQuotaId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS: SurveyDefinitionsSurveyIdQuotagroups,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS_QUOTA_GROUP_ID: SurveyDefinitionsSurveyIdQuotagroupsQuotaGroupId,
        PathValues.SURVEYS_SURVEY_ID_LANGUAGES: SurveysSurveyIdLanguages,
        PathValues.SURVEYS_SURVEY_ID_TRANSLATIONS_LANGUAGE_CODE: SurveysSurveyIdTranslationsLanguageCode,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SURVEYDEFINITIONS: SurveyDefinitions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID: SurveyDefinitionsSurveyId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_METADATA: SurveyDefinitionsSurveyIdMetadata,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_BLOCKS: SurveyDefinitionsSurveyIdBlocks,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_BLOCKS_BLOCK_ID: SurveyDefinitionsSurveyIdBlocksBlockId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS: SurveyDefinitionsSurveyIdQuestions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUESTIONS_QUESTION_ID: SurveyDefinitionsSurveyIdQuestionsQuestionId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_FLOW: SurveyDefinitionsSurveyIdFlow,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_FLOW_FLOW_ID: SurveyDefinitionsSurveyIdFlowFlowId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_OPTIONS: SurveyDefinitionsSurveyIdOptions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_VERSIONS: SurveyDefinitionsSurveyIdVersions,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_VERSIONS_VERSION_ID: SurveyDefinitionsSurveyIdVersionsVersionId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAS: SurveyDefinitionsSurveyIdQuotas,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAS_QUOTA_ID: SurveyDefinitionsSurveyIdQuotasQuotaId,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS: SurveyDefinitionsSurveyIdQuotagroups,
        PathValues.SURVEYDEFINITIONS_SURVEY_ID_QUOTAGROUPS_QUOTA_GROUP_ID: SurveyDefinitionsSurveyIdQuotagroupsQuotaGroupId,
        PathValues.SURVEYS_SURVEY_ID_LANGUAGES: SurveysSurveyIdLanguages,
        PathValues.SURVEYS_SURVEY_ID_TRANSLATIONS_LANGUAGE_CODE: SurveysSurveyIdTranslationsLanguageCode,
    }
)
