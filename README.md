# T_Assignment_Data

Install the python3 on your machine
Then the following commands
>>Python3 Random_string_genration.py
It will generate the random string range
++++++++++++++++++++++++++++++++++++++++++++++++++++

Install the python3 on your machine
Install the pip3 to compitable with python3
Install Awscli using below commands
Please create the bucket in your aws account
>>>pip install awscli

After installing the awscli
>>aws configure

It will ask for following detail
AWS Access Key ID [None]: input your access key
AWS Secret Access Key [None]: input your secret access key
Default region name [None]: input your region
Default output format [None]: json

>>pip install boto3

After installing the boto3 .
Provide/change the following information in the python script based on your environment "AWS_File_Uploads_Downloads.py"
 
Name_of_File_after_Downloads_from_S3 = "Downloads_someFile.txt"
BucketName = "Provide the bucket name which you already created"
Upload_key = "Local path to file which you want to uploads"
Downloads_Key = "someFilename"
Name_of_File_after_Uploads_On_S3 = "someFilename"
Then run the following script using below commands

>>python3 AWS_File_Uploads_Downloads.py


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Pre-requisite
Install the terraform from where you want to run the terrafom 
Install the git  from where you want to take the checkout of github


Step to run  
1.Run the git clone command to take the checkout of github repo
git clone https://github.com/nitishNec/T_Assignment_Data 

2.Generate/create the access key and secret key in your AWS account.
3.Go to the data directory using cd command
4.Place access_key and secret_key value in main.tf file in  provider section of main.tf
access_key = “”
secret_key =””

5.Run the terraform command 
1. Terraform init
2. Terraform plan
3. Terraform apply


6.After doing all the above you also destroy the infra in one go by using following command
Terraform Destroy 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Install the docker from where you want to run the dockerFile
Run the following commands to build the image
>>>docker build --build-arg NEW_PORT=7688 --build-arg MAX_MEMORY=6666 .
>>>docker run -itd --memory 500m d7a858405c19 /bin/bash
>>>docker ps -a
Then check container id and login to running container using below commands
>>>docker attach conainer_ID
Then run ps -ef | grep "redis" it will show you the port redis running on
Note:Assign the memory while running the docker at run time using --memory 500m

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
