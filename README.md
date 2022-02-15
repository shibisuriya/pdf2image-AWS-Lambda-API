# pdf2image - AWS Lambda API

Clone the repository.
```sh
git clone https://github.com/shibisuriya/pdf2image-AWS-Lambda-API.git
```
Run package.sh
```sh
chmod 777 ./package.sh
./package.sh
```
Or zip the /src folder manually... 

Create an AWS Lambda function.
![Alt text](/images/8.png?raw=true "Optional Title")
![Alt text](/images/9.png?raw=true "Optional Title")
![Alt text](/images/10.png?raw=true "Optional Title")
![Alt text](/images/11.png?raw=true "Optional Title")

Upload the generated package.zip file to AWS Lambda.
![Alt text](/images/1.png?raw=true "Optional Title")
![Alt text](/images/2.png?raw=true "Optional Title")
![Alt text](/images/3.png?raw=true "Optional Title")

Configure AWS API gateway to invoke our Lambda function.
![Alt text](/images/4.png?raw=true "Optional Title")
![Alt text](/images/5.png?raw=true "Optional Title")
![Alt text](/images/6.png?raw=true "Optional Title")
![Alt text](/images/7.png?raw=true "Optional Title")
