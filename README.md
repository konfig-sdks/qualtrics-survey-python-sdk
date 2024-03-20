<div align="left">

[![Visit Qualtrics](./header.png)](https://api.qualtrics.com)

# Qualtrics<a id="qualtrics"></a>

The Qualtrics Survey endpoints give you access to the structure of the surveys you create. 

Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints. 

Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`qualtrics.survey_blocks.create_new_block`](#qualtricssurvey_blockscreate_new_block)
  * [`qualtrics.survey_blocks.get_definition_block`](#qualtricssurvey_blocksget_definition_block)
  * [`qualtrics.survey_blocks.remove_block`](#qualtricssurvey_blocksremove_block)
  * [`qualtrics.survey_blocks.update_definition_block`](#qualtricssurvey_blocksupdate_definition_block)
  * [`qualtrics.survey_flows.get_flow_definition`](#qualtricssurvey_flowsget_flow_definition)
  * [`qualtrics.survey_flows.update_definition`](#qualtricssurvey_flowsupdate_definition)
  * [`qualtrics.survey_flows.update_flow_element_definition`](#qualtricssurvey_flowsupdate_flow_element_definition)
  * [`qualtrics.survey_languages.get_available_languages`](#qualtricssurvey_languagesget_available_languages)
  * [`qualtrics.survey_languages.update_enabled_languages`](#qualtricssurvey_languagesupdate_enabled_languages)
  * [Permissions](#permissions)
  * [`qualtrics.survey_options.get_options`](#qualtricssurvey_optionsget_options)
  * [`qualtrics.survey_options.update_options`](#qualtricssurvey_optionsupdate_options)
  * [`qualtrics.survey_questions.create_new_question`](#qualtricssurvey_questionscreate_new_question)
  * [`qualtrics.survey_questions.get_definition`](#qualtricssurvey_questionsget_definition)
  * [`qualtrics.survey_questions.get_list`](#qualtricssurvey_questionsget_list)
  * [`qualtrics.survey_questions.remove_question`](#qualtricssurvey_questionsremove_question)
  * [`qualtrics.survey_questions.update_definition`](#qualtricssurvey_questionsupdate_definition)
  * [`qualtrics.survey_quotas.create_new_quota`](#qualtricssurvey_quotascreate_new_quota)
  * [`qualtrics.survey_quotas.create_quota_group`](#qualtricssurvey_quotascreate_quota_group)
  * [`qualtrics.survey_quotas.delete_quota`](#qualtricssurvey_quotasdelete_quota)
  * [`qualtrics.survey_quotas.get_all`](#qualtricssurvey_quotasget_all)
  * [`qualtrics.survey_quotas.get_definition`](#qualtricssurvey_quotasget_definition)
  * [`qualtrics.survey_quotas.get_quota_group_definition`](#qualtricssurvey_quotasget_quota_group_definition)
  * [`qualtrics.survey_quotas.list_quota_groups`](#qualtricssurvey_quotaslist_quota_groups)
  * [`qualtrics.survey_quotas.remove_quota_group`](#qualtricssurvey_quotasremove_quota_group)
  * [`qualtrics.survey_quotas.update_definition`](#qualtricssurvey_quotasupdate_definition)
  * [`qualtrics.survey_quotas.update_quota_group_definition`](#qualtricssurvey_quotasupdate_quota_group_definition)
  * [`qualtrics.survey_translations.get_by_survey_id_and_language_code`](#qualtricssurvey_translationsget_by_survey_id_and_language_code)
  * [`qualtrics.survey_translations.update_translations`](#qualtricssurvey_translationsupdate_translations)
  * [Permissions](#permissions-1)
  * [`qualtrics.survey_versions.create_new_version`](#qualtricssurvey_versionscreate_new_version)
  * [`qualtrics.survey_versions.get_definition`](#qualtricssurvey_versionsget_definition)
  * [`qualtrics.survey_versions.list`](#qualtricssurvey_versionslist)
  * [`qualtrics.surveys.create_definition`](#qualtricssurveyscreate_definition)
  * [`qualtrics.surveys.get_definition`](#qualtricssurveysget_definition)
  * [`qualtrics.surveys.get_metadata`](#qualtricssurveysget_metadata)
  * [`qualtrics.surveys.remove_definition`](#qualtricssurveysremove_definition)
  * [`qualtrics.surveys.update_metadata`](#qualtricssurveysupdate_metadata)
  * [Date fields in this API use MySQL DateTime instead of ISO-8601.](#date-fields-in-this-api-use-mysql-datetime-instead-of-iso-8601)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Qualtrics&serviceName=Survey&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from qualtrics_survey_python_sdk import Qualtrics, ApiException

qualtrics = Qualtrics(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Create Block
    create_new_block_response = qualtrics.survey_blocks.create_new_block(
        body={
        "type": "Standard",
        "sub_type": "Reference",
        "id": "BL_d7tGuyhg0ec00PH",
        "description": "description_example",
        "library_id": "UR_Cu2LC4aWwWL",
        "referenced_block_id": "LB_39jTPoKafNaUF9z",
    },
        survey_id="SV_0ODVm59K4i9tjcp",
        block_elements=[
        None
    ],
        type="ExperienceBlock",
        sub_type="CBConjoint",
        id="BL_d7tGuyhg0ec00PH",
        description="My Trash Block Name",
        library_id="UR_Cu2LC4aWwWL",
        referenced_block_id="LB_39jTPoKafNaUF9z",
        options={
        "block_locking": "true",
        "block_password": "6dca3fa58e4c508071ecef74d4c9b06bd6879529",
        "block_visiblity": "Collapsed",
        "randomize_questions": "RandomWithXPerPage",
        "looping": "None",
        "next_button": "Some Text Here",
        "previous_button": "",
        "next_button_mid": "",
        "previous_button_library_id": "",
    },
    )
    print(create_new_block_response)
except ApiException as e:
    print("Exception when calling SurveyBlocksApi.create_new_block: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["meta"])
    if e.status == 401:
        pprint(e.body["meta"])
    if e.status == 500:
        pprint(e.body["meta"])
    if e.status == 403:
        pprint(e.body["meta"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from qualtrics_survey_python_sdk import Qualtrics, ApiException

qualtrics = Qualtrics(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Create Block
        create_new_block_response = await qualtrics.survey_blocks.acreate_new_block(
            body={
        "type": "Standard",
        "sub_type": "Reference",
        "id": "BL_d7tGuyhg0ec00PH",
        "description": "description_example",
        "library_id": "UR_Cu2LC4aWwWL",
        "referenced_block_id": "LB_39jTPoKafNaUF9z",
    },
            survey_id="SV_0ODVm59K4i9tjcp",
            block_elements=[
        None
    ],
            type="ExperienceBlock",
            sub_type="CBConjoint",
            id="BL_d7tGuyhg0ec00PH",
            description="My Trash Block Name",
            library_id="UR_Cu2LC4aWwWL",
            referenced_block_id="LB_39jTPoKafNaUF9z",
            options={
        "block_locking": "true",
        "block_password": "6dca3fa58e4c508071ecef74d4c9b06bd6879529",
        "block_visiblity": "Collapsed",
        "randomize_questions": "RandomWithXPerPage",
        "looping": "None",
        "next_button": "Some Text Here",
        "previous_button": "",
        "next_button_mid": "",
        "previous_button_library_id": "",
    },
        )
        print(create_new_block_response)
    except ApiException as e:
        print("Exception when calling SurveyBlocksApi.create_new_block: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["meta"])
        if e.status == 401:
            pprint(e.body["meta"])
        if e.status == 500:
            pprint(e.body["meta"])
        if e.status == 403:
            pprint(e.body["meta"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from qualtrics_survey_python_sdk import Qualtrics, ApiException

qualtrics = Qualtrics(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Create Block
    create_new_block_response = qualtrics.survey_blocks.raw.create_new_block(
        body={
        "type": "Standard",
        "sub_type": "Reference",
        "id": "BL_d7tGuyhg0ec00PH",
        "description": "description_example",
        "library_id": "UR_Cu2LC4aWwWL",
        "referenced_block_id": "LB_39jTPoKafNaUF9z",
    },
        survey_id="SV_0ODVm59K4i9tjcp",
        block_elements=[
        None
    ],
        type="ExperienceBlock",
        sub_type="CBConjoint",
        id="BL_d7tGuyhg0ec00PH",
        description="My Trash Block Name",
        library_id="UR_Cu2LC4aWwWL",
        referenced_block_id="LB_39jTPoKafNaUF9z",
        options={
        "block_locking": "true",
        "block_password": "6dca3fa58e4c508071ecef74d4c9b06bd6879529",
        "block_visiblity": "Collapsed",
        "randomize_questions": "RandomWithXPerPage",
        "looping": "None",
        "next_button": "Some Text Here",
        "previous_button": "",
        "next_button_mid": "",
        "previous_button_library_id": "",
    },
    )
    pprint(create_new_block_response.body)
    pprint(create_new_block_response.body["meta"])
    pprint(create_new_block_response.body["result"])
    pprint(create_new_block_response.headers)
    pprint(create_new_block_response.status)
    pprint(create_new_block_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SurveyBlocksApi.create_new_block: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["meta"])
    if e.status == 401:
        pprint(e.body["meta"])
    if e.status == 500:
        pprint(e.body["meta"])
    if e.status == 403:
        pprint(e.body["meta"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `qualtrics.survey_blocks.create_new_block`<a id="qualtricssurvey_blockscreate_new_block"></a>

Create a new [block](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/block-options-overview/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_block_response = qualtrics.survey_blocks.create_new_block(
    body={
        "type": "Standard",
        "sub_type": "Reference",
        "id": "BL_d7tGuyhg0ec00PH",
        "description": "description_example",
        "library_id": "UR_Cu2LC4aWwWL",
        "referenced_block_id": "LB_39jTPoKafNaUF9z",
    },
    survey_id="SV_0ODVm59K4i9tjcp",
    block_elements=[
        None
    ],
    type="ExperienceBlock",
    sub_type="CBConjoint",
    id="BL_d7tGuyhg0ec00PH",
    description="My Trash Block Name",
    library_id="UR_Cu2LC4aWwWL",
    referenced_block_id="LB_39jTPoKafNaUF9z",
    options={
        "block_locking": "true",
        "block_password": "6dca3fa58e4c508071ecef74d4c9b06bd6879529",
        "block_visiblity": "Collapsed",
        "randomize_questions": "RandomWithXPerPage",
        "looping": "None",
        "next_button": "Some Text Here",
        "previous_button": "",
        "next_button_mid": "",
        "previous_button_library_id": "",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

##### block_elements: [`BlockElements`](./qualtrics_survey_python_sdk/type/block_elements.py)<a id="block_elements-blockelementsqualtrics_survey_python_sdktypeblock_elementspy"></a>

##### type: `str`<a id="type-str"></a>

##### sub_type: `str`<a id="sub_type-str"></a>

Choice Based Conjoint Blocks hide their elements from editing using the Group Flow element and ViewFlow: false

##### id: [`BlockID`](./qualtrics_survey_python_sdk/type/block_id.py)<a id="id-blockidqualtrics_survey_python_sdktypeblock_idpy"></a>

##### description: `str`<a id="description-str"></a>

##### library_id: `LibraryID`<a id="library_id-libraryid"></a>

##### referenced_block_id: [`ReferencedBlockID`](./qualtrics_survey_python_sdk/type/referenced_block_id.py)<a id="referenced_block_id-referencedblockidqualtrics_survey_python_sdktypereferenced_block_idpy"></a>

##### options: [`BlockOptions`](./qualtrics_survey_python_sdk/type/block_options.py)<a id="options-blockoptionsqualtrics_survey_python_sdktypeblock_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BlockDefinition`](./qualtrics_survey_python_sdk/type/block_definition.py)
Create block request.

#### 🔄 Return<a id="🔄-return"></a>

[`CreateBlockResponse`](./qualtrics_survey_python_sdk/pydantic/create_block_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/blocks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_blocks.get_definition_block`<a id="qualtricssurvey_blocksget_definition_block"></a>

Retrieve a [block](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/block-options-overview/) definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_definition_block_response = qualtrics.survey_blocks.get_definition_block(
    survey_id="SV_0ODVm59K4i9tjcp",
    block_id="BL_d7tGuyhg0ec00PH",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

##### block_id: [`BlockID`](./qualtrics_survey_python_sdk/type/.py)<a id="block_id-blockidqualtrics_survey_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetBlockResponse`](./qualtrics_survey_python_sdk/pydantic/get_block_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/blocks/{blockId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_blocks.remove_block`<a id="qualtricssurvey_blocksremove_block"></a>

Delete a [block](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/block-options-overview/) from the survey.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_block_response = qualtrics.survey_blocks.remove_block(
    survey_id="SV_0ODVm59K4i9tjcp",
    block_id="BL_d7tGuyhg0ec00PH",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

##### block_id: [`BlockID`](./qualtrics_survey_python_sdk/type/.py)<a id="block_id-blockidqualtrics_survey_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/blocks/{blockId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_blocks.update_definition_block`<a id="qualtricssurvey_blocksupdate_definition_block"></a>

Update a [block](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/block-options-overview/) definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_definition_block_response = qualtrics.survey_blocks.update_definition_block(
    body={
        "type": "Standard",
        "sub_type": "Reference",
        "id": "BL_d7tGuyhg0ec00PH",
        "description": "description_example",
        "library_id": "UR_Cu2LC4aWwWL",
        "referenced_block_id": "LB_39jTPoKafNaUF9z",
    },
    survey_id="SV_0ODVm59K4i9tjcp",
    block_id="BL_d7tGuyhg0ec00PH",
    block_elements=[
        None
    ],
    type="ExperienceBlock",
    sub_type="CBConjoint",
    id="BL_d7tGuyhg0ec00PH",
    description="My Trash Block Name",
    library_id="UR_Cu2LC4aWwWL",
    referenced_block_id="LB_39jTPoKafNaUF9z",
    options={
        "block_locking": "true",
        "block_password": "6dca3fa58e4c508071ecef74d4c9b06bd6879529",
        "block_visiblity": "Collapsed",
        "randomize_questions": "RandomWithXPerPage",
        "looping": "None",
        "next_button": "Some Text Here",
        "previous_button": "",
        "next_button_mid": "",
        "previous_button_library_id": "",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

##### block_id: [`BlockID`](./qualtrics_survey_python_sdk/type/.py)<a id="block_id-blockidqualtrics_survey_python_sdktypepy"></a>

##### block_elements: [`BlockElements`](./qualtrics_survey_python_sdk/type/block_elements.py)<a id="block_elements-blockelementsqualtrics_survey_python_sdktypeblock_elementspy"></a>

##### type: `str`<a id="type-str"></a>

##### sub_type: `str`<a id="sub_type-str"></a>

Choice Based Conjoint Blocks hide their elements from editing using the Group Flow element and ViewFlow: false

##### id: [`BlockID`](./qualtrics_survey_python_sdk/type/block_id.py)<a id="id-blockidqualtrics_survey_python_sdktypeblock_idpy"></a>

##### description: `str`<a id="description-str"></a>

##### library_id: `LibraryID`<a id="library_id-libraryid"></a>

##### referenced_block_id: [`ReferencedBlockID`](./qualtrics_survey_python_sdk/type/referenced_block_id.py)<a id="referenced_block_id-referencedblockidqualtrics_survey_python_sdktypereferenced_block_idpy"></a>

##### options: [`BlockOptions`](./qualtrics_survey_python_sdk/type/block_options.py)<a id="options-blockoptionsqualtrics_survey_python_sdktypeblock_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BlockDefinition`](./qualtrics_survey_python_sdk/type/block_definition.py)
Update block request

#### 🔄 Return<a id="🔄-return"></a>

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/blocks/{blockId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_flows.get_flow_definition`<a id="qualtricssurvey_flowsget_flow_definition"></a>

Retrieve a [flow](https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/survey-flow-overview/) definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_flow_definition_response = qualtrics.survey_flows.get_flow_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetFlowResponse`](./qualtrics_survey_python_sdk/pydantic/get_flow_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/flow` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_flows.update_definition`<a id="qualtricssurvey_flowsupdate_definition"></a>

Update a [flow](https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/survey-flow-overview/) definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_definition_response = qualtrics.survey_flows.update_definition(
    flow_id="FL_1",
    type="Root",
    flow=[
        {
            "type": "Authenticator",
            "flow_id": "FL_1",
            "panel_data": {
                "library_id": "UR_3Cz41f8fIqINzaR",
                "panel_id": "CG_0jjTqUJhwxz7KU5",
                "type": "Expression",
                "logic_type": "Panel",
            },
            "field_data": {
                "type": "BooleanExpression",
            },
            "filter_data_fields": True,
            "sso_options": {
                "capture_respondent_info": "false",
                "type": "Token",
                "use_panel": "true",
                "use_person": "true",
                "use_sso": "",
            },
            "options": {
                "max_attempts": 3,
                "allow_retake": False,
                "load_existing_session": False,
            },
        }
    ],
    properties={
        "count": 2,
    },
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flow_id: [`FlowID`](./qualtrics_survey_python_sdk/type/flow_id.py)<a id="flow_id-flowidqualtrics_survey_python_sdktypeflow_idpy"></a>

##### type: [`FlowType`](./qualtrics_survey_python_sdk/type/flow_type.py)<a id="type-flowtypequaltrics_survey_python_sdktypeflow_typepy"></a>

##### flow: [`Flow`](./qualtrics_survey_python_sdk/type/flow.py)<a id="flow-flowqualtrics_survey_python_sdktypeflowpy"></a>

##### properties: [`FlowProperties`](./qualtrics_survey_python_sdk/type/flow_properties.py)<a id="properties-flowpropertiesqualtrics_survey_python_sdktypeflow_propertiespy"></a>


##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FlowDefinition`](./qualtrics_survey_python_sdk/type/flow_definition.py)
Update flow request

#### 🔄 Return<a id="🔄-return"></a>

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/flow` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_flows.update_flow_element_definition`<a id="qualtricssurvey_flowsupdate_flow_element_definition"></a>

Update [flow](https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/survey-flow-overview/) by ID.

If you're having trouble capturing single sign-on (SSO) information, make sure you've included all fields within the `Options` object. See this example:

```JSON
"Options": {
 "maxAttempts": 3,
 "authenticationError": {
 "SystemMessage": {
 "Section": "Message example",
 "Message": "Test System Message"
 }
 } 
 "failedAuthenticationError": {
 "SystemMessage": {
 "Section": "Message example",
 "Message": "Test System Message"
 }
 } 
 "questionText": "{
 "SystemMessage": {
 "Section": "Question Text section example",
 "Message": "Question Text message example"
 }
 } 
 "allowRetake": "true",
 "loadExistingSession": "false"
}


#### 🛠️ Usage

```python
update_flow_element_definition_response = qualtrics.survey_flows.update_flow_element_definition(
    body=[
        {
            "type": "Authenticator",
            "flow_id": "FL_1",
            "panel_data": {
                "library_id": "UR_3Cz41f8fIqINzaR",
                "panel_id": "CG_0jjTqUJhwxz7KU5",
                "type": "Expression",
                "logic_type": "Panel",
            },
            "field_data": {
                "type": "BooleanExpression",
            },
            "filter_data_fields": True,
            "sso_options": {
                "capture_respondent_info": "false",
                "type": "Token",
                "use_panel": "true",
                "use_person": "true",
                "use_sso": "",
            },
            "options": {
                "max_attempts": 3,
                "allow_retake": False,
                "load_existing_session": False,
            },
        }
    ],
    survey_id="SV_0ODVm59K4i9tjcp",
    flow_id="FL_1",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### flow_id: [`FlowID`](./qualtrics_survey_python_sdk/type/.py)

##### requestBody: [`Flow`](./qualtrics_survey_python_sdk/type/flow.py)

Update flow element request

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/flow/{flowId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_languages.get_available_languages`

Returns a list of available [languages](https://www.qualtrics.com/support/survey-platform/getting-started/languages-in-qualtrics/) for a survey given the `surveyId`.

#### 🛠️ Usage

```python
get_available_languages_response = qualtrics.survey_languages.get_available_languages(
    survey_id="surveyId_example",
)
```

#### ⚙️ Parameters

##### survey_id: `str`

The unique identifier of the survey.

#### 🔄 Return

[`LanguagesResponse`](./qualtrics_survey_python_sdk/pydantic/languages_response.py)

#### 🌐 Endpoint

`/surveys/{surveyId}/languages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_languages.update_enabled_languages`

Updates enabled [languages](https://www.qualtrics.com/support/survey-platform/getting-started/languages-in-qualtrics/) given the `surveyId`.
<!--From Readme-->
For more information about using the survey APIs, see [Managing Surveys](../../../../docs/Guides/Common%20Tasks/managing-surveys.md).
<!-- theme: info -->

>### Permissions
>**Set Survey Options** permission must be enabled for the user to update survey languages.



#### 🛠️ Usage

```python
update_enabled_languages_response = qualtrics.survey_languages.update_enabled_languages(
    available_languages=[
        "string_example"
    ],
    survey_id="surveyId_example",
)
```

#### ⚙️ Parameters

##### available_languages: [`SurveyLanguageElements`](./qualtrics_survey_python_sdk/type/survey_language_elements.py)

##### survey_id: `str`

#### ⚙️ Request Body

[`SurveyLanguages`](./qualtrics_survey_python_sdk/type/survey_languages.py)
All languages to be enabled for the survey. Must include existing languages

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/surveys/{surveyId}/languages` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_options.get_options`

Retrieve [survey options](https://www.qualtrics.com/support/survey-platform/survey-module/survey-options/survey-options-overview/) for a survey with the `surveyId`.

#### 🛠️ Usage

```python
get_options_response = qualtrics.survey_options.get_options(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`GetSurveyOptionsResponse`](./qualtrics_survey_python_sdk/pydantic/get_survey_options_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/options` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_options.update_options`

Update [survey options](https://www.qualtrics.com/support/survey-platform/survey-module/survey-options/survey-options-overview/) for a survey with the `surveyId`.

#### 🛠️ Usage

```python
update_options_response = qualtrics.survey_options.update_options(
    back_button=False,
    ballot_box_stuffing_prevention=False,
    header="",
    footer="",
    no_index="true",
    next_button=" ← ",
    partial_data="+1 week",
    previous_button=" ← ",
    progress_bar_display="None",
    save_and_continue=True,
    secure_response_files="true",
    skin={
        "template_id": "*base",
    },
    survey_expiration="true",
    survey_protection="PublicSurvey",
    survey_termination="DefaultMessage",
    validation_message="MS_abcdefg12345",
    survey_id="SV_0ODVm59K4i9tjcp",
    anonymize_response="false",
    autofocus=True,
    autoadvance=True,
    autoadvance_pages=True,
    available_languages={
        "key": [
            "string_example"
        ],
    },
    ballot_box_stuffing_prevention_behavior="default",
    ballot_box_stuffing_prevention_message="MS_abcdefg12345",
    ballot_box_stuffing_prevention_message_library="UR_SomeUserId001",
    ballot_box_stuffing_prevention_url="string_example",
    collect_geo_location="true",
    custom_styles="[]",
    custom_languages={
        "key": {
            "display_name": "display_name_example",
            "error_messages": "error_messages_example",
        },
    },
    email_thank_you="false",
    eos_message="MS_abcdefg12345",
    eos_redirect_url="string_example",
    external_css="string_example",
    header_mid="MS_abcdefg12345",
    footer_mid="MS_abcdefg12345",
    inactive_survey="DefaultMessage",
    inactive_message="MS_abcdefg12345",
    inactive_message_library="UR_SomeUserId001",
    next_button_mid="MS_abcdefg12345",
    page_transition="None",
    partial_data_close_after="",
    password="string_example",
    password_protection="false",
    previous_button_mid="MS_abcdefg12345",
    questions_per_page="4",
    recaptcha_v3="true",
    referer_check="false",
    referer_url="string_example",
    response_summary="false",
    survey_expiration_date="1970-01-01T00:00:00.00Z",
    survey_meta_description="string_example",
    survey_language="EN",
    survey_name="string_example",
    survey_start_date="1970-01-01T00:00:00.00Z",
    survey_title="string_example",
    thank_you_email_message="MS_abcdefg12345",
    thank_you_email_message_library="UR_SomeUserId001",
    validate_message="false",
    validation_message_library="UR_SomeUserId001",
)
```

#### ⚙️ Parameters

##### back_button: `bool`

If true, display the back button

##### ballot_box_stuffing_prevention: `bool`

If true, prevent respondents from taking the survey multiple times.

##### header: `str`

Header to display on each page such as a logo. Do not use in conjunction with `headerMid`.

##### footer: `str`

Footer to display on each page such as a logo. Do not use in conjunction with `footerMid`.

##### no_index: [`NoIndex`](./qualtrics_survey_python_sdk/type/no_index.py)

##### next_button: `str`

The text to use as the \\\"next\\\" Button. Note that `BackButton` should be enabled for this property to be used. See `nextButtonMid` and `BackButton`.

##### partial_data: [`PartialData`](./qualtrics_survey_python_sdk/type/partial_data.py)

##### previous_button: `str`

The text to use as the \\\"previous\\\" Button. Note that `BackButton` should be enabled for this property to be used. See `previousButtonMid` and `BackButton`.

##### progress_bar_display: [`ProgressBarDisplay`](./qualtrics_survey_python_sdk/type/progress_bar_display.py)

##### save_and_continue: `bool`

If true, allow respondents to save and continue later.

##### secure_response_files: [`SecureResponseFiles`](./qualtrics_survey_python_sdk/type/secure_response_files.py)

##### skin: [`Skin`](./qualtrics_survey_python_sdk/type/skin.py)


##### survey_expiration: [`SurveyExpiration`](./qualtrics_survey_python_sdk/type/survey_expiration.py)

##### survey_protection: [`SurveyProtection`](./qualtrics_survey_python_sdk/type/survey_protection.py)

##### survey_termination: [`SurveyTermination`](./qualtrics_survey_python_sdk/type/survey_termination.py)

##### validation_message: [`ValidationMessage`](./qualtrics_survey_python_sdk/type/validation_message.py)

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### anonymize_response: [`AnonymizeResponse`](./qualtrics_survey_python_sdk/type/anonymize_response.py)

##### autofocus: `bool`

If true, provide autofocus for questions.

##### autoadvance: `bool`

Enables autoadvance on questions

##### autoadvance_pages: `bool`

Enables autoadvance on pages. This requires `Autoadvance` to be anbled as well

##### available_languages: [`AvailableLanguages`](./qualtrics_survey_python_sdk/type/available_languages.py)

##### ballot_box_stuffing_prevention_behavior: [`BallotBoxStuffingPreventionBehavior`](./qualtrics_survey_python_sdk/type/ballot_box_stuffing_prevention_behavior.py)

##### ballot_box_stuffing_prevention_message: [`BallotBoxStuffingPreventionMessage`](./qualtrics_survey_python_sdk/type/ballot_box_stuffing_prevention_message.py)

##### ballot_box_stuffing_prevention_message_library: [`BallotBoxStuffingPreventionMessageLibrary`](./qualtrics_survey_python_sdk/type/ballot_box_stuffing_prevention_message_library.py)

##### ballot_box_stuffing_prevention_url: `str`

Ballot Box stuffing prevention URL.

##### collect_geo_location: [`CollectGeoLocation`](./qualtrics_survey_python_sdk/type/collect_geo_location.py)

##### custom_styles: `str`

Custom CSS to load when survey taking. See also `ExternalCSS`.

##### custom_languages: [`CustomLanguages`](./qualtrics_survey_python_sdk/type/custom_languages.py)

##### email_thank_you: [`EmailThankYou`](./qualtrics_survey_python_sdk/type/email_thank_you.py)

##### eos_message: [`EOSMessage`](./qualtrics_survey_python_sdk/type/eos_message.py)

##### eos_redirect_url: `str`

The URL to redirect respondents to at the end of the survey used when `SurveyTermination` is set to `Redirect`.

##### external_css: `str`

CSS URL to load when survey taking. See also `CustomStyles`.

##### header_mid: [`HeaderMid`](./qualtrics_survey_python_sdk/type/header_mid.py)

##### footer_mid: [`FooterMid`](./qualtrics_survey_python_sdk/type/footer_mid.py)

##### inactive_survey: [`InactiveSurvey`](./qualtrics_survey_python_sdk/type/inactive_survey.py)

##### inactive_message: [`InactiveMessage`](./qualtrics_survey_python_sdk/type/inactive_message.py)

##### inactive_message_library: [`InactiveMessageLibrary`](./qualtrics_survey_python_sdk/type/inactive_message_library.py)

##### next_button_mid: [`NextButtonMid`](./qualtrics_survey_python_sdk/type/next_button_mid.py)

##### page_transition: [`PageTransition`](./qualtrics_survey_python_sdk/type/page_transition.py)

##### partial_data_close_after: [`PartialDataCloseAfter`](./qualtrics_survey_python_sdk/type/partial_data_close_after.py)

##### password: `str`

The password to take the survey. See `PasswordProtection`.

##### password_protection: [`PasswordProtection`](./qualtrics_survey_python_sdk/type/password_protection.py)

##### previous_button_mid: [`PreviousButtonMid`](./qualtrics_survey_python_sdk/type/previous_button_mid.py)

##### questions_per_page: [`QuestionsPerPage`](./qualtrics_survey_python_sdk/type/questions_per_page.py)

##### recaptcha_v3: [`RecaptchaV3`](./qualtrics_survey_python_sdk/type/recaptcha_v3.py)

##### referer_check: [`RefererCheck`](./qualtrics_survey_python_sdk/type/referer_check.py)

##### referer_url: `str`

The URL respondents must come from to access the survey. See `RefererCheck`.

##### response_summary: [`ResponseSummary`](./qualtrics_survey_python_sdk/type/response_summary.py)

##### survey_expiration_date: [`SurveyExpirationDate`](./qualtrics_survey_python_sdk/type/survey_expiration_date.py)

##### survey_meta_description: [`SurveyMetaDescription`](./qualtrics_survey_python_sdk/type/survey_meta_description.py)

##### survey_language: [`LanguageCode`](./qualtrics_survey_python_sdk/type/language_code.py)

##### survey_name: [`SurveyName`](./qualtrics_survey_python_sdk/type/survey_name.py)

##### survey_start_date: [`SurveyStartDate`](./qualtrics_survey_python_sdk/type/survey_start_date.py)

##### survey_title: [`SurveyTitle`](./qualtrics_survey_python_sdk/type/survey_title.py)

##### thank_you_email_message: [`ThankYouEmailMessage`](./qualtrics_survey_python_sdk/type/thank_you_email_message.py)

##### thank_you_email_message_library: [`ThankYouEmailMessageLibrary`](./qualtrics_survey_python_sdk/type/thank_you_email_message_library.py)

##### validate_message: [`ValidateMessage`](./qualtrics_survey_python_sdk/type/validate_message.py)

##### validation_message_library: [`ValidationMessageLibrary`](./qualtrics_survey_python_sdk/type/validation_message_library.py)

#### ⚙️ Request Body

[`SurveyOptions`](./qualtrics_survey_python_sdk/type/survey_options.py)
Survey Options

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/options` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_questions.create_new_question`

Create a new question in the specified [block](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/block-options-overview/) or the default block if not specified.

#### 🛠️ Usage

```python
create_new_question_response = qualtrics.survey_questions.create_new_question(
    survey_id="SV_0ODVm59K4i9tjcp",
    choice_order=["1", "2"],
    choices={
        "key": {
        },
    },
    configuration={
        "question_description_option": "UseText",
        "text_position": "inline",
        "choice_column_width": 25,
        "repeat_headers": "none",
        "white_space": "true",
        "label_position": "BELOW",
        "mobile_first": True,
    },
    data_export_tag="string_example",
    language=None,
    next_answer_id=1,
    next_choice_id=1,
    question_description="string_example",
    question_id="QID1",
    question_text="",
    question_type="DB",
    randomization=None,
    recode_values={
        "key": "string_example",
    },
    selector="GRB",
    sub_selector="SingleAnswer",
    validation={
        "settings": {
            "force_response": "RequestResponse",
            "force_response_type": "RequestResponse",
            "type": "CustomValidation",
        },
    },
    answer_order=["1", "2"],
    answers={
        "key": {
        },
    },
    answer_randomization=None,
    choice_data_export_tags=True,
    default_choices=True,
    labels={
    },
    graphics="IM_Cu2LC4aWwWL",
    graphics_description="string_example",
    block_id="BL_d7tGuyhg0ec00PH",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### choice_order: [`ChoiceOrder`](./qualtrics_survey_python_sdk/type/choice_order.py)

##### choices: [`QuestionChoices`](./qualtrics_survey_python_sdk/type/question_choices.py)

##### configuration: [`QuestionConfiguration`](./qualtrics_survey_python_sdk/type/question_configuration.py)


##### data_export_tag: `str`

The tag to identify the question in exported data.

##### language: `Language`

##### next_answer_id: `int`

##### next_choice_id: `int`

##### question_description: `str`

##### question_id: [`QuestionID`](./qualtrics_survey_python_sdk/type/question_id.py)

##### question_text: [`QuestionText`](./qualtrics_survey_python_sdk/type/question_text.py)

##### question_type: `str`

##### randomization: `Randomization`

##### recode_values: [`RecodeValues`](./qualtrics_survey_python_sdk/type/recode_values.py)

##### selector: `str`

##### sub_selector: [`QuestionSubSelector`](./qualtrics_survey_python_sdk/type/question_sub_selector.py)

##### validation: [`Validation`](./qualtrics_survey_python_sdk/type/validation.py)


##### answer_order: [`ChoiceOrder`](./qualtrics_survey_python_sdk/type/choice_order.py)

##### answers: [`QuestionChoices`](./qualtrics_survey_python_sdk/type/question_choices.py)

##### answer_randomization: `AnswerRandomization`

##### choice_data_export_tags: `bool`

##### default_choices: `bool`

##### labels: [`Selection`](./qualtrics_survey_python_sdk/type/selection.py)


##### graphics: [`ImageID`](./qualtrics_survey_python_sdk/type/image_id.py)

##### graphics_description: `str`

##### block_id: [`BlockID`](./qualtrics_survey_python_sdk/type/.py)

#### ⚙️ Request Body

[`QuestionDefinition`](./qualtrics_survey_python_sdk/type/question_definition.py)
Create question request

#### 🔄 Return

[`CreateQuestionResponse`](./qualtrics_survey_python_sdk/pydantic/create_question_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/questions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_questions.get_definition`

Retrieve a [question](https://api.qualtrics.com/ZG9jOjg3NzY4Mw-example-use-cases-walkthrough#add-question-to-survey) definition.

#### 🛠️ Usage

```python
get_definition_response = qualtrics.survey_questions.get_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    question_id="QID1",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### question_id: [`QuestionID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`QuestionDefinition`](./qualtrics_survey_python_sdk/pydantic/question_definition.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/questions/{questionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_questions.get_list`

Return a list of a [survey questions](https://api.qualtrics.com/ZG9jOjg3NzY4Mw-example-use-cases-walkthrough#add-question-to-survey).

#### 🛠️ Usage

```python
get_list_response = qualtrics.survey_questions.get_list(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`GetQuestionsResponse`](./qualtrics_survey_python_sdk/pydantic/get_questions_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_questions.remove_question`

Delete a [question](https://api.qualtrics.com/ZG9jOjg3NzY4Mw-example-use-cases-walkthrough#add-question-to-survey) from a survey.

#### 🛠️ Usage

```python
remove_question_response = qualtrics.survey_questions.remove_question(
    survey_id="SV_0ODVm59K4i9tjcp",
    question_id="QID1",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### question_id: [`QuestionID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/questions/{questionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_questions.update_definition`

Update a [question](https://api.qualtrics.com/ZG9jOjg3NzY4Mw-example-use-cases-walkthrough#add-question-to-survey) definition.

#### 🛠️ Usage

```python
update_definition_response = qualtrics.survey_questions.update_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    question_id="QID1",
    choice_order=["1", "2"],
    choices={
        "key": {
        },
    },
    configuration={
        "question_description_option": "UseText",
        "text_position": "inline",
        "choice_column_width": 25,
        "repeat_headers": "none",
        "white_space": "true",
        "label_position": "BELOW",
        "mobile_first": True,
    },
    data_export_tag="string_example",
    language=None,
    next_answer_id=1,
    next_choice_id=1,
    question_description="string_example",
    question_id="QID1",
    question_text="",
    question_type="DB",
    randomization=None,
    recode_values={
        "key": "string_example",
    },
    selector="GRB",
    sub_selector="SingleAnswer",
    validation={
        "settings": {
            "force_response": "RequestResponse",
            "force_response_type": "RequestResponse",
            "type": "CustomValidation",
        },
    },
    answer_order=["1", "2"],
    answers={
        "key": {
        },
    },
    answer_randomization=None,
    choice_data_export_tags=True,
    default_choices=True,
    labels={
    },
    graphics="IM_Cu2LC4aWwWL",
    graphics_description="string_example",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### question_id: [`QuestionID`](./qualtrics_survey_python_sdk/type/.py)

##### choice_order: [`ChoiceOrder`](./qualtrics_survey_python_sdk/type/choice_order.py)

##### choices: [`QuestionChoices`](./qualtrics_survey_python_sdk/type/question_choices.py)

##### configuration: [`QuestionConfiguration`](./qualtrics_survey_python_sdk/type/question_configuration.py)


##### data_export_tag: `str`

The tag to identify the question in exported data.

##### language: `Language`

##### next_answer_id: `int`

##### next_choice_id: `int`

##### question_description: `str`

##### question_id: [`QuestionID`](./qualtrics_survey_python_sdk/type/question_id.py)

##### question_text: [`QuestionText`](./qualtrics_survey_python_sdk/type/question_text.py)

##### question_type: `str`

##### randomization: `Randomization`

##### recode_values: [`RecodeValues`](./qualtrics_survey_python_sdk/type/recode_values.py)

##### selector: `str`

##### sub_selector: [`QuestionSubSelector`](./qualtrics_survey_python_sdk/type/question_sub_selector.py)

##### validation: [`Validation`](./qualtrics_survey_python_sdk/type/validation.py)


##### answer_order: [`ChoiceOrder`](./qualtrics_survey_python_sdk/type/choice_order.py)

##### answers: [`QuestionChoices`](./qualtrics_survey_python_sdk/type/question_choices.py)

##### answer_randomization: `AnswerRandomization`

##### choice_data_export_tags: `bool`

##### default_choices: `bool`

##### labels: [`Selection`](./qualtrics_survey_python_sdk/type/selection.py)


##### graphics: [`ImageID`](./qualtrics_survey_python_sdk/type/image_id.py)

##### graphics_description: `str`

#### ⚙️ Request Body

[`QuestionDefinition`](./qualtrics_survey_python_sdk/type/question_definition.py)
Update question request

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/questions/{questionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.create_new_quota`

Create a new [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/).

#### 🛠️ Usage

```python
create_new_quota_response = qualtrics.survey_quotas.create_new_quota(
    name="Test Quota",
    occurrences=1000,
    logic=None,
    quota_action="EndCurrentSurvey",
    id="QO_abcdefghijklmno",
    quota_realm="Survey",
    survey_id="SV_0ODVm59K4i9tjcp",
    count=1,
    count_for_undo=1,
    logic_type=None,
    action_element="SV_Cu2LC4aWwWL",
    action_info={},
    action_logic={},
    quota_schedule=None,
    end_survey_options={
        "ending_type": "Default",
        "response_flag": "QuotaMet",
        "survey_termination": "DefaultMessage",
        "eos_message": "MS_abcdefg12345",
        "email_thank_you": "false",
        "thank_you_email_message_library": "UR_SomeUserId001",
        "thank_you_email_message": "MS_abcdefg12345",
        "response_summary": "false",
        "confirm_response_summary": "true",
        "confirm_message": "",
        "count_quotas": "true",
        "screenout": "true",
        "anonymize_response": "true",
        "ignore_response": "true",
    },
    web_service_options={
        "url": "https://www.1RhdCfdSDVGW=jZy@lSkdQ#Z0v5#-.H=Ev=3AIVZmmJTHDFBluhGK4iewqOA.BeAP8PPnm1BbkWKOit5S1.faQ6oS25F28d#RkT~VpXV=ih4AYItAzlSi4d_gwxS1qZbX.qy:kDaItAVScPW0YwW%eV#aa.x9uK@cOt#q1.dW6:AlAYzeWnJaFxJT5K.B-HgN3l7KK.K2n2FoDWDR+XtiVw%sa=GQ3qP:N+JQ~=LY59.nzLVQla@oc9Y9PLJAUqbPVDiTv%OgMNv_N0NJ@lbpxW0.?.~8K0d93FNgNJUeAjs4Rxg4Za~oiZ:uoRQgUz@5L",
        "params": [
            {
                "key": "key_example",
                "value": "value_example",
            }
        ],
    },
    cross_logic_def=[
        {
            "occurrences": 3.14,
            "description": "description_example",
            "id": 0,
            "logic": {},
        }
    ],
    perform_action_on_user=True,
    quota_group_id="QG_2Ds3413oqlm1sIH",
)
```

#### ⚙️ Parameters

##### name: `str`

Quota Name

##### occurrences: `int`

Quota Limit. Default: 100

##### logic: Union[[`LogicObject`](./qualtrics_survey_python_sdk/type/logic_object.py), List[[`LogicObject`](./qualtrics_survey_python_sdk/type/logic_object.py)]]


Logic of when to increment the quota

##### quota_action: [`QuotaAction`](./qualtrics_survey_python_sdk/type/quota_action.py)

##### id: [`QuotaID`](./qualtrics_survey_python_sdk/type/quota_id.py)

##### quota_realm: `str`

One of Survey or ResponseSet

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### count: `int`

Quota Count. Default: 0

##### count_for_undo: `int`

For restoring quota count

##### logic_type: `str`

One of Simple or Cross Logic Quota

##### action_element: Union[`SurveyID`, `QuestionID`, `BlockID`, `str`]


The element corresponding to the `QuotaAction` when `QuotaAction` is one of `DontDisplaySurvey`, `DontDisplayQuestion`, or `DontDisplayBlock`. See `QuotaAction`

##### action_info: [`ActionInfo`](./qualtrics_survey_python_sdk/type/action_info.py)

##### action_logic: [`ActionInfo`](./qualtrics_survey_python_sdk/type/action_info.py)

##### quota_schedule: `QuotaSchedule`

##### end_survey_options: [`EndSurveyOptions`](./qualtrics_survey_python_sdk/type/end_survey_options.py)


##### web_service_options: [`WebServiceOptions`](./qualtrics_survey_python_sdk/type/web_service_options.py)


##### cross_logic_def: List[`CrossLogicDefEntry`]

Definition for the cross logic quota

##### perform_action_on_user: `bool`

##### quota_group_id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/.py)

#### ⚙️ Request Body

[`Quota`](./qualtrics_survey_python_sdk/type/quota.py)
Create quota request

#### 🔄 Return

[`CreateQuotaResponse`](./qualtrics_survey_python_sdk/pydantic/create_quota_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotas` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.create_quota_group`

Create a new [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) group.

#### 🛠️ Usage

```python
create_quota_group_response = qualtrics.survey_quotas.create_quota_group(
    id="QG_2Ds3413oqlm1sIH",
    survey_id="SV_0ODVm59K4i9tjcp",
    id="QG_2Ds3413oqlm1sIH",
    multiple_match="ReverseOrder",
    name="Quota Group 2",
    public=False,
    quotas=[
        "QO_Cu2LC4aWwWL"
    ],
    selected=False,
)
```

#### ⚙️ Parameters

##### id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/quota_group_id.py)

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/quota_group_id.py)

##### multiple_match: `str`

Determines behavior when a single response matches multiple quotas within the group. One of `PlaceInAll`, `LeastFilled`, `MostFilled`, `LeastFilledPercent`, `MostFilledPercent`, `ReverseOrder`, or `CurrentDefinedOrder`

##### name: `str`

Name of the quota group

##### public: `bool`

`Public` refers to whether or not the Public Quota Dashboard is enabled. Enabling the Public Quota Dashboard will provide a public page where anyone can view the quotas in that group.

##### quotas: List[`QuotaID`]

A list of all the quotas in the group

##### selected: `bool`

Input will not be persisted. It is only used by the Quota Editor UI

#### ⚙️ Request Body

[`QuotaGroup`](./qualtrics_survey_python_sdk/type/quota_group.py)
Create quota group request

#### 🔄 Return

[`CreateQuotaGroupResponse`](./qualtrics_survey_python_sdk/pydantic/create_quota_group_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotagroups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.delete_quota`

Delete a [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) from a survey.

#### 🛠️ Usage

```python
delete_quota_response = qualtrics.survey_quotas.delete_quota(
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_id="QO_abcdefghijklmno",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_id: [`QuotaID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotas/{quotaId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.get_all`

Retrieve all [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) definitions for a survey.

#### 🛠️ Usage

```python
get_all_response = qualtrics.survey_quotas.get_all(
    survey_id="SV_0ODVm59K4i9tjcp",
    page_size=1,
    skip_token="string_example",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### page_size: `int`

##### skip_token: `str`

#### 🔄 Return

[`GetQuotasResponse`](./qualtrics_survey_python_sdk/pydantic/get_quotas_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.get_definition`

Retrieve a specific [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) definition.

#### 🛠️ Usage

```python
get_definition_response = qualtrics.survey_quotas.get_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_id="QO_abcdefghijklmno",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_id: [`QuotaID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`GetQuotaResponse`](./qualtrics_survey_python_sdk/pydantic/get_quota_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotas/{quotaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.get_quota_group_definition`

Retrieve a specific [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) group definition.

#### 🛠️ Usage

```python
get_quota_group_definition_response = qualtrics.survey_quotas.get_quota_group_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_group_id="QG_2Ds3413oqlm1sIH",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_group_id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`GetQuotaGroupResponse`](./qualtrics_survey_python_sdk/pydantic/get_quota_group_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.list_quota_groups`

Return a list of [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) group definitions for a survey.

#### 🛠️ Usage

```python
list_quota_groups_response = qualtrics.survey_quotas.list_quota_groups(
    survey_id="SV_0ODVm59K4i9tjcp",
    page_size=1,
    skip_token="string_example",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### page_size: `int`

##### skip_token: `str`

#### 🔄 Return

[`GetQuotaGroupsResponse`](./qualtrics_survey_python_sdk/pydantic/get_quota_groups_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotagroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.remove_quota_group`

Delete a [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) group and all its quotas from a survey.

#### 🛠️ Usage

```python
remove_quota_group_response = qualtrics.survey_quotas.remove_quota_group(
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_group_id="QG_2Ds3413oqlm1sIH",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_group_id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.update_definition`

Update a [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) definition.

#### 🛠️ Usage

```python
update_definition_response = qualtrics.survey_quotas.update_definition(
    name="Test Quota",
    occurrences=1000,
    logic=None,
    quota_action="EndCurrentSurvey",
    id="QO_abcdefghijklmno",
    quota_realm="Survey",
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_id="QO_abcdefghijklmno",
    count=1,
    count_for_undo=1,
    logic_type=None,
    action_element="SV_Cu2LC4aWwWL",
    action_info={},
    action_logic={},
    quota_schedule=None,
    end_survey_options={
        "ending_type": "Default",
        "response_flag": "QuotaMet",
        "survey_termination": "DefaultMessage",
        "eos_message": "MS_abcdefg12345",
        "email_thank_you": "false",
        "thank_you_email_message_library": "UR_SomeUserId001",
        "thank_you_email_message": "MS_abcdefg12345",
        "response_summary": "false",
        "confirm_response_summary": "true",
        "confirm_message": "",
        "count_quotas": "true",
        "screenout": "true",
        "anonymize_response": "true",
        "ignore_response": "true",
    },
    web_service_options={
        "url": "https://www.1RhdCfdSDVGW=jZy@lSkdQ#Z0v5#-.H=Ev=3AIVZmmJTHDFBluhGK4iewqOA.BeAP8PPnm1BbkWKOit5S1.faQ6oS25F28d#RkT~VpXV=ih4AYItAzlSi4d_gwxS1qZbX.qy:kDaItAVScPW0YwW%eV#aa.x9uK@cOt#q1.dW6:AlAYzeWnJaFxJT5K.B-HgN3l7KK.K2n2FoDWDR+XtiVw%sa=GQ3qP:N+JQ~=LY59.nzLVQla@oc9Y9PLJAUqbPVDiTv%OgMNv_N0NJ@lbpxW0.?.~8K0d93FNgNJUeAjs4Rxg4Za~oiZ:uoRQgUz@5L",
        "params": [
            {
                "key": "key_example",
                "value": "value_example",
            }
        ],
    },
    cross_logic_def=[
        {
            "occurrences": 3.14,
            "description": "description_example",
            "id": 0,
            "logic": {},
        }
    ],
    perform_action_on_user=True,
)
```

#### ⚙️ Parameters

##### name: `str`

Quota Name

##### occurrences: `int`

Quota Limit. Default: 100

##### logic: Union[[`LogicObject`](./qualtrics_survey_python_sdk/type/logic_object.py), List[[`LogicObject`](./qualtrics_survey_python_sdk/type/logic_object.py)]]


Logic of when to increment the quota

##### quota_action: [`QuotaAction`](./qualtrics_survey_python_sdk/type/quota_action.py)

##### id: [`QuotaID`](./qualtrics_survey_python_sdk/type/quota_id.py)

##### quota_realm: `str`

One of Survey or ResponseSet

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_id: [`QuotaID`](./qualtrics_survey_python_sdk/type/.py)

##### count: `int`

Quota Count. Default: 0

##### count_for_undo: `int`

For restoring quota count

##### logic_type: `str`

One of Simple or Cross Logic Quota

##### action_element: Union[`SurveyID`, `QuestionID`, `BlockID`, `str`]


The element corresponding to the `QuotaAction` when `QuotaAction` is one of `DontDisplaySurvey`, `DontDisplayQuestion`, or `DontDisplayBlock`. See `QuotaAction`

##### action_info: [`ActionInfo`](./qualtrics_survey_python_sdk/type/action_info.py)

##### action_logic: [`ActionInfo`](./qualtrics_survey_python_sdk/type/action_info.py)

##### quota_schedule: `QuotaSchedule`

##### end_survey_options: [`EndSurveyOptions`](./qualtrics_survey_python_sdk/type/end_survey_options.py)


##### web_service_options: [`WebServiceOptions`](./qualtrics_survey_python_sdk/type/web_service_options.py)


##### cross_logic_def: List[`CrossLogicDefEntry`]

Definition for the cross logic quota

##### perform_action_on_user: `bool`

#### ⚙️ Request Body

[`Quota`](./qualtrics_survey_python_sdk/type/quota.py)
Update quota request

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotas/{quotaId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_quotas.update_quota_group_definition`

Update a [quota](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/quotas/) group definition.

#### 🛠️ Usage

```python
update_quota_group_definition_response = qualtrics.survey_quotas.update_quota_group_definition(
    id="QG_2Ds3413oqlm1sIH",
    survey_id="SV_0ODVm59K4i9tjcp",
    quota_group_id="QG_2Ds3413oqlm1sIH",
    id="QG_2Ds3413oqlm1sIH",
    multiple_match="ReverseOrder",
    name="Quota Group 2",
    public=False,
    quotas=[
        "QO_Cu2LC4aWwWL"
    ],
    selected=False,
)
```

#### ⚙️ Parameters

##### id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/quota_group_id.py)

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### quota_group_id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/.py)

##### id: [`QuotaGroupID`](./qualtrics_survey_python_sdk/type/quota_group_id.py)

##### multiple_match: `str`

Determines behavior when a single response matches multiple quotas within the group. One of `PlaceInAll`, `LeastFilled`, `MostFilled`, `LeastFilledPercent`, `MostFilledPercent`, `ReverseOrder`, or `CurrentDefinedOrder`

##### name: `str`

Name of the quota group

##### public: `bool`

`Public` refers to whether or not the Public Quota Dashboard is enabled. Enabling the Public Quota Dashboard will provide a public page where anyone can view the quotas in that group.

##### quotas: List[`QuotaID`]

A list of all the quotas in the group

##### selected: `bool`

Input will not be persisted. It is only used by the Quota Editor UI

#### ⚙️ Request Body

[`QuotaGroup`](./qualtrics_survey_python_sdk/type/quota_group.py)
Update quota group request

#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/quotagroups/{quotaGroupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_translations.get_by_survey_id_and_language_code`

Return a list of all fields in a survey that can be [translated](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/translate-survey/) and their existing translations given a `surveyId` and `languageCode`.
<!--From Readme-->
For more information about using the survey APIs, see [Managing Surveys](../../../../docs/Guides/Common%20Tasks/managing-surveys.md).


#### 🛠️ Usage

```python
get_by_survey_id_and_language_code_response = qualtrics.survey_translations.get_by_survey_id_and_language_code(
    survey_id="surveyId_example",
    language_code="languageCode_example",
)
```

#### ⚙️ Parameters

##### survey_id: `str`

##### language_code: `str`

#### 🔄 Return

[`TranslationsResponse`](./qualtrics_survey_python_sdk/pydantic/translations_response.py)

#### 🌐 Endpoint

`/surveys/{surveyId}/translations/{languageCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_translations.update_translations`

Update a [survey translations](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/translate-survey/) for a given `surveyId` and `language code`. Must include existing translations.
<!--From Readme-->
For more information about using the survey APIs, see [Managing Surveys](../../../../docs/Guides/Common%20Tasks/managing-surveys.md).
<!-- theme: info -->

>### Permissions
>**Translate Surveys** permission must be enabled for the user to update survey languages.



#### 🛠️ Usage

```python
update_translations_response = qualtrics.survey_translations.update_translations(
    survey_id="surveyId_example",
    language_code="languageCode_example",
)
```

#### ⚙️ Parameters

##### survey_id: `str`

##### language_code: `str`

#### ⚙️ Request Body

[`SurveyTranslations`](./qualtrics_survey_python_sdk/type/survey_translations.py)
#### 🔄 Return

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint

`/surveys/{surveyId}/translations/{languageCode}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_versions.create_new_version`

Create a new [survey version](https://www.qualtrics.com/support/survey-platform/survey-module/survey-publishing-versions/).

#### 🛠️ Usage

```python
create_new_version_response = qualtrics.survey_versions.create_new_version(
    description="2018 Phone Launch",
    published=True,
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### description: `str`

A user-provided description of the survey version.

##### published: `bool`

When true, mark the survey version as published.

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### ⚙️ Request Body

[`CreateSurveyVersionRequest`](./qualtrics_survey_python_sdk/type/create_survey_version_request.py)
Create new survey version request

#### 🔄 Return

[`CreateSurveyVersionResponse`](./qualtrics_survey_python_sdk/pydantic/create_survey_version_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/versions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_versions.get_definition`

Retrieve a [survey version](https://www.qualtrics.com/support/survey-platform/survey-module/survey-publishing-versions/) definition.

#### 🛠️ Usage

```python
get_definition_response = qualtrics.survey_versions.get_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    version_id="4",
    format="qsf",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### version_id: [`VersionID`](./qualtrics_survey_python_sdk/type/.py)

##### format: `str`

#### 🔄 Return

[`GetSurveyVersionResponse`](./qualtrics_survey_python_sdk/pydantic/get_survey_version_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/versions/{versionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.survey_versions.list`

Return a list of all [versions of a survey](https://www.qualtrics.com/support/survey-platform/survey-module/survey-publishing-versions/), including survey metadata.

#### 🛠️ Usage

```python
list_response = qualtrics.survey_versions.list(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`ListSurveyVersionsResponse`](./qualtrics_survey_python_sdk/pydantic/list_survey_versions_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.surveys.create_definition`

Create a new [survey](https://api.qualtrics.com/ZG9jOjg3NzY4Mg-survey-api-introduction).

#### 🛠️ Usage

```python
create_definition_response = qualtrics.surveys.create_definition(
    body=None,
    survey_name="My cool survey",
    language="EN",
    project_category="CORE",
    survey_entry={
        "survey_id": "SV_0ODVm59K4i9tjcp",
        "survey_name": "new sooorvey",
        "survey_description": "survey_description_example",
        "survey_owner_id": "UR_3Cz41f8fIqINzaR",
        "survey_brand_id": "dpatty",
        "division_id": "division_id_example",
        "survey_language": "EN",
        "survey_active_response_set": "RS_6LLLLDaFHwxSe3z",
        "survey_status": "Inactive",
        "survey_start_date": "1970-01-01T00:00:00.00Z",
        "survey_expiration_date": "1970-01-01T00:00:00.00Z",
        "survey_creation_date": "1970-01-01T00:00:00.00Z",
        "creator_id": "UR_3Cz41f8fIqINzaR",
        "last_modified": "1970-01-01T00:00:00.00Z",
        "last_accessed": "1970-01-01T00:00:00.00Z",
        "last_activated": "1970-01-01T00:00:00.00Z",
        "deleted": "1970-01-01T00:00:00.00Z",
    },
    survey_elements=[
        {}
    ],
)
```

#### ⚙️ Parameters

##### survey_name: `str`

The name of the survey.

##### language: [`LanguageCode`](./qualtrics_survey_python_sdk/type/language_code.py)

##### project_category: [`ProjectCategory`](./qualtrics_survey_python_sdk/type/project_category.py)

##### survey_entry: [`SurveyMetadata`](./qualtrics_survey_python_sdk/type/survey_metadata.py)


##### survey_elements: List[[`SurveyElement`](./qualtrics_survey_python_sdk/type/survey_element.py)]

#### ⚙️ Request Body

[`CreateSurveyRequest`](./qualtrics_survey_python_sdk/type/create_survey_request.py)
Create or import a survey request.

#### 🔄 Return

[`CreateSurveyResponse`](./qualtrics_survey_python_sdk/pydantic/create_survey_response.py)

#### 🌐 Endpoint

`/survey-definitions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.surveys.get_definition`

Retrieve the [survey](https://api.qualtrics.com/ZG9jOjg3NzY4Mg-survey-api-introduction#survey-definition-api-tenets) definition or a specified survey format.

#### 🛠️ Usage

```python
get_definition_response = qualtrics.surveys.get_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
    format="qsf",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

##### format: `str`

#### 🔄 Return

[`GetSurveyResponse`](./qualtrics_survey_python_sdk/pydantic/get_survey_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.surveys.get_metadata`

Retrieve [survey](https://api.qualtrics.com/ZG9jOjg3NzY4Mg-survey-api-introduction) metadata.

#### 🛠️ Usage

```python
get_metadata_response = qualtrics.surveys.get_metadata(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`MetadataResponse`](./qualtrics_survey_python_sdk/pydantic/metadata_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.surveys.remove_definition`

Delete a [survey](https://api.qualtrics.com/ZG9jOjg3NzY4Mg-survey-api-introduction).

#### 🛠️ Usage

```python
remove_definition_response = qualtrics.surveys.remove_definition(
    survey_id="SV_0ODVm59K4i9tjcp",
)
```

#### ⚙️ Parameters

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)

#### 🔄 Return

[`DeleteSurveyResponse`](./qualtrics_survey_python_sdk/pydantic/delete_survey_response.py)

#### 🌐 Endpoint

`/survey-definitions/{surveyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `qualtrics.surveys.update_metadata`

Update [survey](https://api.qualtrics.com/ZG9jOjg3NzY4Mg-survey-api-introduction) metadata.

<!-- theme: warning -->
>### Date fields in this API use MySQL DateTime instead of ISO-8601.

#### 🛠️ Usage

```python
update_metadata_response = qualtrics.surveys.update_metadata(
    survey_id="SV_0ODVm59K4i9tjcp",
    survey_name="string_example",
    survey_description="string_example",
    survey_status="Inactive",
    survey_start_date="0480-72-88 80:01:52",
    survey_expiration_date="0480-72-88 80:01:52",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: [`SurveyID`](./qualtrics_survey_python_sdk/type/.py)<a id="survey_id-surveyidqualtrics_survey_python_sdktypepy"></a>

##### survey_name: `str`<a id="survey_name-str"></a>

The name of the survey.

##### survey_description: `Optional[str]`<a id="survey_description-optionalstr"></a>

A user-provided description of the survey.

##### survey_status: [`SurveyStatusPutMetadata`](./qualtrics_survey_python_sdk/type/survey_status_put_metadata.py)<a id="survey_status-surveystatusputmetadataqualtrics_survey_python_sdktypesurvey_status_put_metadatapy"></a>

##### survey_start_date: `str`<a id="survey_start_date-str"></a>

The start date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.

##### survey_expiration_date: `str`<a id="survey_expiration_date-str"></a>

The expiration date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateMetadataRequest`](./qualtrics_survey_python_sdk/type/update_metadata_request.py)
Update metadata request

#### 🔄 Return<a id="🔄-return"></a>

[`RequestSuccessfulResponse`](./qualtrics_survey_python_sdk/pydantic/request_successful_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/survey-definitions/{surveyId}/metadata` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
