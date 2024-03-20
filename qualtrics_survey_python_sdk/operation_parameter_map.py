operation_parameter_map = {
    '/survey-definitions/{surveyId}/blocks-POST': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'BlockElements'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'SubType'
            },
            {
                'name': 'ID'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'LibraryID'
            },
            {
                'name': 'ReferencedBlockID'
            },
            {
                'name': 'Options'
            },
        ]
    },
    '/survey-definitions/{surveyId}/blocks/{blockId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'blockId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/blocks/{blockId}-DELETE': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'blockId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/blocks/{blockId}-PUT': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'blockId'
            },
            {
                'name': 'BlockElements'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'SubType'
            },
            {
                'name': 'ID'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'LibraryID'
            },
            {
                'name': 'ReferencedBlockID'
            },
            {
                'name': 'Options'
            },
        ]
    },
    '/survey-definitions/{surveyId}/flow-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/flow-PUT': {
        'parameters': [
            {
                'name': 'FlowID'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'Flow'
            },
            {
                'name': 'Properties'
            },
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/flow/{flowId}-PUT': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'flowId'
            },
        ]
    },
    '/surveys/{surveyId}/languages-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/surveys/{surveyId}/languages-PUT': {
        'parameters': [
            {
                'name': 'AvailableLanguages'
            },
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/options-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/options-PUT': {
        'parameters': [
            {
                'name': 'BackButton'
            },
            {
                'name': 'BallotBoxStuffingPrevention'
            },
            {
                'name': 'Header'
            },
            {
                'name': 'Footer'
            },
            {
                'name': 'NoIndex'
            },
            {
                'name': 'NextButton'
            },
            {
                'name': 'PartialData'
            },
            {
                'name': 'PreviousButton'
            },
            {
                'name': 'ProgressBarDisplay'
            },
            {
                'name': 'SaveAndContinue'
            },
            {
                'name': 'SecureResponseFiles'
            },
            {
                'name': 'Skin'
            },
            {
                'name': 'SurveyExpiration'
            },
            {
                'name': 'SurveyProtection'
            },
            {
                'name': 'SurveyTermination'
            },
            {
                'name': 'ValidationMessage'
            },
            {
                'name': 'surveyId'
            },
            {
                'name': 'AnonymizeResponse'
            },
            {
                'name': 'Autofocus'
            },
            {
                'name': 'Autoadvance'
            },
            {
                'name': 'AutoadvancePages'
            },
            {
                'name': 'AvailableLanguages'
            },
            {
                'name': 'BallotBoxStuffingPreventionBehavior'
            },
            {
                'name': 'BallotBoxStuffingPreventionMessage'
            },
            {
                'name': 'BallotBoxStuffingPreventionMessageLibrary'
            },
            {
                'name': 'BallotBoxStuffingPreventionURL'
            },
            {
                'name': 'CollectGeoLocation'
            },
            {
                'name': 'CustomStyles'
            },
            {
                'name': 'CustomLanguages'
            },
            {
                'name': 'EmailThankYou'
            },
            {
                'name': 'EOSMessage'
            },
            {
                'name': 'EOSRedirectURL'
            },
            {
                'name': 'ExternalCSS'
            },
            {
                'name': 'headerMid'
            },
            {
                'name': 'footerMid'
            },
            {
                'name': 'InactiveSurvey'
            },
            {
                'name': 'InactiveMessage'
            },
            {
                'name': 'InactiveMessageLibrary'
            },
            {
                'name': 'nextButtonMid'
            },
            {
                'name': 'PageTransition'
            },
            {
                'name': 'PartialDataCloseAfter'
            },
            {
                'name': 'Password'
            },
            {
                'name': 'PasswordProtection'
            },
            {
                'name': 'previousButtonMid'
            },
            {
                'name': 'QuestionsPerPage'
            },
            {
                'name': 'RecaptchaV3'
            },
            {
                'name': 'RefererCheck'
            },
            {
                'name': 'RefererURL'
            },
            {
                'name': 'ResponseSummary'
            },
            {
                'name': 'SurveyExpirationDate'
            },
            {
                'name': 'SurveyMetaDescription'
            },
            {
                'name': 'SurveyLanguage'
            },
            {
                'name': 'SurveyName'
            },
            {
                'name': 'SurveyStartDate'
            },
            {
                'name': 'SurveyTitle'
            },
            {
                'name': 'ThankYouEmailMessage'
            },
            {
                'name': 'ThankYouEmailMessageLibrary'
            },
            {
                'name': 'ValidateMessage'
            },
            {
                'name': 'ValidationMessageLibrary'
            },
        ]
    },
    '/survey-definitions/{surveyId}/questions-POST': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'ChoiceOrder'
            },
            {
                'name': 'Choices'
            },
            {
                'name': 'Configuration'
            },
            {
                'name': 'DataExportTag'
            },
            {
                'name': 'Language'
            },
            {
                'name': 'NextAnswerId'
            },
            {
                'name': 'NextChoiceId'
            },
            {
                'name': 'QuestionDescription'
            },
            {
                'name': 'QuestionID'
            },
            {
                'name': 'QuestionText'
            },
            {
                'name': 'QuestionType'
            },
            {
                'name': 'Randomization'
            },
            {
                'name': 'RecodeValues'
            },
            {
                'name': 'Selector'
            },
            {
                'name': 'SubSelector'
            },
            {
                'name': 'Validation'
            },
            {
                'name': 'AnswerOrder'
            },
            {
                'name': 'Answers'
            },
            {
                'name': 'AnswerRandomization'
            },
            {
                'name': 'ChoiceDataExportTags'
            },
            {
                'name': 'DefaultChoices'
            },
            {
                'name': 'Labels'
            },
            {
                'name': 'Graphics'
            },
            {
                'name': 'GraphicsDescription'
            },
            {
                'name': 'blockId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/questions/{questionId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'questionId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/questions-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/questions/{questionId}-DELETE': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'questionId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/questions/{questionId}-PUT': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'questionId'
            },
            {
                'name': 'ChoiceOrder'
            },
            {
                'name': 'Choices'
            },
            {
                'name': 'Configuration'
            },
            {
                'name': 'DataExportTag'
            },
            {
                'name': 'Language'
            },
            {
                'name': 'NextAnswerId'
            },
            {
                'name': 'NextChoiceId'
            },
            {
                'name': 'QuestionDescription'
            },
            {
                'name': 'QuestionID'
            },
            {
                'name': 'QuestionText'
            },
            {
                'name': 'QuestionType'
            },
            {
                'name': 'Randomization'
            },
            {
                'name': 'RecodeValues'
            },
            {
                'name': 'Selector'
            },
            {
                'name': 'SubSelector'
            },
            {
                'name': 'Validation'
            },
            {
                'name': 'AnswerOrder'
            },
            {
                'name': 'Answers'
            },
            {
                'name': 'AnswerRandomization'
            },
            {
                'name': 'ChoiceDataExportTags'
            },
            {
                'name': 'DefaultChoices'
            },
            {
                'name': 'Labels'
            },
            {
                'name': 'Graphics'
            },
            {
                'name': 'GraphicsDescription'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotas-POST': {
        'parameters': [
            {
                'name': 'Name'
            },
            {
                'name': 'Occurrences'
            },
            {
                'name': 'Logic'
            },
            {
                'name': 'QuotaAction'
            },
            {
                'name': 'ID'
            },
            {
                'name': 'QuotaRealm'
            },
            {
                'name': 'surveyId'
            },
            {
                'name': 'Count'
            },
            {
                'name': 'CountForUndo'
            },
            {
                'name': 'LogicType'
            },
            {
                'name': 'ActionElement'
            },
            {
                'name': 'ActionInfo'
            },
            {
                'name': 'ActionLogic'
            },
            {
                'name': 'QuotaSchedule'
            },
            {
                'name': 'EndSurveyOptions'
            },
            {
                'name': 'WebServiceOptions'
            },
            {
                'name': 'CrossLogicDef'
            },
            {
                'name': 'PerformActionOnUser'
            },
            {
                'name': 'quotaGroupId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotagroups-POST': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'surveyId'
            },
            {
                'name': 'Id'
            },
            {
                'name': 'MultipleMatch'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'Public'
            },
            {
                'name': 'Quotas'
            },
            {
                'name': 'Selected'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotas/{quotaId}-DELETE': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotas-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'skipToken'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotas/{quotaId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaGroupId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotagroups-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'skipToken'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}-DELETE': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaGroupId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotas/{quotaId}-PUT': {
        'parameters': [
            {
                'name': 'Name'
            },
            {
                'name': 'Occurrences'
            },
            {
                'name': 'Logic'
            },
            {
                'name': 'QuotaAction'
            },
            {
                'name': 'ID'
            },
            {
                'name': 'QuotaRealm'
            },
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaId'
            },
            {
                'name': 'Count'
            },
            {
                'name': 'CountForUndo'
            },
            {
                'name': 'LogicType'
            },
            {
                'name': 'ActionElement'
            },
            {
                'name': 'ActionInfo'
            },
            {
                'name': 'ActionLogic'
            },
            {
                'name': 'QuotaSchedule'
            },
            {
                'name': 'EndSurveyOptions'
            },
            {
                'name': 'WebServiceOptions'
            },
            {
                'name': 'CrossLogicDef'
            },
            {
                'name': 'PerformActionOnUser'
            },
        ]
    },
    '/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}-PUT': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'surveyId'
            },
            {
                'name': 'quotaGroupId'
            },
            {
                'name': 'Id'
            },
            {
                'name': 'MultipleMatch'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'Public'
            },
            {
                'name': 'Quotas'
            },
            {
                'name': 'Selected'
            },
        ]
    },
    '/surveys/{surveyId}/translations/{languageCode}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'languageCode'
            },
        ]
    },
    '/surveys/{surveyId}/translations/{languageCode}-PUT': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'languageCode'
            },
        ]
    },
    '/survey-definitions/{surveyId}/versions-POST': {
        'parameters': [
            {
                'name': 'Description'
            },
            {
                'name': 'Published'
            },
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/versions/{versionId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'versionId'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/survey-definitions/{surveyId}/versions-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions-POST': {
        'parameters': [
            {
                'name': 'SurveyName'
            },
            {
                'name': 'Language'
            },
            {
                'name': 'ProjectCategory'
            },
            {
                'name': 'SurveyEntry'
            },
            {
                'name': 'SurveyElements'
            },
        ]
    },
    '/survey-definitions/{surveyId}-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/survey-definitions/{surveyId}/metadata-GET': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}-DELETE': {
        'parameters': [
            {
                'name': 'surveyId'
            },
        ]
    },
    '/survey-definitions/{surveyId}/metadata-PUT': {
        'parameters': [
            {
                'name': 'surveyId'
            },
            {
                'name': 'SurveyName'
            },
            {
                'name': 'SurveyDescription'
            },
            {
                'name': 'SurveyStatus'
            },
            {
                'name': 'SurveyStartDate'
            },
            {
                'name': 'SurveyExpirationDate'
            },
        ]
    },
};