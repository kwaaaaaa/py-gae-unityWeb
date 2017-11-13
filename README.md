# py-gae-unityWeb

## dependencies

No special libraries are used
Unity games are hosted on a static files

## setting up unity projects

You can just make host the files directly in the static dir

## setting up google storage files

To host large unity data files in Google storage, you need to create
  a bucket and then add a cors header.

This google sdk cloud shell command will create a cors header:
echo '[{"origin": ["*"],"responseHeader": ["Content-Type"],"method": ["GET", "HEAD"],"maxAgeSeconds": 3600}]' > cors-config.json

This gsutil command will set the header
gsutil set cors cors-config.json gs://bucket_name

## notes

When using large textures, the file size of the data is easily over 33mb
  so you need to host these files somewhere else besides appengine

Unity takes a lot of memory and browsers can't handle too much
  use "TOTAL_MEMORY": 134217728, in the json settings
