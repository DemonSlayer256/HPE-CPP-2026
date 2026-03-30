# User Guide

## What is IAM Roles Anywhere?


## IAM Roles Anywhere concepts

User Guide
IAM Roles Anywhere
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.

## Account trust boundary


## Multi-account setups


## Accessing IAM Roles Anywhere

IAM Roles Anywhere User Guide
IAM Roles Anywhere: User Guide
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
IAM Roles Anywhere User Guide
Table of Contents
What is IAM Roles Anywhere? ........................................................................................................ 1
IAM Roles Anywhere concepts ................................................................................................................... 1
Account trust boundary ......................................................................................................................... 2
Multi-account setups .............................................................................................................................. 2
Accessing IAM Roles Anywhere ................................................................................................................. 2
Public key infrastructure ................................................................................................................. 4
Certiﬁcate authorities .................................................................................................................................. 4
Certiﬁcates ..................................................................................................................................................... 4
Key management .......................................................................................................................................... 4
Getting started ................................................................................................................................ 5
Step 1: Establish trust ................................................................................................................................. 5
Step 2: Conﬁgure roles ............................................................................................................................... 7
Next steps ...................................................................................................................................................... 9
Get temporary security credentials .............................................................................................. 10
Credential Helper on GitHub ................................................................................................................... 12
Advanced Features ..................................................................................................................................... 12
OS Certiﬁcate Store Integration ........................................................................................................ 12
PKCS#11 Integration ............................................................................................................................ 14
TPM Integration .................................................................................................................................... 15
Diagnostic Commands ......................................................................................................................... 16
Available commands .................................................................................................................................. 17
Comparison of credential-helper commands .................................................................................. 18
credential-process command ................................................................................................................... 18
Synopsis .................................................................................................................................................. 18
Options .................................................................................................................................................... 19
Output ..................................................................................................................................................... 21
Examples ................................................................................................................................................. 22
serve command .......................................................................................................................................... 23
Synopsis .................................................................................................................................................. 23
Options .................................................................................................................................................... 24
Behavior .................................................................................................................................................. 24
Examples ................................................................................................................................................. 25
update command ....................................................................................................................................... 26
Synopsis .................................................................................................................................................. 26
iii

## Public key infrastructure


## Certiﬁcate authorities


## Certiﬁcates


## Key management

IAM Roles Anywhere User Guide
Options .................................................................................................................................................... 27
Behavior .................................................................................................................................................. 27
Examples ................................................................................................................................................. 28
Credential Helper Changelog .................................................................................................................. 29
CredentialHelper version 1.8.0 ........................................................................................................... 29
CredentialHelper version 1.7.3 ........................................................................................................... 29
CredentialHelper version 1.7.2 ........................................................................................................... 29
CredentialHelper version 1.7.1 ........................................................................................................... 29
CredentialHelper version 1.7.0 ........................................................................................................... 29
CredentialHelper version 1.6.0 ........................................................................................................... 30
CredentialHelper version 1.5.0 ........................................................................................................... 30
CredentialHelper version 1.4.0 ........................................................................................................... 30
CredentialHelper version 1.3.0 ........................................................................................................... 30
CredentialHelper version 1.2.1 ........................................................................................................... 30
CredentialHelper version 1.2.0 ........................................................................................................... 30
CredentialHelper version 1.1.1 ........................................................................................................... 31
CredentialHelper version 1.1.0 ........................................................................................................... 31
CredentialHelper version 1.0.6 ........................................................................................................... 31
CredentialHelper version 1.0.5 ........................................................................................................... 31
CredentialHelper version 1.0.4 ........................................................................................................... 31
CredentialHelper version 1.0.3 ........................................................................................................... 31
CredentialHelper version 1.0.2 ........................................................................................................... 31
CredentialHelper version 1.0.1 ........................................................................................................... 32
IAM Roles Anywhere trust model ................................................................................................. 33
Role trusts .................................................................................................................................................... 33
Signature validation ................................................................................................................................... 34
Trust policy .................................................................................................................................................. 35
Certiﬁcate attribute mapping .................................................................................................................. 43
Default mapping behavior .................................................................................................................. 43
Put attribute mappings ....................................................................................................................... 45
Delete attribute mappings .................................................................................................................. 46
Attribute mapping and trust policy .................................................................................................. 47
Source identity rules .................................................................................................................................. 49
Revocation ................................................................................................................................................... 50
IAM Roles Anywhere authentication ............................................................................................ 51
CreateSession API ....................................................................................................................................... 52
iv

## Getting started


## Step 1: Establish trust

IAM Roles Anywhere User Guide
Request Syntax ...................................................................................................................................... 52
URI Request Parameters ...................................................................................................................... 52
Request Body ......................................................................................................................................... 53
Response Syntax ................................................................................................................................... 54
Response Elements ............................................................................................................................... 55
Credentials Object ................................................................................................................................ 56
The relationship between CreateSession and AssumeRole .......................................................... 57
Signing process ........................................................................................................................................... 58
Task 1: Create a canonical request ................................................................................................... 58
Task 2: Create a string to sign ........................................................................................................... 62
Task 3: Calculate the signature .......................................................................................................... 63
Task 4: Add the signature to the HTTP request ............................................................................. 63
Security .......................................................................................................................................... 65
Workload identities .................................................................................................................................... 66
Data protection ........................................................................................................................................... 66
Encryption in transit ............................................................................................................................ 67
Key management .................................................................................................................................... 4
Inter-network traﬃc privacy .............................................................................................................. 68
Identity and access management ........................................................................................................... 68
Audience .................................................................................................................................................. 68
Authenticating with identities ............................................................................................................ 69
Managing access using policies .......................................................................................................... 70
How IAM Roles Anywhere works with IAM ..................................................................................... 72
Identity-based policy examples ......................................................................................................... 77
Troubleshooting .................................................................................................................................... 80
Using service-linked roles ................................................................................................................... 83
AWS managed policies ........................................................................................................................ 89
Resilience ...................................................................................................................................................... 94
VPC endpoints (AWS PrivateLink) ........................................................................................................... 94
Considerations for IAM Roles Anywhere VPC endpoints .............................................................. 94
Creating an interface VPC endpoint for IAM Roles Anywhere ..................................................... 95
Creating a VPC endpoint policy for IAM Roles Anywhere ............................................................ 95
IPv4 and IPv6 access ................................................................................................................................. 96
What is IPv6? ......................................................................................................................................... 96
Using dual-stack policies ..................................................................................................................... 97
Adding IPv6 to a policy ....................................................................................................................... 97
v
IAM Roles Anywhere User Guide
Verifying your client supports IPv6 .................................................................................................. 99
Monitoring ................................................................................................................................... 101
Customize notiﬁcation settings ............................................................................................................ 101
Notiﬁcation events ............................................................................................................................. 102
Notiﬁcation channels ......................................................................................................................... 102
IAM Roles Anywhere default notiﬁcation settings ...................................................................... 102
Notiﬁcation evaluation criteria ........................................................................................................ 103
Conﬁguring custom notiﬁcation threshold (console) .................................................................. 103
Disabling a notiﬁcation setting (console) ...................................................................................... 104
Monitoring with CloudWatch ................................................................................................................ 104
Monitoring events with Amazon EventBridge ................................................................................... 106
Trust anchor certiﬁcate expiration event ...................................................................................... 106
Intermediate or end-entity certiﬁcate expiration event ............................................................. 107
Responding to an event .................................................................................................................... 107
Monitoring IAM Roles Anywhere notiﬁcations .................................................................................. 108
Aﬀected resources for trust anchor expiry notiﬁcations ............................................................ 108
Aﬀected resources for end-entity certiﬁcate expiry notiﬁcations ............................................ 109
CloudTrail logs .......................................................................................................................................... 109
IAM Roles Anywhere information in CloudTrail ........................................................................... 110
Understanding IAM Roles Anywhere log ﬁle entries ................................................................... 111
Monitoring with IAM Roles Anywhere subjects ................................................................................. 113
AWS CloudFormation resources ................................................................................................. 114
IAM Roles Anywhere and CloudFormation templates ...................................................................... 114
Learn more about CloudFormation ..................................................................................................... 114
Quotas .......................................................................................................................................... 116
Throttling ................................................................................................................................................... 119
Document history ........................................................................................................................ 120
vi

## Step 2: Conﬁgure roles

IAM Roles Anywhere User Guide
What is AWS Identity and Access Management Roles 
Anywhere?
You can use AWS Identity and Access Management Roles Anywhere to obtain temporary security 
credentials in IAM for workloads such as servers, containers, and applications that run outside 
of AWS. Your workloads can use the same IAM policies and IAM roles that you use with AWS 
applications to access AWS resources. Using IAM Roles Anywhere means you don't need to manage 
long-term AWS credentials for workloads running outside of AWS.
To use IAM Roles Anywhere, your workloads must use X.509 certiﬁcates issued by your certiﬁcate 
authority (CA). You register the CA with IAM Roles Anywhere as a trust anchor to establish trust 
between your public-key infrastructure (PKI) and IAM Roles Anywhere. You can also use AWS 
Private Certiﬁcate Authority (AWS Private CA) to create a CA and then use that to establish trust 
with IAM Roles Anywhere. AWS Private CA is a managed private CA service for managing your CA 
infrastructure and your private certiﬁcates. For more information, see What is AWS Private CA.
Topics
• IAM Roles Anywhere concepts
• Accessing IAM Roles Anywhere
IAM Roles Anywhere concepts
Learn the basic terms and concepts used in IAM Roles Anywhere.
• Trust anchors
You establish trust between IAM Roles Anywhere and your certiﬁcate authority (CA) by creating a
trust anchor. A trust anchor is a reference to either AWS Private CA or  an external CA certiﬁcate. 
Your workloads outside of AWS authenticate with the trust anchor using certiﬁcates issued by 
the trusted CA in exchange for temporary AWS credentials. There can be several trust anchors in 
one AWS account. For more information, see IAM Roles Anywhere trust model.
• Roles
An IAM role is an IAM identity that you can create in your account that has speciﬁc permissions. 
A role is intended to be assumable by anyone who needs it. For IAM Roles Anywhere to be able 
to assume a role and deliver temporary AWS credentials, the role must trust the IAM Roles 
IAM Roles Anywhere concepts 1
IAM Roles Anywhere User Guide
Anywhere service principal. A trust anchor is tied to the IAM role via the aws:SourceArn
condition key that uses the trust anchor's ARN as its value in the role's trust policy. For more 
information, see the section called “Role trusts”.
• Proﬁles
To specify which roles IAM Roles Anywhere assumes and what your workloads can do with the 
temporary credentials, you create a proﬁle. In a proﬁle, you can deﬁne IAM session policies, 
which can be managed or inline, to limit the permissions created for a session. A proﬁle can have 
many IAM roles, but only one session policy. Any session returned by a CreateSession call that 
references the proﬁle will have its permissions limited by the session policy.
Note
All IAM Roles Anywhere resources are regional and they must be created in the same 
account and region to be used together.
Account trust boundary
For IAM Roles Anywhere, the trust boundary is established at the account level. This means:
• Certiﬁcates issued by any trust anchor in the account can be used to assume any target role in 
that same account, unless you specify conditions in the role's trust policy.
• There is no automatic integration with organization-wide controls.
Multi-account setups
For information on setting up multi-account access, see: Access for an IAM user in another AWS 
account that you own.
Accessing IAM Roles Anywhere
AWS Management Console
You can manage your IAM Roles Anywhere resources using the IAM Roles Anywhere console.
AWS Command Line Tools
Account trust boundary 2

## Next steps

IAM Roles Anywhere User Guide
You can use the AWS command line tools to issue commands at your system command line to 
perform IAM Roles Anywhere and other AWS tasks. This can be faster and more convenient than 
using the console. The command line tools can be useful if you want to build scripts to perform 
AWS tasks.
AWS provides the AWS Command Line Interface (AWS CLI). For information about installing and 
using the AWS CLI, see the AWS Command Line Interface User Guide .
AWS SDKs
The AWS software development kits (SDKs) consist of libraries and sample code for various 
programming languages and platforms including Java, Python, Ruby, .NET, iOS and Android, and 
others. The SDKs include tasks such as cryptographically signing requests, managing errors, and 
retrying requests automatically. For more information about the AWS SDKs, including how to 
download and install them, see Tools for Amazon Web Services.
Accessing IAM Roles Anywhere 3

## Get temporary security credentials

IAM Roles Anywhere User Guide
Public key infrastructure in IAM Roles Anywhere
AWS Identity and Access Management Roles Anywhere relies on public key infrastructure (PKI) 
to establish trust between your AWS account and certiﬁcate authorities that issue certiﬁcates to 
workloads running in your data centers. PKI involves the generation, distribution, and veriﬁcation 
of digital certiﬁcates through public key encryption. Trust requires either uploading your CA's 
digital certiﬁcate as a trust anchor or referencing an existing AWS Private Certiﬁcate Authority 
(AWS Private CA). Once a trust anchor is created, you can use client certiﬁcates issued by that 
certiﬁcate to authenticate and receive temporary credentials from IAM Roles Anywhere.
Certiﬁcate authorities
Certiﬁcate authorities are entities that are trusted to issue certiﬁcates. The CA issues signed digital 
certiﬁcates that aﬃrm the identity of the certiﬁcate subject and bind that identity to the public key 
contained in the certiﬁcate. The CA signs a certiﬁcate by hashing the contents and then encrypting 
the hash with the private key related to the public key in the certiﬁcate. A client application such 
as a web browser that needs to aﬃrm the identity of a subject uses the public key to verify the 
certiﬁcate signature. It then hashes the certiﬁcate contents and compares the hashed value to the 
decrypted signature to determine whether they match. Certiﬁcates can have constraints on the 
uses of the keys associated with the certiﬁcate. For more information about trust path validation, 
see RFC 5280.
Certiﬁcates
Certiﬁcates, speciﬁcally X.509 certiﬁcates, bind an identity to public key, using a signature 
generated from a corresponding private key.
Key management
PKI uses a pair of keys to perform cryptographic operations such as encryption and generating 
digital signatures. One of the keys is public and is typically made available in an X.509 certiﬁcate. 
The other key is private and should be stored securely. Take care to ensure that your private keys 
are not shared.
Certiﬁcate authorities 4
IAM Roles Anywhere User Guide
Getting started with IAM Roles Anywhere
To use AWS Identity and Access Management Roles Anywhere for authentication to AWS from your 
workloads that run outside of AWS such as servers, containers, and applications, you ﬁrst create a 
trust anchor and proﬁle through the IAM Roles Anywhere console.
You establish trust between IAM Roles Anywhere and your certiﬁcate authority (CA) by creating a
trust anchor. A trust anchor is a reference to either AWS Private Certiﬁcate Authority (AWS Private 
CA) or  an external CA certiﬁcate. You can create trust anchors for each certiﬁcate authority you 
want to trust.
To specify which roles IAM Roles Anywhere assumes and what your workloads can do with the 
temporary credentials, you create a proﬁle. In a proﬁle, you can deﬁne permissions with IAM 
managed policies.
Topics
• Step 1: Establish trust
• Step 2: Conﬁgure roles
• Next steps
Step 1: Establish trust
The ﬁrst step of using IAM Roles Anywhere is creating a trust anchor, which requires you 
to reference a certiﬁcate authority (CA) that IAM Roles Anywhere will use to validate your 
authentication requests. Both root and intermediate CAs can be used as trust anchors. You will 
have to use either a AWS Private CA resource in your account or upload your external CA certiﬁcate. 
Note that CA certiﬁcates that are used as trust anchors have to satisfy certain constraints. For more 
information, see  Signature validation.
To set up a certiﬁcate authority (CA)
• Do one of the following:
• To use a AWS Private CA resource, open the AWS Private CA console. Follow the 
instructions in the AWS Private CA User Guide.
Step 1: Establish trust 5

## Credential Helper on GitHub


## Advanced Features


## OS Certiﬁcate Store Integration

IAM Roles Anywhere User Guide
Important
For AWS Private CA trust anchors, only the validity period can be modiﬁed after 
creation. When the validity period changes, you must call UpdateTrustAnchor to 
register this change. IAM Roles Anywhere honors certiﬁcates based on the validity 
period found during the most recent TrustAnchor Create/Update event.
• To use an external CA, follow the instructions provided by the CA. You provide the 
certiﬁcate body in a later step.
Important
Certiﬁcates issued from public CAs cannot be used as trust anchors.
To create a trust anchor
1. Sign in to the IAM Roles Anywhere console.
2. Choose Create a trust anchor.
3. In Trust anchor name, enter a name for the trust anchor.
4. For Certiﬁcate authority (CA) source, do one of the following:
• To use an AWS Private CA resource, choose AWS Private CA. In the AWS Private CA table, 
choose the AWS Private CA resource.
• To use another CA, choose External certiﬁcate bundle. In External certiﬁcate bundle, 
paste your CA certiﬁcate body. The certiﬁcate must be in Privacy Enhanced Mail (PEM) 
format.
5. (Optional) Customize notiﬁcation settings based on your public key infrastructure. For more 
information, see customize notiﬁcation settings
6. (Optional) Add metadata to the trust anchor by attaching tags as key-value pairs. For more 
information, see Tagging AWS resources.
7. Choose Create a trust anchor.
Step 1: Establish trust 6
IAM Roles Anywhere User Guide
Step 2: Conﬁgure roles
Before you can create an IAM Roles Anywhere proﬁle, you need at least one IAM role that trusts the 
IAM Roles Anywhere service principal. Then you can create a proﬁle that lists the roles IAM Roles 
Anywhere assumes. In a proﬁle, you can also limit the permissions for a created session with IAM 
managed policies.
To conﬁgure a role to trust IAM Roles Anywhere
1. Sign in to the AWS Management Console and open the IAM console at https:// 
console.aws.amazon.com/iam/.
2. On the IAM roles page, choose the role you want to use.
3. On the Trust relationships tab, choose Edit trust policy.
4. Update the trust policy to include rolesanywhere.amazonaws.com as shown below.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Principal": { 
                "Service": [ 
                    "rolesanywhere.amazonaws.com" 
                ] 
            }, 
            "Action": [ 
                "sts:AssumeRole", 
                "sts:TagSession", 
                "sts:SetSourceIdentity" 
            ], 
            "Condition": { 
                "ArnEquals": { 
                    "aws:SourceArn": [ 
                        "arn:aws:rolesanywhere:us-east-1:123456789012:trust-
anchor/TA_ID" 
                    ] 
                }, 
                "StringEquals": { 
Step 2: Conﬁgure roles 7

## PKCS#11 Integration

IAM Roles Anywhere User Guide
                    "aws:PrincipalTag/x509Issuer/CN": "YourCN" 
                } 
            } 
        } 
    ]
}
Important
Without a Condition statement present in a role trust policy, any valid certiﬁcate 
from the CA used as the trust anchor, or CAs subordinate to that trust anchor may be 
used to assume a role via IAM roles anywhere. We recommend you use Condition
statements on both the subject and issuer attributes to ensure that only certiﬁcates 
that you intend to be able to assume a role can do so. For examples, see Trust policy.
For information about editing role trust policies, see Modifying a role (console) in the IAM User 
Guide.
To create a proﬁle
1. Sign in to the IAM Roles Anywhere console.
2. Choose Create a proﬁle.
3. In Proﬁle name, enter a name for the proﬁle.
4. Under Role, choose the role you updated the trust policy for.
5. (Optional) Conﬁgure session policies by choosing up to 10 managed policies or write an inline 
policy.
Session policies limit the permissions for a created session, but do not grant permissions. For 
more information, see Session policies.
6. (Optional) Add metadata to the proﬁle by attaching tags as key–value pairs. For more 
information, see Tagging AWS resources.
7. Choose Create a proﬁle.
Step 2: Conﬁgure roles 8

## TPM Integration

IAM Roles Anywhere User Guide
Next steps
You can now authenticate with IAM Roles Anywhere. Follow the instructions in Get temporary 
security credentials. Also consider Monitoring with IAM Roles Anywhere subjects.
Next steps 9

## Diagnostic Commands

IAM Roles Anywhere User Guide
Get temporary security credentials from IAM Roles 
Anywhere
To obtain temporary security credentials from AWS Identity and Access Management Roles 
Anywhere, use the credential helper tool that IAM Roles Anywhere provides. This tool is compatible 
with the credential_process feature available across the language SDKs. When used with 
an AWS SDK, these credentials automatically refresh before they expire, requiring no additional 
implementation for credential renewal. The helper manages the process of creating a signature 
with the certiﬁcate and calling the endpoint to obtain session credentials; it returns the credentials 
to the calling process in a standard JSON format.
See  Temporary security credentials in IAM  for more information on session credentials.
To download the credential helper tool, use the following links. Releases for Darwin and Windows 
on or after version 1.1.1 are signed.
Platform Architecture Download URL SHA256 checksum
Linux x86-64 https://rolesanywhere.amaz 
onaws.com/releases/1.8.0/ 
X86_64/Linux/Amzn2023/a 
ws_signing_helper
4ec587c4b 
2a7a4b298 
0f0fb084c 
3fabd99a8 
62ce10913 
41ba514ae 
3c0923b905
Windows x86-64 https://rolesanywhere.amaz 
onaws.com/releases/1.8.0/ 
X86_64/Windows/Server202 
2/aws_signing_helper.exe
0ca068266 
38b1d3e80 
46b583c4b 
4c2a9f56b 
e738eb6ed 
bdc44d877 
1a3cc2366b
Darwin x86-64 https://rolesanywhere.amaz 
onaws.com/releases/1.8.0/ 
514d021df 
32b39c78d 
565fbf04d 
10

## Available commands

IAM Roles Anywhere User Guide
Platform Architecture Download URL SHA256 checksum
X86_64/MacOS/Sonoma/aws 
_signing_helper
9a7ed9693 
926824bbf 
3d4fa8b8f 
3ad6b52f13
Linux Aarch64 https://rolesanywhere.amaz 
onaws.com/releases/1.8.0/ 
Aarch64/Linux/Amzn2023/ 
aws_signing_helper
eb1c70b8e 
f8b02326c 
d0f177572 
285d60536 
1920ﬀ22a 
e0876bb41 
72e936f968
Darwin Aarch64 https://rolesanywhere.amaz 
onaws.com/releases/1.8.0/ 
Aarch64/MacOS/Sonoma/aw 
s_signing_helper
a13d8b6be 
18b2031b3 
b900e4349 
ecb8d3012 
76b190988 
a1b599e1d 
70d8067ab0
Important
To get temporary credentials, you need all of the following:
• A Proﬁle conﬁgured in AWS Identity and Access Management Roles Anywhere
• A Role ARN from IAM
• An end-entity certiﬁcate from your certiﬁcate authority
• The certiﬁcate associated private key is required in most cases, except when inferred. For 
example when using OS certiﬁcate stores.
• A trust anchor conﬁgured in IAM Roles Anywhere
11

## Comparison of credential-helper commands


## credential-process command


## Synopsis

IAM Roles Anywhere User Guide
For more information, see Getting started. For detailed examples of using the credential 
helper with the Java SDK, see Using IAM Roles Anywhere credentials.
Credential Helper on GitHub
The source code for the credential helper is available on GitHub so that you can adapt the helper 
to your needs. We encourage you to submit pull requests for changes that you would like to have 
included. However, AWS doesn't provide support for running modiﬁed copies of this software.
Note
You can ﬁnd more modes and options and for credential helper in the README.md.
Advanced Features
The credential helper supports several advanced features for working with diﬀerent types of key 
storage and authentication mechanisms.
OS Certiﬁcate Store Integration
On Windows and macOS, the credential helper can leverage private keys and certiﬁcates stored in 
OS-speciﬁc secure stores:
• Windows: Both CNG and Cryptography APIs are supported. By default, only the user's "MY" 
certiﬁcate store is searched, but you can specify a diﬀerent store using the --system-store-
name option.
• macOS: Keychain Access is supported. The credential helper searches Keychains on the search 
list.
To use certiﬁcates from these stores, use the --cert-selector option instead of providing 
certiﬁcate and private key ﬁles.
Credential Helper on GitHub 12

## Options

IAM Roles Anywhere User Guide
macOS Keychain Integration
For securing keys through macOS Keychain, consider creating a dedicated Keychain that only the 
credential helper can access:
1. Create a new Keychain:
security create-keychain -p ${CREDENTIAL_HELPER_KEYCHAIN_PASSWORD} credential-
helper.keychain
2. Unlock the Keychain:
security unlock-keychain -p ${CREDENTIAL_HELPER_KEYCHAIN_PASSWORD} credential-
helper.keychain
3. Add the Keychain to the search list:
EXISTING_KEYCHAINS=$(security list-keychains | cut -d '"' -f2) security list-
keychains -s credential-helper.keychain $(echo ${EXISTING_KEYCHAINS} | awk -v ORS=" " 
 '{print $1}')
4. Import your certiﬁcate and private key:
security import /path/to/identity.pfx -T /path/to/aws_signing_helper -P 
 ${UNWRAPPING_PASSWORD} -k credential-helper.keychain
Note
Since the oﬃcial credential helper binary is signed, but not notarized, so it isn't trusted 
by macOS by default. You may need to specify your Keychain password whenever the 
credential helper uses the private key, or choose to always allow the credential helper to 
use the Keychain item.
Windows CNG Integration
To use Windows CNG for key storage, import your certiﬁcate and private key into your user's "MY" 
certiﬁcate store:
OS Certiﬁcate Store Integration 13
IAM Roles Anywhere User Guide
certutil -user -p %UNWRAPPING_PASSWORD% -importPFX "MY" \path\to\identity.pfx
You can also use PowerShell cmdlets or Windows CNG/Cryptography APIs to import certiﬁcates.
PKCS#11 Integration
The credential helper supports using certiﬁcates and keys from hardware or software PKCS#11 
tokens and HSMs using PKCS#11 URIs:
• Use a certiﬁcate from a PKCS#11 token:
--certificate 'pkcs11:manufacturer=piv_II;id=%01'
• Use a certiﬁcate by object name:
--certificate 'pkcs11:object=My%20RA%20key'
• Use a certiﬁcate from a ﬁle but the key from a token:
--certificate client-cert.pem --private-key 'pkcs11:model=SoftHSM%20v2;object=My%20RA
%20key'
Most Unix-based systems use p11-kit to provide consistent system-wide and per-user conﬁguration 
of available PKCS#11 providers. For systems or containers that lack p11-kit, you can specify a 
speciﬁc PKCS#11 provider library using the --pkcs11-lib parameter.
If your private key object has the CKA_ALWAYS_AUTHENTICATE attribute set and the
CKU_CONTEXT_SPECIFIC PIN matches the CKU_USER PIN, you can use the --reuse-pin
parameter to avoid being prompted for the PIN multiple times.
Note
For YubiKey devices with PIV support, when a key pair and certiﬁcate exist in slots 9a or 9c, 
the YubiKey automatically generates an attestation certiﬁcate for the slot. To disambiguate 
between your certiﬁcate and the attestation certiﬁcate, use the CKA_LABEL (the object
path attribute in a URI).
PKCS#11 Integration 14

## Output

IAM Roles Anywhere User Guide
TPM Integration
The credential helper supports TPM wrapped keys in the -----BEGIN TSS2 PRIVATE KEY-----
format. You can use such a ﬁle as you would any plain key ﬁle. These ﬁles are supported by both 
TPMv2 OpenSSL engines/providers and GnuTLS.
Important
To use these commands below you must install the tpm2-tools software package. This 
package provides the necessary commands for working with TPM2 devices.
This package is available on many Linux distributions through standard package managers.
To create and use a TPM key with the credential helper:
1. Create a primary key in the TPM owner hierarchy:
tpm2_createprimary -G rsa -g sha256 -p ${TPM_PRIMARY_KEY_PASSWORD} -c parent.ctx -P 
 ${OWNER_HIERARCHY_PASSWORD}
2. Create a child key with the primary key as its parent:
tpm2_create -C parent.ctx -u child.pub -r child.priv -P ${TPM_PRIMARY_KEY_PASSWORD} -
p ${TPM_CHILD_KEY_PASSWORD}
3. Load the child key into the TPM and make it persistent:
tpm2_load -C parent.ctx -u child.pub -r child.priv -c child.ctx -P 
 ${TPM_PRIMARY_KEY_PASSWORD}
CHILD_HANDLE=$(tpm2_evictcontrol -c child.ctx | cut -d ' ' -f 2 | head -n 1)
4. Create a CSR using the TPM key:
openssl req -provider tpm2 -provider default -propquery '?provider=tpm2' \ 
            -new -key handle:${CHILD_HANDLE} \ 
            -out client-csr.pem
5. After obtaining a certiﬁcate from your CA, use it with the credential helper:
./aws_signing_helper credential-process \ 
TPM Integration 15

## Examples

IAM Roles Anywhere User Guide
    --certificate /path/to/certificate/file \ 
    --private-key handle:${CHILD_HANDLE} \ 
    --role-arn ${ROLE_ARN} \ 
    --trust-anchor-arn ${TA_ARN} \ 
    --profile-arn ${PROFILE_ARN}
Important
When using TPM handles, it's your responsibility to clear out the persistent and temporary 
objects from the TPM after you no longer need them. If you load a key into the TPM that 
isn't password-protected, anyone with access to the machine can use that key.
Alternatively, you can use a TPM key ﬁle in the format described in the TSS2 Private Key Format. 
With this approach, the wrapped private key will be loaded into the TPM as a transient object and 
automatically ﬂushed after use.
Note
For RSA keys used with the credential helper, ensure they have the sign attribute set. Some 
tools (like the IBM OpenSSL ENGINE) create RSA keys with the decrypt attribute but not the 
sign attribute by default. The credential helper delegates the signing operation to the TPM 
rather than implementing PKCS#1 v1.5 padding manually.
Diagnostic Commands
The credential helper includes diagnostic commands that can help you troubleshoot issues:
read-certiﬁcate-data
Reads and displays information about a certiﬁcate. This is useful for verifying certiﬁcate details and 
ﬁnding the correct certiﬁcate when multiple certiﬁcates match a selector.
./aws_signing_helper read-certificate-data --certificate /path/to/certificate.pem
Or with a certiﬁcate selector:
Diagnostic Commands 16

## serve command


## Synopsis

IAM Roles Anywhere User Guide
./aws_signing_helper read-certificate-data --cert-selector 
 Key=x509Subject,Value=CN=Subject
If multiple certiﬁcates match a selector, information about each of them is printed. For PKCS#11, 
URIs for each matched certiﬁcate are also printed to help uniquely identify certiﬁcates.
sign-string
Signs a ﬁxed test string to validate your private key and digest conﬁguration:
./aws_signing_helper sign-string --private-key /path/to/private-key.pem
Or with a certiﬁcate selector:
./aws_signing_helper sign-string --cert-selector Key=x509Subject,Value=CN=Subject
Optional parameters include:
• --digest: Must be one of SHA256 (default), SHA384, or SHA512
• --format: Must be one of text (default), json, or bin
Available commands
The credential helper tool provides several commands to help you work with IAM Roles Anywhere. 
This section describes the available commands and their usage.
• credential-process command - Obtains temporary security credentials from IAM Roles Anywhere 
using your certiﬁcate and private key.
• update command - Obtains temporary security credentials from IAM Roles Anywhere and writes 
them directly to the AWS credentials ﬁle.
• serve command - Vends temporary security credentials from IAM Roles Anywhere through a local 
endpoint.
For additional commands and options, see the credential helper README on GitHub.
Available commands 17

## Options


## Behavior

IAM Roles Anywhere User Guide
Comparison of credential-helper commands
Feature credential-process update serve
Automatic credential 
refresh
No (AWS CLI calls for 
each command)
Yes Yes
SDK integration No (requires proﬁle 
setup)
No (requires proﬁle 
setup)
Yes (with environme 
nt variable)
Credentials storage In memory On disk In memory
Best for Single commands AWS CLI usage SDK applications
credential-process command
The credential-process command obtains temporary security credentials from IAM Roles Anywhere 
using your certiﬁcate and private key.
Synopsis
./aws_signing_helper credential-process \ 
    --certificate 
    [--cert-selector] 
    [--endpoint] 
    [--region] 
    [--intermediates] 
    --private-key 
    [--tpm-key-password] 
    [--pkcs11-lib] 
    [--pkcs11-pin] 
    [--reuse-pin] 
    [--system-store-name] 
    [--reuse-latest-expiring-certificate] 
    --profile-arn 
    --role-arn 
    [--session-duration] 
    --trust-anchor-arn 
    [--with-proxy] 
    [--no-verify-ssl] 
Comparison of credential-helper commands 18

## Examples

IAM Roles Anywhere User Guide
    [--role-session-name]
Options
--certificate (string)
Path to certiﬁcate ﬁle. Can also be a PKCS#11 URI (e.g., pkcs11:manufacturer=piv_II;id=
%01) to use certiﬁcates from hardware or software PKCS#11 tokens/HSMs.
--cert-selector (string)
Speciﬁes which certiﬁcate (and associated private key) to use from OS-speciﬁc secure stores. 
On Windows, this searches the user's "MY" certiﬁcate store (or another store speciﬁed with --
system-store-name). On macOS, this searches Keychains on the search list.
The selector can be speciﬁed either through a JSON ﬁle or directly on the command line. It 
allows searching by certiﬁcate Subject, Issuer, and Serial Number using the keys x509Subject,
x509Issuer, and x509Serial.
Example using a JSON ﬁle:
--cert-selector file://path/to/selector.json
Example using command line:
--cert-selector Key=x509Subject,Value=CN=Subject Key=x509Issuer,Value=CN=Issuer 
 Key=x509Serial,Value=15D19632234BF759A32802C0DA88F9E8AFC8702D
--endpoint (string)
The IAM Roles Anywhere endpoint for the region. For a list of endpoints, see Service endpoints 
and quotas.
--region (string)
Signing region.
--intermediates (string)
Path to intermediate certiﬁcate bundle.
--private-key (string)
Speciﬁes the private key to use for signing. This can be:
Options 19

## update command


## Synopsis

IAM Roles Anywhere User Guide
• A Path to a plaintext private key ﬁle
• A PKCS#11 URI (e.g., pkcs11:object=My%20RA%20key)
• A TPM wrapped key ﬁle in the -----BEGIN TSS2 PRIVATE KEY----- format
• A TPM handle reference (e.g., handle:0x81000001)
Not required when using --cert-selector as the private key is inferred from the OS 
certiﬁcate store.
--tpm-key-password (string)
Password for TPM-protected private keys. Required when using password-protected TPM keys.
--pkcs11-lib (string)
Path to a speciﬁc PKCS#11 provider library. Only needed for systems or containers that lack 
p11-kit, otherwise the default p11-kit-proxy provider is used.
--pkcs11-pin (string)
PIN for PKCS#11 token authentication. Required when using PKCS#11 tokens that require 
authentication.
--reuse-pin
Boolean ﬂag to reuse the PKCS#11 user PIN for object-speciﬁc authentication. Useful 
when the private key object has the CKA_ALWAYS_AUTHENTICATE attribute set and the
CKU_CONTEXT_SPECIFIC PIN matches the CKU_USER PIN.
--system-store-name (string)
Windows only: Speciﬁes a system certiﬁcate store other than "MY" (the default) in the
CERT_SYSTEM_STORE_CURRENT_USER context. Only used with --cert-selector.
--reuse-latest-expiring-certificate
Boolean ﬂag to use the latest expiring certiﬁcate when multiple certiﬁcates match a certiﬁcate 
selector. This can be useful when you have multiple valid certiﬁcates and want to use the one 
with the longest remaining validity period.
--profile-arn (string)
Proﬁle to pull policies, attribute mappings and other data from.
--role-arn (string)
Target role to assume.
Options 20
IAM Roles Anywhere User Guide
--session-duration (int)
Duration, in seconds, for the resulting session (corresponds to the durationSeconds
parameter in the CreateSession request). This is optional and can range from 900 seconds 
(15 minutes) up to 43200 seconds (12 hours). Please see the Expiration subsection of 
the Credentials Object section for more details on how this value is used in determining the 
expiration of the vended session.
--trust-anchor-arn (string)
Trust anchor to use for authentication.
--with-proxy
To use the tool with a proxy. This is a boolean ﬂag. Note that you will have to set the
HTTPS_PROXY environment variable with the address of the proxy server.
--no-verify-ssl
To disable SSL veriﬁcation. This is a boolean ﬂag.
Important
Note that this disables TLS host authentication, and can open the connection to man-
in-the-middle attacks. This option should only be used under speciﬁc, tightly controlled 
scenarios, such as debugging proxy connections.
--role-session-name
An identiﬁer for the role session. Please see The relationship between CreateSession and 
AssumeRole section for more details on how this option will aﬀect the CreateSession
operation.
Output
The credential helper tool will return a JSON containing the credentials. This format 
allows the credentials to be consumed by the external credential process supported by the
credential_process.
Output 21
IAM Roles Anywhere User Guide
{ 
    "Version": 1, 
    "AccessKeyId": String, 
    "SecretAccessKey": String, 
    "SessionToken": String, 
    "Expiration": Timestamp
} 
             
Examples
Example Obtain temporary security credentials
Use the following command to get temporary security credentials. Specify the Region where you 
want to make the request.
Important
Before you run this command, make sure you have your certiﬁcate and private key. To get 
these credentials, follow the documentation from your certiﬁcate authority.
$ ./aws_signing_helper credential-process \ 
              --certificate /path/to/certificate \ 
              --private-key /path/to/private-key \ 
              --trust-anchor-arn arn:aws:rolesanywhere:region:account:trust-
anchor/TA_ID \ 
              --profile-arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID \ 
              --role-arn arn:aws:iam::account:role/role-name-with-path
Example Use temporary security credentials with AWS SDKs and the AWS CLI
To use temporary security credentials with AWS SDKs and the AWS CLI, you can conﬁgure the 
credential helper tool as a credential process. For more information, see Sourcing credentials with 
an external process.
The following example shows a the config ﬁle that sets the helper tool as the credential process.
[profile developer] 
    credential_process = ./aws_signing_helper credential-process --certificate /
path/to/certificate --private-key /path/to/private-key --trust-anchor-
Examples 22
IAM Roles Anywhere User Guide
arn arn:aws:rolesanywhere:region:account:trust-anchor/TA_ID --profile-
arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID --role-arn 
 arn:aws:iam::account:role/role-name-with-path
    region = region
For using this proﬁle with any AWS SDK not mentioned below, see 'Set a named proﬁle' from Using 
shared conﬁg and credentials ﬁles to globally conﬁgure AWS SDKs and tools
Example Python SDK
To specify your Roles Anywhere enabled proﬁle for use with Python, see Boto3: Shared credentials 
ﬁle.
Example Java SDK
To specify your Roles Anywhere enabled proﬁle for use with Java, see Java 2.x: Use proﬁles
Example C# SDK
To specify your Roles Anywhere enabled proﬁle for use with C#, see Examples for classes 
SharedCredentialsFile and AWSCredentialsFactory
Example Go SDK
To specify your IAM Roles Anywhere enabled proﬁle for use with Go, see the Specifying Proﬁles 
section in Specifying Credentials
serve command
The serve command vends temporary security credentials from IAM Roles Anywhere through a 
local endpoint running on localhost. This endpoint is compatible with Instance Metadata Service 
(IMDSv2), allowing AWS SDKs to automatically discover and use the credentials without additional 
conﬁguration.
Synopsis
./aws_signing_helper serve \ 
        --certificate 
serve command 23
IAM Roles Anywhere User Guide
        [--cert-selector] 
        [--endpoint] 
        [--region] 
        [--intermediates] 
        --private-key 
        [--tpm-key-password] 
        [--pkcs11-lib] 
        [--pkcs11-pin] 
        [--reuse-pin] 
        [--system-store-name] 
        [--reuse-latest-expiring-certificate] 
        --profile-arn 
        --role-arn 
        [--session-duration] 
        --trust-anchor-arn 
        [--with-proxy] 
        [--no-verify-ssl] 
        [--role-session-name] 
        [--port] 
        [--hop-limit]
Options
The serve command accepts all the options available to the credential-process command, plus the 
following additional options. For details on common options like --cert-selector, --tpm-key-
password, --pkcs11-lib, and others, see the Options section under credential-process.
--port (int)
The port on which the local endpoint will be exposed. Default is 9911.
--hop-limit (int)
The IP TTL (Time To Live) to set on response packets. Default is 64. Setting this to 1 maintains 
parity with EC2's IMDSv2 hop count behavior.
Behavior
When you run the serve command, the credential helper starts a local server that:
• Listens on 127.0.0.1 at the speciﬁed port (default 9911)
• Implements the same URIs and request headers as IMDSv2
Options 24
IAM Roles Anywhere User Guide
• Automatically refreshes credentials ﬁve minutes before the previous set expires
• Continues running until manually terminated
Important
When using the serve command, be aware that any process running on the system that can 
reach 127.0.0.1 will be able to retrieve AWS credentials from the credential helper.
Examples
Example Start a credential server on the default port
$ ./aws_signing_helper serve \ 
                  --certificate /path/to/certificate \ 
                  --private-key /path/to/private-key \ 
                  --trust-anchor-arn arn:aws:rolesanywhere:region:account:trust-
anchor/TA_ID \ 
                  --profile-arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID
 \ 
                  --role-arn arn:aws:iam::account:role/role-name-with-path
Example Start a credential server on a custom port with restricted hop limit
$ ./aws_signing_helper serve \ 
                  --certificate /path/to/certificate \ 
                  --private-key /path/to/private-key \ 
                  --trust-anchor-arn arn:aws:rolesanywhere:region:account:trust-
anchor/TA_ID \ 
                  --profile-arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID
 \ 
                  --role-arn arn:aws:iam::account:role/role-name-with-path \ 
                  --port 8000 \ 
                  --hop-limit 1
Example Use with AWS SDKs
To use the credentials served by the credential helper with AWS SDKs, set the
AWS_EC2_METADATA_SERVICE_ENDPOINT environment variable to point to your local endpoint:
Examples 25
IAM Roles Anywhere User Guide
$ export AWS_EC2_METADATA_SERVICE_ENDPOINT=http://127.0.0.1:9911
Important
Depending on which AWS SDK you are using, the above environment variable must not end 
in a trailing '/' character.
AWS SDKs will use the environment variable and the credentials from this endpoint using their 
credential providers without any changes to application code. The SDKs will request new AWS 
credentials from the credential helper's server as needed.
update command
The update command obtains temporary security credentials from IAM Roles Anywhere and writes 
them directly to the AWS credentials ﬁle. This allows the AWS CLI and SDKs to use the credentials 
without having to call the credential helper for each command.
Synopsis
./aws_signing_helper update \ 
        --certificate 
        [--cert-selector] 
        [--endpoint] 
        [--region] 
        [--intermediates] 
        --private-key 
        [--tpm-key-password] 
        [--pkcs11-lib] 
        [--pkcs11-pin] 
        [--reuse-pin] 
        [--system-store-name] 
        [--reuse-latest-expiring-certificate] 
        --profile-arn 
        --role-arn 
        [--session-duration] 
        --trust-anchor-arn 
        [--with-proxy] 
        [--no-verify-ssl] 
update command 26
IAM Roles Anywhere User Guide
        [--role-session-name] 
        [--profile] 
        [--once]
Options
The update command accepts all the options available to the credential-process command, plus 
the following additional options. For details on common options like --cert-selector, --tpm-
key-password, --pkcs11-lib, and others, see the Options section under credential-process.
--profile (string)
The named proﬁle in the AWS credentials ﬁle to update. If not speciﬁed, the default proﬁle will 
be updated. If the proﬁle doesn't exist, it will be created.
--once
Update the credentials only once and then exit. If not speciﬁed, the command will continuously 
update the credentials before they expire.
Behavior
When you run the update command, the credential helper:
• Obtains temporary security credentials from IAM Roles Anywhere
• Writes the credentials directly to the AWS credentials ﬁle (~/.aws/credentials)
• Unless the --once ﬂag is speciﬁed, automatically refreshes the credentials approximately ﬁve 
minutes before they expire
• Continues running until manually terminated (unless --once is speciﬁed)
Important
When using the update command, be aware that the credentials are written to a ﬁle on 
disk. Any user or process who can read the credentials ﬁle may be able to read and use 
those AWS credentials.
Options 27
IAM Roles Anywhere User Guide
Note
Running the update command multiple times simultaneously, creating multiple processes, 
may not work as intended. There may be issues with concurrent writes to the credentials 
ﬁle.
Examples
Example Update the default proﬁle continuously
$ ./aws_signing_helper update \ 
                  --certificate /path/to/certificate \ 
                  --private-key /path/to/private-key \ 
                  --trust-anchor-arn arn:aws:rolesanywhere:region:account:trust-
anchor/TA_ID \ 
                  --profile-arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID
 \ 
                  --role-arn arn:aws:iam::account:role/role-name-with-path
Example Update a named proﬁle once
$ ./aws_signing_helper update \ 
                  --certificate /path/to/certificate \ 
                  --private-key /path/to/private-key \ 
                  --trust-anchor-arn arn:aws:rolesanywhere:region:account:trust-
anchor/TA_ID \ 
                  --profile-arn arn:aws:rolesanywhere:region:account:profile/PROFILE_ID
 \ 
                  --role-arn arn:aws:iam::account:role/role-name-with-path \ 
                  --profile developer \ 
                  --once
Example Use with AWS CLI
After running the update command, you can use the AWS CLI with the updated proﬁle:
$ aws s3 ls --profile developer
If you updated the default proﬁle, you don't need to specify the proﬁle:
Examples 28
IAM Roles Anywhere User Guide
$ aws s3 ls
Example Use with JavaScript SDK
To specify your Roles Anywhere enabled proﬁle for use with JavaScript, see Loading Credentials in 
Node.js from the Shared Credentials File
Credential Helper Changelog
CredentialHelper version 1.8.0
On March 5, 2026, AWS IAM Roles Anywhere released Credential Helper version 1.8.0. As a part of 
this release, ML-DSA signatures are now supported, the PKCS#11 dynamic linking issue has been 
ﬁxed, and several security vulnerabilities have been patched.
CredentialHelper version 1.7.3
On January 7, 2026, AWS IAM Roles Anywhere released Credential Helper version 1.7.3. As a part 
of this release, some security vulnerabilities were patched.
CredentialHelper version 1.7.2
On November 24, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.2. As 
a part of this release, some security vulnerabilities were patched and some error messages were 
improved.
CredentialHelper version 1.7.1
On August 12, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.1. As part of 
this release, some security vulnerabilities were patched.
CredentialHelper version 1.7.0
On Jun 2, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.0. As part of this 
release, a bug was ﬁxed that prevented adding custom roots for use in TLS, and an enhancement 
was introduced to make parsing logic more robust for cert selectors provided through the CLI. 
Credential Helper Changelog 29
IAM Roles Anywhere User Guide
Dependency module versions were also upgraded to address any vulnerabilities picked up by 
scanners.
CredentialHelper version 1.6.0
On May 6, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.6.0. As part of 
this release, password-protected private keys in PKCS#8 format are now supported, and a ﬁx was 
introduced for a bug where the credential helper opened terminal device ﬁles when the process 
didn't have a controlling terminal.
CredentialHelper version 1.5.0
On April 3, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.5.0. As a part 
of this release, an option was added to use the latest expiring certiﬁcate when multiple match a 
certiﬁcate selector, and some minor ﬁxes were introduced related to PKCS#12 ﬁle support.
CredentialHelper version 1.4.0
On December 13, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.4.0. As a 
part of this release, TPM keys are now supported on Windows systems.
CredentialHelper version 1.3.0
On November 13, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.3.0. As a 
part of this release, TPM keys are supported for non-Windows systems, and a previously unhandled 
error when parsing certiﬁcate data from a ﬁle was ﬁxed.
CredentialHelper version 1.2.1
On October 22, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.2.1. As a part 
of this release, some security vulnerabilities were patched.
CredentialHelper version 1.2.0
On August 23, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.2.0. As a 
part of this release, custom role session name is supported in the CreateSession request, a hop 
limit option is supported to limit the IP TTL on response packets for the serve command, and ﬁle 
updates for certiﬁcate and private key data are recognized by long-running commands and will be 
honored in subsequent credentialing requests.
CredentialHelper version 1.6.0 30
IAM Roles Anywhere User Guide
CredentialHelper version 1.1.1
On October 12, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.1.1. As a 
part of this release, providers in Windows are attempted to be silenced when performing signing 
operations. Also, Windows user certiﬁcate store names can now be explicitly provided.
CredentialHelper version 1.1.0
On September 20, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.1.0. As 
a part of this release, PKCS#11 module integration is now supported. Also, any debug logs that 
previously went to stderr now go to stdout.
CredentialHelper version 1.0.6
On August 16, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.6. As a part 
of this release, certiﬁcates within OS secure stores that can't be parsed are now skipped. An issue 
relating to mismatched regions in the ARN inputs is also now ﬁxed.
CredentialHelper version 1.0.5
On July 25, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.5. As a part 
of this release, some bugs relating to the update command were ﬁxed. PKCS#12 containers that 
aren't password-protected are now supported. Lastly, MacOS Keychain Access and Windows CNG/
CryptoAPI integrations are also now supported.
CredentialHelper version 1.0.4
On January 17, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.4. As a part 
of this release, some bugs speciﬁc to the serve command were ﬁxed.
CredentialHelper version 1.0.3
On December 5, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.3. As a part 
of this release, the tool now supports the update and serve commands.
CredentialHelper version 1.0.2
On September 8, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.2. As a 
part of this release, the tool now sets the minimum TLS version to 1.2.
CredentialHelper version 1.1.1 31
IAM Roles Anywhere User Guide
CredentialHelper version 1.0.1
On July 14, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.1. As a part of 
this release, the tool now has better error handling.
CredentialHelper version 1.0.1 32
IAM Roles Anywhere User Guide
The IAM Roles Anywhere trust model
AWS Identity and Access Management Roles Anywhere works by bridging the trust model of IAM 
and Public Key Infrastructure (PKI). The model connects the role, the IAM Roles Anywhere service 
principal, and identities encoded in X.509 certiﬁcates, that are issued by a Certiﬁcate Authority 
(CA).
Role trusts
To use an IAM role with IAM Roles Anywhere, you must create a trust relationship with the 
IAM Roles Anywhere service principal rolesanywhere.amazonaws.com. To create the trust 
relationship, you create a   trust policy, a JSON policy document. The policy must grant the 
permissions:
• sts:AssumeRole
• sts:SetSourceIdentity
• sts:TagSession
Sessions issued by IAM Roles Anywhere have the source identity set to the common name(s) 
(CN) of the subject(s) you use in end-entity certiﬁcate(s) authenticating to the target role. IAM 
Roles Anywhere extracts values from the subject, issuer, and Subject Alternative Name (SAN) 
ﬁelds of the authenticating certiﬁcate and makes them available for policy evaluation via the 
sourceIdentity and principal tags. The sts:SourceIdentity key is present in the request when IAM 
Roles Anywhere initially sets the source identity while assuming a role. You can apply more 
authorization constraints by using condition clauses in the policy statement. The tags will also be 
evaluated against policies on any resources accessed with the issued session.
Additionally, sessions issued by AWS have a Session Name property that is used as part of the 
assumed role ARN. IAM Roles Anywhere sets this automatically, using the hex-encoded serial 
number of the authenticating certiﬁcate.
To examine the contents of a certiﬁcate, use the following command:
$openssl x509 -text -noout -in certificate.pem
      Certificate: 
Role trusts 33
IAM Roles Anywhere User Guide
      Data: 
          Version: 3 (0x2) 
          Serial Number: 
              1f:71:c5:11:4a:11:9f:c0:cc:5a:5a:52:fb:37:20:ad 
      Signature Algorithm: sha256WithRSAEncryption 
          Issuer: C=US, O=Amazon, OU=IAM, ST=Washington, CN=Roles Anywhere, L=Seattle 
          Validity 
              Not Before: Apr 20 14:13:43 2022 GMT 
              Not After : Jan 10 15:13:43 2023 GMT 
          Subject: CN=awsUser 
          # remainder omitted...
In this case, the value awsUser becomes the source identity. The values from the Issuer ﬁeld 
become principal tags in the resulting session.
For more information, see:
• IAM roles
• IAM roles terms and concepts: trust policy
• Policies and permissions in IAM
• Things to know about source identity
• Passing session tags in AWS Security Token Service
Signature validation
To authenticate a request for credentials, IAM Roles Anywhere validates the incoming signature by 
using the signature validation algorithm required by the key type of the certiﬁcate, for example 
RSA or ECDSA. After validating the signature, IAM Roles Anywhere checks that the certiﬁcate 
was issued by a certiﬁcate authority conﬁgured as a trust anchor in the account using algorithms 
deﬁned by public key infrastructure X.509 (PKIX) standards.
End entity certiﬁcates must satisfy the following constraints to be used for authentication:
• The certiﬁcates MUST be X.509v3.
• If the CA ﬁeld is present in the basic constraints extension, its value MUST be false.
• The key usage MUST include Digital Signature.
• The signing algorithm MUST include SHA256 or stronger. MD5 and SHA1 signing algorithms are 
rejected.
Signature validation 34
IAM Roles Anywhere User Guide
Certiﬁcates used as trust anchors must satisfy the same requirements for signature algorithm, but 
with the following diﬀerences:
• The key usage MUST include Certificate Sign, and MAY include CRL Sign. Certiﬁcate 
Revocation Lists (CRLs) are an optional feature of IAM Roles Anywhere.
• Basic constraints MUST include CA: true.
Important
For AWS Private CA trust anchors, only the validity period can be modiﬁed after creation. 
When the validity period changes, you must call UpdateTrustAnchor to register this change. 
IAM Roles Anywhere honors certiﬁcates based on the validity period found during the most 
recent TrustAnchor Create/Update event.
Trust policy
Temporary credentials for IAM roles are issued to IAM Roles Anywhere clients via the API method
CreateSession. For the call to be authorized, the target role of the CreateSession API call 
must have an Assume Role Policy Document to trust the IAM Roles Anywhere service principal 
(rolesanywhere.amazonaws.com).
Important
It is also recommended to have additional condition statements to further restrict 
authorization based on attributes that are extracted from the X.509 certiﬁcate.
When you use X.509 certiﬁcates, IAM Roles Anywhere extracts the following ﬁelds and makes them 
available as PrincipalTag elements in the session:
• Subject
• Issuer
• Subject Alternative Name (SAN)
Trust policy 35
IAM Roles Anywhere User Guide
These values need to match the pattern deﬁned in STS session tags. The service ignores values that 
do not match this pattern. You cannot use these values in policy conditions.
Note
These tags are also available to be used in conditions in the identity-based policy attached 
to the role.
Certiﬁcate Subject ﬁelds mapping
IAM Roles Anywhere maps Relative Distinguished Names (RDNs) from an authenticating 
certiﬁcate's Subject into distinct PrincipalTag elements in the session.
The following example shows a trust policy that adds a condition based on the Subject Common 
Name (CN) of the certiﬁcate. For example, if the identity asserted in the certiﬁcate is Alice, a 
condition can be created on the CN of the Subject.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Principal": { 
          "Service": "rolesanywhere.amazonaws.com" 
        }, 
        "Action": [ 
          "sts:AssumeRole", 
          "sts:TagSession", 
          "sts:SetSourceIdentity" 
        ], 
        "Condition": { 
          "StringEquals": { 
            "aws:PrincipalTag/x509Subject/CN": "Alice" 
          }, 
          "ArnEquals": { 
            "aws:SourceArn": [ 
              "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
            ] 
Trust policy 36
IAM Roles Anywhere User Guide
          } 
        } 
      } 
    ] 
  }
Certiﬁcate Issuer ﬁelds mapping
IAM Roles Anywhere maps RDNs from an authenticating certiﬁcate’s Issuer into distinct
PrincipalTag elements in the session.
The following example shows a trust policy that adds a condition based on the Issuer Common 
Name (CN) of the certiﬁcate. For example, if the issuer identity asserted in the certiﬁcate is Bob, a 
condition can be created on the CN of the Issuer.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Principal": { 
          "Service": "rolesanywhere.amazonaws.com" 
        }, 
        "Action": [ 
          "sts:AssumeRole", 
          "sts:TagSession", 
          "sts:SetSourceIdentity" 
        ], 
        "Condition": { 
          "StringEquals": { 
            "aws:PrincipalTag/x509Issuer/CN": "Bob" 
          }, 
          "ArnEquals": { 
            "aws:SourceArn": [ 
              "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
            ] 
          } 
        } 
      } 
Trust policy 37
IAM Roles Anywhere User Guide
    ] 
  }
Certiﬁcate Subject Alternative Name (SAN) ﬁelds mapping
X.509v3 certiﬁcates may include an extension to deﬁne additional identities, call Subject 
Alternative Names (SANs). The SAN can have multiple values, each of which can be one of 
nine types – Domain Name System (DNS) names, Uniform Resource Indicators (URIs), Directory 
Names, IP addresses, "Other" names, EDI party names, X400 addresses, RFC 822 names, or 
registered OIDs. IAM Roles Anywhere will map the ﬁrst value of the following types: DNS Names,
Directory Name (DN), and URI Names. The resulting tags will be preﬁxed with x509SAN, with 
a corresponding type code. The type code will be one of DNS, URI, or Name. For values of type DN, 
the individual RDNs will be parsed, as with Subject and Issuer.
      Certificate: 
      Data: 
          Version: 3 (0x2) 
          Serial Number: 
              1f:71:c5:11:4a:11:9f:c0:cc:5a:5a:52:fb:37:20:ad 
      Signature Algorithm: sha256WithRSAEncryption 
          Issuer: C=US, O=Amazon, OU=IAM, ST=Washington, CN=RolesAnywhere, L=Seattle 
          Validity 
              Not Before: Apr 20 14:13:43 2022 GMT 
              Not After : Jan 10 15:13:43 2023 GMT 
          Subject: CN=Alice 
          X509v3 extensions: 
            X509v3 Subject Alternative Name: 
                DNS:example.com, 
                URI:spiffe://example.com/workload/alice, 
                DirName:/CN=Alice 
          # remainder omitted...
For the above certiﬁcate, the session principal tags and the SAN ﬁelds will look like the following:
        "aws:PrincipalTag/x509Subject/CN": "Alice", 
        "aws:PrincipalTag/x509Issuer/C": "US", 
        "aws:PrincipalTag/x509Issuer/O": "Amazon", 
        "aws:PrincipalTag/x509Issuer/OU": "IAM", 
        "aws:PrincipalTag/x509Issuer/ST": "Washington", 
        "aws:PrincipalTag/x509Issuer/L": "Seattle", 
        "aws:PrincipalTag/x509Issuer/CN": "RolesAnywhere", 
Trust policy 38
IAM Roles Anywhere User Guide
        "aws:PrincipalTag/x509SAN/DNS": "example.com", 
        "aws:PrincipalTag/x509SAN/URI": "spiffe://example.com/workload/alice", 
        "aws:PrincipalTag/x509SAN/Name/CN": "Alice" 
        // Additional principal tags may be available...
Some X.509 certiﬁcate ﬁelds can contain multiple values. For example, a Subject can have multiple 
Organization Unit (OU) values in the certiﬁcate. Because principal tags do not support multiple 
values, IAM Roles Anywhere combines multiple values into a single string, separating them with 
forward slashes (/) in the order they appear in the certiﬁcate.
For example, consider a certiﬁcate with these Subject values:
CN=alice, OU=Security, OU=Engineering, OU=Research
IAM Roles Anywhere creates the following principal tag:
"aws:PrincipalTag/x509Subject/OU": "Security/Engineering/Research"
This same behavior applies to any certiﬁcate ﬁeld that contains multiple values. The order of values 
in the principal tag matches their order in the certiﬁcate.
The following example shows a trust policy that adds a condition based on the SAN ﬁelds of the 
certiﬁcate.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Principal": { 
          "Service": "rolesanywhere.amazonaws.com" 
        }, 
        "Action": [ 
          "sts:AssumeRole", 
          "sts:TagSession", 
          "sts:SetSourceIdentity" 
        ], 
        "Condition": { 
Trust policy 39
IAM Roles Anywhere User Guide
          "StringEquals": { 
            "aws:PrincipalTag/x509SAN/DNS": "example.com", 
            "aws:PrincipalTag/x509SAN/URI": "spiffe://example.com/workload/
alice", 
            "aws:PrincipalTag/x509SAN/Name/CN": "Alice" 
          }, 
          "ArnEquals": { 
            "aws:SourceArn": [ 
              "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
            ] 
          } 
        } 
      } 
    ] 
  }
Note
RFC 5280 allows certiﬁcates with empty subjects if and only if the SAN extension is present 
and marked critical. Certiﬁcates with empty subjects are NOT yet supported, since IAM 
Roles Anywhere uses the certiﬁcate subject as the key of the Subject resource to visualize 
and audit activities for certiﬁcates that are authenticated with IAM Roles Anywhere. 
For more information about Subject resource, see Monitoring with IAM Roles Anywhere 
subjects.
Using the aws:SourceArn or aws:SourceAccount or sts:SourceIdentity condition keys
In general, it is strongly recommended that you use the aws:SourceArn or the aws:SourceAccount
global condition keys or the sts:SourceIdentity condition key in your role trust policies. This 
combination of conditions implements least privilege permissions and prevents IAM Roles 
Anywhere from acting as a potential confused deputy. When a client obtains temporary security 
credentials from IAM Roles Anywhere, the aws:SourceArn and aws:SourceAccount will be set 
based on the ARN of the trust anchor speciﬁed in the call to CreateSession.
To use the aws:SourceArn and aws:SourceAccount global condition keys, set the value 
to the Amazon Resource Name (ARN) or account of the trust anchor that you expect to use for 
authentication. As an example, consider the following role trust policy.
Trust policy 40
IAM Roles Anywhere User Guide
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Principal": { 
          "Service": "rolesanywhere.amazonaws.com" 
        }, 
        "Action": [ 
          "sts:AssumeRole", 
          "sts:TagSession", 
          "sts:SetSourceIdentity" 
        ], 
        "Condition": { 
          "ArnEquals": { 
            "aws:SourceArn": [ 
              "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
            ] 
          }, 
          "StringEquals": { 
            "aws:PrincipalTag/x509Issuer/CN": "YourCN" 
          } 
        } 
      } 
    ] 
  }
To use the sts:SourceIdentity condition key, set the source identity preﬁx and source identity 
value according to the following rules. As an example, consider the following role trust policy.
JSON
{ 
  "Version":"2012-10-17",        
  "Statement": [ 
    { 
      "Effect": "Allow", 
Trust policy 41
IAM Roles Anywhere User Guide
      "Principal": { 
        "Service": "rolesanywhere.amazonaws.com" 
      }, 
      "Action": [ 
        "sts:AssumeRole", 
        "sts:SetSourceIdentity" 
      ], 
      "Condition": { 
        "StringEquals": { 
          "sts:SourceIdentity": [ 
            "${sourceIdentityPrefix}${sourceIdentityValue}" 
          ] 
        }, 
        "ArnEquals": { 
          "aws:SourceArn": [ 
            "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
          ] 
        } 
      } 
    }, 
    { 
      "Effect": "Allow", 
      "Principal": { 
        "Service": "rolesanywhere.amazonaws.com" 
      }, 
      "Action": [ 
        "sts:TagSession" 
      ], 
      "Condition": { 
        "StringEquals": { 
          "aws:PrincipalTag/x509Issuer/CN": "YourCN" 
        } 
      } 
    } 
  ]
}
Trust policy 42
IAM Roles Anywhere User Guide
Certiﬁcate attribute mapping
IAM Roles Anywhere provides you with the capability to deﬁne a custom set of mapping rules, 
enabling you to specify which data are extracted from authenticating certiﬁcates as session tags 
for authorization policies. These customized attribute mappings are associated with a proﬁle.
Attributes are data elements that come from speciﬁc ﬁelds in the certiﬁcate. You can use speciﬁers 
to represent one or more attributes.
Note
For information about session tag quotas, see Session tagging operations.
Topics
• Default mapping behavior
• Put attribute mappings
• Delete attribute mappings
• Attribute mapping and trust policy
Default mapping behavior
The following attributes are mapped by default when you create a proﬁle. The default mapping 
rules are as follows:
• x509Subject: maps all supported Relative Distinguished Names (RDNs) from an authenticating 
certiﬁcate's Subject into distinct PrincipalTag elements in the session.
• x509Issuer: maps all supported Relative Distinguished Names (RDNs) from an authenticating 
certiﬁcate's Issuer into distinct PrincipalTag elements in the session.
• x509SAN (Subject Alternative Name): maps the  ﬁrst value of the following types: DNS 
Names, Directory Name (DN), and URI Names
To view your current mappings associated with a proﬁle, using the following command:
$ aws rolesanywhere get-profile --profile-id PROFILE_ID
Certiﬁcate attribute mapping 43
IAM Roles Anywhere User Guide
Default mapping rules in a JSON format:
"attributeMappings": [ 
  { 
    "mappingRules": [ 
        { 
            "specifier": "*" 
        } 
    ], 
    "certificateField": "x509Issuer" 
  }, 
  { 
    "mappingRules": [ 
        { 
            "specifier": "DNS" 
        }, 
        { 
            "specifier": "URI" 
        }, 
        { 
            "specifier": "Name/*" 
        } 
    ], 
    "certificateField": "x509SAN" 
  }, 
  { 
    "mappingRules": [ 
        { 
            "specifier": "*" 
        } 
    ], 
    "certificateField": "x509Subject" 
  }
]
Note
If you see * as a speciﬁer, it signiﬁes the default behavior, which maps all recognizable 
RDNs for x509Subject, x509Issuer and x509SAN/Name. However, * does not have 
a deﬁned behavior in the context of x509SAN/URI, x509SAN/DNS, or x509SAN/. The 
speciﬁer Name/ represents the ﬁrst recognizable attribute of the Directory Name. Both
Default mapping behavior 44
IAM Roles Anywhere User Guide
Name and Name/ are equivalent to Name/* and will be displayed as Name/*in the mapping 
rule.
Put attribute mappings
Put attribute mappings (command line interface)
put-attribute-mapping enables you to attach new mapping rules to your proﬁle. When using 
that proﬁle, the certiﬁcate mapping behavior changes according to your customized rules.
To put a mapping rule, using the following command:
$aws rolesanywhere put-attribute-mapping \ 
        --certificate-field CERTIFICATE_FIELD \ 
        --mapping-rules specifier=SPECIFIER \ 
        --profile-id PROFILE_ID
The CERTIFICATE_FIELD can be in one of x509Subject, x509Issuer and x509SAN. The
SPECIFIER is a string enforced by a standard (for example, OID) that can map to a piece of 
information encoded in the certiﬁcate.
For example, to add mapping rules for x509Subject/CN and x509Subject/OU, use the following 
command:
$aws rolesanywhere put-attribute-mapping \ 
        --certificate-field x509Subject \ 
        --mapping-rules specifier=CN specifier=OU \ 
        --profile-id PROFILE_ID
Put attribute mappings (console)
1. Sign in to IAM Roles Anywhere console.
2. Scroll to ﬁnd proﬁle table and choose the proﬁle to add certiﬁcate attribute mappings.
3. Within proﬁle detail page scroll towards Certiﬁcate attribute mappings section and choose
Manage mappings.
4. Scroll to ﬁnd the Add mappings button and click on it.
5. Choose a certiﬁcate ﬁeld from either Subject, Issuer, or Subject Alternative Name in 
the dropdown list, and enter the speciﬁer
Put attribute mappings 45
IAM Roles Anywhere User Guide
6. Select Save changes to add attribute mappings.
Delete attribute mappings
Delete attribute mappings (command line interface)
delete-attribute-mapping enables you to delete mapping rules from your proﬁle. When 
using that proﬁle, the attribute speciﬁed by the deleted mapping rule will not be mapped from a 
certiﬁcate.
To delete a mapping rule, using the following command:
$aws rolesanywhere delete-attribute-mapping \ 
        --certificate-field CERTIFICATE_FIELD \ 
        --specifiers SPECIFIERS \ 
        --profile-id PROFILE_ID
The CERTIFICATE_FIELD can be in one of x509Subject, x509Issuer and x509SAN. The
SPECIFIER is a string enforced by a standard (for example, OID) that exists in your current 
mapping rules.
For example, to delete mapping rules for x509Subject/CN and x509Subject/OU, use the 
following command:
$aws rolesanywhere delete-attribute-mapping \ 
        --certificate-field x509Subject \ 
        --specifiers CN OU \ 
        --profile-id PROFILE_ID
Delete attribute mappings (console)
1. Sign in to IAM Roles Anywhere console.
2. Scroll to ﬁnd proﬁle table and choose the proﬁle to remove certiﬁcate attribute mappings.
3. Within proﬁle detail page scroll towards Certiﬁcate attribute mappings section and choose
Manage mappings.
4. Scroll to ﬁnd the corresponding attribute mapping row and click on Remove mapping button 
associated with it.
5. Select Save changes to remove attribute mappings.
Delete attribute mappings 46
IAM Roles Anywhere User Guide
Attribute mapping and trust policy
It is recommended to have condition statements in the Assume Role Policy Document to restrict 
authorization based on attributes that are extracted from an end-entity X.509 certiﬁcate. For more 
information about the role trust policy, see Trust policy.
The attribute mapping ﬁeld of a proﬁle controls which attributes from an authenticating X.509 
certiﬁcate will be mapped for principal tags. Therefore, while adding condition statements to 
an Assume Role Policy Document, be cautious that the speciﬁers used in mapping rules for 
authorization need to be mapped accordingly.
The following example shows trust policies that add a condition based on the Issuer Common 
Name (CN) of the certiﬁcate.
JSON
{ 
  "Version":"2012-10-17",        
  "Statement": [ 
    { 
      "Effect": "Allow", 
      "Principal": { 
        "Service": "rolesanywhere.amazonaws.com" 
      }, 
      "Action": [ 
        "sts:AssumeRole", 
        "sts:TagSession", 
        "sts:SetSourceIdentity" 
      ], 
      "Condition": { 
        "StringEquals": { 
          "aws:PrincipalTag/x509Issuer/CN": "Bob" 
        }, 
        "ArnEquals": { 
          "aws:SourceArn": [ 
            "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
          ] 
        } 
      } 
    } 
  ]
Attribute mapping and trust policy 47
IAM Roles Anywhere User Guide
}
If a proﬁle is used with an Attribute Mapping ﬁeld that lacks specifier: CN or specifier: *
in the mappingRules for x509Issuer, the ﬁrst condition in the Assume Role Policy Document will 
evaluate as false because there will be no value mapped aws:PrincipalTag/x509Issuer/CN.
JSON
{ 
  "Version":"2012-10-17",        
  "Statement": [ 
    { 
      "Effect": "Allow", 
      "Principal": { 
        "Service": "rolesanywhere.amazonaws.com" 
      }, 
      "Action": [ 
        "sts:AssumeRole", 
        "sts:TagSession", 
        "sts:SetSourceIdentity" 
      ], 
      "Condition": { 
        "StringNotEquals": { 
          "aws:PrincipalTag/x509Issuer/CN": "Bob" 
        }, 
        "ArnEquals": { 
          "aws:SourceArn": [ 
            "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TA_ID" 
          ] 
        } 
      } 
    } 
  ]
}
Likewise, if the condition is StringNotEquals, the condition will evaluate to true using the same 
proﬁle. This happens because the condition is disregarded when the principal tag is dropped due to 
attribute mapping APIs.
Attribute mapping and trust policy 48
IAM Roles Anywhere User Guide
Having the Attribute Mapping ﬁeld provided below in a proﬁle, the StringEquals condition for
x509Issuer/CN will assess to false, or the StringNotEquals condition will assess to true.
"attributeMappings": [ 
  { 
    "mappingRules": [ 
        { 
            "specifier": "O" 
        } 
    ], 
    "certificateField": "x509Issuer" 
  }, 
  { 
    "mappingRules": [ 
        { 
            "specifier": "DNS" 
        }, 
        { 
            "specifier": "URI" 
        }, 
        { 
            "specifier": "Name/*" 
        } 
    ], 
    "certificateField": "x509SAN" 
  }, 
  { 
    "mappingRules": [ 
        { 
            "specifier": "*" 
        } 
    ], 
    "certificateField": "x509Subject" 
  }
]
Source identity rules
We deﬁne a source identity preﬁx as follows:
• "CN=": the common name of the subject in the certiﬁcate is set and less than or equal to 61 
characters.
Source identity rules 49
IAM Roles Anywhere User Guide
• "ID=": the common name of the subject in the certiﬁcate is not set. This value is left-padded 
with zero to be even in length.
• "": (empty string) the common name of the subject in the certiﬁcate is set and has a length from 
62 to 64 characters.
Hex encoding example:
• Decimal serial number 291 converts to hex 123, which becomes ID=0123
• Decimal serial number 17767 converts to hex 4567, which becomes ID=4567
Revocation
Certiﬁcate revocation is supported through the use of imported certiﬁcate revocation lists (CRLs). 
Currently, certiﬁcation revocation is only supported by the API and CLI. You can import a CRL that 
is generated from your CA using ImportCrl API or import-crl CLI command. Certiﬁcates used 
for authentication will be checked for their revocation status.
Callbacks to CRL Distribution Points (CDPs) or Online Certiﬁcate Status Protocol (OCSP) endpoints 
are not supported.
Revocation 50
IAM Roles Anywhere User Guide
The IAM Roles Anywhere authentication process
To provide credentials, AWS Identity and Access Management Roles Anywhere uses the IAM 
Roles Anywhere CreateSession API. The API authenticates requests with a signature using keys 
associated with the X.509 certiﬁcate, which was used for authentication. It acts like AssumeRole – 
exchanging the signature for a standard SigV4-compatible session credential.
To successfully authenticate, the following constraints must be satisﬁed:
• The signature attached to the request MUST be validated against the signing certiﬁcate (also 
attached to the request).
• The signing certiﬁcate MUST have a valid trust chain to a Certiﬁcate Authority (CA) certiﬁcate 
conﬁgured in the customer account.
• The target role for which credentials are issued MUST have an AssumeRolePolicyDocument
that allows IAM Roles Anywhere service principal, rolesanywhere.amazonaws.com, to call
sts:AssumeRole, sts:TagSession, and sts:SetSourceIdentity. For more information, 
see Granting permissions to pass a role to a service in the IAM User Guide.
• The target role for which credentials are issued MAY have additional Condition predicates in 
the AssumeRolePolicyDocument that restrict authorization based on attributes extracted 
from the X.509 Certiﬁcate (for example, Subject or Issuer).
The signature uses the same canonicalization mechanism as AWS Signature V4 for API requests
(SigV4), with the following changes and additions:
• The private key used to sign the request MUST be bound to an X.509 Certiﬁcate.
• The signing certiﬁcate MUST be a v3 certiﬁcate.
• The signing certiﬁcate MUST be attached to the request via the header X-Amz-X509, as Base64-
encoded Distinguished Encoding Rules (DER) data.
• The relevant headers – X-Amz-X509 and X-Amz-X509-Chain (if applicable) MUST be included 
in the signed headers ﬁeld of the Authorization header.
• The X-Amz-X509-Chain header MUST be encoded as comma-delimited, base64-encoded DER.
• The X-Amx-X509-Chain header MUST NOT exceed the maximum depth of 5 certiﬁcates.
• The signing certiﬁcate's serial number MUST be included in the Credential portion of the Scope 
ﬁeld of the Authorization header.
51
IAM Roles Anywhere User Guide
RSA, EC and ML-DSA keys are supported; RSA keys are used with the RSA PKCS#1 v1.5 signing 
algorithm. EC keys are used with the ECDSA. ML-DSA keys can be used with ML-DSA-44, ML-
DSA-65 or ML-DSA-87.
Topics
• IAM Roles Anywhere CreateSession API
• The IAM Roles Anywhere authentication signing process
IAM Roles Anywhere CreateSession API
The CreateSession API returns temporary security credentials for workloads that have been 
authenticated with IAM Roles Anywhere to access AWS resources. For endpoints, see Roles 
Anywhere Endpoints and Quotas. To get temporary security credentials through this API, see Get 
temporary security credentials from IAM Roles Anywhere
Request Syntax
    POST /sessions HTTP/1.1 
    Content-type: application/json 
    { 
      "durationSeconds": number,  
      "profileArn": string,  
      "roleArn": string,  
      "trustAnchorArn": string,  
      "roleSessionName": string,  
    } 
     
URI Request Parameters
The request accepts the following as URI parameters or as JSON in the request body. Our examples 
put these in the request body.
profileArn
The Amazon Resource Name (ARN) of the proﬁle.
Type: String
CreateSession API 52
IAM Roles Anywhere User Guide
Required: Yes
roleArn
The Amazon Resource Name (ARN) of the role to assume.
Type: String
Required: Yes
trustAnchorArn
The Amazon Resource Name (ARN) of the trust anchor.
Type: String
Required: Yes
Request Body
The request accepts the following data in JSON format.
durationSeconds
The duration, in seconds, of the role session. The value is optional and can range from 900 
seconds (15 minutes) up to 43200 seconds (12 hours). Please see the Expiration subsection 
of the Credentials Object section for more details on how this value is used in determining the 
expiration of the vended session.
Type: Number
Required: No
profileArn
The Amazon Resource Name (ARN) of the proﬁle.
Type: String
Required: Yes
roleArn
The Amazon Resource Name (ARN) of the role to assume.
Type: String
Request Body 53
IAM Roles Anywhere User Guide
Required: Yes
sessionName
This parameter has been deprecated.
This parameter is no longer used. Instead, use the roleSessionName parameter.
Type: String
Required: No
trustAnchorArn
The Amazon Resource Name (ARN) of the trust anchor.
Type: String
Required: Yes
roleSessionName
An identiﬁer for the role session.
Type: String
Required: No
Response Syntax
    HTTP/1.1 201 
    Content-type: application/json 
    { 
      "credentialSet":[ 
        { 
          "assumedRoleUser": { 
          "arn": ARN, 
          "assumedRoleId": String
          }, 
          "credentials":{ 
            "accessKeyId": String, 
            "expiration": Timestamp, 
            "secretAccessKey": String, 
            "sessionToken": String
Response Syntax 54
IAM Roles Anywhere User Guide
          }, 
          "packedPolicySize": Number, 
          "roleArn": ARN, 
          "sourceIdentity": String
        } 
      ], 
      "subjectArn": ARN
    } 
       
Response Elements
If the action is successful, the service sends back an HTTP 201 response.
The following data is returned in JSON format by the service.
assumedRoleUser
The Amazon Resource Name (ARN) and the assumed role ID, which are identiﬁers that you can 
use to refer to the resulting temporary security credentials.
Type: AssumedRoleUser object
credentials
The temporary security credentials, which include an access key ID, a secret access key, and a 
security (or session) token.
Type: Credentials Object
packedPolicySize
A percentage value that indicates the packed size of the session policies and session tags 
combined passed in the request. The request fails if the packed size is greater than 100 percent, 
which means the policies and tags exceeded the allowed space.
Type: Integer
Valid Range: Minimum value of 0
sourceIdentity
The source identity is speciﬁed by the principal that is calling the CreateSession operation. For 
more information on how the source identity is derived please see the Trust Model section.
Response Elements 55
IAM Roles Anywhere User Guide
Type: String
Pattern: [\p{L}\p{Z}\p{N}_.:/=+\-@]+
roleArn
The Amazon Resource Name (ARN) of the assumed role.
Type: String
subjectArn
The Amazon Resource Name (ARN) of the Subject resource.
The Subject resource records the history of the principal that is calling the CreateSession 
operation, including its ﬁrst recorded authentication time, and last recorded authentication 
time.
Type: String
Credentials Object
AWS credentials for API authentication.
AccessKeyId
The access key ID that identiﬁes the temporary security credentials.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Required: Yes
Expiration
The time at which the vended credentials expire. This value is determined based on the 
values set for profileDurationSeconds and createSessionDurationSeconds, where
profileDurationSeconds is the value of the durationSeconds ﬁeld that's set on the 
proﬁle referenced in the call to CreateSession, and createSessionDurationSeconds
is the value of the durationSeconds parameter in the request to CreateSession. From 
this, finalDurationSeconds is determined by the following: finalDurationSeconds 
= min(profileDurationSeconds, createSessionDurationSeconds), where
Credentials Object 56
IAM Roles Anywhere User Guide
finalDurationSeconds is the value for durationSeconds that will be sent in the
AssumeRole request to assume the target role. If createSessionDurationSeconds
isn't provided, then finalDurationSeconds = profileDurationSeconds. From 
this, Expiration is determined by the following: Expiration = CurrentTime + 
finalDurationSeconds. Note that if finalDurationSeconds is greater than the maximum 
session duration (MaxSessionDuration) set on the role, you will receive an error response 
from the API.
Type: Timestamp
Required: Yes
SecretAccessKey
The secret access key that can be used to sign requests.
Type: String
Required: Yes
SessionToken
The token that users must pass to the service API to use the temporary credentials.
Type: String
Required: Yes
The relationship between CreateSession and AssumeRole
CreateSession is an X.509 wrapper around AssumeRole. The temporary session credentials are 
delivered to RolesAnywhere by AssumeRole, and then passed on without modiﬁcation in the result 
of CreateSession. CreateSession is not included in any SDK or client as there is not yet native SDK 
or client support for CreateSession's signing process.
The roleSessionName option in the CreateSession request allows you to customize the identiﬁer 
of a role session. The provided value will be passed into the AssumeRole request during the 
CreateSession process and will be incorporated into the ARN and ID of the assumed role user. 
This means that subsequent API requests using the temporary session credentials vended by 
CreateSession will expose the role session name to the corresponding account in their CloudTrail 
logs. Also, you can reference these credentials in a resource-based policy by the ARN or the ID. 
The relationship between CreateSession and AssumeRole 57
IAM Roles Anywhere User Guide
The default role session name, when not provided, is the serial number of the X.509 certiﬁcate 
provided in a session request.
The acceptRoleSessionName option on a proﬁle controls whether or not a role session name 
will be accepted in a session request with this proﬁle. By setting the acceptRoleSessionName
option to true, you acknowledge that a role session name will be honored in a session request if 
the CreateSession call is made with this speciﬁc proﬁle. This means that the default role session 
name, which is the serial number of the X.509 certiﬁcate, will no longer be used and included in 
the ARN or ID of the assumed role user.
By default, the acceptRoleSessionName attached to the proﬁle is false. If you provide a 
custom role session name in the CreateSession request but custom role session names are not 
accepted, you will receive an Access Denied error. However, when a role session name is not 
presented in the CreateSession request, the role session name will default to the serial number 
of the end-entity X.509 certiﬁcate that was used to authenticate the request, even when the
acceptRoleSessionName on the proﬁle is true.
The IAM Roles Anywhere authentication signing process
The signing process is identical to SigV4, with the exception of the keys used, the signature 
algorithm, and the addition of headers related to the X.509 certiﬁcate and trust chain. For 
more information, see AWS Signature Version 4 for API requests, which should be treated as 
authoritative unless speciﬁcally addressed in this user guide.
Topics
• Task 1: Create a canonical request
• Task 2: Create a string to sign
• Task 3: Calculate the signature
• Task 4: Add the signature to the HTTP request
Task 1: Create a canonical request
To begin the signing process, create a string that includes information from your request in a 
standardized (canonical) format. This ensures that when the request is received, the string to sign 
can be calculated in the same way you did. This string will then be used for signature veriﬁcation by 
IAM Roles Anywhere.
Signing process 58
IAM Roles Anywhere User Guide
Follow the steps below to create a canonical version of the request. Otherwise, your version and 
the version calculated by AWS won't match, and the request will be denied.
The following example shows the pseudocode to create a canonical request.
Example Canonical request pseudocode
    CanonicalRequest =  
       HttpRequestMethod + '\n' + 
       CanonicalUri + '\n' + 
       CanonicalQueryString + '\n' + 
       CanonicalHeaders + '\n' + 
       SignedHeaders + '\n' + 
      Lowercase(Hex(SHA256(RequestPayload))) 
     
A canonical request has the above structure, in which speciﬁc elements of the request are 
transformed into a canonical value and concatenated together with other elements, joined with a 
newline character.
The following examples shows how to construct the canonical form of a request to IAM Roles 
Anywhere. The original request might look like this as it is sent from the client to AWS.
Example Request
    POST /sessions HTTP/1.1 
    Host: rolesanywhere.us-east-1.amazonaws.com 
    Content-Type: application/json 
    X-Amz-Date: 20211103T120000Z 
    X-Amz-X509: {base64-encoded DER data} 
    { 
      "durationSeconds": number, 
      "profileArn": string, 
      "roleArn": string, 
      "trustAnchorArn": string
    } 
     
To create a canonical request, concatenate the following components from each step into a 
single string:
Task 1: Create a canonical request 59
IAM Roles Anywhere User Guide
1. The HttpRequestMethod is the verb of the HTTP request, in upper case. From the example,
POST.
2. The CanonicalUri is the path of the request up until the query string delimiter ?. From the 
example, /sessions. The path MUST be normalized according to RFC 3986, with redundant 
and relative path components removed. Path segments MUST be URI-encoded twice.
3. The CanonicalQueryString is the string following ? in the request URI. If the request 
does not include a query string, use an empty string (essentially, a blank line). The example 
request does not include a query string, therefore we will use an empty string. To construct the 
canonical query string, complete the following steps:
a. Sort the parameter names by character code point in ascending order. Parameters with 
duplicate names should be sorted by value. For example, a parameter name that begins 
with the uppercase letter F precedes a parameter name that begins with a lowercase letter 
b.
b. URI-encode each parameter name and value according to the following rules:
i. Do not URI-encode any of the unreserved characters that RFC 3986 deﬁnes: A-Z, a-z, 
0-9, hyphen ( ‐ ), underscore ( _ ), period ( . ), and tilde ( ˜ ).
ii. Percent-encode all other characters with %XY, where X and Y are hexadecimal 
characters (0-9 and uppercase A-F). For example, the space character must be 
encoded as %20 (not using '+', as some encoding schemes do) and extended UTF-8 
characters must be in the form %XY%ZA%BC.
iii. Double-encode any equals ( = ) characters in parameter values.
c. Build the canonical query string by starting with the ﬁrst parameter name in the sorted 
list.
d. For each parameter, append the URI-encoded parameter name, followed by the equals 
sign character (=), followed by the URI-encoded parameter value. Use an empty string for 
parameters that have no value.
e. Append the ampersand character (&) after each parameter value, except for the last value 
in the list.
4. The CanonicalHeaders is a string capturing the header key and value that are included in 
the signature. The ﬁeld is structured as follows:
    CanonicalHeaders = 
Task 1: Create a canonical request 60
IAM Roles Anywhere User Guide
      CanonicalHeadersEntry0 + CanonicalHeadersEntry1 + ... + 
 CanonicalHeadersEntryN
    CanonicalHeadersEntry = 
      Lowercase(HeaderName) + ':' + Trimall(HeaderValue) + '\n' 
         
Lowercase represents a function that converts all characters to lowercase. The TrimAll
function removes excess white space before and after values, and converts sequential spaces 
to a single space.
Important
The signing certiﬁcate MUST be presented in the header X-Amz-X509, as base64-
encoded Distinguished Encoding Rules (DER), and the X-Amz-X509 header MUST be 
included in CanonicalHeaders and SignedHeaders
If the client is providing the chain of intermediate certiﬁcates, the X-Amz-X509-
Chain MUST be added to the request as well.
Build the canonical headers list by sorting the (lowercase) headers by character code and then 
iterating through the header names. Construct each header according to the following rules:
• Append the lowercase header name followed by a colon.
• Append a comma-separated list of values for that header. Do not sort the values in 
headers that have multiple values.
• Append a new line ('\n').
5. The SignedHeaders is a list of the header names, sorted by lowercase character code, 
delimited by semi-colon. For example – content-type;host;x-amz-date;x-amz-x509
6. A hash of the request payload is appended to the canonical request. The bytes of the request 
are encoded as UTF-8, hashed with SHA-256, the resulting bytes hex encoded, and ﬁnally 
lowercased.
7. To construct the ﬁnished canonical request, combine all the components from each step as 
a single string. As noted, each component ends with a newline character. If you follow the 
canonical request pseudocode explained earlier, the resulting canonical request is shown in the 
following example.
Example Canonical request
Task 1: Create a canonical request 61
IAM Roles Anywhere User Guide
    POST 
    /sessions 
     
    content-type:application/json 
    host:rolesanywhere.us-east-1.amazonaws.com 
    x-amz-date:20211103T120000Z 
    x-amz-x509:{base64-encoded DER data} 
    content-type;host;x-amz-date;x-amz-x509 
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
     
8. Create a digest (hash) of the canonical request with the same algorithm that you used to 
hash the payload. The bytes of the request are encoded as UTF-8, hashed with SHA-256, the 
resulting bytes hex encoded, and ﬁnally lowercased.
Task 2: Create a string to sign
The “string to sign” is the actual input to the signing algorithm, and includes meta information 
about the request, along with the canonical request created in the previous step.
Example StringToSign pseudocode
 StringToSign = Algorithm + '\n' + RequestDateTime + '\n' + CredentialScope + '\n' 
 + HashedCanonicalRequest 
The structure is as follows:
1. The Algorithm is a string that indicates how the signature is calculated. It must be one of
AWS4-X509-RSA-SHA256, AWS4-X509-ECDSA-SHA256 or AWS4-X509-MLDSA and MUST be 
supported by the key type of the signing certiﬁcate's private key. For example, if the signing 
certiﬁcate has an RSA private key, the full algorithm string will be AWS4-X509-RSA-SHA256.
2. The RequestDateTime is a string derived at time of the signing operation, at second 
granularity, in UTC, formatted as ISO8601 basic, YYYYMMDD’T’HHMMSS’Z’. For example,
20211101T121030Z.
Task 2: Create a string to sign 62
IAM Roles Anywhere User Guide
3. The CredentialScope is structured ﬁeld of the form Date + '/' + Region + '/' + 
Service + '/aws4_request’. The Region and service name strings must be UTF-8 
encoded. For example, 20211101/us-east-1/rolesanywhere/aws4_request.
4. Finally, append a newline followed by the HashedCanonicalRequest computed in the previous 
step.
Task 3: Calculate the signature
    Signature = HexEncode(SigningAlgorithm(CertPrivateKey,StringToSign)) 
     
SigningAlgorithm must be one of the following algorithms
• SHA256WithRSA
• SHA256WithECDSA
• ML-DSA-44
• ML-DSA-65
• ML-DSA-87
Task 4: Add the signature to the HTTP request
The signature derived from the previous step is added to the HTTP request in the Authorization
header ﬁeld. The Authorization header is attached to the request and validated for 
authentication. It is partitioned into multiple ﬁelds – signing algorithm, credentials, signed headers, 
and the actual signature. The header of the authentication mechanism based on X.509 diﬀers from 
a SigV4 header in two ways:
• Algorithm. As described above, instead of AWS4-HMAC-SHA256, the algorithm ﬁeld will have 
the values of the form AWS4-X509-RSA-SHA256, AWS4-X509-ECDSA-SHA256 or AWS4-
X509-MLDSA depending on whether an RSA, Elliptic Curve algorithm or ML-DSA. This, in turn, is 
determined by the key bound to the signing certiﬁcate.
• Scope ﬁeld/credentials. As speciﬁed above, the serial number of the certiﬁcate used to sign the 
request will be in place of the Access Key ID (credential) in the Scope ﬁeld.
Task 3: Calculate the signature 63
IAM Roles Anywhere User Guide
The structure of the ﬁeld is as follows:
      Authorization: {Algorithm} Credential={CredentialString}, 
 SignedHeaders={SignedHeaders}, Signature={Signature} 
       
1. The Algorithm must be one of AWS4-X509-RSA-SHA256, AWS4-X509-ECDSA-SHA256 or
AWS4-X509-MLDSA.
2. The Credential is constructed via {SerialNumber}/{Scope} where serial number is the 
decimal representation of the serial number of the signing certiﬁcate, and Scope is the value 
constructed as input to the StringToSign. For example:
    Credential=11111222223333344444/20201105/us-east-1/rolesanywhere/aws4_request 
         
3. The SignedHeaders is a comma-delimited list of the headers signed as part of the request.
4. The Signature is the hex encoded output of the previous step.
Task 4: Add the signature to the HTTP request 64
IAM Roles Anywhere User Guide
IAM Roles Anywhere cloud security and shared 
responsibility
Cloud security at AWS is the highest priority. As an AWS customer, you beneﬁt from data centers 
and network architectures that are built to meet the requirements of the most security-sensitive 
organizations.
Security is a shared responsibility between AWS and you. The shared responsibility model describes 
this as security of the cloud and security in the cloud:
• Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS 
services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-
party auditors regularly test and verify the eﬀectiveness of our security as part of the AWS 
Compliance Programs. To learn about the compliance programs that apply to AWS Identity and 
Access Management Roles Anywhere, see AWS Services in Scope by Compliance Program.
• Security in the cloud – Your responsibility is determined by the AWS service that you use. You 
are also responsible for other factors including the sensitivity of your data, your company’s 
requirements, and applicable laws and regulations.
This documentation helps you understand how to apply the shared responsibility model when 
using AWS Identity and Access Management Roles Anywhere. The following topics show you how 
to conﬁgure IAM Roles Anywhere to meet your security and compliance objectives. You can also 
learn how to use other AWS services that help you to monitor and secure your IAM Roles Anywhere 
resources.
Topics
• Mapping identities to your workloads with IAM Roles Anywhere
• Data protection and privacy in IAM Roles Anywhere
• Identity and access management for IAM Roles Anywhere
• Disaster recovery and resilience in IAM Roles Anywhere
• IAM Roles Anywhere and interface VPC endpoints (AWS PrivateLink)
• Control API access with IAM policies
65
IAM Roles Anywhere User Guide
Mapping identities to your workloads with IAM Roles Anywhere
A key element to using IAM Roles Anywhere is managing how identities are assigned to workloads. 
Certiﬁcates are issued to compute instances (servers, containers), in which the identity is encoded 
as the Subject of the certiﬁcate. The subject may be a simple Common Name (CN), a Fully 
Qualiﬁed Distinguished Name (FQDN), that contains information about organizational structure, or 
a simple hostname. Alternatively, a standard such as SPIFFE could be used to create a hierarchical 
namespace for the workload identities.
IAM Roles Anywhere lets the workload use the certiﬁcate to obtain temporary credentials 
instead of issuing Access Key IDs and Secret Access Keys, and the identity in the subject is 
encoded in the session credentials in a way that can be used in resource policies. For example, if a 
certiﬁcate has a Subject with CN=Alice, the value is added to the session as a PrincipalTag:
aws:PrincipalTag/x509Subject/CN.
The ﬁelds Subject, Issuer and Subject Alternative Name (SAN) are extracted from x509 tickets 
and used as elements of the PrincipalTags. Tags that start with the preﬁx x509Subject are usually 
followed by the suﬃx /CN used to identify the subject’s common name. Tags starting with the 
preﬁx x509Issuer are usually followed by /C, /O, /OU, /ST, /L, and /CN in order to identify the 
issuer’s country, organization, organization unit, state, locality and common name respectively. 
Tags starting with x509SAN preﬁx are followed by /DNS, /URI or /CN to identify the subject 
alternative name’s DNS, URI or common name of the subject alternative name respectively. These 
are some of the diﬀerent ways x509 ﬁelds are implemented as PrincipalTags for use in identity 
mapping.
Data protection and privacy in IAM Roles Anywhere
The AWS shared responsibility model applies to data protection in AWS Identity and Access 
Management Roles Anywhere. As described in this model, AWS is responsible for protecting the 
global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control 
over your content that is hosted on this infrastructure. You are also responsible for the security 
conﬁguration and management tasks for the AWS services that you use. For more information 
about data privacy, see the Data Privacy FAQ. For information about data protection in Europe, see 
the AWS Shared Responsibility Model and GDPR blog post on the AWS Security Blog.
For data protection purposes, we recommend that you protect AWS account credentials and set 
up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). 
Workload identities 66
IAM Roles Anywhere User Guide
That way, each user is given only the permissions necessary to fulﬁll their job duties. We also 
recommend that you secure your data in the following ways:
• Use multi-factor authentication (MFA) with each account.
• Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
• Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail 
trails to capture AWS activities, see Working with CloudTrail trails in the AWS CloudTrail User 
Guide.
• Use AWS encryption solutions, along with all default security controls within AWS services.
• Use advanced managed security services such as Amazon Macie, which assists in discovering and 
securing sensitive data that is stored in Amazon S3.
• If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a 
command line interface or an API, use a FIPS endpoint. For more information about the available 
FIPS endpoints, see Federal Information Processing Standard (FIPS) 140-3.
We strongly recommend that you never put conﬁdential or sensitive information, such as your 
customers' email addresses, into tags or free-form text ﬁelds such as a Name ﬁeld. This includes 
when you work with IAM Roles Anywhere or other AWS services using the console, API, AWS CLI, or 
AWS SDKs. Any data that you enter into tags or free-form text ﬁelds used for names may be used 
for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend 
that you do not include credentials information in the URL to validate your request to that server.
Encryption in transit
IAM Roles Anywhere provides secure and private endpoints for encrypting data in transit. The 
secure and private endpoints allow AWS to protect the integrity of API requests to IAM Roles 
Anywhere. AWS requires API calls to be signed by the caller using a secret access key. This 
requirement is stated in the Signature Version 4 Signing Process (Sigv4).
Key management
Authenticating to IAM Roles Anywhere requires the use of asymmetric (public/private) key pairs. 
IAM Roles Anywhere does not hold customer private keys. Those remain on customer instances in 
data centers. Care should be taken to minimize the risk of accidental disclosure.
• Use OS ﬁle system permissions to restrict read access to the owning user.
Encryption in transit 67
IAM Roles Anywhere User Guide
• Never check keys into source control. Store them separately from source code to reduce the risk 
of accidentally including them in a change set. If possible, consider the use of a secure storage 
mechanism.
Inter-network traﬃc privacy
When accessing AWS APIs and resources from your data center, be aware of how the traﬃc is 
routed. Connectivity may occur via Network Address Translation (NAT) at the data center outbound 
ﬁrewall, or it may occur through Virtual Private Network (VPN).
Identity and access management for IAM Roles Anywhere
AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely 
control access to AWS resources. IAM administrators control who can be authenticated (signed in) 
and authorized (have permissions) to use IAM Roles Anywhere resources. IAM is an AWS service that 
you can use with no additional charge.
Topics
• Audience
• Authenticating with identities
• Managing access using policies
• How IAM Roles Anywhere works with IAM
• Identity-based policy examples for IAM Roles Anywhere
• Troubleshooting IAM Roles Anywhere identity and access
• Using service-linked roles for IAM Roles Anywhere
• AWS managed policies for IAM Roles Anywhere
Audience
How you use AWS Identity and Access Management (IAM) diﬀers based on your role:
• Service user - request permissions from your administrator if you cannot access features (see
Troubleshooting IAM Roles Anywhere identity and access)
• Service administrator - determine user access and submit permission requests (see How IAM 
Roles Anywhere works with IAM)
Inter-network traﬃc privacy 68
IAM Roles Anywhere User Guide
• IAM administrator - write policies to manage access (see Identity-based policy examples for IAM 
Roles Anywhere)
Authenticating with identities
Authentication is how you sign in to AWS using your identity credentials. You must be 
authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.
You can sign in as a federated identity using credentials from an identity source like AWS 
IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook 
credentials. For more information about signing in, see How to sign in to your AWS account in the
AWS Sign-In User Guide.
For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For 
more information, see AWS Signature Version 4 for API requests in the IAM User Guide.
AWS account root user
When you create an AWS account, you begin with one sign-in identity called the AWS account root 
user that has complete access to all AWS services and resources. We strongly recommend that you 
don't use the root user for everyday tasks. For tasks that require root user credentials, see Tasks 
that require root user credentials in the IAM User Guide.
Federated identity
As a best practice, require human users to use federation with an identity provider to access AWS 
services using temporary credentials.
A federated identity is a user from your enterprise directory, web identity provider, or Directory 
Service that accesses AWS services using credentials from an identity source. Federated identities 
assume roles that provide temporary credentials.
For centralized access management, we recommend AWS IAM Identity Center. For more 
information, see What is IAM Identity Center? in the AWS IAM Identity Center User Guide.
IAM users and groups
An IAM user is an identity with speciﬁc permissions for a single person or application. We 
recommend using temporary credentials instead of IAM users with long-term credentials. For more 
Authenticating with identities 69
IAM Roles Anywhere User Guide
information, see Require human users to use federation with an identity provider to access AWS 
using temporary credentials in the IAM User Guide.
An IAM group speciﬁes a collection of IAM users and makes permissions easier to manage for large 
sets of users. For more information, see Use cases for IAM users in the IAM User Guide.
IAM roles
An IAM role is an identity with speciﬁc permissions that provides temporary credentials. You can 
assume a role by switching from a user to an IAM role (console) or by calling an AWS CLI or AWS 
API operation. For more information, see Methods to assume a role in the IAM User Guide.
IAM roles are useful for federated user access, temporary IAM user permissions, cross-account 
access, cross-service access, and applications running on Amazon EC2. For more information, see
Cross account resource access in IAM in the IAM User Guide.
Managing access using policies
You control access in AWS by creating policies and attaching them to AWS identities or resources. 
A policy deﬁnes permissions when associated with an identity or resource. AWS evaluates these 
policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For 
more information about JSON policy documents, see Overview of JSON policies in the IAM User 
Guide.
Using policies, administrators specify who has access to what by deﬁning which principal can 
perform actions on what resources, and under what conditions.
By default, users and roles have no permissions. An IAM administrator creates IAM policies and 
adds them to roles, which users can then assume. IAM policies deﬁne permissions regardless of the 
method used to perform the operation.
Identity-based policies
Identity-based policies are JSON permissions policy documents that you attach to an identity (user, 
group, or role). These policies control what actions identities can perform, on which resources, and 
under what conditions. To learn how to create an identity-based policy, see Deﬁne custom IAM 
permissions with customer managed policies in the IAM User Guide.
Identity-based policies can be inline policies (embedded directly into a single identity) or managed 
policies (standalone policies attached to multiple identities). To learn how to choose between 
Managing access using policies 70
IAM Roles Anywhere User Guide
managed and inline policies, see Choose between managed policies and inline policies in the IAM 
User Guide.
Resource-based policies
Resource-based policies are JSON policy documents that you attach to a resource. Examples 
include IAM role trust policies and Amazon S3 bucket policies. In services that support resource-
based policies, service administrators can use them to control access to a speciﬁc resource. You 
must specify a principal in a resource-based policy.
Resource-based policies are inline policies that are located in that service. You can't use AWS 
managed policies from IAM in a resource-based policy.
Other policy types
AWS supports additional policy types that can set the maximum permissions granted by more 
common policy types:
• Permissions boundaries – Set the maximum permissions that an identity-based policy can grant 
to an IAM entity. For more information, see Permissions boundaries for IAM entities in the IAM 
User Guide.
• Service control policies (SCPs) – Specify the maximum permissions for an organization or 
organizational unit in AWS Organizations. For more information, see Service control policies in 
the AWS Organizations User Guide.
• Resource control policies (RCPs) – Set the maximum available permissions for resources in your 
accounts. For more information, see Resource control policies (RCPs) in the AWS Organizations 
User Guide.
• Session policies – Advanced policies passed as a parameter when creating a temporary session 
for a role or federated user. For more information, see Session policies in the IAM User Guide.
Multiple policy types
When multiple types of policies apply to a request, the resulting permissions are more complicated 
to understand. To learn how AWS determines whether to allow a request when multiple policy 
types are involved, see Policy evaluation logic in the IAM User Guide.
Managing access using policies 71
IAM Roles Anywhere User Guide
How IAM Roles Anywhere works with IAM
Before you use IAM to manage access to IAM Roles Anywhere, learn what IAM features are available 
to use with IAM Roles Anywhere.
IAM features you can use with AWS Identity and Access Management Roles Anywhere
IAM feature IAM Roles Anywhere support
Identity-based policies Yes
Resource-based policies No
Policy actions Yes
Policy resources Yes
Policy condition keys Yes
ACLs No
ABAC (tags in policies) Partial
Temporary credentials Yes
Principal permissions Yes
Service roles Yes
Service-linked roles Yes
To get a high-level view of how IAM Roles Anywhere and other AWS services work with most IAM 
features, see AWS services that work with IAM in the IAM User Guide.
Identity-based policies for IAM Roles Anywhere
Supports identity-based policies: Yes
Identity-based policies are JSON permissions policy documents that you can attach to an identity, 
such as an IAM user, group of users, or role. These policies control what actions users and roles can 
How IAM Roles Anywhere works with IAM 72
IAM Roles Anywhere User Guide
perform, on which resources, and under what conditions. To learn how to create an identity-based 
policy, see Deﬁne custom IAM permissions with customer managed policies in the IAM User Guide.
With IAM identity-based policies, you can specify allowed or denied actions and resources as well 
as the conditions under which actions are allowed or denied. To learn about all of the elements 
that you can use in a JSON policy, see IAM JSON policy elements reference in the IAM User Guide.
Identity-based policy examples for IAM Roles Anywhere
To view examples of IAM Roles Anywhere identity-based policies, see Identity-based policy 
examples for IAM Roles Anywhere.
Resource-based policies within IAM Roles Anywhere
Supports resource-based policies: No
Resource-based policies are JSON policy documents that you attach to a resource. Examples of 
resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that 
support resource-based policies, service administrators can use them to control access to a speciﬁc 
resource. For the resource where the policy is attached, the policy deﬁnes what actions a speciﬁed 
principal can perform on that resource and under what conditions. You must specify a principal
in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS 
services.
To enable cross-account access, you can specify an entire account or IAM entities in another 
account as the principal in a resource-based policy. For more information, see Cross account 
resource access in IAM in the IAM User Guide.
Policy actions for IAM Roles Anywhere
Supports policy actions: Yes
Administrators can use AWS JSON policies to specify who has access to what. That is, which
principal can perform actions on what resources, and under what conditions.
The Action element of a JSON policy describes the actions that you can use to allow or deny 
access in a policy. Include actions in a policy to grant permissions to perform the associated 
operation.
How IAM Roles Anywhere works with IAM 73
IAM Roles Anywhere User Guide
To see a list of IAM Roles Anywhere actions, see Actions deﬁned by AWS Identity and Access 
Management Roles Anywhere in the Service Authorization Reference.
Policy actions in IAM Roles Anywhere use the following preﬁx before the action:
rolesanywhere
To specify multiple actions in a single statement, separate them with commas.
"Action": [ 
      "rolesanywhere:action1", 
      "rolesanywhere:action2" 
         ]
To view examples of IAM Roles Anywhere identity-based policies, see Identity-based policy 
examples for IAM Roles Anywhere.
Policy resources for IAM Roles Anywhere
Supports policy resources: Yes
Administrators can use AWS JSON policies to specify who has access to what. That is, which
principal can perform actions on what resources, and under what conditions.
The Resource JSON policy element speciﬁes the object or objects to which the action applies. As 
a best practice, specify a resource using its Amazon Resource Name (ARN). For actions that don't 
support resource-level permissions, use a wildcard (*) to indicate that the statement applies to all 
resources.
"Resource": "*"
To see a list of IAM Roles Anywhere resource types and their ARNs, see Resources deﬁned by AWS 
Identity and Access Management Roles Anywhere in the Service Authorization Reference. To learn 
with which actions you can specify the ARN of each resource, see Actions deﬁned by AWS Identity 
and Access Management Roles Anywhere.
How IAM Roles Anywhere works with IAM 74
IAM Roles Anywhere User Guide
To view examples of IAM Roles Anywhere identity-based policies, see Identity-based policy 
examples for IAM Roles Anywhere.
Policy condition keys for IAM Roles Anywhere
Supports service-speciﬁc policy condition keys: Yes
Administrators can use AWS JSON policies to specify who has access to what. That is, which
principal can perform actions on what resources, and under what conditions.
The Condition element speciﬁes when statements execute based on deﬁned criteria. You can 
create conditional expressions that use condition operators, such as equals or less than, to match 
the condition in the policy with values in the request. To see all AWS global condition keys, see
AWS global condition context keys in the IAM User Guide.
To see a list of IAM Roles Anywhere condition keys, see Condition keys for AWS Identity and 
Access Management Roles Anywhere in the Service Authorization Reference. To learn with which 
actions and resources you can use a condition key, see Actions deﬁned by AWS Identity and Access 
Management Roles Anywhere.
To view examples of IAM Roles Anywhere identity-based policies, see Identity-based policy 
examples for IAM Roles Anywhere.
Access control lists (ACLs) in IAM Roles Anywhere
Supports ACLs: No
Access control lists (ACLs) control which principals (account members, users, or roles) have 
permissions to access a resource. ACLs are similar to resource-based policies, although they do not 
use the JSON policy document format.
Attribute-based access control (ABAC) with IAM Roles Anywhere
Supports ABAC (tags in policies): Partial
Attribute-based access control (ABAC) is an authorization strategy that deﬁnes permissions based 
on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC 
policies to allow operations when the principal's tag matches the tag on the resource.
To control access based on tags, you provide tag information in the condition element of a policy 
using the aws:ResourceTag/key-name, aws:RequestTag/key-name, or aws:TagKeys
condition keys.
How IAM Roles Anywhere works with IAM 75
IAM Roles Anywhere User Guide
If a service supports all three condition keys for every resource type, then the value is Yes for the 
service. If a service supports all three condition keys for only some resource types, then the value is
Partial.
For more information about ABAC, see Deﬁne permissions with ABAC authorization in the IAM User 
Guide. To view a tutorial with steps for setting up ABAC, see Use attribute-based access control 
(ABAC) in the IAM User Guide.
Using Temporary credentials with IAM Roles Anywhere
Supports temporary credentials: Yes
Temporary credentials provide short-term access to AWS resources and are automatically created 
when you use federation or switch roles. AWS recommends that you dynamically generate 
temporary credentials instead of using long-term access keys. For more information, see
Temporary security credentials in IAM and AWS services that work with IAM in the IAM User Guide.
Cross-service principal permissions for IAM Roles Anywhere
Supports forward access sessions (FAS): Yes
Forward access sessions (FAS) use the permissions of the principal calling an AWS service, 
combined with the requesting AWS service to make requests to downstream services. For policy 
details when making FAS requests, see Forward access sessions.
Service roles for IAM Roles Anywhere
Supports service roles: Yes
A service role is an IAM role that a service assumes to perform actions on your behalf. An IAM 
administrator can create, modify, and delete a service role from within IAM. For more information, 
see Create a role to delegate permissions to an AWS service in the IAM User Guide.
Warning
Changing the permissions for a service role might break IAM Roles Anywhere functionality. 
Edit service roles only when IAM Roles Anywhere provides guidance to do so.
Service-linked roles for IAM Roles Anywhere
Supports service-linked roles: Yes
How IAM Roles Anywhere works with IAM 76
IAM Roles Anywhere User Guide
A service-linked role is a type of service role that is linked to an AWS service. The service can 
assume the role to perform an action on your behalf. Service-linked roles appear in your AWS 
account and are owned by the service. An IAM administrator can view, but not edit the permissions 
for service-linked roles.
For details about creating or managing service-linked roles, see AWS services that work with IAM. 
Find a service in the table that includes a Yes in the Service-linked role column. Choose the Yes
link to view the service-linked role documentation for that service.
Identity-based policy examples for IAM Roles Anywhere
By default, users and roles don't have permission to create or modify IAM Roles Anywhere 
resources. To grant users permission to perform actions on the resources that they need, an IAM 
administrator can create IAM policies.
To learn how to create an IAM identity-based policy by using these example JSON policy 
documents, see Create IAM policies (console) in the IAM User Guide.
For details about actions and resource types deﬁned by IAM Roles Anywhere, including the format 
of the ARNs for each of the resource types, see Actions, resources, and condition keys for AWS 
Identity and Access Management Roles Anywhere in the Service Authorization Reference.
Topics
• Policy best practices
• Using the IAM Roles Anywhere console
• Allow users to view their own permissions
Policy best practices
Identity-based policies determine whether someone can create, access, or delete IAM Roles 
Anywhere resources in your account. These actions can incur costs for your AWS account. When you 
create or edit identity-based policies, follow these guidelines and recommendations:
• Get started with AWS managed policies and move toward least-privilege permissions – To 
get started granting permissions to your users and workloads, use the AWS managed policies
that grant permissions for many common use cases. They are available in your AWS account. We 
recommend that you reduce permissions further by deﬁning AWS customer managed policies 
Identity-based policy examples 77
IAM Roles Anywhere User Guide
that are speciﬁc to your use cases. For more information, see AWS managed policies or AWS 
managed policies for job functions in the IAM User Guide.
• Apply least-privilege permissions – When you set permissions with IAM policies, grant only the 
permissions required to perform a task. You do this by deﬁning the actions that can be taken on 
speciﬁc resources under speciﬁc conditions, also known as least-privilege permissions. For more 
information about using IAM to apply permissions, see  Policies and permissions in IAM in the
IAM User Guide.
• Use conditions in IAM policies to further restrict access – You can add a condition to your 
policies to limit access to actions and resources. For example, you can write a policy condition to 
specify that all requests must be sent using SSL. You can also use conditions to grant access to 
service actions if they are used through a speciﬁc AWS service, such as CloudFormation. For more 
information, see  IAM JSON policy elements: Condition in the IAM User Guide.
• Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional 
permissions – IAM Access Analyzer validates new and existing policies so that the policies 
adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides 
more than 100 policy checks and actionable recommendations to help you author secure and 
functional policies. For more information, see Validate policies with IAM Access Analyzer in the
IAM User Guide.
• Require multi-factor authentication (MFA) – If you have a scenario that requires IAM users or 
a root user in your AWS account, turn on MFA for additional security. To require MFA when API 
operations are called, add MFA conditions to your policies. For more information, see  Secure API 
access with MFA in the IAM User Guide.
For more information about best practices in IAM, see Security best practices in IAM in the IAM User 
Guide.
Using the IAM Roles Anywhere console
To access the AWS Identity and Access Management Roles Anywhere console, you must have a 
minimum set of permissions. These permissions must allow you to list and view details about the 
IAM Roles Anywhere resources in your AWS account. If you create an identity-based policy that is 
more restrictive than the minimum required permissions, the console won't function as intended 
for entities (users or roles) with that policy.
You don't need to allow minimum console permissions for users that are making calls only to the 
AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation 
that they're trying to perform.
Identity-based policy examples 78
IAM Roles Anywhere User Guide
To ensure that users and roles can still use the IAM Roles Anywhere console, also attach the IAM 
Roles Anywhere ConsoleAccess or ReadOnly AWS managed policy to the entities. For more 
information, see Adding permissions to a user in the IAM User Guide.
Allow users to view their own permissions
This example shows how you might create a policy that allows IAM users to view the inline and 
managed policies that are attached to their user identity. This policy includes permissions to 
complete this action on the console or programmatically using the AWS CLI or AWS API.
{ 
    "Version": "2012-10-17",        
    "Statement": [ 
        { 
            "Sid": "ViewOwnUserInfo", 
            "Effect": "Allow", 
            "Action": [ 
                "iam:GetUserPolicy", 
                "iam:ListGroupsForUser", 
                "iam:ListAttachedUserPolicies", 
                "iam:ListUserPolicies", 
                "iam:GetUser" 
            ], 
            "Resource": ["arn:aws:iam::*:user/${aws:username}"] 
        }, 
        { 
            "Sid": "NavigateInConsole", 
            "Effect": "Allow", 
            "Action": [ 
                "iam:GetGroupPolicy", 
                "iam:GetPolicyVersion", 
                "iam:GetPolicy", 
                "iam:ListAttachedGroupPolicies", 
                "iam:ListGroupPolicies", 
                "iam:ListPolicyVersions", 
                "iam:ListPolicies", 
                "iam:ListUsers" 
            ], 
            "Resource": "*" 
        } 
    ]
}
Identity-based policy examples 79
IAM Roles Anywhere User Guide
Troubleshooting IAM Roles Anywhere identity and access
Use the following information to help you diagnose and ﬁx common issues that you might 
encounter when working with IAM Roles Anywhere and IAM.
Topics
• I am not authorized to perform an action in IAM Roles Anywhere
• I am not authorized to perform iam:PassRole
• I want to view my access keys
• I'm an administrator and want to allow others to access IAM Roles Anywhere
• I want to allow people outside of my AWS account to access my IAM Roles Anywhere resources
• Invalidating a IAM Roles Anywhere session
I am not authorized to perform an action in IAM Roles Anywhere
If the AWS Management Console tells you that you're not authorized to perform an action, then 
you must contact your administrator for assistance. Your administrator is the person that provided 
you with your user name and password.
The following example error occurs when the mateojackson IAM user tries to use the console 
to view details about a ﬁctional my-example-widget resource but does not have the ﬁctional
rolesanywhere:GetWidget permissions.
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: 
 rolesanywhere:GetWidget on resource: my-example-widget
In this case, Mateo asks his administrator to update his policies to allow him to access the my-
example-widget resource using the rolesanywhere:GetWidget action.
I am not authorized to perform iam:PassRole
If you receive an error that you're not authorized to perform the iam:PassRole action, your 
policies must be updated to allow you to pass a role to IAM Roles Anywhere.
Troubleshooting 80
IAM Roles Anywhere User Guide
Some AWS services allow you to pass an existing role to that service instead of creating a new 
service role or service-linked role. To do this, you must have permissions to pass the role to the 
service.
The following example error occurs when an IAM user named marymajor tries to use the console 
to perform an action in IAM Roles Anywhere. However, the action requires the service to have 
permissions that are granted by a service role. Mary does not have permissions to pass the role to 
the service.
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: 
 iam:PassRole
In this case, Mary's policies must be updated to allow her to perform the iam:PassRole action.
If you need help, contact your AWS administrator. Your administrator is the person who provided 
you with your sign-in credentials.
I want to view my access keys
After you create your IAM user access keys, you can view your access key ID at any time. However, 
you can't view your secret access key again. If you lose your secret key, you must create a new 
access key pair.
Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and 
a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). Like a 
user name and password, you must use both the access key ID and secret access key together to 
authenticate your requests. Manage your access keys as securely as you do your user name and 
password.
Important
Do not provide your access keys to a third party, even to help ﬁnd your canonical user ID. By 
doing this, you might give someone permanent access to your AWS account.
When you create an access key pair, you are prompted to save the access key ID and secret access 
key in a secure location. The secret access key is available only at the time you create it. If you lose 
your secret access key, you must add new access keys to your IAM user. You can have a maximum of 
Troubleshooting 81
IAM Roles Anywhere User Guide
two access keys. If you already have two, you must delete one key pair before creating a new one. 
To view instructions, see Managing access keys in the IAM User Guide.
I'm an administrator and want to allow others to access IAM Roles Anywhere
To allow others to access IAM Roles Anywhere, you must grant permission to the people or 
applications that need access. If you are using AWS IAM Identity Center to manage people 
and applications, you assign permission sets to users or groups to deﬁne their level of access. 
Permission sets automatically create and assign IAM policies to IAM roles that are associated with 
the person or application. For more information, see Permission sets in the AWS IAM Identity Center 
User Guide.
If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people 
or applications that need access. You must then attach a policy to the entity that grants them 
the correct permissions in IAM Roles Anywhere. After the permissions are granted, provide the 
credentials to the user or application developer. They will use those credentials to access AWS. 
To learn more about creating IAM users, groups, policies, and permissions, see IAM Identities and
Policies and permissions in IAM in the IAM User Guide.
I want to allow people outside of my AWS account to access my IAM Roles 
Anywhere resources
You can create a role that users in other accounts or people outside of your organization can use to 
access your resources. You can specify who is trusted to assume the role. For services that support 
resource-based policies or access control lists (ACLs), you can use those policies to grant people 
access to your resources.
To learn more, consult the following:
• To learn whether IAM Roles Anywhere supports these features, see How IAM Roles Anywhere 
works with IAM.
• To learn how to provide access to your resources across AWS accounts that you own, see
Providing access to an IAM user in another AWS account that you own in the IAM User Guide.
• To learn how to provide access to your resources to third-party AWS accounts, see Providing 
access to AWS accounts owned by third parties in the IAM User Guide.
• To learn how to provide access through identity federation, see Providing access to externally 
authenticated users (identity federation) in the IAM User Guide.
Troubleshooting 82
IAM Roles Anywhere User Guide
• To learn the diﬀerence between using roles and resource-based policies for cross-account access, 
see Cross account resource access in IAM in the IAM User Guide.
Invalidating a IAM Roles Anywhere session
You can invalidate a IAM Roles Anywhere session if you need to revoke access for certiﬁcates issued 
by AWS Private Certiﬁcate Authority (AWS Private CA) or another certiﬁcate authority.
To invalidate a IAM Roles Anywhere session
1. To get an updated certiﬁcate revocation list (CRL), do one of the following:
• If you use AWS Private CA, see Revoking IAM role session permissions.
• If you use a diﬀerent certiﬁcate authority:
a. Follow their documentation for revoking certiﬁcate access and invalidating sessions.
b. Request a new CRL from your certiﬁcate authority.
2. After you get your updated CRL, import it using one of the following:
• The ImportCrl API operation
• The import-crl AWS CLI command
Using service-linked roles for IAM Roles Anywhere
AWS Identity and Access Management Roles Anywhere uses IAM service-linked roles. A service-
linked role is a unique type of IAM role that is linked directly to IAM Roles Anywhere. Service-
linked roles are predeﬁned by IAM Roles Anywhere and include all the permissions that the service 
requires to publish CloudWatch metrics and ensure the private certiﬁcate authorities you use as 
trust anchors can be accessed as part of authenticating with IAM Roles Anywhere. They also ensure 
that you receive auditing information regarding IAM Roles Anywhere. Service-linked roles are 
diﬀerent from the roles that you conﬁgure for the service and obtain temporary credentials for.
A service-linked role makes setting up IAM Roles Anywhere easier because you don’t have to 
manually add the necessary permissions. IAM Roles Anywhere deﬁnes the permissions of its 
service-linked roles. Unless deﬁned otherwise, only IAM Roles Anywhere can assume its service-
linked roles. The deﬁned permissions include the trust policy and the permissions policy. The 
permissions policy cannot be attached to any other IAM entity.
Using service-linked roles 83
IAM Roles Anywhere User Guide
You can delete a service-linked role only after ﬁrst deleting its related resources. This protects your 
IAM Roles Anywhere resources because you can't inadvertently remove permission to access the 
resources.
For information about other services that support service-linked roles, see AWS services that work 
with IAM and look for the services that have Yes in the Service-linked roles column. Choose a Yes
with a link to view the service-linked role documentation for that service.
Service-linked role permissions for IAM Roles Anywhere
IAM Roles Anywhere uses the service-linked role named AWSServiceRoleForRolesAnywhere
which allows IAM Roles Anywhere to publish CloudWatch metrics and check the conﬁguration of 
AWS Private CA in your account. This service-linked role has an IAM policy attached to it named
AWSRolesAnywhereServicePolicy.
The AWSServiceRoleForRolesAnywhere service-linked role trusts the following services to assume 
the role:
• rolesanywhere.amazonaws.com
The role permissions policy named AWSRolesAnywhereServicePolicy allows IAM Roles Anywhere to 
complete the following actions on the speciﬁed resources:
• Actions on CloudWatch:
• cloudwatch:PutMetricData – Allows IAM Roles Anywhere to publish metric data points to 
the AWS/RolesAnywhere and AWS/Usage namespaces.
• Actions on AWS Private CA:
• acm-pca:GetCertificateAuthorityCertificate – Allows IAM Roles Anywhere to 
retrieve the certiﬁcate and certiﬁcate chain for your private certiﬁcate authority.
• acm-pca:DescribeCertificateAuthority – Allows IAM Roles Anywhere to list 
information about your private certiﬁcate authority.
JSON
  { 
    "Version":"2012-10-17",        
Using service-linked roles 84
IAM Roles Anywhere User Guide
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Action": [ 
          "cloudwatch:PutMetricData" 
        ], 
        "Resource": "*", 
        "Condition": { 
          "StringEquals": { 
            "cloudwatch:namespace": [ 
              "AWS/RolesAnywhere", 
              "AWS/Usage" 
            ] 
          } 
        } 
      }, 
      { 
        "Effect": "Allow", 
        "Action": [ 
          "acm-pca:GetCertificateAuthorityCertificate", 
          "acm-pca:DescribeCertificateAuthority" 
        ], 
        "Resource": "arn:aws:acm-pca:*:*:*" 
      } 
    ] 
  } 
     
JSON
  { 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Action": [ 
          "cloudwatch:PutMetricData" 
        ], 
        "Resource": "*", 
        "Condition": { 
          "StringEquals": { 
Using service-linked roles 85
IAM Roles Anywhere User Guide
            "cloudwatch:namespace": [ 
              "AWS/RolesAnywhere", 
              "AWS/Usage" 
            ] 
          } 
        } 
      } 
    ] 
  } 
     
You must conﬁgure permissions to allow an IAM entity (such as a user, group, or role) to create, 
edit, or delete a service-linked role. For more information, see Service-linked role permissions in 
the IAM User Guide.
Creating a service-linked role for IAM Roles Anywhere
You don't need to manually create a service-linked role. When you create your ﬁrst trust anchor 
in the AWS Management Console, the AWS CLI, or the AWS API, IAM Roles Anywhere creates the 
service-linked role for you.
If you delete this service-linked role, and then need to create it again, you can use the same process 
to recreate the role in your account. Note that credentials will still be issued, but metrics will not be 
reported.
You can also use the IAM console to create a service-linked role when you have trust anchors in 
your account but no service-linked role. In the AWS CLI or the AWS API, create a service-linked role 
with the rolesanywhere.amazonaws.com service name. For more information, see Creating 
a service-linked role in the IAM User Guide. If you delete this service-linked role, you can use this 
same process to create the role again.
Editing a service-linked role for IAM Roles Anywhere
IAM Roles Anywhere does not allow you to edit the AWSServiceRoleForRolesAnywhere service-
linked role. After you create a service-linked role, you cannot change the name of the role because 
various entities might reference the role. However, you can edit the description of the role using 
IAM. For more information, see Editing a service-linked role in the IAM User Guide.
Using service-linked roles 86
IAM Roles Anywhere User Guide
Deleting a service-linked role for IAM Roles Anywhere
If you no longer need to use a feature or service that requires a service-linked role, we recommend 
that you delete that role. That way you don’t have an unused entity that is not actively monitored 
or maintained. However, you must clean up the resources for your service-linked role before you 
can manually delete it.
Note
If IAM Roles Anywhere is using the role when you try to delete the resources, then the 
deletion might fail. If that happens, wait for a few minutes and try the operation again.
To delete IAM Roles Anywhere resources used by the AWSServiceRoleForRolesAnywhere
• Delete all trust anchors in your account in all Regions that contain them.
To manually delete the service-linked role using IAM
• For information about using the IAM console, the AWS CLI, or the AWS API to delete the 
AWSServiceRoleForRolesAnywhere service-linked role, see Deleting a service-linked role in the
IAM User Guide.
Supported regions for IAM Roles Anywhere service-linked roles
IAM Roles Anywhere supports using service-linked roles in all of the regions where the service is 
available. For more information, see AWS regions and endpoints.
Region name Region identity Support in IAM 
Roles Anywhere
US East (N. Virginia) us-east-1 Yes
US East (Ohio) us-east-2 Yes
US West (N. California) us-west-1 Yes
US West (Oregon) us-west-2 Yes
Using service-linked roles 87
IAM Roles Anywhere User Guide
Region name Region identity Support in IAM 
Roles Anywhere
Asia Paciﬁc (Mumbai) ap-south-1 Yes
Asia Paciﬁc (Osaka) ap-northeast-3 Yes
Asia Paciﬁc (Seoul) ap-northeast-2 Yes
Asia Paciﬁc (Singapore) ap-southeast-1 Yes
Asia Paciﬁc (Sydney) ap-southeast-2 Yes
Asia Paciﬁc (Tokyo) ap-northeast-1 Yes
Asia Paciﬁc (Hong Kong) ap-east-1 Yes
Asia Paciﬁc (Jakarta) ap-southeast-3 Yes
Canada (Central) ca-central-1 Yes
Europe (Frankfurt) eu-central-1 Yes
Europe (Ireland) eu-west-1 Yes
Europe (London) eu-west-2 Yes
Europe (Paris) eu-west-3 Yes
Europe (Milan) eu-south-1 Yes
Europe (Stockholm) eu-north-1 Yes
Africa (Cape Town) af-south-1 Yes
South America (São Paulo) sa-east-1 Yes
Middle East (Bahrain) me-south-1 Yes
Asia Paciﬁc (Hyderabad) ap-south-2 Yes
Europe (Zurich) eu-central-2 Yes
Using service-linked roles 88
IAM Roles Anywhere User Guide
Region name Region identity Support in IAM 
Roles Anywhere
Europe (Spain) eu-south-2 Yes
Middle East (UAE) me-central-1 Yes
Asia Paciﬁc (Melbourne) ap-southeast-4 Yes
Israel (Tel Aviv) il-central-1 Yes
Canada West (Calgary) ca-west-1 Yes
Asia Paciﬁc (Thailand) ap-southeast-7 Yes
Asia Paciﬁc (Malaysia) ap-southeast-5 Yes
Mexico (Central) mx-central-1 Yes
Asia Paciﬁc (Taipei) ap-east-2 Yes
Asia Paciﬁc (New Zealand) ap-southeast-6 Yes
AWS GovCloud (US-West) us-gov-west-1 Yes
AWS GovCloud (US-East) us-gov-east-1 Yes
AWS managed policies for IAM Roles Anywhere
An AWS managed policy is a standalone policy that is created and administered by AWS. AWS 
managed policies are designed to provide permissions for many common use cases so that you can 
start assigning permissions to users, groups, and roles.
Keep in mind that AWS managed policies might not grant least-privilege permissions for your 
speciﬁc use cases because they're available for all AWS customers to use. We recommend that you 
reduce permissions further by deﬁning  customer managed policies that are speciﬁc to your use 
cases.
AWS managed policies 89
IAM Roles Anywhere User Guide
You cannot change the permissions deﬁned in AWS managed policies. If AWS updates the 
permissions deﬁned in an AWS managed policy, the update aﬀects all principal identities (users, 
groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed 
policy when a new AWS service is launched or new API operations become available for existing 
services.
For more information, see AWS managed policies in the IAM User Guide.
AWS managed policy: AWSRolesAnywhereServicePolicy
AWSRolesAnywhereServicePolicy provides the required permissions to publish metrics data 
to CloudWatch namespaces (AWS/RolesAnywhere and AWS/Usage).  This policy also grants 
permissions to list information about your private certiﬁcate authority (CA) and retrieve the 
certiﬁcate and certiﬁcate chain for your private CA from AWS Private CA.
You can't attach AWSRolesAnywhereServicePolicy to your IAM entities. This policy is attached to 
a service-linked role that allows IAM Roles Anywhere to perform actions on your behalf. For more 
information, see  Service-linked role permissions for IAM Roles Anywhere.
This policy grants administrative permissions that allow IAM Roles Anywhere to publish 
CloudWatch metrics  and check the conﬁguration of AWS Private CA.
Permissions details
This policy includes the following permissions.
• cloudwatch – Allows principals to publish metric data points to the AWS/RolesAnywhere and
AWS/Usage namespaces.
• acm-pca – Allows principals to list information about your private certiﬁcate authority (CA) and 
retrieve the certiﬁcate and certiﬁcate chain for your private CA from AWS Private CA.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
AWS managed policies 90
IAM Roles Anywhere User Guide
        "Effect": "Allow", 
        "Action": [ 
          "cloudwatch:PutMetricData" 
        ], 
        "Resource": "*", 
        "Condition": { 
          "StringEquals": { 
            "cloudwatch:namespace": [ 
              "AWS/RolesAnywhere", 
              "AWS/Usage" 
            ] 
          } 
        } 
      }, 
      { 
        "Effect": "Allow", 
        "Action": [ 
          "acm-pca:GetCertificateAuthorityCertificate", 
          "acm-pca:DescribeCertificateAuthority" 
        ], 
        "Resource": "arn:aws:acm-pca:*:*:*" 
      } 
    ] 
  }
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
      { 
        "Effect": "Allow", 
        "Action": [ 
          "cloudwatch:PutMetricData" 
        ], 
        "Resource": "*", 
        "Condition": { 
          "StringEquals": { 
            "cloudwatch:namespace": [ 
              "AWS/RolesAnywhere", 
              "AWS/Usage" 
            ] 
AWS managed policies 91
IAM Roles Anywhere User Guide
          } 
        } 
      } 
    ] 
  }
For more information and deﬁnition of this policy, see: AWSRolesAnywhereServicePolicy.
AWS managed policy: AWSRolesAnywhereFullAccess
This policy provides all permissions to IAM Roles Anywhere resources, including but not limited to: 
CreateProﬁle, DeleteTrustAnchor, DisableCRL, ResetNotiﬁcationSettings.
You can attach the AWSRolesAnywhereFullAccess policy to your IAM identities.
This policy grants full access permissions that allow users to view, create, update, and delete all 
IAM Roles Anywhere resources.
Permissions details
This policy includes the following permissions:
• rolesanywhere – Allows principals to perform all actions on IAM Roles Anywhere resources 
including trust anchors, proﬁles, CRLs, subjects, and notiﬁcation settings.
• iam:PassRole – Allows principals to pass a role to IAM Roles Anywhere.
• iam:CreateServiceLinkedRole – Allows principals to create the service-linked role for IAM 
Roles Anywhere. This permission is needed when the service-linked role doesn't exist in the 
account yet.
For more information and deﬁnition of this policy, see AWSRolesAnywhereFullAccess.
AWS managed policy: AWSRolesAnywhereReadOnly
This policy provides read-only permissions to IAM Roles Anywhere resources, including but not 
limited to: GetTrustAnchor, ListProﬁles, GetCRL.
You can attach the AWSRolesAnywhereReadOnly policy to your IAM identities.
This policy grants read-only permissions that allow users to view IAM Roles Anywhere resources 
but not modify them.
AWS managed policies 92
IAM Roles Anywhere User Guide
Permissions details
This policy includes the following permissions:
• rolesanywhere – Allows principals to view all IAM Roles Anywhere resources including trust 
anchors, proﬁles, CRLs, and subjects.
For more information and deﬁnition of this policy, see AWSRolesAnywhereReadOnly.
IAM Roles Anywhere updates to AWS managed policies
View details about updates to AWS managed policies for IAM Roles Anywhere since this service 
began tracking these changes. For automatic alerts about changes to this page, subscribe to the 
RSS feed on the IAM Roles Anywhere  Document history page.
Change Description Date
AWSRolesAnywhereFullAccess
– New policy
IAM Roles Anywhere added 
a new policy to allow users 
to grant full access IAM Roles 
Anywhere permissions to 
principals in a standardized 
way.
July 16, 2025
AWSRolesAnywhereReadOnly
– New policy
IAM Roles Anywhere added 
a new policy to allow users 
to grant read only IAM Roles 
Anywhere permissions to 
principals in a standardized 
way.
July 16, 2025
IAM Roles Anywhere started 
tracking changes
IAM Roles Anywhere started 
tracking changes for its AWS 
managed policies.
February 27, 2023
AWS managed policies 93
IAM Roles Anywhere User Guide
Disaster recovery and resilience in IAM Roles Anywhere
The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions 
provide multiple physically separated and isolated Availability Zones, which are connected with 
low-latency, high-throughput, and highly redundant networking. With Availability Zones, you 
can design and operate applications and databases that automatically fail over between zones 
without interruption. Availability Zones are more highly available, fault tolerant, and scalable than 
traditional single or multiple data center infrastructures.
For more information about AWS Regions and Availability Zones, see AWS Global Infrastructure.
IAM Roles Anywhere and interface VPC endpoints (AWS 
PrivateLink)
You can establish a private connection between your VPC and AWS Identity and Access 
Management Roles Anywhere by creating an interface VPC endpoint. Interface endpoints are 
powered by AWS PrivateLink, a technology that enables you to privately access IAM Roles 
Anywhere APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect 
connection. Instances in your VPC don't need public IP addresses to communicate with IAM Roles 
Anywhere APIs. Traﬃc between your VPC and IAM Roles Anywhere does not leave the Amazon 
network.
Each interface endpoint is represented by one or more Elastic Network Interfaces in your subnets.
For more information, see Interface VPC endpoints (AWS PrivateLink) in the Amazon VPC User 
Guide.
Considerations for IAM Roles Anywhere VPC endpoints
Before you set up an interface VPC endpoint for IAM Roles Anywhere, ensure that you review
Interface endpoint properties and limitations in the Amazon VPC User Guide.
IAM Roles Anywhere supports making calls to all of its API actions from your VPC.
Note
VPC endpoint policies are supported for IAM Roles Anywhere on all API methods except
CreateSession.
Resilience 94
IAM Roles Anywhere User Guide
Full access to IAM Roles Anywhere is allowed through the endpoint by default, including
CreateSession. For more information, see Controlling access to services with VPC endpoints in 
the Amazon VPC User Guide.
Creating an interface VPC endpoint for IAM Roles Anywhere
You can create a VPC endpoint for the IAM Roles Anywhere service using either the Amazon VPC 
console or the AWS Command Line Interface (AWS CLI). For more information, see Creating an 
interface endpoint in the Amazon VPC User Guide.
Create a VPC endpoint for IAM Roles Anywhere using the following service name:
• com.amazonaws.region.rolesanywhere
If you enable private DNS for the endpoint, you can make API requests to IAM Roles 
Anywhere using its default DNS name for the Region, for example, rolesanywhere.us-
east-1.amazonaws.com.
For more information, see Accessing a service through an interface endpoint in the Amazon VPC 
User Guide.
Creating a VPC endpoint policy for IAM Roles Anywhere
You can attach an endpoint policy to your VPC endpoint that controls access to IAM Roles 
Anywhere. The policy speciﬁes the following information:
• The principal that can perform actions.
• The actions that can be performed.
• The resources on which actions can be performed.
For more information, see Controlling access to services with VPC endpoints in the Amazon VPC 
User Guide.
Example: VPC endpoint policy for IAM Roles Anywhere actions
The following is an example of an endpoint policy for IAM Roles Anywhere. When attached to an 
endpoint, this policy grants access to the listed IAM Roles Anywhere actions for all principals on all 
resources.
Creating an interface VPC endpoint for IAM Roles Anywhere 95
IAM Roles Anywhere User Guide
{ 
   "Statement":[ 
      { 
         "Principal":"*", 
         "Effect":"Allow", 
         "Action":[ 
            "rolesanywhere:CreateTrustAnchor", 
            "rolesanywhere:CreateProfile", 
            "rolesanywhere:UpdateProfile" 
         ], 
         "Resource":"*" 
      } 
   ]
}
Control API access with IAM policies
If you use IAM policies to control access to AWS services based on IP addresses, you might 
need to update your policies to include IPv6 address ranges. This guide explains the diﬀerences 
between IPv4 and IPv6 and describes how to update your IAM policies to support both protocols. 
Implementing these changes helps you maintain secure access to your AWS resources while 
supporting IPv6.
What is IPv6?
IPv6 is the next generation IP standard intended to eventually replace IPv4. The previous version, 
IPv4, uses a 32-bit addressing scheme to support 4.3 billion devices. IPv6 instead uses 128-bit 
addressing to support approximately 340 trillion trillion trillion (or 2 to the 128th power) devices.
For more information, see the VPC IPv6 web page.
These are examples of IPv6 addresses:
2001:cdba:0000:0000:0000:0000:3257:9652 # This is a full, unabbreviated IPv6 address.
2001:cdba:0:0:0:0:3257:9652             # The same address with leading zeros in each 
 group omitted
2001:cdba::3257:965                     # A compressed version of the same address.
IPv4 and IPv6 access 96
IAM Roles Anywhere User Guide
IAM dual-stack (IPv4 and IPv6) policies
You can use IAM policies to control access to IAM Roles Anywhere APIs and prevent IP addresses 
outside the conﬁgured range from accessing IAM Roles Anywhere APIs.
The rolesanywhere.{region}.api.aws dual-stack endpoint for IAM Roles Anywhere APIs supports both 
IPv6 and IPv4.
If you need to support both IPv4 and IPv6, update your IP address ﬁltering policies to handle IPv6 
addresses. Otherwise, you might not be able to connect to IAM Roles Anywhere over IPv6.
Who should make this change?
This change aﬀects you if you use dual addressing with policies that contain aws:sourceIp. Dual 
addressing means that the network supports both IPv4 and IPv6.
If you use dual addressing, update your IAM policies that currently use IPv4 format addresses to 
include IPv6 format addresses.
Who should not make this change?
This change doesn't aﬀect you if you only use IPv4 networks.
Adding IPv6 to an IAM policy
IAM policies use the aws:SourceIp condition key to control access from speciﬁc IP addresses.If 
your network uses dual addressing (IPv4 and IPv6), update your IAM policies to include IPv6 
address ranges.
In the Condition element of your policies, use the IpAddress and NotIpAddress operators 
for IP address conditions. Don't use string operators, as they can't handle the various valid IPv6 
address formats.
These examples use aws:SourceIp. For VPCs, use aws:VpcSourceIp instead.
The following is the Denies access to AWS based on the source IP reference policy from the IAM 
User Guide. The NotIPAddress in the Condition element to lists two IPv4 address ranges,
192.0.2.0/24 and 203.0.113.0/24, which will be denied access to the API.
Using dual-stack policies 97
IAM Roles Anywhere User Guide
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": { 
        "Effect": "Deny", 
        "Action": "*", 
        "Resource": "*", 
        "Condition": { 
            "NotIpAddress": { 
                "aws:SourceIp": [ 
                    "192.0.2.0/24", 
                    "203.0.113.0/24" 
                ] 
            }, 
            "Bool": { 
                "aws:ViaAWSService": "false" 
            } 
        } 
    }
}
To update this policy, change the Condition element to include the IPv6 address ranges
2001:DB8:1234:5678::/64 and 2001:cdba:3257:8593::/64.
Note
Don't remove the existing IPv4 addresses. They're needed for backward compatibility.
"Condition": { 
                "NotIpAddress": { 
                    "aws:SourceIp": [ 
                        "192.0.2.0/24", <<DO NOT REMOVE existing IPv4 address>> 
                        "203.0.113.0/24", <<DO NOT REMOVE existing IPv4 address>> 
                         "2001:DB8:1234:5678::/64", <<New IPv6 IP address>> 
                        "2001:cdba:3257:8593::/64" <<New IPv6 IP address>>
                    ] 
                }, 
                "Bool": { 
Adding IPv6 to a policy 98
IAM Roles Anywhere User Guide
                    "aws:ViaAWSService": "false" 
                } 
            }
Verifying your client supports IPv6
If you use the rolesanywhere.{region}.api.aws endpoint, verify that you can connect to it. The 
following steps describe how to perform the veriﬁcation.
This examples uses Linux and curl version 8.6.0 and uses the AWS Identity and Access Management 
Roles Anywhere service endpoints which has IPv6 enabled endpoints located at the api.aws
endpoint.
Note
Switch the AWS Region to the same Region where your service is located. In this example, 
we use the US East (N. Virginia) – us-east-1 endpoint.
1. Determine if the endpoint resolves with an IPv6 address using the following dig command.
$ dig +short AAAA rolesanywhere.us-east-1.api.aws
> 2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
2. Determine if the client network can make an IPv6 connection using the following curl
command. A 404 response code means the connection succeeded, while a 0 response code 
means the connection failed.
$ curl --ipv6 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: 
 %{response_code}\n" https://rolesanywhere.us-east-1.api.aws
> remote ip: 2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
> response code: 404
If a remote IP was identiﬁed and the response code is not 0, a network connection was successfully 
made to the endpoint using IPv6. The remote IP should be an IPv6 address because the operating 
system should select the protocol that is valid for the client. If the remote IP is not an IPv6 address, 
use the following command to force curl to use IPv4.
Verifying your client supports IPv6 99
IAM Roles Anywhere User Guide
$ curl --ipv4 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: 
 %{response_code}\n" https://rolesanywhere.us-east-1.api.aws
> remote ip: 3.123.154.250
> response code: 404
If the remote IP is blank or the response code is 0, the client network or the network path to the 
endpoint is IPv4-only. You can verify this conﬁguration with the following curl command.
$ curl -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: 
 %{response_code}\n" https://rolesanywhere.us-east-1.api.aws
> remote ip: 3.123.154.250
> response code: 404
Verifying your client supports IPv6 100
IAM Roles Anywhere User Guide
AWS services for monitoring IAM Roles Anywhere
Monitoring is an important part of maintaining the reliability, availability, and performance of AWS 
Identity and Access Management Roles Anywhere and your other AWS solutions. AWS provides the 
following monitoring tools to watch IAM Roles Anywhere, report when something is wrong, and 
take automatic actions when appropriate:
• Amazon CloudWatch monitors your AWS resources and the applications you run on AWS in real 
time. You can collect and track metrics, create customized dashboards, and set alarms that notify 
you or take actions when a speciﬁed metric reaches a threshold that you specify. For example, 
you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances 
and automatically launch new instances when needed. For more information, see the Amazon 
CloudWatch User Guide.
• Amazon EventBridge can be used to automate your AWS services and respond automatically 
to system events, such as application availability issues or resource changes. Events from AWS 
services are delivered to EventBridge in near real time. You can write simple rules to indicate 
which events are of interest to you and which automated actions to take when an event matches 
a rule. For more information, see Amazon EventBridge User Guide.
• Amazon EventBridge is a serverless event bus service that makes it easy to connect your 
applications with data from a variety of sources. EventBridge delivers a stream of real-time 
data from your own applications, Software-as-a-Service (SaaS) applications, and AWS services 
and routes that data to targets such as Lambda. This enables you to monitor events that 
happen in services, and build event-driven architectures. For more information, see the Amazon 
EventBridge User Guide.
• AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account 
and delivers the log ﬁles to an Amazon S3 bucket that you specify. You can identify which users 
and accounts called AWS, the source IP address from which the calls were made, and when the 
calls occurred. For more information, see the AWS CloudTrail User Guide.
Customize notiﬁcation settings in IAM Roles Anywhere
You can customize notiﬁcation settings based on your public key infrastructure. These settings are 
attached to your trust anchor and allow you to deﬁne custom thresholds for a notiﬁcation event. 
IAM Roles Anywhere will consume these settings while evaluating for a notiﬁcation event to send 
metrics/events/notiﬁcations through their respective notiﬁcation channels.
Customize notiﬁcation settings 101
IAM Roles Anywhere User Guide
Topics
• Notiﬁcation events
• Notiﬁcation channels
• IAM Roles Anywhere default notiﬁcation settings
• Notiﬁcation evaluation criteria
• Conﬁguring custom notiﬁcation threshold (console)
• Disabling a notiﬁcation setting (console)
Notiﬁcation events
• CA certiﬁcate expiry: IAM Roles Anywhere sends notiﬁcation when a certiﬁcate authority (CA) in 
your trust anchor is approaching expiry.
• End-entity certiﬁcate expiry: IAM Roles Anywhere sends notiﬁcation when your end-entity 
certiﬁcate used to vend temporary security credentials is expiring soon.
Notiﬁcation channels
Note
Notiﬁcation channel with a value of ALL will apply the custom settings to all the channels 
listed below.
• Amazon CloudWatch metrics
• Amazon EventBridge events
• AWS Health notiﬁcations
IAM Roles Anywhere default notiﬁcation settings
Following are the default notiﬁcation settings IAM Roles Anywhere has deﬁned. These values are 
applied in the absence of custom notiﬁcation settings.
Notiﬁcation events 102
IAM Roles Anywhere User Guide
Event Channel Threshold Enabled
CA certiﬁcate 
expiry
CloudWatch, EventBrid 
ge and AWS Health
45 days before expiry True
End entity 
certiﬁcate 
expiry
EventBridge and AWS 
Health
45 days before expiry True
Notiﬁcation evaluation criteria
Following are the evaluation criteria used to send notiﬁcation events.
These criteria do not apply if your notiﬁcation setting is in a disabled state.
Event Channel Starts when Ends at
CA certiﬁca 
te expiry
CloudWatch Number of days until certiﬁcate expiry 
≤ threshold
Day of certiﬁcate 
expiry
CA certiﬁca 
te expiry
EventBridge and 
AWS Health
Number of days until certiﬁcate expiry 
≤ threshold
14 days after 
certiﬁcate expires
End-entity 
certiﬁcate 
expiry
EventBridge and 
AWS Health
Number of days until certiﬁcate expiry 
≤ threshold
Day of certiﬁcate 
expiry
Conﬁguring custom notiﬁcation threshold (console)
1. Sign in to IAM Roles Anywhere console.
2. Scroll to ﬁnd trust anchor table and choose the trust anchor to apply custom notiﬁcation 
settings.
3. Within trust anchor detail page scroll towards Notiﬁcation settings section and choose
Manage settings.
Notiﬁcation evaluation criteria 103
IAM Roles Anywhere User Guide
4. Customize threshold for the notiﬁcation event. IAM Roles Anywhere will start sending 
metrics/events/notiﬁcations when number of days until your X.509 certiﬁcate expires is less 
than or equal this threshold. See IAM Roles Anywhere notiﬁcation evaluation criteria.
5. Choose Save changes to apply custom notiﬁcation threshold.
Disabling a notiﬁcation setting (console)
1. Sign in to IAM Roles Anywhere console.
2. Scroll to ﬁnd trust anchor table and choose the trust anchor to apply custom notiﬁcation 
settings.
3. Within trust anchor detail page scroll towards Notiﬁcation settings section and choose
Manage settings.
4. Choose the table cell from Status column for notiﬁcation event name End entity certiﬁcate 
expiry.
5. From the options displayed in the selection pane choose the Disable option.
6. Choose Save changes to apply to disable notiﬁcation settings for end-entity certiﬁcate expiry 
event.
Monitoring IAM Roles Anywhere with Amazon CloudWatch
You can monitor AWS Identity and Access Management Roles Anywhere using CloudWatch, which 
collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 
15 months, so that you can access historical information and gain a better perspective on how your 
web application or service is performing. You can also set alarms that watch for certain thresholds, 
and send notiﬁcations or take actions when those thresholds are met. For more information, see 
the Amazon CloudWatch User Guide.
For IAM Roles Anywhere, you might want to watch for trust anchor and end-entity certiﬁcates 
expiration dates and renew your certiﬁcates when your certiﬁcates are nearing expiration.
The IAM Roles Anywhere service reports the following metrics in the AWS/RolesAnywhere
namespace.
Disabling a notiﬁcation setting (console) 104
IAM Roles Anywhere User Guide
Metric Description
Success Gets published every time CreateSession  succeeds in returning 
credentials to the user.
Valid Dimensions: Operation, TrustAnchorArn
Valid Statistic: Sum
Units: Count
Failure Gets published every time CreateSession  fails to return credentials 
to the user.
Valid Dimensions: Operation, ErrorType
Valid Statistic: Sum
Units: Count
DaysToExpiry Gets published every time trust anchor certiﬁcates satisﬁes notiﬁcation 
evaluation criteria. This metric will be published at most once a day.
Valid Dimensions: TrustAnchorArn
Units: Integer
The following dimensions are supported for the IAM Roles Anywhere metrics.
Dimension Description
Operation The operation for which the metric applies to. This can only 
take on the value, CreateSession.
TrustAnchorArn The ARN of the trust anchor that is relevant for this metric.
ErrorType The type of error that CreateSession  errors out with.
Monitoring with CloudWatch 105
IAM Roles Anywhere User Guide
Monitoring IAM Roles Anywhere events in Amazon EventBridge
You can monitor IAM Roles Anywhere events in Amazon EventBridge. Events from IAM Roles 
Anywhere are delivered to EventBridge in near-real time. You can write simple rules to indicate 
which events are of interest to you and the automated actions to take when an event matches a 
rule. With EventBridge, you can use events to trigger targets including AWS Lambda functions, 
AWS Batch jobs, Amazon SNS topics, and many others. For more information, see Creating Amazon 
EventBridge rules that react to events.
The following examples show events for IAM Roles Anywhere.
Topics
• Trust anchor certiﬁcate expiration event
• Intermediate or end-entity certiﬁcate expiration event
• Responding to an event
Trust anchor certiﬁcate expiration event
IAM Roles Anywhere sends daily expiration event for each trust anchor certiﬁcate that satisﬁes
notiﬁcation evaluation criteria. You can use expiration events to conﬁgure Amazon SNS to send a 
text notiﬁcation whenever IAM Roles Anywhere generates this event.
Expiration events have the following structure.
{ 
  "version": "0", 
  "id": "9c95e8e4-96a4-ef3f-b739-b6aa5b193afb", 
  "detail-type": "Roles Anywhere Certificate Expiration State Change", 
  "source": "aws.rolesanywhere", 
  "account": "123456789012", 
  "time": "2022-06-10T06:51:08Z", 
  "region": "us-west-1", 
  "resources": [ 
    "arn:aws:rolesanywhere:us-west-1:123456789012:trust-anchor/61f50cd4-45b9-4259-b049-
d0a53682fa4b" 
  ], 
  "detail": { 
    "certificate-serial-number": "00936EACBE07F201DF", 
    "days-to-expiry": 3, 
Monitoring events with Amazon EventBridge 106
IAM Roles Anywhere User Guide
    "issuer": "L=Seattle,CN=CA Root v1,ST=Washington,C=US" 
  }
}
Intermediate or end-entity certiﬁcate expiration event
IAM Roles Anywhere sends an expiration event for intermediate or end-entity certiﬁcates when 
the certiﬁcate satisﬁes notiﬁcation evaluation criteria and used in createSession API. You can 
use expiration events to conﬁgure Amazon SNS to send a text notiﬁcation whenever IAM Roles 
Anywhere generates this event.
Expiration events have the following structure.
{ 
  "version": "0", 
  "id": "9c95e8e4-96a4-ef3f-b739-b6aa5b193afb", 
  "detail-type": "Roles Anywhere Certificate Expiration State Change", 
  "source": "aws.rolesanywhere", 
  "account": "123456789012", 
  "time": "2022-06-10T06:51:08Z", 
  "region": "us-west-1", 
  "detail": { 
    "certificate-serial-number": "00936EACBE07F201DF", 
    "days-to-expiry": 3, 
    "issuer": "L=Seattle,CN=CA Root v1,ST=Washington,C=US" 
  }
}
Responding to an event
You can conﬁgure Amazon Simple Notiﬁcation Service to send a text notiﬁcation whenever IAM 
Roles Anywhere generates an EventBridge event.
To create an Amazon EventBridge rule that reacts to events
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. In the navigation pane, choose Rules.
3. Choose Create rule.
4. Enter a name and description for the rule.
Intermediate or end-entity certiﬁcate expiration event 107
IAM Roles Anywhere User Guide
A rule can't have the same name as another rule in the same Region and on the same event 
bus.
5. For Event bus, choose the event bus that you want to associate with this rule. If you want this 
rule to match events that come from your account, select  AWS default event bus. When an 
AWS service in your account emits an event, it always goes to your account’s default event bus.
6. For Rule type, choose Rule with an event pattern.
7. Choose Next.
8. For Event source, choose AWS services.
9. For Sample events, choose an event under IAM Roles Anywhere.
10. For Event pattern, do the following:
a. For Event source, choose AWS services.
b. For AWS service, choose IAM Roles Anywhere.
c. For Event Type, choose an IAM Roles Anywhere event.
d. Choose Next
11. In the Targets section, choose a service that can consume your event such as Amazon SNS, or 
choose Lambda function to pass the event to customized executable code.
Monitoring IAM Roles Anywhere notiﬁcations with AWS Health
You can monitor IAM Roles Anywhere health notiﬁcations in AWS Health. Notiﬁcations from IAM 
Roles Anywhere are delivered to AWS Health when certiﬁcates (both CA certiﬁcates in trust anchors 
and end-entity certiﬁcates) that are conﬁgured with IAM Roles Anywhere are nearing expiry. You 
can use these AWS Health notiﬁcations to take renewal actions on your certiﬁcates. For more 
information see Monitoring AWS Health events with Amazon EventBridge
Aﬀected resources for trust anchor expiry notiﬁcations
IAM Roles Anywhere sends daily expiry notiﬁcations for each trust anchor that satisﬁes the
notiﬁcation evaluation criteria. For these notiﬁcations, the "Aﬀected Resources" will each be trust 
anchors. If you have multiple certiﬁcates within a single trust anchor, it's possible that multiple 
are nearing expiry. IAM Roles Anywhere will determine whether a notiﬁcation should be sent 
for a given trust anchor based on the certiﬁcate in the trust anchor that is expiring the soonest. 
Thus, you'll have to check each certiﬁcate in the trust anchor and take the necessary actions so as 
Monitoring IAM Roles Anywhere notiﬁcations 108
IAM Roles Anywhere User Guide
to not cause impact to your workloads that rely on IAM Roles Anywhere for temporary security 
credentials.
Aﬀected resources for end-entity certiﬁcate expiry notiﬁcations
IAM Roles Anywhere also sends daily expiry notiﬁcations for each end-entity certiﬁcate that was 
used to authenticate over the last day and satisﬁes the notiﬁcation evaluation criteria. For these 
notiﬁcations, the "Aﬀected Resources" will each be end-entity certiﬁcates. Each of these end-entity 
certiﬁcates will have a composite "Resource ID/ARN", of the form given below.
serialNumber=SerialNumber;certificateId=CertificateId
The serialNumber in the above resource identiﬁer will contain the value of the serial number 
of the end-entity certiﬁcate that was used for authentication and will be expiring soon. And the
certificateId in the above resource identiﬁer will contain the value of the certiﬁcate ID for that 
certiﬁcate. The certiﬁcate ID is deﬁned as Hex(SHA256(ASN.1 DER Certificate Bytes)), 
where the result is a lowercase hex-encoded string. If you have a PEM ﬁle that contains your 
certiﬁcate data, you can use OpenSSL to convert your certiﬁcate into its DER representation and 
then take the SHA256 hash of the resulting value.
openssl x509 -in end-entity-certificate.pem -inform PEM -outform DER | sha256sum
Logging IAM Roles Anywhere API calls using AWS CloudTrail
AWS Identity and Access Management Roles Anywhere is integrated with AWS CloudTrail, a service 
that provides a record of actions taken by a user, role, or an AWS service in IAM Roles Anywhere. 
CloudTrail captures all API calls for IAM Roles Anywhere as events. The calls captured include calls 
from the IAM Roles Anywhere console and code calls to the IAM Roles Anywhere API operations. 
If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 
bucket, including events for IAM Roles Anywhere. If you don't conﬁgure a trail, you can still view 
the most recent events in the CloudTrail console in Event history. Using the information collected 
by CloudTrail, you can determine the request that was made to IAM Roles Anywhere, the IP address 
from which the request was made, who made the request, when it was made, and additional 
details.
To learn more about CloudTrail, see the AWS CloudTrail User Guide.
Aﬀected resources for end-entity certiﬁcate expiry notiﬁcations 109
IAM Roles Anywhere User Guide
IAM Roles Anywhere information in CloudTrail
CloudTrail is enabled on your AWS account when you create the account. When activity occurs in 
IAM Roles Anywhere, that activity is recorded in a CloudTrail event along with other AWS service 
events in Event history. You can view, search, and download recent events in your AWS account. 
For more information, see Viewing events with CloudTrail Event history.
For an ongoing record of events in your AWS account, including events for IAM Roles Anywhere, 
create a trail. A trail enables CloudTrail to deliver log ﬁles to an Amazon S3 bucket. By default, 
when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events 
from all Regions in the AWS partition and delivers the log ﬁles to the Amazon S3 bucket that you 
specify. Additionally, you can conﬁgure other AWS services to further analyze and act upon the 
event data collected in CloudTrail logs. For more information, see the following:
• Overview for creating a trail
• CloudTrail supported services and integrations
• Conﬁguring Amazon SNS notiﬁcations for CloudTrail
• Receiving CloudTrail log ﬁles from multiple regions and Receiving CloudTrail log ﬁles from 
multiple accounts
All IAM Roles Anywhere actions are logged by CloudTrail and are documented in the IAM Roles 
Anywhere API Reference. For example, calls to the CreateTrustAnchor, ListProfiles, 
and CreateSession operations generate entries in the CloudTrail log ﬁles. In addition, the 
userIdentity element's Role Session Name property is the hex-encoded serial number of the 
certiﬁcate the session was created with and can be used to track a session back to it.
Every event or log entry contains information about who generated the request. The identity 
information helps you determine the following:
• Whether the request was made with root or AWS Identity and Access Management (IAM) user 
credentials.
• Whether the request was made with temporary security credentials for a role or federated user.
• Whether the request was made by another AWS service.
For more information, see the CloudTrail userIdentity element.
IAM Roles Anywhere information in CloudTrail 110
IAM Roles Anywhere User Guide
Understanding IAM Roles Anywhere log ﬁle entries
A trail is a conﬁguration that enables delivery of events as log ﬁles to an Amazon S3 bucket that 
you specify. CloudTrail log ﬁles contain one or more log entries. An event represents a single 
request from any source and includes information about the requested action, the date and time of 
the action, request parameters, and so on. CloudTrail log ﬁles aren't an ordered stack trace of the 
public API calls, so they don't appear in any speciﬁc order.
The following example shows a CloudTrail log entry that demonstrates the UpdateProfile
operation.
{ 
  "eventVersion": "1.08", 
  "userIdentity": { 
    "type": "AssumedRole", 
    "principalId": "AROAZR5EMTJKE753U4ZDS:test-session", 
    "arn": "arn:aws:sts::111122223333:assumed-role/Admin/test-session", 
    "accountId": "111122223333", 
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE", 
    "sessionContext": { 
      "sessionIssuer": { 
        "type": "Role", 
        "principalId": "AROAZR5EMTJKE753U4ZDS", 
        "arn": "arn:aws:iam::111122223333:role/Admin", 
        "accountId": "111122223333", 
        "userName": "Admin" 
      }, 
      "webIdFederationData": {}, 
      "attributes": { 
        "creationDate": "2022-03-21T22:40:46Z", 
        "mfaAuthenticated": "false" 
      } 
    } 
  }, 
  "eventTime": "2022-07-01T18:11:27Z", 
  "eventSource": "rolesanywhere.amazonaws.com", 
  "eventName": "UpdateProfile", 
  "awsRegion": "us-east-1", 
  "sourceIPAddress": "1.1.1.1", 
  "userAgent": "test-agent", 
  "requestParameters": { 
    "durationSeconds": 3600, 
Understanding IAM Roles Anywhere log ﬁle entries 111
IAM Roles Anywhere User Guide
    "managedPolicyArns": [ 
        "arn:aws:iam::aws:policy/AdministratorAccess", 
        "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" 
    ], 
    "name": "Updated Test Profile", 
    "profileId": "0ace5b12-24b9-427e-a483-c55884852fbf", 
    "sessionPolicy": "{\n  \"Version\":\"2012-10-17\",\n  \"Statement\":[\n    {\n    
   \"Effect\":\"Allow\",\n      \"Action\":\"s3:ListObjects\",\n      \"Resource\":\"*
\"\n    }\n  ]\n}\n"
},
"responseElements": { 
  "profile": { 
      "createdAt": "2022-07-01T18:11:27.380711Z", 
      "createdBy": "arn:aws:sts::111122223333:assumed-role/Admin/test-session", 
      "durationSeconds": 3600, 
      "enabled": false, 
      "managedPolicyArns": [ 
          "arn:aws:iam::aws:policy/AdministratorAccess", 
          "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" 
      ], 
      "name": "Updated Test Profile", 
      "profileArn": "arn:aws:rolesanywhere:us-
east-1:111122223333:profile/0ace5b12-24b9-427e-a483-c55884852fbf", 
      "profileId": "0ace5b12-24b9-427e-a483-c55884852fbf", 
      "requireInstanceProperties": false, 
      "roleArns": [ 
          "arn:aws:iam::111122223333:role/test-role" 
      ], 
      "sessionPolicy": "{\n  \"Version\":\"2012-10-17\",\n  \"Statement\":[\n    {\n   
    \"Effect\":\"Allow\",\n      \"Action\":\"s3:ListObjects\",\n      \"Resource\":\"*
\"\n    }\n  ]\n}\n", 
      "updatedAt": "2022-07-01T18:11:27.936687Z" 
  }
}, 
  "requestID": "ca28860f-504a-4f2d-9f3f-f9cfb4ba0491", 
  "eventID": "a7bb90c3-c47b-4832-88e7-aeaccda21f1a", 
  "readOnly": false, 
  "eventType": "AwsApiCall", 
  "managementEvent": true, 
  "recipientAccountId": "111122223333", 
  "eventCategory": "Management", 
  "tlsDetails": { 
    "clientProvidedHostHeader": "rolesanywhere.us-east-1.amazonaws.com" 
  }
Understanding IAM Roles Anywhere log ﬁle entries 112
IAM Roles Anywhere User Guide
}
Monitoring authentications with IAM Roles Anywhere subjects
You can use the Subject Activity tab in the IAM Roles Anywhere console to visualize and audit 
activities for certiﬁcates that are authenticated with IAM Roles Anywhere. A subject represents a 
unique identity deﬁned by the X.509 subject of any certiﬁcates you use to authenticate with IAM 
Roles Anywhere. IAM Roles Anywhere creates a subject for you at the time of authentication if 
there isn't one already for the X.509 subject. Each subject contains the most recent certiﬁcates you 
have used with IAM Roles Anywhere.
To view the history of an X.509 subject
1. Sign in to the IAM Roles Anywhere console.
2. Navigate to the Subject activity tab.
3. In the list of certiﬁcates records grouped by X.509 Subject, choose the Subject record that you 
want to check.
4. On the Subject details page, view the details of the subject record.
5. In the Certiﬁcates section, you can see the most recent record for certiﬁcates authenticated 
with IAM Roles Anywhere that have the same certiﬁcate subject.
6. Choose the Serial number record to view or copy the certiﬁcate body.
Monitoring with IAM Roles Anywhere subjects 113
IAM Roles Anywhere User Guide
Create IAM Roles Anywhere resources with AWS 
CloudFormation
AWS Identity and Access Management Roles Anywhere is integrated with AWS CloudFormation, 
a service that helps you to model and set up your AWS resources so that you can spend 
less time creating and managing your resources and infrastructure. You create a template 
that describes all the AWS resources that you want (such as AWS::RolesAnywhere::Crl,
AWS::RolesAnywhere::Profile, and AWS::RolesAnywhere::TrustAnchor), and 
CloudFormation provisions and conﬁgures those resources for you. For more information, see 
resource type reference in the AWS CloudFormation User Guide.
When you use CloudFormation, you can reuse your template to set up your IAM Roles Anywhere 
resources consistently and repeatedly. Describe your resources once, and then provision the same 
resources over and over in multiple AWS accounts and Regions.
IAM Roles Anywhere and CloudFormation templates
To provision and conﬁgure resources for IAM Roles Anywhere and related services, you must 
understand CloudFormation templates. Templates are formatted text ﬁles in JSON or YAML. These 
templates describe the resources that you want to provision in your CloudFormation stacks. If 
you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started 
with CloudFormation templates. For more information, see What is CloudFormation Designer? in 
the AWS CloudFormation User Guide.
IAM Roles Anywhere supports creating certiﬁcate revocation lists, trust anchors, and proﬁles in 
CloudFormation. For more information, including examples of JSON and YAML templates for CRL,
TrustAnchor, and Proﬁle, see the AWS CloudFormation User Guide.
Learn more about CloudFormation
To learn more about CloudFormation, see the following resources:
• AWS CloudFormation
• AWS CloudFormation User Guide
• CloudFormation API Reference
IAM Roles Anywhere and CloudFormation templates 114
IAM Roles Anywhere User Guide
• AWS CloudFormation Command Line Interface User Guide
Learn more about CloudFormation 115
IAM Roles Anywhere User Guide
Quotas for AWS Identity and Access Management Roles 
Anywhere
Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless 
otherwise noted, each quota is Region-speciﬁc. You can request increases for some quotas, and 
other quotas cannot be increased.
To view the quotas for AWS Identity and Access Management Roles Anywhere, open the Service 
Quotas console. In the navigation pane, choose AWS services and select IAM Roles Anywhere.
To request a quota increase, see Requesting a Quota Increase in the Service Quotas User Guide. If 
the quota is not yet available in Service Quotas, use the limit increase form.
Your AWS account has the following quotas related to IAM Roles Anywhere and each quota is per 
AWS Region.
Resource Description Default value Adjustable
Combined rate of 
trust anchor requests
The maximum 
transactions per 
second for ListTrust 
Anchors, CreateTru 
stAnchor, GetTrustA 
nchor, UpdateTru 
stAnchor, DeleteTru 
stAnchor, EnableTru 
stAnchor, and 
DisableTrustAnchor 
requests combined.
1 per second Yes
Combined rate of 
proﬁle requests
The maximum 
transactions per 
second for ListProﬁ 
les, CreatePro 
ﬁle, GetProﬁle, 
UpdateProﬁle, 
DeleteProﬁle, 
1 per second Yes
116
IAM Roles Anywhere User Guide
Resource Description Default value Adjustable
EnableProﬁle, 
and DisableProﬁle 
requests combined.
Combined rate of 
subject requests
The maximum 
transactions per 
second for ListSubje 
cts and GetSubject 
requests combined.
1 per second Yes
Combined rate of 
tagging requests
The maximum 
transactions per 
second for TagResour 
ce, UntagReso 
urce, and ListTagsF 
orResource requests 
combined.
1 per second Yes
Combined rate of CRL 
requests
The maximum 
transactions per 
second for ListCrls, 
GetCrl, ImportCrl, 
UpdateCrl, DeleteCrl 
, EnableCrl, and 
DisableCrl requests 
combined.
1 per second Yes
Rate of CreateSession 
requests
The maximum 
transactions per 
second for CreateSes 
sion requests.
10 per second Yes
117
IAM Roles Anywhere User Guide
Resource Description Default value Adjustable
Trust anchors The maximum 
number of trust 
anchors that you 
can create within an 
account.
50 Yes
Proﬁles The maximum 
number of proﬁles 
that you can create 
within an account.
250 Yes
CRLs per trust anchor The maximum 
number of Certiﬁca 
te Revocation Lists 
(CRLs) that you can 
create per trust 
anchor within an 
account.
2 No
Certiﬁcates per trust 
anchor
The maximum 
number of certiﬁca 
tes that you can 
create per trust 
anchor within an 
account.
2 No
Roles per proﬁle The maximum 
number of roles that 
you can create per 
proﬁle within an 
account.
250 No
118
IAM Roles Anywhere User Guide
Throttling
Workloads obtain session credentials by using an endpoint that does not use AWS authenticated 
principals, which would typically be used to limit the rate of operations. IAM Roles Anywhere will 
limit the rate of calls to the credential endpoint by the authenticating certiﬁcate information and 
IP address (including VPC Endpoint, if applicable).
Throttling 119
IAM Roles Anywhere User Guide
Document history for the AWS Identity and Access 
Management Roles Anywhere User Guide
The following table describes the documentation releases for IAM Roles Anywhere.
Change Description Date
IAM Roles Anywhere Adds 
support for ML-DSA signature 
s
Update signing specﬁcat 
ion to include AWS4-X509 
-MLDSA in the signing 
specﬁcation. Adds ML-DSA-44 
, ML-DSA-65, ML-DSA-87.
February 27, 2026
IAM Roles Anywhere released 
new AWS managed policies
Introduced new policies: 
  AWSRolesAnywhereReadOnly
and AWSRolesAnywhereFu 
llAccess.
July 16, 2025
Released Credential Helper 
version 1.7.0
IAM Roles Anywhere released 
Credential Helper version 
1.7.0. For more informati 
on, see  Credential Helper 
Changelog.
June 2, 2025
Added IPv6 and dual-stack 
endpoint
Added section for managing 
access to IPv4 and IPv6 
endpoints. See https:// 
docs.aws.amazon.com/rolesa 
nywhere/latest/userguide/ip-
access.html
December 18, 2024
Updated the service-linked 
role description
Updated the service-linked 
role description and added 
role permissions policy. 
For more information, see 
February 27, 2023
120
IAM Roles Anywhere User Guide
Service-linked role permissio 
ns for IAM Roles Anywhere.
Released Credential Helper 
version 1.0.4
IAM Roles Anywhere released 
Credential Helper version 
1.0.4. For more informati 
on, see  Credential Helper 
Changelog.
January 17, 2023
Released Credential Helper 
version 1.0.3
IAM Roles Anywhere released 
Credential Helper version 
1.0.3. For more informati 
on, see  Credential Helper 
Changelog.
December 5, 2022
Released Credential Helper 
version 1.0.2
IAM Roles Anywhere released 
Credential Helper version 
1.0.2. For more informati 
on, see  Credential Helper 
Changelog.
September 8, 2022
Added Signing Process and 
CreateSession
Added Signing Process and 
CreateSession sections. For 
more information, see Signing 
process and CreateSession
July 15, 2022
Released Credential Helper 
version 1.0.1
IAM Roles Anywhere released 
Credential Helper version 
1.0.1. For more informati 
on, see  Credential Helper 
Changelog.
July 14, 2022
Added certiﬁcate revocation Added certiﬁcate revocatio 
n in the IAM Roles Anywhere 
trust model page. For more 
information, see Revocation.
July 13, 2022
121
IAM Roles Anywhere User Guide
Initial release Initial release of the IAM Roles 
Anywhere User Guide
July 5, 2022
122

