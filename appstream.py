#Simple python script to create aws appstream users

import boto3
import time
#telling boto3 which aws client api to connect to

client = boto3.client('appstream')

#storing user information in a dictionary

user_details = {
    "UserName": "tegaokosiako@gmail2.com",
    "MessageAction":  "SUPPRESS",
    "FirstName": "Testing",
    "LastName": "LastnameTesting",
    "AuthenticationType": "USERPOOL"

}

# creating user with the client(appstream)


create_user = client.create_user(
     UserName = user_details["UserName"],
     MessageAction = user_details["MessageAction"],
     FirstName = user_details["FirstName"],
     LastName = user_details["LastName"],
     AuthenticationType = user_details["AuthenticationType"]
 )

time.sleep(100)
assign_user_stack = client.batch_associate_user_stack(
    UserStackAssociations=[
        {
            "StackName": "precious-appstream-stack",
            "UserName": user_details["UserName"],
            "AuthenticationType": "USERPOOL",
            "SendEmailNotification": True
        },
    ]
)


# assigning a stack to the user created

assign_user_stack = client.batch_associate_user_stack(
    UserStackAssociations=[
        {
            "StackName": "precious-appstream-stack",
            "UserName": user_details["UserName"],
            "AuthenticationType": "USERPOOL",
            "SendEmailNotification": True
        },
    ]
)
