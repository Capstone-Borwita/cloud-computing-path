---
title: API KTP Borwita v1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="api-ktp-borwita">API KTP Borwita v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- oAuth2 authentication. 

    - Flow: password

    - Token URL = [token](token)

|Scope|Scope Description|
|---|---|

<h1 id="api-ktp-borwita-auth">auth</h1>

## login_user_api_v1_auth_login_post

<a id="opIdlogin_user_api_v1_auth_login_post"></a>

`POST /api/v1/auth/login`

*Login User*

> Body parameter

```yaml
email: user@example.com
password: stringst

```

<h3 id="login_user_api_v1_auth_login_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_login_user_api_v1_auth_login_post](#schemabody_login_user_api_v1_auth_login_post)|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "token": "string"
  }
}
```

<h3 id="login_user_api_v1_auth_login_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CredentialResponse](#schemacredentialresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## register_user_api_v1_auth_register_post

<a id="opIdregister_user_api_v1_auth_register_post"></a>

`POST /api/v1/auth/register`

*Register User*

> Body parameter

```yaml
email: user@example.com
password: stringst
name: string
avatar: string

```

<h3 id="register_user_api_v1_auth_register_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_register_user_api_v1_auth_register_post](#schemabody_register_user_api_v1_auth_register_post)|true|none|

> Example responses

> 201 Response

```json
{
  "detail": "success",
  "data": {
    "token": "string"
  }
}
```

<h3 id="register_user_api_v1_auth_register_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[CredentialResponse](#schemacredentialresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## edit_profile_api_v1_auth_edit_profile_put

<a id="opIdedit_profile_api_v1_auth_edit_profile_put"></a>

`PUT /api/v1/auth/edit-profile`

*Edit Profile*

> Body parameter

```yaml
name: string
email: user@example.com

```

<h3 id="edit_profile_api_v1_auth_edit_profile_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_edit_profile_api_v1_auth_edit_profile_put](#schemabody_edit_profile_api_v1_auth_edit_profile_put)|false|none|

> Example responses

> 200 Response

```json
{
  "detail": "success"
}
```

<h3 id="edit_profile_api_v1_auth_edit_profile_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessResponse](#schemasuccessresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## edit_photo_profile_api_v1_auth_edit_photo_profile_put

<a id="opIdedit_photo_profile_api_v1_auth_edit_photo_profile_put"></a>

`PUT /api/v1/auth/edit-photo-profile`

*Edit Photo Profile*

> Body parameter

```yaml
avatar: string

```

<h3 id="edit_photo_profile_api_v1_auth_edit_photo_profile_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_edit_photo_profile_api_v1_auth_edit_photo_profile_put](#schemabody_edit_photo_profile_api_v1_auth_edit_photo_profile_put)|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success"
}
```

<h3 id="edit_photo_profile_api_v1_auth_edit_photo_profile_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessResponse](#schemasuccessresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## edit_password_api_v1_auth_edit_password_put

<a id="opIdedit_password_api_v1_auth_edit_password_put"></a>

`PUT /api/v1/auth/edit-password`

*Edit Password*

> Body parameter

```yaml
old_password: stringst
new_password: stringst

```

<h3 id="edit_password_api_v1_auth_edit_password_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_edit_password_api_v1_auth_edit_password_put](#schemabody_edit_password_api_v1_auth_edit_password_put)|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "token": "string"
  }
}
```

<h3 id="edit_password_api_v1_auth_edit_password_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CredentialResponse](#schemacredentialresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## profile_api_v1_auth_profile_get

<a id="opIdprofile_api_v1_auth_profile_get"></a>

`GET /api/v1/auth/profile`

*Profile*

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "email": "string",
    "name": "string",
    "avatar_path": "string"
  }
}
```

<h3 id="profile_api_v1_auth_profile_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_UserGet_](#schemasuccessdataresponse_userget_)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="api-ktp-borwita-ocr">OCR</h1>

## ocr_ktp_api_v1_ocr_ktp_post

<a id="opIdocr_ktp_api_v1_ocr_ktp_post"></a>

`POST /api/v1/ocr/ktp`

*Ocr Ktp*

> Body parameter

```yaml
ktp_photo: string

```

<h3 id="ocr_ktp_api_v1_ocr_ktp_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_ocr_ktp_api_v1_ocr_ktp_post](#schemabody_ocr_ktp_api_v1_ocr_ktp_post)|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "identifier": "string",
    "nik": "string",
    "name": "string",
    "address": "string"
  }
}
```

<h3 id="ocr_ktp_api_v1_ocr_ktp_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_KTP_OCR_Result_](#schemasuccessdataresponse_ktp_ocr_result_)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="api-ktp-borwita-store">store</h1>

## get_all_stores_api_v1_stores__get

<a id="opIdget_all_stores_api_v1_stores__get"></a>

`GET /api/v1/stores/`

*Get All Stores*

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": [
    {
      "name": "string",
      "code": "string",
      "owner_name": "string",
      "keeper_phone_number": "string",
      "ktp_photo_path": "string",
      "keeper_name": "string",
      "keeper_nik": "string",
      "keeper_address": "string",
      "store_photo_path": "string",
      "longitude": "string",
      "latitude": "string",
      "georeverse": "string",
      "user_id": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z",
      "id": 0
    }
  ]
}
```

<h3 id="get_all_stores_api_v1_stores__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_List_Store__](#schemasuccessdataresponse_list_store__)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## create_store_api_v1_stores__post

<a id="opIdcreate_store_api_v1_stores__post"></a>

`POST /api/v1/stores/`

*Create Store*

> Body parameter

```yaml
name: string
owner_name: string
keeper_phone_number: string
keeper_nik: string
keeper_name: string
keeper_address: string
longitude: -180
latitude: -90
georeverse: string
ktp_photo_identifier: string
store_photo: string

```

<h3 id="create_store_api_v1_stores__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_create_store_api_v1_stores__post](#schemabody_create_store_api_v1_stores__post)|true|none|

> Example responses

> 201 Response

```json
{
  "detail": "success",
  "data": {
    "id": 0
  }
}
```

<h3 id="create_store_api_v1_stores__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[SuccessIdResponse](#schemasuccessidresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## update_store_api_v1_stores__store_id__put

<a id="opIdupdate_store_api_v1_stores__store_id__put"></a>

`PUT /api/v1/stores/{store_id}`

*Update Store*

> Body parameter

```yaml
name: string
owner_name: string
keeper_phone_number: string
keeper_nik: string
keeper_name: string
keeper_address: string
longitude: -180
latitude: -90
georeverse: string
ktp_photo_identifier: string
store_photo: string

```

<h3 id="update_store_api_v1_stores__store_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|store_id|path|integer|true|none|
|body|body|[Body_update_store_api_v1_stores__store_id__put](#schemabody_update_store_api_v1_stores__store_id__put)|false|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "id": 0
  }
}
```

<h3 id="update_store_api_v1_stores__store_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessIdResponse](#schemasuccessidresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## get_store_by_id_api_v1_stores__store_id__get

<a id="opIdget_store_by_id_api_v1_stores__store_id__get"></a>

`GET /api/v1/stores/{store_id}`

*Get Store By Id*

<h3 id="get_store_by_id_api_v1_stores__store_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|store_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "name": "string",
    "code": "string",
    "owner_name": "string",
    "keeper_phone_number": "string",
    "ktp_photo_path": "string",
    "keeper_name": "string",
    "keeper_nik": "string",
    "keeper_address": "string",
    "store_photo_path": "string",
    "longitude": "string",
    "latitude": "string",
    "georeverse": "string",
    "user_id": 0,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "id": 0
  }
}
```

<h3 id="get_store_by_id_api_v1_stores__store_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_Store_](#schemasuccessdataresponse_store_)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## delete_store_api_v1_stores__store_id__delete

<a id="opIddelete_store_api_v1_stores__store_id__delete"></a>

`DELETE /api/v1/stores/{store_id}`

*Delete Store*

<h3 id="delete_store_api_v1_stores__store_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|store_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success"
}
```

<h3 id="delete_store_api_v1_stores__store_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessResponse](#schemasuccessresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="api-ktp-borwita-news">news</h1>

## create_news_api_v1_news__post

<a id="opIdcreate_news_api_v1_news__post"></a>

`POST /api/v1/news/`

*Create News*

> Body parameter

```yaml
title: string
content: string
poster: string

```

<h3 id="create_news_api_v1_news__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_create_news_api_v1_news__post](#schemabody_create_news_api_v1_news__post)|true|none|

> Example responses

> 201 Response

```json
{
  "detail": "success",
  "data": {
    "id": 0
  }
}
```

<h3 id="create_news_api_v1_news__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[SuccessIdResponse](#schemasuccessidresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## get_news_api_v1_news__get

<a id="opIdget_news_api_v1_news__get"></a>

`GET /api/v1/news/`

*Get News*

<h3 id="get_news_api_v1_news__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": [
    {
      "title": "string",
      "content": "string",
      "poster": "string",
      "author_id": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z",
      "id": 0
    }
  ]
}
```

<h3 id="get_news_api_v1_news__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_List_News__](#schemasuccessdataresponse_list_news__)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## update_news_api_v1_news__news_id__put

<a id="opIdupdate_news_api_v1_news__news_id__put"></a>

`PUT /api/v1/news/{news_id}`

*Update News*

> Body parameter

```yaml
title: string
content: string
poster: string

```

<h3 id="update_news_api_v1_news__news_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|news_id|path|integer|true|none|
|body|body|[Body_update_news_api_v1_news__news_id__put](#schemabody_update_news_api_v1_news__news_id__put)|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "id": 0
  }
}
```

<h3 id="update_news_api_v1_news__news_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessIdResponse](#schemasuccessidresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## get_news_by_id_api_v1_news__news_id__get

<a id="opIdget_news_by_id_api_v1_news__news_id__get"></a>

`GET /api/v1/news/{news_id}`

*Get News By Id*

<h3 id="get_news_by_id_api_v1_news__news_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|news_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success",
  "data": {
    "title": "string",
    "content": "string",
    "poster": "string",
    "author_id": 0,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "id": 0
  }
}
```

<h3 id="get_news_by_id_api_v1_news__news_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessDataResponse_News_](#schemasuccessdataresponse_news_)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## delete_news_api_v1_news__news_id__delete

<a id="opIddelete_news_api_v1_news__news_id__delete"></a>

`DELETE /api/v1/news/{news_id}`

*Delete News*

<h3 id="delete_news_api_v1_news__news_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|news_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "detail": "success"
}
```

<h3 id="delete_news_api_v1_news__news_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SuccessResponse](#schemasuccessresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

# Schemas

<h2 id="tocS_Body_create_news_api_v1_news__post">Body_create_news_api_v1_news__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_create_news_api_v1_news__post"></a>
<a id="schema_Body_create_news_api_v1_news__post"></a>
<a id="tocSbody_create_news_api_v1_news__post"></a>
<a id="tocsbody_create_news_api_v1_news__post"></a>

```json
{
  "title": "string",
  "content": "string",
  "poster": "string"
}

```

Body_create_news_api_v1_news__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|content|string|true|none|none|
|poster|string(binary)|true|none|none|

<h2 id="tocS_Body_create_store_api_v1_stores__post">Body_create_store_api_v1_stores__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_create_store_api_v1_stores__post"></a>
<a id="schema_Body_create_store_api_v1_stores__post"></a>
<a id="tocSbody_create_store_api_v1_stores__post"></a>
<a id="tocsbody_create_store_api_v1_stores__post"></a>

```json
{
  "name": "string",
  "owner_name": "string",
  "keeper_phone_number": "string",
  "keeper_nik": "string",
  "keeper_name": "string",
  "keeper_address": "string",
  "longitude": -180,
  "latitude": -90,
  "georeverse": "string",
  "ktp_photo_identifier": "string",
  "store_photo": "string"
}

```

Body_create_store_api_v1_stores__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|owner_name|string|true|none|none|
|keeper_phone_number|string|true|none|none|
|keeper_nik|string|true|none|none|
|keeper_name|string|true|none|none|
|keeper_address|string|true|none|none|
|longitude|number|true|none|none|
|latitude|number|true|none|none|
|georeverse|string|true|none|none|
|ktp_photo_identifier|string|true|none|none|
|store_photo|string(binary)|true|none|none|

<h2 id="tocS_Body_edit_password_api_v1_auth_edit_password_put">Body_edit_password_api_v1_auth_edit_password_put</h2>
<!-- backwards compatibility -->
<a id="schemabody_edit_password_api_v1_auth_edit_password_put"></a>
<a id="schema_Body_edit_password_api_v1_auth_edit_password_put"></a>
<a id="tocSbody_edit_password_api_v1_auth_edit_password_put"></a>
<a id="tocsbody_edit_password_api_v1_auth_edit_password_put"></a>

```json
{
  "old_password": "stringst",
  "new_password": "stringst"
}

```

Body_edit_password_api_v1_auth_edit_password_put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|old_password|string|true|none|none|
|new_password|string|true|none|none|

<h2 id="tocS_Body_edit_photo_profile_api_v1_auth_edit_photo_profile_put">Body_edit_photo_profile_api_v1_auth_edit_photo_profile_put</h2>
<!-- backwards compatibility -->
<a id="schemabody_edit_photo_profile_api_v1_auth_edit_photo_profile_put"></a>
<a id="schema_Body_edit_photo_profile_api_v1_auth_edit_photo_profile_put"></a>
<a id="tocSbody_edit_photo_profile_api_v1_auth_edit_photo_profile_put"></a>
<a id="tocsbody_edit_photo_profile_api_v1_auth_edit_photo_profile_put"></a>

```json
{
  "avatar": "string"
}

```

Body_edit_photo_profile_api_v1_auth_edit_photo_profile_put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|avatar|string(binary)|true|none|none|

<h2 id="tocS_Body_edit_profile_api_v1_auth_edit_profile_put">Body_edit_profile_api_v1_auth_edit_profile_put</h2>
<!-- backwards compatibility -->
<a id="schemabody_edit_profile_api_v1_auth_edit_profile_put"></a>
<a id="schema_Body_edit_profile_api_v1_auth_edit_profile_put"></a>
<a id="tocSbody_edit_profile_api_v1_auth_edit_profile_put"></a>
<a id="tocsbody_edit_profile_api_v1_auth_edit_profile_put"></a>

```json
{
  "name": "string",
  "email": "user@example.com"
}

```

Body_edit_profile_api_v1_auth_edit_profile_put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|email|string(email)|false|none|none|

<h2 id="tocS_Body_login_user_api_v1_auth_login_post">Body_login_user_api_v1_auth_login_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_login_user_api_v1_auth_login_post"></a>
<a id="schema_Body_login_user_api_v1_auth_login_post"></a>
<a id="tocSbody_login_user_api_v1_auth_login_post"></a>
<a id="tocsbody_login_user_api_v1_auth_login_post"></a>

```json
{
  "email": "user@example.com",
  "password": "stringst"
}

```

Body_login_user_api_v1_auth_login_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string(email)|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_Body_ocr_ktp_api_v1_ocr_ktp_post">Body_ocr_ktp_api_v1_ocr_ktp_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_ocr_ktp_api_v1_ocr_ktp_post"></a>
<a id="schema_Body_ocr_ktp_api_v1_ocr_ktp_post"></a>
<a id="tocSbody_ocr_ktp_api_v1_ocr_ktp_post"></a>
<a id="tocsbody_ocr_ktp_api_v1_ocr_ktp_post"></a>

```json
{
  "ktp_photo": "string"
}

```

Body_ocr_ktp_api_v1_ocr_ktp_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ktp_photo|string(binary)|true|none|none|

<h2 id="tocS_Body_register_user_api_v1_auth_register_post">Body_register_user_api_v1_auth_register_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_register_user_api_v1_auth_register_post"></a>
<a id="schema_Body_register_user_api_v1_auth_register_post"></a>
<a id="tocSbody_register_user_api_v1_auth_register_post"></a>
<a id="tocsbody_register_user_api_v1_auth_register_post"></a>

```json
{
  "email": "user@example.com",
  "password": "stringst",
  "name": "string",
  "avatar": "string"
}

```

Body_register_user_api_v1_auth_register_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string(email)|true|none|none|
|password|string|true|none|none|
|name|string|true|none|none|
|avatar|string(binary)|false|none|none|

<h2 id="tocS_Body_update_news_api_v1_news__news_id__put">Body_update_news_api_v1_news__news_id__put</h2>
<!-- backwards compatibility -->
<a id="schemabody_update_news_api_v1_news__news_id__put"></a>
<a id="schema_Body_update_news_api_v1_news__news_id__put"></a>
<a id="tocSbody_update_news_api_v1_news__news_id__put"></a>
<a id="tocsbody_update_news_api_v1_news__news_id__put"></a>

```json
{
  "title": "string",
  "content": "string",
  "poster": "string"
}

```

Body_update_news_api_v1_news__news_id__put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|content|string|true|none|none|
|poster|string(binary)|false|none|none|

<h2 id="tocS_Body_update_store_api_v1_stores__store_id__put">Body_update_store_api_v1_stores__store_id__put</h2>
<!-- backwards compatibility -->
<a id="schemabody_update_store_api_v1_stores__store_id__put"></a>
<a id="schema_Body_update_store_api_v1_stores__store_id__put"></a>
<a id="tocSbody_update_store_api_v1_stores__store_id__put"></a>
<a id="tocsbody_update_store_api_v1_stores__store_id__put"></a>

```json
{
  "name": "string",
  "owner_name": "string",
  "keeper_phone_number": "string",
  "keeper_nik": "string",
  "keeper_name": "string",
  "keeper_address": "string",
  "longitude": -180,
  "latitude": -90,
  "georeverse": "string",
  "ktp_photo_identifier": "string",
  "store_photo": "string"
}

```

Body_update_store_api_v1_stores__store_id__put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|owner_name|string|false|none|none|
|keeper_phone_number|string|false|none|none|
|keeper_nik|string|false|none|none|
|keeper_name|string|false|none|none|
|keeper_address|string|false|none|none|
|longitude|number|false|none|none|
|latitude|number|false|none|none|
|georeverse|string|false|none|none|
|ktp_photo_identifier|string|false|none|none|
|store_photo|string(binary)|false|none|none|

<h2 id="tocS_Credential">Credential</h2>
<!-- backwards compatibility -->
<a id="schemacredential"></a>
<a id="schema_Credential"></a>
<a id="tocScredential"></a>
<a id="tocscredential"></a>

```json
{
  "token": "string"
}

```

Credential

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|token|string|true|none|none|

<h2 id="tocS_CredentialResponse">CredentialResponse</h2>
<!-- backwards compatibility -->
<a id="schemacredentialresponse"></a>
<a id="schema_CredentialResponse"></a>
<a id="tocScredentialresponse"></a>
<a id="tocscredentialresponse"></a>

```json
{
  "detail": "success",
  "data": {
    "token": "string"
  }
}

```

CredentialResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[Credential](#schemacredential)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": "invalid",
  "data": null,
  "message": "string"
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|null|false|none|none|
|message|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|invalid|

<h2 id="tocS_KTP_OCR_Result">KTP_OCR_Result</h2>
<!-- backwards compatibility -->
<a id="schemaktp_ocr_result"></a>
<a id="schema_KTP_OCR_Result"></a>
<a id="tocSktp_ocr_result"></a>
<a id="tocsktp_ocr_result"></a>

```json
{
  "identifier": "string",
  "nik": "string",
  "name": "string",
  "address": "string"
}

```

KTP_OCR_Result

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|string|true|none|none|
|nik|string|true|none|none|
|name|string|true|none|none|
|address|string|true|none|none|

<h2 id="tocS_ModelId">ModelId</h2>
<!-- backwards compatibility -->
<a id="schemamodelid"></a>
<a id="schema_ModelId"></a>
<a id="tocSmodelid"></a>
<a id="tocsmodelid"></a>

```json
{
  "id": 0
}

```

ModelId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|

<h2 id="tocS_News">News</h2>
<!-- backwards compatibility -->
<a id="schemanews"></a>
<a id="schema_News"></a>
<a id="tocSnews"></a>
<a id="tocsnews"></a>

```json
{
  "title": "string",
  "content": "string",
  "poster": "string",
  "author_id": 0,
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "id": 0
}

```

News

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|content|string|true|none|none|
|poster|string|true|none|none|
|author_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_at|string(date-time)|false|none|none|
|updated_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_Store">Store</h2>
<!-- backwards compatibility -->
<a id="schemastore"></a>
<a id="schema_Store"></a>
<a id="tocSstore"></a>
<a id="tocsstore"></a>

```json
{
  "name": "string",
  "code": "string",
  "owner_name": "string",
  "keeper_phone_number": "string",
  "ktp_photo_path": "string",
  "keeper_name": "string",
  "keeper_nik": "string",
  "keeper_address": "string",
  "store_photo_path": "string",
  "longitude": "string",
  "latitude": "string",
  "georeverse": "string",
  "user_id": 0,
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "id": 0
}

```

Store

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|code|string|true|none|none|
|owner_name|string|true|none|none|
|keeper_phone_number|string|true|none|none|
|ktp_photo_path|string|true|none|none|
|keeper_name|string|true|none|none|
|keeper_nik|string|true|none|none|
|keeper_address|string|true|none|none|
|store_photo_path|string|true|none|none|
|longitude|string|true|none|none|
|latitude|string|true|none|none|
|georeverse|string|true|none|none|
|user_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_at|string(date-time)|false|none|none|
|updated_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SuccessDataResponse_KTP_OCR_Result_">SuccessDataResponse_KTP_OCR_Result_</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_ktp_ocr_result_"></a>
<a id="schema_SuccessDataResponse_KTP_OCR_Result_"></a>
<a id="tocSsuccessdataresponse_ktp_ocr_result_"></a>
<a id="tocssuccessdataresponse_ktp_ocr_result_"></a>

```json
{
  "detail": "success",
  "data": {
    "identifier": "string",
    "nik": "string",
    "name": "string",
    "address": "string"
  }
}

```

SuccessDataResponse[KTP_OCR_Result]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[KTP_OCR_Result](#schemaktp_ocr_result)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessDataResponse_List_News__">SuccessDataResponse_List_News__</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_list_news__"></a>
<a id="schema_SuccessDataResponse_List_News__"></a>
<a id="tocSsuccessdataresponse_list_news__"></a>
<a id="tocssuccessdataresponse_list_news__"></a>

```json
{
  "detail": "success",
  "data": [
    {
      "title": "string",
      "content": "string",
      "poster": "string",
      "author_id": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z",
      "id": 0
    }
  ]
}

```

SuccessDataResponse[List[News]]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[[News](#schemanews)]|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessDataResponse_List_Store__">SuccessDataResponse_List_Store__</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_list_store__"></a>
<a id="schema_SuccessDataResponse_List_Store__"></a>
<a id="tocSsuccessdataresponse_list_store__"></a>
<a id="tocssuccessdataresponse_list_store__"></a>

```json
{
  "detail": "success",
  "data": [
    {
      "name": "string",
      "code": "string",
      "owner_name": "string",
      "keeper_phone_number": "string",
      "ktp_photo_path": "string",
      "keeper_name": "string",
      "keeper_nik": "string",
      "keeper_address": "string",
      "store_photo_path": "string",
      "longitude": "string",
      "latitude": "string",
      "georeverse": "string",
      "user_id": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z",
      "id": 0
    }
  ]
}

```

SuccessDataResponse[List[Store]]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[[Store](#schemastore)]|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessDataResponse_News_">SuccessDataResponse_News_</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_news_"></a>
<a id="schema_SuccessDataResponse_News_"></a>
<a id="tocSsuccessdataresponse_news_"></a>
<a id="tocssuccessdataresponse_news_"></a>

```json
{
  "detail": "success",
  "data": {
    "title": "string",
    "content": "string",
    "poster": "string",
    "author_id": 0,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "id": 0
  }
}

```

SuccessDataResponse[News]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[News](#schemanews)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessDataResponse_Store_">SuccessDataResponse_Store_</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_store_"></a>
<a id="schema_SuccessDataResponse_Store_"></a>
<a id="tocSsuccessdataresponse_store_"></a>
<a id="tocssuccessdataresponse_store_"></a>

```json
{
  "detail": "success",
  "data": {
    "name": "string",
    "code": "string",
    "owner_name": "string",
    "keeper_phone_number": "string",
    "ktp_photo_path": "string",
    "keeper_name": "string",
    "keeper_nik": "string",
    "keeper_address": "string",
    "store_photo_path": "string",
    "longitude": "string",
    "latitude": "string",
    "georeverse": "string",
    "user_id": 0,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "id": 0
  }
}

```

SuccessDataResponse[Store]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[Store](#schemastore)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessDataResponse_UserGet_">SuccessDataResponse_UserGet_</h2>
<!-- backwards compatibility -->
<a id="schemasuccessdataresponse_userget_"></a>
<a id="schema_SuccessDataResponse_UserGet_"></a>
<a id="tocSsuccessdataresponse_userget_"></a>
<a id="tocssuccessdataresponse_userget_"></a>

```json
{
  "detail": "success",
  "data": {
    "email": "string",
    "name": "string",
    "avatar_path": "string"
  }
}

```

SuccessDataResponse[UserGet]

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[UserGet](#schemauserget)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessIdResponse">SuccessIdResponse</h2>
<!-- backwards compatibility -->
<a id="schemasuccessidresponse"></a>
<a id="schema_SuccessIdResponse"></a>
<a id="tocSsuccessidresponse"></a>
<a id="tocssuccessidresponse"></a>

```json
{
  "detail": "success",
  "data": {
    "id": 0
  }
}

```

SuccessIdResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|
|data|[ModelId](#schemamodelid)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_SuccessResponse">SuccessResponse</h2>
<!-- backwards compatibility -->
<a id="schemasuccessresponse"></a>
<a id="schema_SuccessResponse"></a>
<a id="tocSsuccessresponse"></a>
<a id="tocssuccessresponse"></a>

```json
{
  "detail": "success"
}

```

SuccessResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|detail|success|

<h2 id="tocS_UserGet">UserGet</h2>
<!-- backwards compatibility -->
<a id="schemauserget"></a>
<a id="schema_UserGet"></a>
<a id="tocSuserget"></a>
<a id="tocsuserget"></a>

```json
{
  "email": "string",
  "name": "string",
  "avatar_path": "string"
}

```

UserGet

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|true|none|none|
|name|string|true|none|none|
|avatar_path|string|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

