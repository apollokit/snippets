# get cuda version using cut
# -d " " marks space as the delimiter
# -f15 means choose the 15th element that was cut
cuda_ver=$(nvidia-smi | grep "CUDA Version" | cut -d " " -f15)

## extract build_id "90598e33-172d-45ef-814b-b07c70d4f2cd" from the following output from gcloud builds:
#      Created [https://cloudbuild.googleapis.com/v1/projects/s/locations/90598e33-172d-45ef-814b-b07c70d4f2cd].                                                  
#      Logs are available at [https://console.cloud.google.com/cloud-build/builds/90598e33-172d-45ef-814b-b07c70d4f2cd?project=653248281140].
#      {                                                                                             
#        "artifacts": {                                                                              
#          "images": [                                                                               
#            "gcr.io/s/m:latest"                                                                                                                       
#          ]                               
#        },                                                                                                                                                                                         
#        "createTime": "2021-07-21T21:17:53.781401626Z",                                                                                                                                            
#        "id": "90598e33-172d-45ef-814b-b07c70d4f2cd",                                               
#        "images": [
build_id=$(gcloud builds submit --no-source  --config=clouditeration.yml --async --format=json 2>&1 \
		| grep "Created \[https://cloudbuild.googleapis" \
		| cut -d "/" -f10 \
		| cut -d "]" -f1)