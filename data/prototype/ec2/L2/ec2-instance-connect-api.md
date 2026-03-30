# API Reference

## Welcome

API Reference
Amazon EC2 Instance Connect
API Version 2018-04-02
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.

## Actions

Amazon EC2 Instance Connect API Reference
Amazon EC2 Instance Connect: API Reference
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.

## SendSerialConsoleSSHPublicKey


## Request Syntax


## Request Parameters

Amazon EC2 Instance Connect API Reference
Table of Contents
Welcome ........................................................................................................................................... 1
Actions .............................................................................................................................................. 2
SendSerialConsoleSSHPublicKey ............................................................................................................... 3
Request Syntax ........................................................................................................................................ 3
Request Parameters ................................................................................................................................ 3
Response Syntax ...................................................................................................................................... 4
Response Elements ................................................................................................................................. 4
Errors .......................................................................................................................................................... 4
See Also ..................................................................................................................................................... 6
SendSSHPublicKey ........................................................................................................................................ 8
Request Syntax ........................................................................................................................................ 8
Request Parameters ................................................................................................................................ 8
Response Syntax ...................................................................................................................................... 9
Response Elements ................................................................................................................................. 9
Errors ....................................................................................................................................................... 10
Examples ................................................................................................................................................. 11
See Also .................................................................................................................................................. 11
Data Types ..................................................................................................................................... 13
Common Parameters ..................................................................................................................... 14
Common Errors .............................................................................................................................. 17
API Version 2018-04-02 iii

## Response Syntax


## Response Elements


## Errors

Amazon EC2 Instance Connect API Reference
Welcome
This is the  Amazon EC2 Instance Connect API Reference. It provides descriptions, syntax, and usage 
examples for each of the actions for Amazon EC2 Instance Connect. Amazon EC2 Instance Connect 
enables system administrators to publish one-time use SSH public keys to EC2, providing users a 
simple and secure way to connect to their instances.
To view the Amazon EC2 Instance Connect content in the  Amazon EC2 User Guide, see Connect to 
your Linux instance using EC2 Instance Connect.
For Amazon EC2 APIs, see the Amazon EC2 API Reference.
This document was last published on March 19, 2026.
API Version 2018-04-02 1
Amazon EC2 Instance Connect API Reference
Actions
The following actions are supported:
• SendSerialConsoleSSHPublicKey
• SendSSHPublicKey
API Version 2018-04-02 2

## See Also

Amazon EC2 Instance Connect API Reference
SendSerialConsoleSSHPublicKey
Pushes an SSH public key to the speciﬁed EC2 instance. The key remains for 60 seconds, which 
gives you 60 seconds to establish a serial console connection to the instance using SSH. For more 
information, see EC2 Serial Console in the Amazon EC2 User Guide.
Request Syntax
{ 
   "InstanceId": "string", 
   "SerialPort": number, 
   "SSHPublicKey": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
InstanceId
The ID of the EC2 instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: ^i-[a-f0-9]+$
Required: Yes
SerialPort
The serial port of the EC2 instance. Currently only port 0 is supported.
Default: 0
Type: Integer
Valid Range: Fixed value of 0.
Required: No
SendSerialConsoleSSHPublicKey API Version 2018-04-02 3
Amazon EC2 Instance Connect API Reference
SSHPublicKey
The public key material. To use the public key, you must have the matching private key. For 
information about the supported key formats and lengths, see Requirements for key pairs in the
Amazon EC2 User Guide.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 4096.
Required: Yes
Response Syntax
{ 
   "RequestId": "string", 
   "Success": boolean
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
RequestId
The ID of the request. Please provide this ID when contacting AWS Support for assistance.
Type: String
Success
Is true if the request succeeds and an error otherwise.
Type: Boolean
Errors
For information about the errors that are common to all actions, see Common Errors.
Response Syntax API Version 2018-04-02 4

## SendSSHPublicKey


## Request Syntax


## Request Parameters

Amazon EC2 Instance Connect API Reference
AuthException
Either your AWS credentials are not valid or you do not have access to the EC2 instance.
HTTP Status Code: 400
EC2InstanceNotFoundException
The speciﬁed instance was not found.
HTTP Status Code: 400
EC2InstanceStateInvalidException
Unable to connect because the instance is not in a valid state. Connecting to a stopped or 
terminated instance is not supported. If the instance is stopped, start your instance, and try to 
connect again.
HTTP Status Code: 400
EC2InstanceTypeInvalidException
The instance type is not supported for connecting via the serial console. Only Nitro instance 
types are currently supported.
HTTP Status Code: 400
EC2InstanceUnavailableException
The instance is currently unavailable. Wait a few minutes and try again.
HTTP Status Code: 400
InvalidArgsException
One of the parameters is not valid.
HTTP Status Code: 400
SerialConsoleAccessDisabledException
Your account is not authorized to use the EC2 Serial Console. To authorize your account, run 
the EnableSerialConsoleAccess API. For more information, see EnableSerialConsoleAccess in the
Amazon EC2 API Reference.
HTTP Status Code: 400
Errors API Version 2018-04-02 5

## Response Syntax


## Response Elements

Amazon EC2 Instance Connect API Reference
SerialConsoleSessionLimitExceededException
The instance currently has 1 active serial console session. Only 1 session is supported at a time.
HTTP Status Code: 400
SerialConsoleSessionUnavailableException
Unable to start a serial console session. Please try again.
HTTP Status Code: 500
ServiceException
The service encountered an error. Follow the instructions in the error message and try again.
HTTP Status Code: 500
ThrottlingException
The requests were made too frequently and have been throttled. Wait a while and try again. To 
increase the limit on your request frequency, contact AWS Support.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-04-02 6

## Errors

Amazon EC2 Instance Connect API Reference
See Also API Version 2018-04-02 7

## Examples


## See Also

Amazon EC2 Instance Connect API Reference
SendSSHPublicKey
Pushes an SSH public key to the speciﬁed EC2 instance for use by the speciﬁed user. The key 
remains for 60 seconds. For more information, see Connect to your Linux instance using EC2 
Instance Connect in the Amazon EC2 User Guide.
Request Syntax
{ 
   "AvailabilityZone": "string", 
   "InstanceId": "string", 
   "InstanceOSUser": "string", 
   "SSHPublicKey": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
AvailabilityZone
The Availability Zone in which the EC2 instance was launched.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 32.
Pattern: ^(\w+-){2,3}\d+\w+$
Required: No
InstanceId
The ID of the EC2 instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: ^i-[a-f0-9]+$
SendSSHPublicKey API Version 2018-04-02 8
Amazon EC2 Instance Connect API Reference
Required: Yes
InstanceOSUser
The OS user on the EC2 instance for whom the key can be used to authenticate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: ^[A-Za-z_][A-Za-z0-9\@\._-]{0,30}[A-Za-z0-9\$_-]?$
Required: Yes
SSHPublicKey
The public key material. To use the public key, you must have the matching private key.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 4096.
Required: Yes
Response Syntax
{ 
   "RequestId": "string", 
   "Success": boolean
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
RequestId
The ID of the request. Please provide this ID when contacting AWS Support for assistance.
Type: String
Response Syntax API Version 2018-04-02 9

## Data Types

Amazon EC2 Instance Connect API Reference
Success
Is true if the request succeeds and an error otherwise.
Type: Boolean
Errors
For information about the errors that are common to all actions, see Common Errors.
AuthException
Either your AWS credentials are not valid or you do not have access to the EC2 instance.
HTTP Status Code: 400
EC2InstanceNotFoundException
The speciﬁed instance was not found.
HTTP Status Code: 400
EC2InstanceStateInvalidException
Unable to connect because the instance is not in a valid state. Connecting to a stopped or 
terminated instance is not supported. If the instance is stopped, start your instance, and try to 
connect again.
HTTP Status Code: 400
EC2InstanceUnavailableException
The instance is currently unavailable. Wait a few minutes and try again.
HTTP Status Code: 400
InvalidArgsException
One of the parameters is not valid.
HTTP Status Code: 400
ServiceException
The service encountered an error. Follow the instructions in the error message and try again.
Errors API Version 2018-04-02 10

## Common Parameters

Amazon EC2 Instance Connect API Reference
HTTP Status Code: 500
ThrottlingException
The requests were made too frequently and have been throttled. Wait a while and try again. To 
increase the limit on your request frequency, contact AWS Support.
HTTP Status Code: 400
Examples
Push an SSH public key to an instance
This example sends the speciﬁed SSH public key to the speciﬁed instance in the speciﬁed 
Availability Zone. The key is used to authenticate the speciﬁed user.
Sample Request
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSEC2InstanceConnectService.SendSSHPublicKey
{ 
   "AvailabilityZone": "us-east-2b", 
   "InstanceId": "i-1234567890abcdef0", 
   "InstanceOSUser": "ec2-user", 
   "SSHPublicKey": "<ssh-public-key-material>"
}
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
Examples API Version 2018-04-02 11
Amazon EC2 Instance Connect API Reference
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-04-02 12
Amazon EC2 Instance Connect API Reference
Data Types
The AWS EC2 Instance Connect API has no separate data types.
API Version 2018-04-02 13

## Common Errors

Amazon EC2 Instance Connect API Reference
Common Parameters
The following list contains the parameters that all actions use for signing Signature Version 4 
requests with a query string. Any action-speciﬁc parameters are listed in the topic for that action. 
For more information about Signature Version 4, see Signing AWS API requests in the IAM User 
Guide.
Action
The action to be performed.
Type: string
Required: Yes
Version
The API version that the request is written for, expressed in the format YYYY-MM-DD.
Type: string
Required: Yes
X-Amz-Algorithm
The hash algorithm that you used to create the request signature.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Valid Values: AWS4-HMAC-SHA256
Required: Conditional
X-Amz-Credential
The credential scope value, which is a string that includes your access key, the date, the region 
you are targeting, the service you are requesting, and a termination string ("aws4_request"). 
The value is expressed in the following format: access_key/YYYYMMDD/region/service/
aws4_request.
API Version 2018-04-02 14
Amazon EC2 Instance Connect API Reference
For more information, see Create a signed AWS API request in the IAM User Guide.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Required: Conditional
X-Amz-Date
The date that is used to create the signature. The format must be ISO 8601 basic format 
(YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value:
20120325T120000Z.
Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for 
signing requests. If the Date header is speciﬁed in the ISO 8601 basic format, X-Amz-Date is not 
required. When X-Amz-Date is used, it always overrides the value of the Date header. For more 
information, see Elements of an AWS API request signature in the IAM User Guide.
Type: string
Required: Conditional
X-Amz-Security-Token
The temporary security token that was obtained through a call to AWS Security Token Service 
(AWS STS). For a list of services that support temporary security credentials from AWS STS, see
AWS services that work with IAM in the IAM User Guide.
Condition: If you're using temporary security credentials from AWS STS, you must include the 
security token.
Type: string
Required: Conditional
X-Amz-Signature
Speciﬁes the hex-encoded signature that was calculated from the string to sign and the derived 
signing key.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
API Version 2018-04-02 15
Amazon EC2 Instance Connect API Reference
Type: string
Required: Conditional
X-Amz-SignedHeaders
Speciﬁes all the HTTP headers that were included as part of the canonical request. For more 
information about specifying signed headers, see Create a signed AWS API request in the IAM 
User Guide.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Required: Conditional
API Version 2018-04-02 16
Amazon EC2 Instance Connect API Reference
Common Errors
This section lists the errors common to the API actions of all AWS services. For errors speciﬁc to an 
API action for this service, see the topic for that API action.
AccessDeniedException
You do not have suﬃcient access to perform this action.
HTTP Status Code: 400
IncompleteSignature
The request signature does not conform to AWS standards.
HTTP Status Code: 400
InternalFailure
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500
InvalidAction
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400
InvalidClientTokenId
The X.509 certiﬁcate or AWS access key ID provided does not exist in our records.
HTTP Status Code: 403
NotAuthorized
You do not have permission to perform this action.
HTTP Status Code: 400
OptInRequired
The AWS access key ID needs a subscription for the service.
HTTP Status Code: 403
API Version 2018-04-02 17
Amazon EC2 Instance Connect API Reference
RequestExpired
The request reached the service more than 15 minutes after the date stamp on the request or 
more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the 
date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 400
ServiceUnavailable
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503
ThrottlingException
The request was denied due to request throttling.
HTTP Status Code: 400
ValidationError
The input fails to satisfy the constraints speciﬁed by an AWS service.
HTTP Status Code: 400
API Version 2018-04-02 18

