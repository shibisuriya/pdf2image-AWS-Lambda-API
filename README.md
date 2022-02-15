# pdf2image - AWS Lambda API
## About:
A stand alone microservice written in Python3.8 for AWS Lambda to convert pages of a .pdf file into images. This microservice is written with the help of pdf2image.py. pdf2image.py is a Python module that wraps pdftoppm and pdftocairo to convert PDF to a PIL Image object.

## Instructions:
#### Clone the repository
```sh
git clone https://github.com/shibisuriya/pdf2image-AWS-Lambda-API.git
```
### Run package.sh
```sh
chmod 777 ./package.sh
./package.sh
```
Or zip the /src folder manually... 

### Create an AWS Lambda function
![Alt text](/images/8.png?raw=true "Optional Title")
![Alt text](/images/9.png?raw=true "Optional Title")
![Alt text](/images/10.png?raw=true "Optional Title")
![Alt text](/images/11.png?raw=true "Optional Title")

### Upload the generated package.zip file to AWS Lambda
![Alt text](/images/1.png?raw=true "Optional Title")
![Alt text](/images/2.png?raw=true "Optional Title")
![Alt text](/images/3.png?raw=true "Optional Title")

### Configure AWS API gateway to invoke our Lambda function
![Alt text](/images/4.png?raw=true "Optional Title")
![Alt text](/images/5.png?raw=true "Optional Title")
![Alt text](/images/6.png?raw=true "Optional Title")
![Alt text](/images/7.png?raw=true "Optional Title")
![Alt text](/images/11.png?raw=true "Optional Title")

### Results
If we send a base64 pdf string as request to the API, we will recieve an array of base64 images.
![Alt text](/images/12.png?raw=true "Optional Title")
![Alt text](/images/13.png?raw=true "Optional Title")
