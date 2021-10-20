#Simple python script to create aws appstream users

import boto3

#telling boto3 which aws client api to connect to

client = boto3.client('appstream')

#storing user information in a dictionary

user_details = {
    "UserName": "precious.okosiako@gmail.com",
    "MessageAction":  "SUPPRESS",
    "FirstName": "Precious",
    "LastName": "Okosiako",
    "AuthenticationType": "USERPOOL"

}

# creating user with the client(appstream)

response = client.create_user(
    UserName = user_details["UserName"],
    MessageAction = user_details["MessageAction"],
    FirstName = user_details["FirstName"],
    LastName = user_details["LastName"],
    AuthenticationType = user_details["AuthenticationType"]
)

# assigning a stack to the user created

response = client.batch_associate_user_stack(
    UserStackAssociations=[
        {
            "StackName": "precious-appstream-stack",
            "UserName": user_details["UserName"],
            "AuthenticationType": "USERPOOL",
            "SendEmailNotification": True
        },
    ]
)