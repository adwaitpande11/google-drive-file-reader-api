# Google Drive File Reader API

Python 3.6

#### Summary
This API lets user read the files directly from their Google Drive. Currently, this supports reading of plain text file formats like - txt, csv etc.

> This is designed to work with AWS Lambda and AWS API Gateway; nonetheless, it will work on any other server by tweaking main.py as per specific requirements.

#### Pre-Requisite
- Python 3.6 (not tested for compatibility with other versions)
- Pip
- A service account in Google API Developer Console.
- Environment variable `SERVICE_ACCOUNT_FILE_CONTENT` (description below)

#### Description
* This API connects to Google Drive via service account's json file (using OAuth 2.0). Read more about service accounts, go to Reference #2.

* A service account is different from user account; which implies that the files on Google Drive for `my_personal_email@gmail.com` are not accessible to `api-user@project-id.iam.gserviceaccount.com` (service account's email ID). To allow access to person drive files, one should `share` the file with service account email ID. Refer section _'Computer > Choose who to share with > Specific People'_ from [this link](https://support.google.com/drive/answer/7166529?co=GENIE.Platform%3DDesktop&hl=en).

* Use of environment variable - As a general practice, it is not preferred for credentials to be inside repo or hardcoded. Hence, I have used environment variable `SERVICE_ACCOUNT_FILE_CONTENT` to hold contents of service account JSON file (a sample of this is available in repo). 

#### Installation
`pip install -r requirements.txt`
or
`pip3 install -r requirements.txt`

#### Code
 
* **main.py**: `lambda_handler(): event, context`
AWS Lambda passes the `event` and `context` param to bootstrap function. `event` receives the input JSON from AWS Lambda; `context` param is unused.

* Rest is self explanatory

##### Payload
_Type_ - `application/json, Python dict`

_Sample Payload_ - `{ "filename":"myfile.txt" }`

##### Response
_Type_ - plain text

_Sample Response_ - `This is the content of file myfile.txt`

#### References and Documentations
1. Drive API Reference Python -
https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.files.html#get_media
2. Google Service Account OAuth 2.0 - https://developers.google.com/identity/protocols/OAuth2ServiceAccount