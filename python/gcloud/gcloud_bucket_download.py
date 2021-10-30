# setup:
# https://googleapis.dev/python/google-api-core/latest/auth.html
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/.../<service account name>-asdfas21112.json"

# using default credentials
from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('<bucket name>')
# Then do other things...
blob = bucket.get_blob('foo.yaml')
if blob is not None:
    blob.download_to_filename('hi.yaml')
else:
    print('no blob!')



## or

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/Users/.../gcloud/foo.json')

from google.cloud import storage
client = storage.Client(credentials=credentials)