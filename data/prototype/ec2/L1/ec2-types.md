# Instance Types

## Instance types

Instance Types
Amazon EC2
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.

## Current generation instances


## Previous generation instances

Amazon EC2 Instance Types
Amazon EC2: Instance Types
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.

## Instance performance

Amazon EC2 Instance Types
Table of Contents
Instance types .................................................................................................................................. 1
Current generation instances ..................................................................................................................... 2
Previous generation instances ................................................................................................................... 2
Instance performance .................................................................................................................................. 3
Naming conventions ........................................................................................................................ 5
Speciﬁcations ................................................................................................................................... 7
General purpose ............................................................................................................................................ 8
Instance families and instance types .................................................................................................. 9
Instance family summary .................................................................................................................... 13
Performance speciﬁcations ................................................................................................................. 17
Network speciﬁcations ......................................................................................................................... 43
Amazon EBS speciﬁcations ................................................................................................................. 73
Instance store speciﬁcations ............................................................................................................ 117
Security speciﬁcations ....................................................................................................................... 126
Compute optimized ................................................................................................................................. 160
Instance families and instance types ............................................................................................. 161
Instance family summary .................................................................................................................. 164
Performance speciﬁcations ............................................................................................................... 166
Network speciﬁcations ...................................................................................................................... 188
Amazon EBS speciﬁcations ............................................................................................................... 213
Instance store speciﬁcations ............................................................................................................ 249
Security speciﬁcations ....................................................................................................................... 256
Memory optimized .................................................................................................................................. 285
Instance families and instance types ............................................................................................. 285
Instance family summary .................................................................................................................. 290
Performance speciﬁcations ............................................................................................................... 295
Network speciﬁcations ...................................................................................................................... 326
Amazon EBS speciﬁcations ............................................................................................................... 362
Instance store speciﬁcations ............................................................................................................ 415
Security speciﬁcations ....................................................................................................................... 427
Storage optimized ................................................................................................................................... 466
Instance families and instance types ............................................................................................. 466
Instance family summary .................................................................................................................. 468
Performance speciﬁcations ............................................................................................................... 469
iii
Amazon EC2 Instance Types
Network speciﬁcations ...................................................................................................................... 479
Amazon EBS speciﬁcations ............................................................................................................... 489
Instance store speciﬁcations ............................................................................................................ 505
Security speciﬁcations ....................................................................................................................... 515
Accelerated computing ........................................................................................................................... 521
Instance families and instance types ............................................................................................. 522
Instance family summary .................................................................................................................. 524
Performance speciﬁcations ............................................................................................................... 527
Network speciﬁcations ...................................................................................................................... 542
Amazon EBS speciﬁcations ............................................................................................................... 552
Instance store speciﬁcations ............................................................................................................ 566
Security speciﬁcations ....................................................................................................................... 574
High-performance computing ............................................................................................................... 581
Instance families and instance types ............................................................................................. 582
Instance family summary .................................................................................................................. 583
Performance speciﬁcations ............................................................................................................... 583
Network speciﬁcations ...................................................................................................................... 585
Amazon EBS speciﬁcations ............................................................................................................... 586
Instance store speciﬁcations ............................................................................................................ 589
Security speciﬁcations ....................................................................................................................... 589
Previous generation ................................................................................................................................. 591
Instance families and instance types ............................................................................................. 592
Instance family summary .................................................................................................................. 593
Performance speciﬁcations ............................................................................................................... 594
Network speciﬁcations ...................................................................................................................... 601
Amazon EBS speciﬁcations ............................................................................................................... 607
Instance store speciﬁcations ............................................................................................................ 616
Security speciﬁcations ....................................................................................................................... 618
Instance types by Region ............................................................................................................ 625
US East (N. Virginia) ................................................................................................................................ 625
US East (Ohio) .......................................................................................................................................... 626
US West (N. California) ........................................................................................................................... 626
US West (Oregon) .................................................................................................................................... 627
Africa (Cape Town) .................................................................................................................................. 627
Asia Paciﬁc (Hong Kong) ........................................................................................................................ 628
Asia Paciﬁc (Hyderabad) ......................................................................................................................... 628
iv

## Naming conventions

Amazon EC2 Instance Types
Asia Paciﬁc (Jakarta) ............................................................................................................................... 628
Asia Paciﬁc (Malaysia) ............................................................................................................................. 629
Asia Paciﬁc (Melbourne) ......................................................................................................................... 629
Asia Paciﬁc (Mumbai) .............................................................................................................................. 629
Asia Paciﬁc (New Zealand) ..................................................................................................................... 630
Asia Paciﬁc (Osaka) .................................................................................................................................. 630
Asia Paciﬁc (Seoul) .................................................................................................................................. 630
Asia Paciﬁc (Singapore) .......................................................................................................................... 631
Asia Paciﬁc (Sydney) ................................................................................................................................ 631
Asia Paciﬁc (Taipei) .................................................................................................................................. 632
Asia Paciﬁc (Thailand) ............................................................................................................................. 632
Asia Paciﬁc (Tokyo) .................................................................................................................................. 632
Canada (Central) ....................................................................................................................................... 633
Canada West (Calgary) ............................................................................................................................ 633
China (Beijing) ........................................................................................................................................... 634
China (Ningxia) ......................................................................................................................................... 634
Europe (Frankfurt) ................................................................................................................................... 634
Europe (Ireland) ........................................................................................................................................ 635
Europe (London) ....................................................................................................................................... 635
Europe (Milan) .......................................................................................................................................... 636
Europe (Paris) ............................................................................................................................................ 636
Europe (Spain) .......................................................................................................................................... 637
Europe (Stockholm) ................................................................................................................................. 637
Europe (Zurich) ......................................................................................................................................... 637
Israel (Tel Aviv) ......................................................................................................................................... 638
Mexico (Central) ........................................................................................................................................ 638
Middle East (Bahrain) .............................................................................................................................. 638
Middle East (UAE) .................................................................................................................................... 639
South America (Sao Paulo) .................................................................................................................... 639
AWS GovCloud (US-East) ....................................................................................................................... 639
AWS GovCloud (US-West) ...................................................................................................................... 640
AWS Nitro System ....................................................................................................................... 641
Nitro components .................................................................................................................................... 641
Network feature support ....................................................................................................................... 642
Virtualized instances ............................................................................................................................... 643
Bare metal instances ............................................................................................................................... 645
v
Amazon EC2 Instance Types
Nitro instance requirements .................................................................................................................. 646
Linux instances with AWS Graviton processors ............................................................................ 649
Quotas .......................................................................................................................................... 650
On-Demand Instance quotas ................................................................................................................. 650
Spot Instance quotas .............................................................................................................................. 651
Dedicated Host quotas ........................................................................................................................... 651
Capacity Blocks quotas ........................................................................................................................... 659
Document history ........................................................................................................................ 661
vi

## Speciﬁcations

Amazon EC2 Instance Types
Amazon EC2 instance types
End of sale notice
The U-9tb1, U-12tb1, U-18tb1, and U-24tb1 instance types are no longer available for new 
instance launches. If your workload requires a high-memory instance, we recommend that 
you use a U7i instance type instead.
When you launch an EC2 instance, the instance type that you specify determines the hardware of 
the host computer used for your instance. Each instance type oﬀers diﬀerent compute, memory, 
and storage capabilities, and is grouped in an instance family based on these capabilities. Select 
an instance type based on the requirements of the application or software that you plan to run on 
your instance.
Amazon EC2 dedicates some resources of the host computer, such as CPU, memory, and instance 
storage, to a particular instance. Amazon EC2 shares other resources of the host computer, such as 
the network and the disk subsystem, among instances. If each instance on a host computer tries 
to use as much of one of these shared resources as possible, each receives an equal share of that 
resource. However, when a resource is underused, an instance can consume a higher share of that 
resource while it's available.
Each instance type provides higher or lower minimum performance from a shared resource. For 
example, instance types with high I/O performance have a larger allocation of shared resources. 
Allocating a larger share of shared resources also reduces the variance of I/O performance. For 
most applications, moderate I/O performance is more than enough. However, for applications that 
require greater or more consistent I/O performance, consider an instance type with higher I/O 
performance.
For pricing information, see Amazon EC2 Pricing.
Topics
• Current generation instances
• Previous generation instances
• Instance performance
1

## General purpose

Amazon EC2 Instance Types
Current generation instances
For the best performance, we recommend that you use the following instance types when you 
launch new instances. For more information, see Amazon EC2 Instance Types.
• General purpose: M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i | M6id 
| M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8azn | M8g | M8gb | M8gd | M8gn | 
M8i | M8id | M8i-ﬂex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-m2pro | Mac-m4 | Mac-
m4pro | T2 | T3 | T3a | T4g
• Compute optimized: C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7a 
| C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8a | C8g | C8gb | C8gd | C8gn | C8i | C8id | C8i-ﬂex
• Memory optimized: R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6id | 
R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gb | R8gd | R8gn | R8i | R8id | R8i-
ﬂex | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | 
U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X1 | X1e | X2gd | X2idn | X2iedn | X2iezn | X8g | 
X8aedz | X8i | z1d
• Storage optimized: D2 | D3 | D3en | H1 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | Is4gen
• Accelerated computing: DL1 | DL2q | F1 | F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f 
| G7e | Inf1 | Inf2 | P4d | P4de | P5 | P5e | P5en | P6-B200 | P6-B300 | P6e-GB200 | Trn1 | Trn1n | 
Trn2 | Trn2u | VT1
• High-performance computing: Hpc6a | Hpc6id | Hpc7a | Hpc7g | Hpc8a
Previous generation instances
Amazon Web Services oﬀers previous generation instance types for users who have optimized their 
applications around them and have yet to upgrade. We encourage you to use current generation 
instance types to get the best performance, but we continue to support the following previous 
generation instance types. For more information about which current generation instance type 
would be a suitable upgrade, see  Previous Generation Instances.
• General purpose: A1 | M1 | M2 | M3 | M4 | T1
• Compute optimized: C1 | C3 | C4
• Memory optimized: R3 | R4
• Storage optimized: I2
• Accelerated computing: G3 | P3 | P3dn
Current generation instances 2

## Instance families and instance types

Amazon EC2 Instance Types
Instance performance
Fixed performance instances
Fixed performance instances provide ﬁxed CPU resources. These instances can deliver and sustain 
full CPU performance at any time, and for as long as a workload needs it. If you need consistently 
high CPU performance for applications such as video encoding, high volume websites, or HPC 
applications, we recommend that you use ﬁxed performance instances.
Burstable performance instances
Burstable performance (T) instances provide a baseline level of CPU performance with the 
ability to burst above the baseline. The baseline CPU is designed to meet the needs of the 
majority of general purpose workloads, such as large-scale micro-services, web servers, small and 
medium databases, data logging, code repositories, virtual desktops, and development and test 
environments.
The baseline utilization and ability to burst are governed by CPU credits. Each burstable 
performance instance continuously earns credits when it stays below the CPU baseline, and 
continuously spends credits when it bursts above the baseline. For more information, see Burstable 
performance instances in the Amazon EC2 User Guide.
Flex instances
C7i-ﬂex, C8i-ﬂex, M7i-ﬂex, M8i-ﬂex, R8i-ﬂex instances oﬀer a balance of compute, memory, 
and network resources, and they provide the most cost-eﬀective way to run a broad spectrum 
of general purpose applications. These instances provide reliable CPU resources to deliver a 
baseline CPU performance of 40 percent, which is designed to meet the compute requirements 
for a majority of general purpose workloads. When more performance is needed, these instances 
provide the ability to exceed the baseline CPU performance and deliver up to 100 percent CPU 
performance for 95 percent of the time over a 24-hour window.
Flex instances running at a high CPU utilization that is consistently above the baseline for long 
periods of time might see a gradual reduction in the maximum burst CPU throughput. For more 
information, see the following:
• C7i-ﬂex instances
• C8i-ﬂex instances
• M7i-ﬂex instances
Instance performance 3
Amazon EC2 Instance Types
• M8i-ﬂex instances
• R8i-ﬂex instances
Instance performance 4
Amazon EC2 Instance Types
Amazon EC2 instance type naming conventions
Amazon EC2 provides a variety of instance types so you can choose the type that best meets your 
requirements. Instance types are named based on their instance family and instance size. The ﬁrst 
position of the instance family indicates the series, for example c. The second position indicates the
generation, for example 7. The third position indicates the options, for example gn. After the period 
(.) is the instance size, such as small or 4xlarge, or metal for bare metal instances.
Series Options
• C – Compute optimized
• D – Dense storage
• F – FPGA
• G – Graphics intensive
• Hpc – High performance computing
• I – Storage optimized
• Im – Storage optimized (1 to 4 ratio of vCPU 
to memory)
• Is – Storage optimized (1 to 6 ratio of vCPU 
to memory)
• a – AMD processors
• b*00 | gb*00 – Accelerated by NVIDIA 
Blackwell GPUs
• g – AWS Graviton processors
• i – Intel processors
• m* | m*pro– Apple chip
• b – Block storage optimization
• d – Instance store volumes
• e – Extra instance storage (for storage 
optimized instance types), extra memory 
5
Amazon EC2 Instance Types
Series Options
• Inf – AWS Inferentia
• M – General purpose
• Mac – macOS
• P – GPU accelerated
• R – Memory optimized
• T – Burstable performance
• Trn – AWS Trainium
• U – High memory
• VT – Video transcoding
• X – Memory intensive
• Z – High memory
(for memory optimized instance types), 
or extra GPU memory (for accelerated 
computing instance types).
• ﬂex – Flex instance
• n – Network and EBS optimized
• q – Qualcomm inference accelerators
• *tb – Amount of memory for high-memory 
instances (3 TiB to 32 TiB)
• z – High CPU frequency
6

## Instance family summary

Amazon EC2 Instance Types
Amazon EC2 instance type speciﬁcations
Amazon EC2 provides a wide selection of instance types optimized to ﬁt diﬀerent use cases. 
Instance types comprise varying combinations of CPU, memory, storage, and networking capacity 
and give you the ﬂexibility to choose the appropriate mix of resources for your applications. Each 
instance type includes one or more instance sizes, allowing you to scale your resources to the 
requirements of your target workload.
We group EC2 instance into the following categories:
• General purpose – Provide a balance of compute, memory, and networking resources. These 
instances are ideal for applications that use these resources in equal proportions, such as web 
servers and code repositories.
Burstable performance – The T instance family is also referred to as burstable performance 
instances. These instances provide a baseline CPU performance with the ability to burst above 
the baseline at any time. For more information, see Burstable performance instances in the
Amazon EC2 User Guide.
• Compute optimized – Designed for compute intensive applications that beneﬁt from high 
performance processors. These instances are ideal for batch processing workloads, media 
transcoding, high performance web servers, high performance computing (HPC), scientiﬁc 
modeling, dedicated gaming servers, ad server engines, and machine learning inference.
• Memory optimized – Designed to deliver fast performance for workloads that process large data 
sets in memory.
• Storage optimized – Designed for workloads that require high, sequential read and write access 
to very large data sets on local storage. They are optimized to deliver tens of thousands of low-
latency, random I/O operations per second (IOPS) to applications.
• Accelerated computing – Use hardware accelerators, or co-processors, to perform functions, 
such as ﬂoating point number calculations, graphics processing, or data pattern matching, more 
eﬃciently than is possible in software running on CPUs.
• High-performance computing – Purpose built to oﬀer the best price performance for running 
HPC workloads at scale on AWS. These instances are ideal for applications that beneﬁt from 
high-performance processors, such as large, complex simulations and deep learning workloads.
• Previous generation – AWS oﬀers previous generation instance types for users who have 
optimized their applications around them and have yet to upgrade. We encourage you to use 
7
Amazon EC2 Instance Types
current generation instance types to get the best performance, but we continue to support 
previous generation instance types.
To determine which instance types meet your requirements, such as supported Regions, compute 
resources, or storage resources, see Find an Amazon EC2 instance type in the Amazon EC2 User 
Guide.
Categories
• Speciﬁcations for Amazon EC2 general purpose instances
• Speciﬁcations for Amazon EC2 compute optimized instances
• Speciﬁcations for Amazon EC2 memory optimized instances
• Speciﬁcations for Amazon EC2 storage optimized instances
• Speciﬁcations for Amazon EC2 accelerated computing instances
• Speciﬁcations for Amazon EC2 high-performance computing instances
• Speciﬁcations for Amazon EC2 previous generation instances
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Speciﬁcations for Amazon EC2 general purpose instances
General purpose instances provide a balance of compute, memory, and networking resources. 
These instances are ideal for applications that use these resources in equal proportions, such as 
web servers and code repositories.
For information on previous generation instance types of this category, such as M4 instances, see
Speciﬁcations for Amazon EC2 previous generation instances.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
General purpose 8
Amazon EC2 Instance Types
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Instance families and instance types
Instance 
family
Available instance types
M5 m5.large | m5.xlarge  | m5.2xlarge  | m5.4xlarge  | m5.8xlarge  |
m5.12xlarge  | m5.16xlarge  | m5.24xlarge  | m5.metal
M5a m5a.large  | m5a.xlarge  | m5a.2xlarge  | m5a.4xlarge  | m5a.8xlar 
ge  | m5a.12xlarge  | m5a.16xlarge  | m5a.24xlarge
M5ad m5ad.large  | m5ad.xlarge  | m5ad.2xlarge  | m5ad.4xlarge  |
m5ad.8xlarge  | m5ad.12xlarge  | m5ad.16xlarge  | m5ad.24xlarge
M5d m5d.large  | m5d.xlarge  | m5d.2xlarge  | m5d.4xlarge  | m5d.8xlar 
ge  | m5d.12xlarge  | m5d.16xlarge  | m5d.24xlarge  | m5d.metal
M5dn m5dn.large  | m5dn.xlarge  | m5dn.2xlarge  | m5dn.4xlarge  |
m5dn.8xlarge  | m5dn.12xlarge  | m5dn.16xlarge  | m5dn.24xlarge  |
m5dn.metal
M5n m5n.large  | m5n.xlarge  | m5n.2xlarge  | m5n.4xlarge  | m5n.8xlar 
ge  | m5n.12xlarge  | m5n.16xlarge  | m5n.24xlarge  | m5n.metal
M5zn m5zn.large  | m5zn.xlarge  | m5zn.2xlarge  | m5zn.3xlarge  |
m5zn.6xlarge  | m5zn.12xlarge  | m5zn.metal
M6a m6a.large  | m6a.xlarge  | m6a.2xlarge  | m6a.4xlarge  | m6a.8xlar 
ge  | m6a.12xlarge  | m6a.16xlarge  | m6a.24xlarge  | m6a.32xlarge  |
m6a.48xlarge  | m6a.metal
Instance families and instance types 9
Amazon EC2 Instance Types
Instance 
family
Available instance types
M6g m6g.medium  | m6g.large  | m6g.xlarge  | m6g.2xlarge  | m6g.4xlarge
| m6g.8xlarge  | m6g.12xlarge  | m6g.16xlarge  | m6g.metal
M6gd m6gd.medium  | m6gd.large  | m6gd.xlarge  | m6gd.2xlarge  |
m6gd.4xlarge  | m6gd.8xlarge  | m6gd.12xlarge  | m6gd.16xlarge  |
m6gd.metal
M6i m6i.large  | m6i.xlarge  | m6i.2xlarge  | m6i.4xlarge  | m6i.8xlar 
ge  | m6i.12xlarge  | m6i.16xlarge  | m6i.24xlarge  | m6i.32xlarge  |
m6i.metal
M6id m6id.large  | m6id.xlarge  | m6id.2xlarge  | m6id.4xlarge  |
m6id.8xlarge  | m6id.12xlarge  | m6id.16xlarge  | m6id.24xlarge  |
m6id.32xlarge  | m6id.metal
M6idn m6idn.large  | m6idn.xlarge  | m6idn.2xlarge  | m6idn.4xlarge
| m6idn.8xlarge  | m6idn.12xlarge  | m6idn.16xlarge  | m6idn.24x 
large  | m6idn.32xlarge  | m6idn.metal
M6in m6in.large  | m6in.xlarge  | m6in.2xlarge  | m6in.4xlarge  |
m6in.8xlarge  | m6in.12xlarge  | m6in.16xlarge  | m6in.24xlarge  |
m6in.32xlarge  | m6in.metal
M7a m7a.medium  | m7a.large  | m7a.xlarge  | m7a.2xlarge  | m7a.4xlar 
ge  | m7a.8xlarge  | m7a.12xlarge  | m7a.16xlarge  | m7a.24xlarge  |
m7a.32xlarge  | m7a.48xlarge  | m7a.metal-48xl
M7g m7g.medium  | m7g.large  | m7g.xlarge  | m7g.2xlarge  | m7g.4xlarge
| m7g.8xlarge  | m7g.12xlarge  | m7g.16xlarge  | m7g.metal
M7gd m7gd.medium  | m7gd.large  | m7gd.xlarge  | m7gd.2xlarge  |
m7gd.4xlarge  | m7gd.8xlarge  | m7gd.12xlarge  | m7gd.16xlarge  |
m7gd.metal
Instance families and instance types 10

## Performance speciﬁcations

Amazon EC2 Instance Types
Instance 
family
Available instance types
M7i m7i.large  | m7i.xlarge  | m7i.2xlarge  | m7i.4xlarge  | m7i.8xlar 
ge  | m7i.12xlarge  | m7i.16xlarge  | m7i.24xlarge  | m7i.48xlarge  |
m7i.metal-24xl  | m7i.metal-48xl
M7i-ﬂex m7i-flex.large  | m7i-flex.xlarge  | m7i-flex.2xlarge  | m7i-flex. 
4xlarge  | m7i-flex.8xlarge  | m7i-flex.12xlarge  | m7i-flex. 
16xlarge
M8a m8a.medium  | m8a.large  | m8a.xlarge  | m8a.2xlarge  | m8a.4xlar 
ge  | m8a.8xlarge  | m8a.12xlarge  | m8a.16xlarge  | m8a.24xlarge  |
m8a.48xlarge  | m8a.metal-24xl  | m8a.metal-48xl
M8azn m8azn.medium  | m8azn.large  | m8azn.xlarge  | m8azn.3xlarge  |
m8azn.6xlarge  | m8azn.12xlarge  | m8azn.24xlarge  | m8azn.met 
al-12xl  | m8azn.metal-24xl
M8g m8g.medium  | m8g.large  | m8g.xlarge  | m8g.2xlarge  | m8g.4xlar 
ge  | m8g.8xlarge  | m8g.12xlarge  | m8g.16xlarge  | m8g.24xlarge  |
m8g.48xlarge  | m8g.metal-24xl  | m8g.metal-48xl
M8gb m8gb.medium  | m8gb.large  | m8gb.xlarge  | m8gb.2xlarge  |
m8gb.4xlarge  | m8gb.8xlarge  | m8gb.12xlarge  | m8gb.16xlarge
| m8gb.24xlarge  | m8gb.48xlarge  | m8gb.metal-24xl  | m8gb.meta 
l-48xl
M8gd m8gd.medium  | m8gd.large  | m8gd.xlarge  | m8gd.2xlarge  |
m8gd.4xlarge  | m8gd.8xlarge  | m8gd.12xlarge  | m8gd.16xlarge
| m8gd.24xlarge  | m8gd.48xlarge  | m8gd.metal-24xl  | m8gd.meta 
l-48xl
M8gn m8gn.medium  | m8gn.large  | m8gn.xlarge  | m8gn.2xlarge  |
m8gn.4xlarge  | m8gn.8xlarge  | m8gn.12xlarge  | m8gn.16xlarge
| m8gn.24xlarge  | m8gn.48xlarge  | m8gn.metal-24xl  | m8gn.meta 
l-48xl
Instance families and instance types 11
Amazon EC2 Instance Types
Instance 
family
Available instance types
M8i m8i.large  | m8i.xlarge  | m8i.2xlarge  | m8i.4xlarge  | m8i.8xlar 
ge  | m8i.12xlarge  | m8i.16xlarge  | m8i.24xlarge  | m8i.32xlarge  |
m8i.48xlarge  | m8i.96xlarge  | m8i.metal-48xl  | m8i.metal-96xl
M8id m8id.large  | m8id.xlarge  | m8id.2xlarge  | m8id.4xlarge  |
m8id.8xlarge  | m8id.12xlarge  | m8id.16xlarge  | m8id.24xlarge  |
m8id.32xlarge  | m8id.48xlarge  | m8id.96xlarge  | m8id.metal-48xl
| m8id.metal-96xl
M8i-ﬂex m8i-flex.large  | m8i-flex.xlarge  | m8i-flex.2xlarge  | m8i-flex. 
4xlarge  | m8i-flex.8xlarge  | m8i-flex.12xlarge  | m8i-flex. 
16xlarge
Mac1 mac1.metal
Mac2 mac2.metal
Mac2-
m1ultra
mac2-m1ultra.metal
Mac2-m2 mac2-m2.metal
Mac2-
m2pro
mac2-m2pro.metal
Mac-m4 mac-m4.metal
Mac-
m4pro
mac-m4pro.metal
T2 t2.nano | t2.micro | t2.small | t2.medium  | t2.large | t2.xlarge  |
t2.2xlarge
T3 t3.nano | t3.micro | t3.small | t3.medium  | t3.large | t3.xlarge  |
t3.2xlarge
Instance families and instance types 12
Amazon EC2 Instance Types
Instance 
family
Available instance types
T3a t3a.nano | t3a.micro  | t3a.small  | t3a.medium  | t3a.large  |
t3a.xlarge  | t3a.2xlarge
T4g t4g.nano | t4g.micro  | t4g.small  | t4g.medium  | t4g.large  |
t4g.xlarge  | t4g.2xlarge
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
M5 Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M5a Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
M5ad Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
M5d Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M5dn Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
M5n Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
M5zn Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Instance family summary 13
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
M6a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M6g Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M6gd Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M6i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M6id Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M6idn Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M6in Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M7a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M7g Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M7gd Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
Instance family summary 14
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
M7i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M7i-ﬂex Nitro v4 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
M8a Nitro v6 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M8azn Nitro v6 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M8g Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M8gb Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M8gd Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M8gn Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
M8i Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M8id Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Instance family summary 15
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
M8i-ﬂex Nitro v6 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
Mac1 Nitro v2 Intel 
(x86_64_m 
ac)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac2 Nitro v2 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac2-
m1ultra
Nitro v2 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac2-
m2
Nitro v2 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac2-
m2pro
Nitro v2 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac-m4 Nitro v5 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
Mac-
m4pro
Nitro v5 Apple 
(arm64_ma 
c)
✓  Yes ✓  Yes ✗  No ✗  No Linux
T2 Xen Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 16
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
T3 Nitro v2 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
T3a Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
T4g Nitro v2 AWS 
Graviton 
(arm64)
✗  No ✗  No ✓  Yes ✓  Yes Linux
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
M5
m5.large 8.00 Intel Xeon Platinum 
8175
2 1 2 ✗  No ✗  No
m5.xlarge 16.00 Intel Xeon Platinum 
8175
4 2 2 ✗  No ✗  No
m5.2xlarge 32.00 Intel Xeon Platinum 
8175
8 4 2 ✗  No ✗  No
m5.4xlarge 64.00 Intel Xeon Platinum 
8175
16 8 2 ✗  No ✗  No
m5.8xlarge 128.00 Intel Xeon Platinum 
8175
32 16 2 ✗  No ✗  No
Performance speciﬁcations 17
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m5.12xlarge 192.00 Intel Xeon Platinum 
8175
48 24 2 ✗  No ✗  No
m5.16xlarge 256.00 Intel Xeon Platinum 
8175
64 32 2 ✗  No ✗  No
m5.24xlarge 384.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
m5.metal 384.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
M5a
m5a.large 8.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
m5a.xlarge 16.00 AMD EPYC 7571 4 2 2 ✗  No ✗  No
m5a.2xlarge 32.00 AMD EPYC 7571 8 4 2 ✗  No ✗  No
m5a.4xlarge 64.00 AMD EPYC 7571 16 8 2 ✗  No ✗  No
m5a.8xlarge 128.00 AMD EPYC 7571 32 16 2 ✗  No ✗  No
m5a.12xlarge 192.00 AMD EPYC 7571 48 24 2 ✗  No ✗  No
m5a.16xlarge 256.00 AMD EPYC 7571 64 32 2 ✗  No ✗  No
m5a.24xlarge 384.00 AMD EPYC 7571 96 48 2 ✗  No ✗  No
M5ad
m5ad.large 8.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
m5ad.xlarge 16.00 AMD EPYC 7571 4 2 2 ✗  No ✗  No
m5ad.2xlarge 32.00 AMD EPYC 7571 8 4 2 ✗  No ✗  No
Performance speciﬁcations 18
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m5ad.4xlarge 64.00 AMD EPYC 7571 16 8 2 ✗  No ✗  No
m5ad.8xlarge 128.00 AMD EPYC 7571 32 16 2 ✗  No ✗  No
m5ad.12xl 
arge
192.00 AMD EPYC 7571 48 24 2 ✗  No ✗  No
m5ad.16xl 
arge
256.00 AMD EPYC 7571 64 32 2 ✗  No ✗  No
m5ad.24xl 
arge
384.00 AMD EPYC 7571 96 48 2 ✗  No ✗  No
M5d
m5d.large 8.00 Intel Xeon Platinum 
8175
2 1 2 ✗  No ✗  No
m5d.xlarge 16.00 Intel Xeon Platinum 
8175
4 2 2 ✗  No ✗  No
m5d.2xlarge 32.00 Intel Xeon Platinum 
8175
8 4 2 ✗  No ✗  No
m5d.4xlarge 64.00 Intel Xeon Platinum 
8175
16 8 2 ✗  No ✗  No
m5d.8xlarge 128.00 Intel Xeon Platinum 
8175
32 16 2 ✗  No ✗  No
m5d.12xlarge 192.00 Intel Xeon Platinum 
8175
48 24 2 ✗  No ✗  No
m5d.16xlarge 256.00 Intel Xeon Platinum 
8175
64 32 2 ✗  No ✗  No
Performance speciﬁcations 19
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m5d.24xlarge 384.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
m5d.metal 384.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
M5dn
m5dn.large 8.00 Intel Xeon Platinum 
8259
2 1 2 ✗  No ✗  No
m5dn.xlarge 16.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
m5dn.2xlarge 32.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
m5dn.4xlarge 64.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
m5dn.8xlarge 128.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
m5dn.12xl 
arge
192.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
m5dn.16xl 
arge
256.00 Intel Xeon Platinum 
8259
64 32 2 ✗  No ✗  No
m5dn.24xl 
arge
384.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
m5dn.metal 384.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
M5n
Performance speciﬁcations 20
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m5n.large 8.00 Intel Xeon Platinum 
8259
2 1 2 ✗  No ✗  No
m5n.xlarge 16.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
m5n.2xlarge 32.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
m5n.4xlarge 64.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
m5n.8xlarge 128.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
m5n.12xlarge 192.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
m5n.16xlarge 256.00 Intel Xeon Platinum 
8259
64 32 2 ✗  No ✗  No
m5n.24xlarge 384.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
m5n.metal 384.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
M5zn
m5zn.large 8.00 Intel Xeon Platinum 
8252
2 1 2 ✗  No ✗  No
m5zn.xlarge 16.00 Intel Xeon Platinum 
8252
4 2 2 ✗  No ✗  No
Performance speciﬁcations 21
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m5zn.2xlarge 32.00 Intel Xeon Platinum 
8252
8 4 2 ✗  No ✗  No
m5zn.3xlarge 48.00 Intel Xeon Platinum 
8252
12 6 2 ✗  No ✗  No
m5zn.6xlarge 96.00 Intel Xeon Platinum 
8252
24 12 2 ✗  No ✗  No
m5zn.12xl 
arge
192.00 Intel Xeon Platinum 
8252
48 24 2 ✗  No ✗  No
m5zn.metal 192.00 Intel Xeon Platinum 
8252
48 24 2 ✗  No ✗  No
M6a
m6a.large 8.00 AMD EPYC 7R13 2 1 2 ✗  No ✗  No
m6a.xlarge 16.00 AMD EPYC 7R13 4 2 2 ✗  No ✗  No
m6a.2xlarge 32.00 AMD EPYC 7R13 8 4 2 ✗  No ✗  No
m6a.4xlarge 64.00 AMD EPYC 7R13 16 8 2 ✗  No ✗  No
m6a.8xlarge 128.00 AMD EPYC 7R13 32 16 2 ✗  No ✗  No
m6a.12xlarge 192.00 AMD EPYC 7R13 48 24 2 ✗  No ✗  No
m6a.16xlarge 256.00 AMD EPYC 7R13 64 32 2 ✗  No ✗  No
m6a.24xlarge 384.00 AMD EPYC 7R13 96 48 2 ✗  No ✗  No
m6a.32xlarge 512.00 AMD EPYC 7R13 128 64 2 ✗  No ✗  No
m6a.48xlarge 768.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
Performance speciﬁcations 22
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m6a.metal 768.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
M6g
m6g.medium 4.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
m6g.large 8.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
m6g.xlarge 16.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
m6g.2xlarge 32.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
m6g.4xlarge 64.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
m6g.8xlarge 128.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
m6g.12xlarge 192.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
m6g.16xlarge 256.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
m6g.metal 256.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
M6gd
m6gd.medi 
um
4.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
Performance speciﬁcations 23
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m6gd.large 8.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
m6gd.xlarge 16.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
m6gd.2xlarge 32.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
m6gd.4xlarge 64.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
m6gd.8xlarge 128.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
m6gd.12xl 
arge
192.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
m6gd.16xl 
arge
256.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
m6gd.metal 256.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
M6i
m6i.large 8.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
m6i.xlarge 16.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
m6i.2xlarge 32.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
m6i.4xlarge 64.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
m6i.8xlarge 128.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
Performance speciﬁcations 24
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m6i.12xlarge 192.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
m6i.16xlarge 256.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
m6i.24xlarge 384.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
m6i.32xlarge 512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
m6i.metal 512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
M6id
m6id.large 8.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
m6id.xlarge 16.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
m6id.2xlarge 32.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
m6id.4xlarge 64.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
m6id.8xlarge 128.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
m6id.12xl 
arge
192.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
m6id.16xl 
arge
256.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
m6id.24xl 
arge
384.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
m6id.32xl 
arge
512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
m6id.metal 512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
M6idn
Performance speciﬁcations 25
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m6idn.large 8.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
m6idn.xlarge 16.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
m6idn.2xl 
arge
32.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
m6idn.4xl 
arge
64.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
m6idn.8xl 
arge
128.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
m6idn.12x 
large
192.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
m6idn.16x 
large
256.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
m6idn.24x 
large
384.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
m6idn.32x 
large
512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
m6idn.metal 512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
M6in
m6in.large 8.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
m6in.xlarge 16.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
m6in.2xlarge 32.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
m6in.4xlarge 64.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
Performance speciﬁcations 26
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m6in.8xlarge 128.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
m6in.12xl 
arge
192.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
m6in.16xl 
arge
256.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
m6in.24xl 
arge
384.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
m6in.32xl 
arge
512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
m6in.metal 512.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
M7a
m7a.medium 4.00 AMD EPYC 9R14 1 1 1 ✗  No ✗  No
m7a.large 8.00 AMD EPYC 9R14 2 2 1 ✗  No ✗  No
m7a.xlarge 16.00 AMD EPYC 9R14 4 4 1 ✗  No ✗  No
m7a.2xlarge 32.00 AMD EPYC 9R14 8 8 1 ✗  No ✗  No
m7a.4xlarge 64.00 AMD EPYC 9R14 16 16 1 ✗  No ✗  No
m7a.8xlarge 128.00 AMD EPYC 9R14 32 32 1 ✗  No ✗  No
m7a.12xlarge 192.00 AMD EPYC 9R14 48 48 1 ✗  No ✗  No
m7a.16xlarge 256.00 AMD EPYC 9R14 64 64 1 ✗  No ✗  No
m7a.24xlarge 384.00 AMD EPYC 9R14 96 96 1 ✗  No ✗  No
m7a.32xlarge 512.00 AMD EPYC 9R14 128 128 1 ✗  No ✗  No
Performance speciﬁcations 27
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m7a.48xlarge 768.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
m7a.metal 
-48xl
768.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
M7g
m7g.medium 4.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
m7g.large 8.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
m7g.xlarge 16.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
m7g.2xlarge 32.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
m7g.4xlarge 64.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
m7g.8xlarge 128.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
m7g.12xlarge 192.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
m7g.16xlarge 256.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
m7g.metal 256.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
M7gd
Performance speciﬁcations 28
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m7gd.medi 
um
4.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
m7gd.large 8.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
m7gd.xlarge 16.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
m7gd.2xlarge 32.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
m7gd.4xlarge 64.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
m7gd.8xlarge 128.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
m7gd.12xl 
arge
192.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
m7gd.16xl 
arge
256.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
m7gd.metal 256.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
M7i
m7i.large 8.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
m7i.xlarge 16.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
Performance speciﬁcations 29
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m7i.2xlarge 32.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
m7i.4xlarge 64.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
m7i.8xlarge 128.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
m7i.12xlarge 192.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
m7i.16xlarge 256.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
m7i.24xlarge 384.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
m7i.48xlarge 768.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
m7i.metal 
-24xl
384.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
m7i.metal 
-48xl
768.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
M7i-ﬂex
m7i-ﬂex. 
large
8.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
m7i-ﬂex. 
xlarge
16.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
Performance speciﬁcations 30
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m7i-ﬂex. 
2xlarge
32.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
m7i-ﬂex. 
4xlarge
64.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
m7i-ﬂex. 
8xlarge
128.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
m7i-ﬂex. 
12xlarge
192.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
m7i-ﬂex. 
16xlarge
256.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
M8a
m8a.medium 4.00 AMD EPYC 9R45 1 1 1 ✗  No ✗  No
m8a.large 8.00 AMD EPYC 9R45 2 2 1 ✗  No ✗  No
m8a.xlarge 16.00 AMD EPYC 9R45 4 4 1 ✗  No ✗  No
m8a.2xlarge 32.00 AMD EPYC 9R45 8 8 1 ✗  No ✗  No
m8a.4xlarge 64.00 AMD EPYC 9R45 16 16 1 ✗  No ✗  No
m8a.8xlarge 128.00 AMD EPYC 9R45 32 32 1 ✗  No ✗  No
m8a.12xlarge 192.00 AMD EPYC 9R45 48 48 1 ✗  No ✗  No
m8a.16xlarge 256.00 AMD EPYC 9R45 64 64 1 ✗  No ✗  No
m8a.24xlarge 384.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
m8a.48xlarge 768.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
Performance speciﬁcations 31
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8a.metal 
-24xl
384.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
m8a.metal 
-48xl
768.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
M8azn
m8azn.med 
ium
4.00 AMD EPYC 9R05 1 1 1 ✗  No ✗  No
m8azn.large 8.00 AMD EPYC 9R05 2 2 1 ✗  No ✗  No
m8azn.xlarge 16.00 AMD EPYC 9R05 4 4 1 ✗  No ✗  No
m8azn.3xl 
arge
48.00 AMD EPYC 9R05 12 12 1 ✗  No ✗  No
m8azn.6xl 
arge
96.00 AMD EPYC 9R05 24 24 1 ✗  No ✗  No
m8azn.12x 
large
192.00 AMD EPYC 9R05 48 48 1 ✗  No ✗  No
m8azn.24x 
large
384.00 AMD EPYC 9R05 96 96 1 ✗  No ✗  No
m8azn.met 
al-12xl
192.00 AMD EPYC 9R05 48 48 1 ✗  No ✗  No
m8azn.met 
al-24xl
384.00 AMD EPYC 9R05 96 96 1 ✗  No ✗  No
M8g
Performance speciﬁcations 32
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8g.medium 4.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
m8g.large 8.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
m8g.xlarge 16.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
m8g.2xlarge 32.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
m8g.4xlarge 64.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
m8g.8xlarge 128.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
m8g.12xlarge 192.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
m8g.16xlarge 256.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
m8g.24xlarge 384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8g.48xlarge 768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
m8g.metal 
-24xl
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8g.metal 
-48xl
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Performance speciﬁcations 33
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
M8gb
m8gb.medi 
um
4.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
m8gb.large 8.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
m8gb.xlarge 16.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
m8gb.2xlarge 32.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
m8gb.4xlarge 64.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
m8gb.8xlarge 128.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
m8gb.12xl 
arge
192.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
m8gb.16xl 
arge
256.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
m8gb.24xl 
arge
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8gb.48xl 
arge
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
m8gb.meta 
l-24xl
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
Performance speciﬁcations 34
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8gb.meta 
l-48xl
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
M8gd
m8gd.medi 
um
4.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
m8gd.large 8.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
m8gd.xlarge 16.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
m8gd.2xlarge 32.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
m8gd.4xlarge 64.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
m8gd.8xlarge 128.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
m8gd.12xl 
arge
192.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
m8gd.16xl 
arge
256.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
m8gd.24xl 
arge
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8gd.48xl 
arge
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Performance speciﬁcations 35
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8gd.meta 
l-24xl
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8gd.meta 
l-48xl
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
M8gn
m8gn.medi 
um
4.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
m8gn.large 8.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
m8gn.xlarge 16.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
m8gn.2xlarge 32.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
m8gn.4xlarge 64.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
m8gn.8xlarge 128.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
m8gn.12xl 
arge
192.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
m8gn.16xl 
arge
256.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
m8gn.24xl 
arge
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
Performance speciﬁcations 36

## Network speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8gn.48xl 
arge
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
m8gn.meta 
l-24xl
384.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
m8gn.meta 
l-48xl
768.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
M8i
m8i.large 8.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
m8i.xlarge 16.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
m8i.2xlarge 32.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
m8i.4xlarge 64.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
m8i.8xlarge 128.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
m8i.12xlarge 192.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
m8i.16xlarge 256.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
m8i.24xlarge 384.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
Performance speciﬁcations 37
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8i.32xlarge 512.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
m8i.48xlarge 768.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
m8i.96xlarge 1536.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
m8i.metal 
-48xl
768.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
m8i.metal 
-96xl
1536.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
M8id
m8id.large 8.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
m8id.xlarge 16.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
m8id.2xlarge 32.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
m8id.4xlarge 64.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
m8id.8xlarge 128.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
m8id.12xl 
arge
192.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
Performance speciﬁcations 38
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8id.16xl 
arge
256.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
m8id.24xl 
arge
384.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
m8id.32xl 
arge
512.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
m8id.48xl 
arge
768.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
m8id.96xl 
arge
1536.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
m8id.meta 
l-48xl
768.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
m8id.meta 
l-96xl
1536.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
M8i-ﬂex
m8i-ﬂex. 
large
8.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
m8i-ﬂex. 
xlarge
16.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
m8i-ﬂex. 
2xlarge
32.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
m8i-ﬂex. 
4xlarge
64.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
Performance speciﬁcations 39
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m8i-ﬂex. 
8xlarge
128.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
m8i-ﬂex. 
12xlarge
192.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
m8i-ﬂex. 
16xlarge
256.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
Mac1
mac1.metal 32.00 Intel Core i7-8700B 12 6 2 ✗  No ✗  No
Mac2
mac2.metal 16.00 Apple M1 chip with 
8-core CPU
8 4 2 ✗  No ✗  No
Mac2-m1ultra
mac2-m1ul 
tra.metal
128.00 Apple M1 Ultra 
with  20‑core  CPU
20 20 1 ✗  No ✗  No
Mac2-m2
mac2-m2.m 
etal
24.00 Apple M2 with 
8‑core  CPU
8 8 1 ✗  No ✗  No
Mac2-m2pro
mac2-m2pr 
o.metal
32.00 Apple M2 Pro with 
12‑core  CPU
12 12 1 ✗  No ✗  No
Mac-m4
Performance speciﬁcations 40
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
mac-m4.me 
tal
24.00 Apple M4 with 
10‑core  CPU
10 10 1 ✗  No ✗  No
Mac-m4pro
mac-m4pro 
.metal
48.00 Apple M4 with 
12‑core  CPU
14 14 1 ✗  No ✗  No
T2
t2.nano 1 0.50 Intel Xeon Family 1 1 1 ✗  No ✗  No
t2.micro 1 1.00 Intel Xeon Family 1 1 1 ✗  No ✗  No
t2.small 1 2.00 Intel Xeon Family 1 1 1 ✗  No ✗  No
t2.medium 1 4.00 Intel Broadwell 
E5-2686v4
2 2 1 ✗  No ✗  No
t2.large 1 8.00 Intel Broadwell 
E5-2686v4
2 2 1 ✗  No ✗  No
t2.xlarge 1 16.00 Intel Broadwell 
E5-2686v4
4 4 1 ✗  No ✗  No
t2.2xlarge 1 32.00 Intel Broadwell 
E5-2686v4
8 8 1 ✗  No ✗  No
T3
t3.nano 1 0.50 Intel Skylake 
P-8175
2 1 2 ✗  No ✗  No
t3.micro 1 1.00 Intel Skylake 
P-8175
2 1 2 ✗  No ✗  No
Performance speciﬁcations 41
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
t3.small 1 2.00 Intel Skylake 
P-8175
2 1 2 ✗  No ✗  No
t3.medium 1 4.00 Intel Skylake 
P-8175
2 1 2 ✗  No ✗  No
t3.large 1 8.00 Intel Skylake 
P-8175
2 1 2 ✗  No ✗  No
t3.xlarge 1 16.00 Intel Skylake 
P-8175
4 2 2 ✗  No ✗  No
t3.2xlarge 1 32.00 Intel Skylake 
P-8175
8 4 2 ✗  No ✗  No
T3a
t3a.nano 1 0.50 AMD EPYC 7571 2 1 2 ✗  No ✗  No
t3a.micro 1 1.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
t3a.small 1 2.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
t3a.medium 1 4.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
t3a.large 1 8.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
t3a.xlarge 1 16.00 AMD EPYC 7571 4 2 2 ✗  No ✗  No
t3a.2xlarge 1 32.00 AMD EPYC 7571 8 4 2 ✗  No ✗  No
T4g
t4g.nano 1 0.50 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
Performance speciﬁcations 42
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
t4g.micro 1 1.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
t4g.small 1 2.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
t4g.medium 1 4.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
t4g.large 1 8.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
t4g.xlarge 1 16.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
t4g.2xlarge 1 32.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
Note
1 These are burstable instance types that provide a baseline CPU performance with the 
ability to burst beyond their baseline at any time using CPU credits. For more information, 
see  Burstable performance instances.
Network speciﬁcations
Note
M8a, M8g, M8gd, M8i, M8id, M8i-ﬂex instance types support conﬁgurable bandwidth 
weightings. With these instance types, you can optimize an instance's bandwidth for either 
networking performance or Amazon EBS performance. The following table shows the 
Network speciﬁcations 43
Amazon EC2 Instance Types
default networking bandwidth performance for these instance types. For the supported 
conﬁgurable weightings, see  Conﬁgurable bandwidth weighting preferences.
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
M5
m5.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5a
Network speciﬁcations 44
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m5a.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5a.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5a.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5a.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5a.8xlarge 1 7.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5a.12xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5a.16xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5a.24xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5ad
m5ad.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5ad.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5ad.2xlarge
1
2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 45
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m5ad.4xlarge
1
5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5ad.8xlarge
1
7.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5ad.12xl 
arge
10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5ad.16xl 
arge
12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5ad.24xl 
arge
20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5d
m5d.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5d.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5d.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5d.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5d.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5d.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 46
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m5d.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5d.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5d.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5dn
m5dn.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5dn.xlarge 1 4.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5dn.2xlarge
1
8.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5dn.4xlarge
1
16.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5dn.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5dn.12xl 
arge
50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5dn.16xl 
arge
75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5dn.24xl 
arge
100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Network speciﬁcations 47
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m5dn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5n
m5n.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5n.xlarge 1 4.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5n.2xlarge 1 8.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5n.4xlarge 1 16.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5n.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5n.12xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5n.16xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5n.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5n.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M5zn
Network speciﬁcations 48
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m5zn.large 1 3.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m5zn.xlarge 1 5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5zn.2xlarge
1
10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m5zn.3xlarge
1
15.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5zn.6xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m5zn.12xl 
arge
100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m5zn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M6a
m6a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 49
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m6a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6a.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M6g
m6g.medium
1
0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m6g.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6g.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6g.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 50
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m6g.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6g.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6g.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6g.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m6g.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M6gd
m6gd.medi 
um 1
0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m6gd.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6gd.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6gd.2xlarge
1
2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6gd.4xlarge
1
5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6gd.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 51
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m6gd.12xl 
arge
20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6gd.16xl 
arge
25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
m6gd.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M6i
m6i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 52
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m6i.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6i.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M6id
m6id.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6id.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6id.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6id.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6id.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6id.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6id.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6id.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6id.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 53
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m6id.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M6idn
m6idn.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6idn.xlarge
1
6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6idn.2xlarge
1
12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6idn.4xlarge
1
25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6idn.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6idn.12x 
large
75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6idn.16x 
large
100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6idn.24x 
large
150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6idn.32x 
large
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
m6idn.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
Network speciﬁcations 54
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
M6in
m6in.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m6in.xlarge 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6in.2xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m6in.4xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m6in.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6in.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m6in.16xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6in.24xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m6in.32xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
m6in.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
M7a
Network speciﬁcations 55
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m7a.medium
1
0.39 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m7a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m7a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m7a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 56
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m7a.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M7g
m7g.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m7g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m7g.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m7g.16xlarge 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7g.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M7gd
Network speciﬁcations 57
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m7gd.medi 
um 1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m7gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m7gd.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7gd.2xlarge
1
3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7gd.4xlarge
1
7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7gd.12xl 
arge
22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m7gd.16xl 
arge
30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7gd.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M7i
m7i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m7i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 58
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m7i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m7i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7i.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7i.metal 
-24xl
37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m7i.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M7i-ﬂex
m7i-ﬂex.large
1
0.39 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m7i-ﬂex. 
xlarge 1
0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 59
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m7i-ﬂex. 
2xlarge 1
1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m7i-ﬂex. 
4xlarge 1
3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7i-ﬂex. 
8xlarge 1
6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7i-ﬂex. 
12xlarge 1
9.375 / 18.75 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m7i-ﬂex. 
16xlarge 1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
M8a
m8a.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m8a.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
m8a.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
m8a.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 40 ✓ 
Yes
m8a.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
m8a.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 40 ✓ 
Yes
Network speciﬁcations 60
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8a.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 64 ✓ 
Yes
m8a.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8a.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8a.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8a.metal 
-24xl
40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8a.metal 
-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
M8azn
m8azn.med 
ium 1
2.08 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 4 ✓ 
Yes
m8azn.large 1 4.17 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
m8azn.xlarge
1
8.33 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
m8azn.3xl 
arge 1
25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
m8azn.6xl 
arge
50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
Network speciﬁcations 61
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8azn.12x 
large
100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8azn.24x 
large
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8azn.met 
al-12xl
100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8azn.met 
al-24xl
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
M8g
m8g.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m8g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m8g.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m8g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m8g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
Network speciﬁcations 62
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8g.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8g.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8g.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8g.metal 
-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8g.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M8gb
m8gb.medi 
um 1
2.083 / 
16.666
✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m8gb.large 1 4.166 / 20.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m8gb.xlarge 1 8.333 / 
26.666
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8gb.2xlarge
1
16.666 / 
33.333
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8gb.4xlarge 33.33 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m8gb.8xlarge 66.66 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
Network speciﬁcations 63
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8gb.12xl 
arge
100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
m8gb.16xl 
arge
133.33 
Gigabit
✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
m8gb.24xl 
arge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
m8gb.48xl 
arge
400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
m8gb.meta 
l-24xl
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
m8gb.meta 
l-48xl
400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
M8gd
m8gd.medi 
um 1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m8gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m8gd.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8gd.2xlarge
1
3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8gd.4xlarge
1
7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 64
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m8gd.12xl 
arge
22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
m8gd.16xl 
arge
30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8gd.24xl 
arge
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8gd.48xl 
arge
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8gd.meta 
l-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
m8gd.meta 
l-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
M8gn
m8gn.medi 
um 1
3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
m8gn.large 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
m8gn.xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
m8gn.2xlarge
1
25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 65
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8gn.4xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
m8gn.8xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
m8gn.12xl 
arge
150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
m8gn.16xl 
arge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
m8gn.24xl 
arge
300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
m8gn.48xl 
arge
600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
m8gn.meta 
l-24xl
300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
m8gn.meta 
l-48xl
600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
M8i
m8i.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
m8i.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
m8i.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
Network speciﬁcations 66

## Amazon EBS speciﬁcations

Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8i.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
m8i.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
m8i.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
m8i.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
m8i.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8i.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8i.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8i.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8i.metal 
-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8i.metal 
-96xl
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
M8id
m8id.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
Network speciﬁcations 67
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8id.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
m8id.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
m8id.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
m8id.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
m8id.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
m8id.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
m8id.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
m8id.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8id.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8id.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
m8id.meta 
l-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
Network speciﬁcations 68
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m8id.meta 
l-96xl
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
M8i-ﬂex
m8i-ﬂex.large
1
0.468 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
m8i-ﬂex. 
xlarge 1
0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
m8i-ﬂex. 
2xlarge 1
1.875 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
m8i-ﬂex. 
4xlarge 1
3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
m8i-ﬂex. 
8xlarge 1
7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
m8i-ﬂex. 
12xlarge 1
11.25 / 22.5 ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
m8i-ﬂex. 
16xlarge 1
15.0 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
Mac1
mac1.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Mac2
mac2.metal 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 69
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
Mac2-m1ultra
mac2-m1ul 
tra.metal
10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Mac2-m2
mac2-m2.m 
etal
10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Mac2-m2pro
mac2-m2pr 
o.metal
10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Mac-m4
mac-m4.metal 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Mac-m4pro
mac-m4pro 
.metal
10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
T2
t2.nano Low to 
Moderate
✗ 
No
✗ 
No
✗  No 1 2 2 ✓ 
Yes
t2.micro Low to 
Moderate
✗ 
No
✗ 
No
✗  No 1 2 2 ✓ 
Yes
t2.small Low to 
Moderate
✗ 
No
✗ 
No
✗  No 1 3 4 ✓ 
Yes
Network speciﬁcations 70
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
t2.medium Low to 
Moderate
✗ 
No
✗ 
No
✗  No 1 3 6 ✓ 
Yes
t2.large Low to 
Moderate
✗ 
No
✗ 
No
✗  No 1 3 12 ✓ 
Yes
t2.xlarge Moderate ✗ 
No
✗ 
No
✗  No 1 3 15 ✓ 
Yes
t2.2xlarge Moderate ✗ 
No
✗ 
No
✗  No 1 3 15 ✓ 
Yes
T3
t3.nano 1 0.032 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t3.micro 1 0.064 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t3.small 1 0.128 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 4 ✓ 
Yes
t3.medium 1 0.256 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 6 ✓ 
Yes
t3.large 1 0.512 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 12 ✓ 
Yes
t3.xlarge 1 1.024 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
t3.2xlarge 1 2.048 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 71
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
T3a
t3a.nano 1 0.032 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t3a.micro 1 0.064 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t3a.small 1 0.128 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
t3a.medium 1 0.256 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 6 ✓ 
Yes
t3a.large 1 0.512 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 12 ✓ 
Yes
t3a.xlarge 1 1.024 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
t3a.2xlarge 1 2.048 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
T4g
t4g.nano 1 0.032 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t4g.micro 1 0.064 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 2 2 ✓ 
Yes
t4g.small 1 0.128 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 4 ✓ 
Yes
Network speciﬁcations 72
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
t4g.medium 1 0.256 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 6 ✓ 
Yes
t4g.large 1 0.512 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 3 12 ✓ 
Yes
t4g.xlarge 1 1.024 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
t4g.2xlarge 1 2.048 / 5.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
For m6in.32xlarge, m6in.metal, m6idn.32xlarge, m6idn.metal, you must attach at 
least 2 ENIs, to separate network cards, to achieve 200 Gbps throughput. Each ENI attached 
to a network card can achieve up to 170 Gbps.
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Amazon EBS speciﬁcations 73
Amazon EC2 Instance Types
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Note
M8a, M8g, M8gd, M8i, M8id, M8i-ﬂex instance types support conﬁgurable bandwidth 
weightings. With these instance types, you can optimize an instance's bandwidth for either 
networking performance or Amazon EBS performance. The following table shows the 
default networking bandwidth performance for these instance types. For the supported 
conﬁgurable weightings, see  Conﬁgurable bandwidth weighting preferences.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M5
m5.large 1 650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 74
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5.xlarge
1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.2xlarg 
e 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.4xlarge 4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.8xlarge 6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.12xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.16xlar 
ge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.24xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 75
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M5a
m5a.large
1
650.00 / 
2880.00
81.25 / 
360.00
3600.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.xlarg 
e 1
1085.00 / 
2880.00
135.62 / 
360.00
6000.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.2xlar 
ge 1
1580.00 / 
2880.00
197.50 / 
360.00
8333.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.4xlar 
ge
2880.00 360.00 16000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.8xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.12xla 
rge
6780.00 847.50 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5a.16xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 76
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5a.24xla 
rge
13750.00 1718.75 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
M5ad
m5ad.larg 
e 1
650.00 / 
2880.00
81.25 / 
360.00
3600.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5ad.xlar 
ge 1
1085.00 / 
2880.00
135.62 / 
360.00
6000.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5ad.2xla 
rge 1
1580.00 / 
2880.00
197.50 / 
360.00
8333.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5ad.4xla 
rge
2880.00 360.00 16000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5ad.8xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5ad.12xl 
arge
6780.00 847.50 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 77
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5ad.16xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m5ad.24xl 
arge
13750.00 1718.75 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
M5d
m5d.large
1
650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5d.xlarg 
e 1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5d.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5d.4xlar 
ge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5d.8xlar 
ge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 78
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5d.12xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5d.16xla 
rge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m5d.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m5d.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M5dn
m5dn.larg 
e 1
650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5dn.xlar 
ge 1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m5dn.2xla 
rge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 79
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5dn.4xla 
rge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5dn.8xla 
rge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5dn.12xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m5dn.16xl 
arge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m5dn.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m5dn.meta 
l
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M5n
m5n.large
1
650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 80
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m5n.xlarg 
e 1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.4xlar 
ge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.8xlar 
ge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.12xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.16xla 
rge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5n.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 81
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M5zn
m5zn.larg 
e 1
800.00 / 
3170.00
100.00 / 
396.25
3333.00 / 
13333.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.xlar 
ge 1
1564.00 / 
3170.00
195.50 / 
396.25
6667.00 / 
13333.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.2xla 
rge
3170.00 396.25 13333.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.3xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.6xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.12xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m5zn.meta 
l
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6a
Amazon EBS speciﬁcations 82
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6a.large
1
650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.xlarg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 83
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6a.metal 40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6g
m6g.mediu 
m 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.large
1
630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.xlarg 
e 1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.2xlar 
ge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 84
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6g.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.8xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.12xla 
rge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.16xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6g.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6gd
m6gd.medi 
um 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6gd.larg 
e 1
630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 85
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6gd.xlar 
ge 1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6gd.2xla 
rge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6gd.4xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6gd.8xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6gd.12xl 
arge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6gd.16xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6gd.meta 
l
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6i
Amazon EBS speciﬁcations 86
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 87
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6i.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6id
m6id.large
1
650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6id.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 88
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m6id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m6id.meta 
l
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M6idn
m6idn.lar 
ge 1
1562.00 / 
25000.00
195.31 / 
3125.00
6250.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6idn.xla 
rge 1
3125.00 / 
25000.00
390.62 / 
3125.00
12500.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 89
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6idn.2xl 
arge 1
6250.00 / 
25000.00
781.25 / 
3125.00
25000.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6idn.4xl 
arge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
50000.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6idn.8xl 
arge
25000.00 3125.00 100000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
m6idn.12x 
large
37500.00 4687.50 150000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6idn.16x 
large
50000.00 6250.00 200000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m6idn.24x 
large
75000.00 9375.00 300000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m6idn.32x 
large
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
m6idn.met 
al
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 90
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M6in
m6in.large
1
1562.00 / 
25000.00
195.31 / 
3125.00
6250.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.xlar 
ge 1
3125.00 / 
25000.00
390.62 / 
3125.00
12500.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.2xla 
rge 1
6250.00 / 
25000.00
781.25 / 
3125.00
25000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.4xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
50000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.8xla 
rge
25000.00 3125.00 100000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.12xl 
arge
37500.00 4687.50 150000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.16xl 
arge
50000.00 6250.00 200000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 91
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m6in.24xl 
arge
75000.00 9375.00 300000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.32xl 
arge
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m6in.meta 
l
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M7a
m7a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.large
1
650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.xlarg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 92
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m7a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m7a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m7a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m7a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
m7a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m7a.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 93
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M7g
m7g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.xlarg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 94
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m7g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
m7g.metal 20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M7gd
m7gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m7gd.larg 
e 1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m7gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m7gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
m7gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 95
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m7gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
m7gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m7gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
m7gd.meta 
l
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
M7i
m7i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 96
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m7i.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m7i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m7i.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m7i.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
m7i.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 97
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M7i-ﬂex
m7i-ﬂex. 
large 1
312.00 / 
10000.00
39.06 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
xlarge 1
625.00 / 
10000.00
78.12 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
2xlarge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
4xlarge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
8xlarge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
12xlarge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m7i-ﬂex. 
16xlarge 1
10000.00 / 
20000.00
1250.00 / 
2500.00
40000.00 / 
80000.00
✓  Yes ✗  No 48 
(Dedicated 
limit)
M8a
Amazon EBS speciﬁcations 98
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.large
1
650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.xlarg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 99
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8a.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8a.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8a.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
M8azn
m8azn.med 
ium 1
625.00 / 
15000.00
78.12 / 
1875.00
2500.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8azn.lar 
ge 1
1250.00 / 
15000.00
156.25 / 
1875.00
5000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8azn.xla 
rge 1
2500.00 / 
15000.00
312.50 / 
1875.00
10000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 100
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8azn.3xl 
arge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8azn.6xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8azn.12x 
large
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8azn.24x 
large
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8azn.met 
al-12xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8azn.met 
al-24xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
M8g
m8g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 101
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8g.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.xlarg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m8g.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Amazon EBS speciﬁcations 102
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8g.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8g.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
m8g.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
M8gb
m8gb.medi 
um 1
1562.00 / 
25000.00
195.31 / 
3125.00
7500.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.larg 
e 1
3125.00 / 
25000.00
390.62 / 
3125.00
15000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.xlar 
ge 1
6250.00 / 
25000.00
781.25 / 
3125.00
30000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.2xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
60000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 103
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8gb.4xla 
rge
25000.00 3125.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.8xla 
rge
50000.00 6250.00 240000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.12xl 
arge
75000.00 9375.00 360000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gb.16xl 
arge
100000.00 12500.00 480000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m8gb.24xl 
arge
150000.00 18750.00 720000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8gb.48xl 
arge
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
128 
(Dedicated 
limit)
m8gb.meta 
l-24xl
150000.00 18750.00 720000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
m8gb.meta 
l-48xl
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
78 
(Dedicated 
limit)
Amazon EBS speciﬁcations 104
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M8gd
m8gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.larg 
e 1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 105
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m8gd.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8gd.48xl 
arge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8gd.meta 
l-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
m8gd.meta 
l-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
M8gn
m8gn.medi 
um 1
760.00 / 
10000.00
95.00 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.larg 
e 1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 106
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8gn.xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.2xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.4xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.8xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.12xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8gn.16xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m8gn.24xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8gn.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Amazon EBS speciﬁcations 107
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8gn.meta 
l-24xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
m8gn.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
M8i
m8i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 108
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
m8i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
m8i.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8i.96xla 
rge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8i.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8i.metal 
-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 109
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M8id
m8id.large
1
650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
m8id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 110

## Instance store speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
m8id.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8id.96xl 
arge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
m8id.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
m8id.meta 
l-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
M8i-ﬂex
m8i-ﬂex. 
large 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 111
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m8i-ﬂex. 
xlarge 1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i-ﬂex. 
2xlarge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i-ﬂex. 
4xlarge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i-ﬂex. 
8xlarge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i-ﬂex. 
12xlarge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
m8i-ﬂex. 
16xlarge 1
10000.00 / 
20000.00
1250.00 / 
2500.00
40000.00 / 
80000.00
✓  Yes ✗  No 48 
(Dedicated 
limit)
Mac1
mac1.meta 
l
14000.00 1750.00 80000.00 ✓  Yes ✗  No Up to 16 
(Shared 
limit)
Mac2
Amazon EBS speciﬁcations 112
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
mac2.meta 
l
10000.00 1250.00 55000.00 ✓  Yes ✗  No Up to 10 
(Shared 
limit)
Mac2-m1ultra
mac2-
m1ul 
tra.metal
10000.00 1250.00 55000.00 ✓  Yes ✗  No Up to 10 
(Shared 
limit)
Mac2-m2
mac2-
m2.metal
8000.00 1000.00 55000.00 ✓  Yes ✗  No Up to 10 
(Shared 
limit)
Mac2-m2pro
mac2-
m2pr 
o.metal
8000.00 1000.00 55000.00 ✓  Yes ✗  No Up to 10 
(Shared 
limit)
Mac-m4
mac-
m4.metal
8000.00 1000.00 55000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Mac-m4pro
Amazon EBS speciﬁcations 113
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
mac-
m4pro 
.metal
8000.00 1000.00 55000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
T2
T3
t3.nano 1 43.00 / 
2085.00
5.38 / 
260.62
250.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3.micro 1 87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3.small 1 174.00 / 
2085.00
21.75 / 
260.62
1000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3.medium
1
347.00 / 
2085.00
43.38 / 
260.62
2000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3.large 1 695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3.xlarge 1 695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 114
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
t3.2xlarge
1
695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
T3a
t3a.nano 1 45.00 / 
2085.00
5.62 / 
260.62
250.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3a.micro 1 90.00 / 
2085.00
11.25 / 
260.62
500.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3a.small 1 175.00 / 
2085.00
21.88 / 
260.62
1000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3a.mediu 
m 1
350.00 / 
2085.00
43.75 / 
260.62
2000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3a.large 1 695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t3a.xlarge
1
695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 115
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
t3a.2xlarge
1
695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
T4g
t4g.nano 1 43.00 / 
2085.00
5.38 / 
260.62
250.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t4g.micro 1 87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t4g.small 1 174.00 / 
2085.00
21.75 / 
260.62
1000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t4g.mediu 
m 1
347.00 / 
2085.00
43.38 / 
260.62
2000.00 / 
11800.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t4g.large 1 695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
t4g.xlarge
1
695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 116
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
t4g.2xlar 
ge 1
695.00 / 
2780.00
86.88 / 
347.50
4000.00 / 
15700.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
M5ad
m5ad.large 1 x 75 GB NVMe 
SSD
30,000 / 15,000 ✓  Yes
m5ad.xlarge 1 x 150 GB NVMe 
SSD
59,000 / 29,000 ✓  Yes
Instance store speciﬁcations 117
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m5ad.2xlarge 1 x 300 GB NVMe 
SSD
117,000 / 57,000 ✓  Yes
m5ad.4xlarge 2 x 300 GB NVMe 
SSD
234,000 / 114,000 ✓  Yes
m5ad.8xlarge 2 x 600 GB NVMe 
SSD
466,666 / 233,334 ✓  Yes
m5ad.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
m5ad.16xlarge 4 x 600 GB NVMe 
SSD
933,332 / 466,668 ✓  Yes
m5ad.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
M5d
m5d.large 1 x 75 GB NVMe 
SSD
30,000 / 15,000 ✓  Yes
m5d.xlarge 1 x 150 GB NVMe 
SSD
59,000 / 29,000 ✓  Yes
m5d.2xlarge 1 x 300 GB NVMe 
SSD
117,000 / 57,000 ✓  Yes
m5d.4xlarge 2 x 300 GB NVMe 
SSD
234,000 / 114,000 ✓  Yes
m5d.8xlarge 2 x 600 GB NVMe 
SSD
466,666 / 233,334 ✓  Yes
Instance store speciﬁcations 118
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m5d.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
m5d.16xlarge 4 x 600 GB NVMe 
SSD
933,332 / 466,668 ✓  Yes
m5d.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
m5d.metal 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
M5dn
m5dn.large 1 x 75 GB NVMe 
SSD
29,000 / 14,500 ✓  Yes
m5dn.xlarge 1 x 150 GB NVMe 
SSD
58,000 / 29,000 ✓  Yes
m5dn.2xlarge 1 x 300 GB NVMe 
SSD
116,000 / 58,000 ✓  Yes
m5dn.4xlarge 2 x 300 GB NVMe 
SSD
232,000 / 116,000 ✓  Yes
m5dn.8xlarge 2 x 600 GB NVMe 
SSD
464,000 / 232,000 ✓  Yes
m5dn.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 350,000 ✓  Yes
m5dn.16xlarge 4 x 600 GB NVMe 
SSD
930,000 / 465,000 ✓  Yes
Instance store speciﬁcations 119

## Security speciﬁcations

Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m5dn.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
700,000
✓  Yes
m5dn.metal 4 x 900 GB NVMe 
SSD
1,400,000 / 
700,000
✓  Yes
M6gd
m6gd.medium 1 x 59 GB NVMe 
SSD
13,438 / 5,625 ✓  Yes
m6gd.large 1 x 118 GB NVMe 
SSD
26,875 / 11,250 ✓  Yes
m6gd.xlarge 1 x 237 GB NVMe 
SSD
53,750 / 22,500 ✓  Yes
m6gd.2xlarge 1 x 474 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
m6gd.4xlarge 1 x 950 GB NVMe 
SSD
215,000 / 90,000 ✓  Yes
m6gd.8xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
m6gd.12xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
m6gd.16xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
m6gd.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
M6id
Instance store speciﬁcations 120
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m6id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
m6id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
m6id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
m6id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
m6id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
m6id.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
m6id.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
m6id.24xlarge 4 x 1425 GB NVMe 
SSD
1,609,996 / 
805,000
✓  Yes
m6id.32xlarge 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
m6id.metal 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
M6idn
m6idn.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
Instance store speciﬁcations 121
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m6idn.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
m6idn.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
m6idn.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
m6idn.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
m6idn.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
m6idn.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
m6idn.24xlarge 4 x 1425 GB NVMe 
SSD
1,609,996 / 
805,000
✓  Yes
m6idn.32xlarge 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
m6idn.metal 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
M7gd
m7gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
m7gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
Instance store speciﬁcations 122
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m7gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
m7gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
m7gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
m7gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
m7gd.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
m7gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
m7gd.metal 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
M8gd
m8gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
m8gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
m8gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
m8gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
Instance store speciﬁcations 123
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m8gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
m8gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
m8gd.12xlarge 3 x 950 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
m8gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
m8gd.24xlarge 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
m8gd.48xlarge 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
m8gd.metal-24xl 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
m8gd.metal-48xl 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
M8id
m8id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
m8id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
m8id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
Instance store speciﬁcations 124
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m8id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
m8id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
m8id.12xlarge 1 x 2850 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
m8id.16xlarge 1 x 3800 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
m8id.24xlarge 2 x 2850 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
m8id.32xlarge 2 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
m8id.48xlarge 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
m8id.96xlarge 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
m8id.metal-48xl 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
m8id.metal-96xl 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
Mac-m4
mac-m4.metal 1 x 1900 GB NVMe 
SSD
550,000 / 275,000 ✓  Yes
Mac-m4pro
Instance store speciﬁcations 125
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
mac-m4pro 
.metal
1 x 1900 GB NVMe 
SSD
550,000 / 275,000 ✓  Yes
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
M5
m5.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
m5.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 126
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
M5a
m5a.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
m5a.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5a.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 127
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5a.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5a.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5a.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5a.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m5a.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
M5ad
m5ad.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
m5ad.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5ad.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5ad.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5ad.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5ad.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5ad.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 128
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5ad.24xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
M5d
m5d.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
m5d.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.24xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m5d.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
M5dn
m5dn.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m5dn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 129
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5dn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m5dn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
M5n
m5n.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m5n.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 130
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5n.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5n.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M5zn
m5zn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m5zn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5zn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5zn.3xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5zn.6xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m5zn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 131
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m5zn.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M6a
m6a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✗  No
m6a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
m6a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
m6a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
m6a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
m6a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 132
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6a.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M6g
m6g.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
m6g.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 133
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6g.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
m6g.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
M6gd
m6gd.medium ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
m6gd.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 134
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6gd.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
m6gd.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
M6i
m6i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m6i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 135
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6i.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M6id
m6id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m6id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6id.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
M6idn
Security speciﬁcations 136
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6idn.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m6idn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m6idn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
M6in
m6in.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m6in.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 137
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m6in.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m6in.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M7a
m7a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 138
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m7a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 139
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m7a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M7g
m7g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 140
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m7g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7g.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M7gd
m7gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m7gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m7gd.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 141
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
M7i
m7i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 142
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m7i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m7i.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m7i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M7i-ﬂex
m7i-ﬂex.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i-ﬂex.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i-ﬂex.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i-ﬂex.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i-ﬂex.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 143
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m7i-ﬂex.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m7i-ﬂex.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
M8a
m8a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 144
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8a.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m8a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8azn
m8azn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8azn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 145
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8azn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8azn.3xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8azn.6xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8azn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8azn.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8azn.metal-12xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m8azn.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8g
m8g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 146
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 147
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8g.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8g.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m8g.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8gb
m8gb.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8gb.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 148
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8gb.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gb.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m8gb.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8gd
m8gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m8gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 149
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8gd.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
m8gd.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
M8gn
m8gn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8gn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 150
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8gn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8gn.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 151
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8gn.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8i
m8i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 152
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
m8i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
m8i.metal-96xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
M8id
m8id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
m8id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 153

## Compute optimized

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.96xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
m8id.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
m8id.metal-96xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
M8i-ﬂex
m8i-ﬂex.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i-ﬂex.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i-ﬂex.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i-ﬂex.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 154

## Instance families and instance types

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m8i-ﬂex.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i-ﬂex.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
m8i-ﬂex.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Mac1
mac1.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Mac2
mac2.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Mac2-m1ultra
mac2-m1ul 
tra.metal
✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Mac2-m2
Security speciﬁcations 155
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
mac2-m2.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Mac2-m2pro
mac2-m2pr 
o.metal
✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Mac-m4
mac-m4.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Mac-m4pro
mac-m4pro.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
T2
t2.nano ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
t2.micro ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
t2.small ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 156
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
t2.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
t2.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
t2.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
t2.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
T3
t3.nano ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3.micro ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3.small ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
Security speciﬁcations 157

## Instance family summary

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
t3.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
T3a
t3a.nano ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3a.micro ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3a.small ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3a.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3a.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
Security speciﬁcations 158
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
t3a.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t3a.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
T4g
t4g.nano ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t4g.micro ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t4g.small ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t4g.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t4g.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
t4g.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
Security speciﬁcations 159

## Performance speciﬁcations

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
t4g.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
Speciﬁcations for Amazon EC2 compute optimized instances
Compute optimized instances are designed for compute intensive applications that beneﬁt 
from high performance processors. These instances are ideal for batch processing workloads, 
media transcoding, high performance web servers, high performance computing (HPC), scientiﬁc 
modeling, dedicated gaming servers, ad server engines, and machine learning inference.
For information on previous generation instance types of this category, such as C4 instances, see
Speciﬁcations for Amazon EC2 previous generation instances.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Compute optimized 160
Amazon EC2 Instance Types
Instance families and instance types
Instance 
family
Available instance types
C5 c5.large | c5.xlarge  | c5.2xlarge  | c5.4xlarge  | c5.9xlarge  |
c5.12xlarge  | c5.18xlarge  | c5.24xlarge  | c5.metal
C5a c5a.large  | c5a.xlarge  | c5a.2xlarge  | c5a.4xlarge  | c5a.8xlar 
ge  | c5a.12xlarge  | c5a.16xlarge  | c5a.24xlarge
C5ad c5ad.large  | c5ad.xlarge  | c5ad.2xlarge  | c5ad.4xlarge  |
c5ad.8xlarge  | c5ad.12xlarge  | c5ad.16xlarge  | c5ad.24xlarge
C5d c5d.large  | c5d.xlarge  | c5d.2xlarge  | c5d.4xlarge  | c5d.9xlar 
ge  | c5d.12xlarge  | c5d.18xlarge  | c5d.24xlarge  | c5d.metal
C5n c5n.large  | c5n.xlarge  | c5n.2xlarge  | c5n.4xlarge  | c5n.9xlar 
ge  | c5n.18xlarge  | c5n.metal
C6a c6a.large  | c6a.xlarge  | c6a.2xlarge  | c6a.4xlarge  | c6a.8xlar 
ge  | c6a.12xlarge  | c6a.16xlarge  | c6a.24xlarge  | c6a.32xlarge  |
c6a.48xlarge  | c6a.metal
C6g c6g.medium  | c6g.large  | c6g.xlarge  | c6g.2xlarge  | c6g.4xlarge
| c6g.8xlarge  | c6g.12xlarge  | c6g.16xlarge  | c6g.metal
C6gd c6gd.medium  | c6gd.large  | c6gd.xlarge  | c6gd.2xlarge  |
c6gd.4xlarge  | c6gd.8xlarge  | c6gd.12xlarge  | c6gd.16xlarge  |
c6gd.metal
C6gn c6gn.medium  | c6gn.large  | c6gn.xlarge  | c6gn.2xlarge  |
c6gn.4xlarge  | c6gn.8xlarge  | c6gn.12xlarge  | c6gn.16xlarge
C6i c6i.large  | c6i.xlarge  | c6i.2xlarge  | c6i.4xlarge  | c6i.8xlar 
ge  | c6i.12xlarge  | c6i.16xlarge  | c6i.24xlarge  | c6i.32xlarge  |
c6i.metal
Instance families and instance types 161
Amazon EC2 Instance Types
Instance 
family
Available instance types
C6id c6id.large  | c6id.xlarge  | c6id.2xlarge  | c6id.4xlarge  |
c6id.8xlarge  | c6id.12xlarge  | c6id.16xlarge  | c6id.24xlarge  |
c6id.32xlarge  | c6id.metal
C6in c6in.large  | c6in.xlarge  | c6in.2xlarge  | c6in.4xlarge  |
c6in.8xlarge  | c6in.12xlarge  | c6in.16xlarge  | c6in.24xlarge  |
c6in.32xlarge  | c6in.metal
C7a c7a.medium  | c7a.large  | c7a.xlarge  | c7a.2xlarge  | c7a.4xlar 
ge  | c7a.8xlarge  | c7a.12xlarge  | c7a.16xlarge  | c7a.24xlarge  |
c7a.32xlarge  | c7a.48xlarge  | c7a.metal-48xl
C7g c7g.medium  | c7g.large  | c7g.xlarge  | c7g.2xlarge  | c7g.4xlarge
| c7g.8xlarge  | c7g.12xlarge  | c7g.16xlarge  | c7g.metal
C7gd c7gd.medium  | c7gd.large  | c7gd.xlarge  | c7gd.2xlarge  |
c7gd.4xlarge  | c7gd.8xlarge  | c7gd.12xlarge  | c7gd.16xlarge  |
c7gd.metal
C7gn c7gn.medium  | c7gn.large  | c7gn.xlarge  | c7gn.2xlarge  |
c7gn.4xlarge  | c7gn.8xlarge  | c7gn.12xlarge  | c7gn.16xlarge  |
c7gn.metal
C7i c7i.large  | c7i.xlarge  | c7i.2xlarge  | c7i.4xlarge  | c7i.8xlar 
ge  | c7i.12xlarge  | c7i.16xlarge  | c7i.24xlarge  | c7i.48xlarge  |
c7i.metal-24xl  | c7i.metal-48xl
C7i-ﬂex c7i-flex.large  | c7i-flex.xlarge  | c7i-flex.2xlarge  | c7i-flex. 
4xlarge  | c7i-flex.8xlarge  | c7i-flex.12xlarge  | c7i-flex. 
16xlarge
C8a c8a.medium  | c8a.large  | c8a.xlarge  | c8a.2xlarge  | c8a.4xlar 
ge  | c8a.8xlarge  | c8a.12xlarge  | c8a.16xlarge  | c8a.24xlarge  |
c8a.48xlarge  | c8a.metal-24xl  | c8a.metal-48xl
Instance families and instance types 162
Amazon EC2 Instance Types
Instance 
family
Available instance types
C8g c8g.medium  | c8g.large  | c8g.xlarge  | c8g.2xlarge  | c8g.4xlar 
ge  | c8g.8xlarge  | c8g.12xlarge  | c8g.16xlarge  | c8g.24xlarge  |
c8g.48xlarge  | c8g.metal-24xl  | c8g.metal-48xl
C8gb c8gb.medium  | c8gb.large  | c8gb.xlarge  | c8gb.2xlarge  |
c8gb.4xlarge  | c8gb.8xlarge  | c8gb.12xlarge  | c8gb.16xlarge
| c8gb.24xlarge  | c8gb.48xlarge  | c8gb.metal-24xl  | c8gb.meta 
l-48xl
C8gd c8gd.medium  | c8gd.large  | c8gd.xlarge  | c8gd.2xlarge  |
c8gd.4xlarge  | c8gd.8xlarge  | c8gd.12xlarge  | c8gd.16xlarge
| c8gd.24xlarge  | c8gd.48xlarge  | c8gd.metal-24xl  | c8gd.meta 
l-48xl
C8gn c8gn.medium  | c8gn.large  | c8gn.xlarge  | c8gn.2xlarge  |
c8gn.4xlarge  | c8gn.8xlarge  | c8gn.12xlarge  | c8gn.16xlarge
| c8gn.24xlarge  | c8gn.48xlarge  | c8gn.metal-24xl  | c8gn.meta 
l-48xl
C8i c8i.large  | c8i.xlarge  | c8i.2xlarge  | c8i.4xlarge  | c8i.8xlar 
ge  | c8i.12xlarge  | c8i.16xlarge  | c8i.24xlarge  | c8i.32xlarge  |
c8i.48xlarge  | c8i.96xlarge  | c8i.metal-48xl  | c8i.metal-96xl
C8id c8id.large  | c8id.xlarge  | c8id.2xlarge  | c8id.4xlarge  |
c8id.8xlarge  | c8id.12xlarge  | c8id.16xlarge  | c8id.24xlarge  |
c8id.32xlarge  | c8id.48xlarge  | c8id.96xlarge  | c8id.metal-48xl
| c8id.metal-96xl
C8i-ﬂex c8i-flex.large  | c8i-flex.xlarge  | c8i-flex.2xlarge  | c8i-flex. 
4xlarge  | c8i-flex.8xlarge  | c8i-flex.12xlarge  | c8i-flex. 
16xlarge
Instance families and instance types 163
Amazon EC2 Instance Types
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
C5 Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C5a Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
C5ad Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
C5d Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C5n Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
C6a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C6g Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C6gd Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C6gn Nitro v4 AWS 
Graviton 
(arm64)
✗  No ✓  Yes ✓  Yes ✓  Yes Linux
C6i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 164
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
C6id Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C6in Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C7a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C7g Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C7gd Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C7gn Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C7i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C7i-ﬂex Nitro v4 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
C8a Nitro v6 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C8g Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
Instance family summary 165
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
C8gb Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C8gd Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C8gn Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
C8i Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C8id Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
C8i-ﬂex Nitro v6 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
C5
c5.large 4.00 Intel Xeon Platinum 
8124M
2 1 2 ✗  No ✗  No
Performance speciﬁcations 166
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c5.xlarge 8.00 Intel Xeon Platinum 
8124M
4 2 2 ✗  No ✗  No
c5.2xlarge 16.00 Intel Xeon Platinum 
8124M
8 4 2 ✗  No ✗  No
c5.4xlarge 32.00 Intel Xeon Platinum 
8124M
16 8 2 ✗  No ✗  No
c5.9xlarge 72.00 Intel Xeon Platinum 
8124M
36 18 2 ✗  No ✗  No
c5.12xlarge 96.00 2nd Gen Intel Xeon 
Platinum 8275CL
48 24 2 ✗  No ✗  No
c5.18xlarge 144.00 Intel Xeon Platinum 
8124M
72 36 2 ✗  No ✗  No
c5.24xlarge 192.00 2nd Gen Intel Xeon 
Platinum 8275CL
96 48 2 ✗  No ✗  No
c5.metal 192.00 2nd Gen Intel Xeon 
Platinum 8275CL
96 48 2 ✗  No ✗  No
C5a
c5a.large 4.00 2nd Gen AMD EPYC 
7R32
2 1 2 ✗  No ✗  No
c5a.xlarge 8.00 2nd Gen AMD EPYC 
7R32
4 2 2 ✗  No ✗  No
c5a.2xlarge 16.00 2nd Gen AMD EPYC 
7R32
8 4 2 ✗  No ✗  No
Performance speciﬁcations 167
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c5a.4xlarge 32.00 2nd Gen AMD EPYC 
7R32
16 8 2 ✗  No ✗  No
c5a.8xlarge 64.00 2nd Gen AMD EPYC 
7R32
32 16 2 ✗  No ✗  No
c5a.12xlarge 96.00 2nd Gen AMD EPYC 
7R32
48 24 2 ✗  No ✗  No
c5a.16xlarge 128.00 2nd Gen AMD EPYC 
7R32
64 32 2 ✗  No ✗  No
c5a.24xlarge 192.00 2nd Gen AMD EPYC 
7R32
96 48 2 ✗  No ✗  No
C5ad
c5ad.large 4.00 2nd Gen AMD EPYC 
7R32
2 1 2 ✗  No ✗  No
c5ad.xlarge 8.00 2nd Gen AMD EPYC 
7R32
4 2 2 ✗  No ✗  No
c5ad.2xlarge 16.00 2nd Gen AMD EPYC 
7R32
8 4 2 ✗  No ✗  No
c5ad.4xlarge 32.00 2nd Gen AMD EPYC 
7R32
16 8 2 ✗  No ✗  No
c5ad.8xlarge 64.00 2nd Gen AMD EPYC 
7R32
32 16 2 ✗  No ✗  No
c5ad.12xl 
arge
96.00 2nd Gen AMD EPYC 
7R32
48 24 2 ✗  No ✗  No
Performance speciﬁcations 168
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c5ad.16xl 
arge
128.00 2nd Gen AMD EPYC 
7R32
64 32 2 ✗  No ✗  No
c5ad.24xl 
arge
192.00 2nd Gen AMD EPYC 
7R32
96 48 2 ✗  No ✗  No
C5d
c5d.large 4.00 Intel Xeon Platinum 
8124M
2 1 2 ✗  No ✗  No
c5d.xlarge 8.00 Intel Xeon Platinum 
8124M
4 2 2 ✗  No ✗  No
c5d.2xlarge 16.00 Intel Xeon Platinum 
8124M
8 4 2 ✗  No ✗  No
c5d.4xlarge 32.00 Intel Xeon Platinum 
8124M
16 8 2 ✗  No ✗  No
c5d.9xlarge 72.00 Intel Xeon Platinum 
8124M
36 18 2 ✗  No ✗  No
c5d.12xlarge 96.00 2nd Gen Intel Xeon 
Platinum 8275CL
48 24 2 ✗  No ✗  No
c5d.18xlarge 144.00 Intel Xeon Platinum 
8124M
72 36 2 ✗  No ✗  No
c5d.24xlarge 192.00 2nd Gen Intel Xeon 
Platinum 8275CL
96 48 2 ✗  No ✗  No
c5d.metal 192.00 2nd Gen Intel Xeon 
Platinum 8275CL
96 48 2 ✗  No ✗  No
C5n
Performance speciﬁcations 169
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c5n.large 5.25 Intel Xeon Platinum 
8124M
2 1 2 ✗  No ✗  No
c5n.xlarge 10.50 Intel Xeon Platinum 
8124M
4 2 2 ✗  No ✗  No
c5n.2xlarge 21.00 Intel Xeon Platinum 
8124M
8 4 2 ✗  No ✗  No
c5n.4xlarge 42.00 Intel Xeon Platinum 
8124M
16 8 2 ✗  No ✗  No
c5n.9xlarge 96.00 Intel Xeon Platinum 
8124M
36 18 2 ✗  No ✗  No
c5n.18xlarge 192.00 Intel Xeon Platinum 
8124M
72 36 2 ✗  No ✗  No
c5n.metal 192.00 Intel Xeon Platinum 
8124M
72 36 2 ✗  No ✗  No
C6a
c6a.large 4.00 AMD EPYC 7R13 2 1 2 ✗  No ✗  No
c6a.xlarge 8.00 AMD EPYC 7R13 4 2 2 ✗  No ✗  No
c6a.2xlarge 16.00 AMD EPYC 7R13 8 4 2 ✗  No ✗  No
c6a.4xlarge 32.00 AMD EPYC 7R13 16 8 2 ✗  No ✗  No
c6a.8xlarge 64.00 AMD EPYC 7R13 32 16 2 ✗  No ✗  No
c6a.12xlarge 96.00 AMD EPYC 7R13 48 24 2 ✗  No ✗  No
c6a.16xlarge 128.00 AMD EPYC 7R13 64 32 2 ✗  No ✗  No
Performance speciﬁcations 170
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c6a.24xlarge 192.00 AMD EPYC 7R13 96 48 2 ✗  No ✗  No
c6a.32xlarge 256.00 AMD EPYC 7R13 128 64 2 ✗  No ✗  No
c6a.48xlarge 384.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
c6a.metal 384.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
C6g
c6g.medium 2.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
c6g.large 4.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
c6g.xlarge 8.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
c6g.2xlarge 16.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
c6g.4xlarge 32.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
c6g.8xlarge 64.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
c6g.12xlarge 96.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
c6g.16xlarge 128.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
c6g.metal 128.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
Performance speciﬁcations 171
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
C6gd
c6gd.medium 2.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
c6gd.large 4.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
c6gd.xlarge 8.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
c6gd.2xlarge 16.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
c6gd.4xlarge 32.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
c6gd.8xlarge 64.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
c6gd.12xl 
arge
96.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
c6gd.16xl 
arge
128.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
c6gd.metal 128.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
C6gn
c6gn.medium 2.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
c6gn.large 4.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
Performance speciﬁcations 172
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c6gn.xlarge 8.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
c6gn.2xlarge 16.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
c6gn.4xlarge 32.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
c6gn.8xlarge 64.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
c6gn.12xl 
arge
96.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
c6gn.16xl 
arge
128.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
C6i
c6i.large 4.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
c6i.xlarge 8.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
c6i.2xlarge 16.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
c6i.4xlarge 32.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
c6i.8xlarge 64.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
c6i.12xlarge 96.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
c6i.16xlarge 128.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
c6i.24xlarge 192.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
c6i.32xlarge 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
Performance speciﬁcations 173
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c6i.metal 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
C6id
c6id.large 4.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
c6id.xlarge 8.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
c6id.2xlarge 16.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
c6id.4xlarge 32.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
c6id.8xlarge 64.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
c6id.12xlarge 96.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
c6id.16xlarge 128.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
c6id.24xlarge 192.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
c6id.32xlarge 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
c6id.metal 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
C6in
c6in.large 4.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
c6in.xlarge 8.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
c6in.2xlarge 16.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
c6in.4xlarge 32.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
c6in.8xlarge 64.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
c6in.12xlarge 96.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
Performance speciﬁcations 174
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c6in.16xlarge 128.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
c6in.24xlarge 192.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
c6in.32xlarge 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
c6in.metal 256.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
C7a
c7a.medium 2.00 AMD EPYC 9R14 1 1 1 ✗  No ✗  No
c7a.large 4.00 AMD EPYC 9R14 2 2 1 ✗  No ✗  No
c7a.xlarge 8.00 AMD EPYC 9R14 4 4 1 ✗  No ✗  No
c7a.2xlarge 16.00 AMD EPYC 9R14 8 8 1 ✗  No ✗  No
c7a.4xlarge 32.00 AMD EPYC 9R14 16 16 1 ✗  No ✗  No
c7a.8xlarge 64.00 AMD EPYC 9R14 32 32 1 ✗  No ✗  No
c7a.12xlarge 96.00 AMD EPYC 9R14 48 48 1 ✗  No ✗  No
c7a.16xlarge 128.00 AMD EPYC 9R14 64 64 1 ✗  No ✗  No
c7a.24xlarge 192.00 AMD EPYC 9R14 96 96 1 ✗  No ✗  No
c7a.32xlarge 256.00 AMD EPYC 9R14 128 128 1 ✗  No ✗  No
c7a.48xlarge 384.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
c7a.metal 
-48xl
384.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
C7g
Performance speciﬁcations 175
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c7g.medium 2.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
c7g.large 4.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
c7g.xlarge 8.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
c7g.2xlarge 16.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
c7g.4xlarge 32.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
c7g.8xlarge 64.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
c7g.12xlarge 96.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
c7g.16xlarge 128.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
c7g.metal 128.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
C7gd
c7gd.medium 2.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
c7gd.large 4.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
Performance speciﬁcations 176
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c7gd.xlarge 8.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
c7gd.2xlarge 16.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
c7gd.4xlarge 32.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
c7gd.8xlarge 64.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
c7gd.12xl 
arge
96.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
c7gd.16xl 
arge
128.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
c7gd.metal 128.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
C7gn
c7gn.medium 2.00 AWS Graviton3E 
Processor
1 1 1 ✗  No ✗  No
c7gn.large 4.00 AWS Graviton3E 
Processor
2 2 1 ✗  No ✗  No
c7gn.xlarge 8.00 AWS Graviton3E 
Processor
4 4 1 ✗  No ✗  No
c7gn.2xlarge 16.00 AWS Graviton3E 
Processor
8 8 1 ✗  No ✗  No
Performance speciﬁcations 177
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c7gn.4xlarge 32.00 AWS Graviton3E 
Processor
16 16 1 ✗  No ✗  No
c7gn.8xlarge 64.00 AWS Graviton3E 
Processor
32 32 1 ✗  No ✗  No
c7gn.12xl 
arge
96.00 AWS Graviton3E 
Processor
48 48 1 ✗  No ✗  No
c7gn.16xl 
arge
128.00 AWS Graviton3E 
Processor
64 64 1 ✗  No ✗  No
c7gn.metal 128.00 AWS Graviton3E 
Processor
64 64 1 ✗  No ✗  No
C7i
c7i.large 4.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
c7i.xlarge 8.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
c7i.2xlarge 16.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
c7i.4xlarge 32.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
c7i.8xlarge 64.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
c7i.12xlarge 96.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
Performance speciﬁcations 178
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c7i.16xlarge 128.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
c7i.24xlarge 192.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
c7i.48xlarge 384.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
c7i.metal 
-24xl
192.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
c7i.metal 
-48xl
384.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
C7i-ﬂex
c7i-ﬂex.large 4.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
c7i-ﬂex. 
xlarge
8.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
c7i-ﬂex. 
2xlarge
16.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
c7i-ﬂex. 
4xlarge
32.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
c7i-ﬂex. 
8xlarge
64.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
c7i-ﬂex. 
12xlarge
96.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
Performance speciﬁcations 179
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c7i-ﬂex. 
16xlarge
128.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
C8a
c8a.medium 2.00 AMD EPYC 9R45 1 1 1 ✗  No ✗  No
c8a.large 4.00 AMD EPYC 9R45 2 2 1 ✗  No ✗  No
c8a.xlarge 8.00 AMD EPYC 9R45 4 4 1 ✗  No ✗  No
c8a.2xlarge 16.00 AMD EPYC 9R45 8 8 1 ✗  No ✗  No
c8a.4xlarge 32.00 AMD EPYC 9R45 16 16 1 ✗  No ✗  No
c8a.8xlarge 64.00 AMD EPYC 9R45 32 32 1 ✗  No ✗  No
c8a.12xlarge 96.00 AMD EPYC 9R45 48 48 1 ✗  No ✗  No
c8a.16xlarge 128.00 AMD EPYC 9R45 64 64 1 ✗  No ✗  No
c8a.24xlarge 192.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
c8a.48xlarge 384.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
c8a.metal 
-24xl
192.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
c8a.metal 
-48xl
384.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
C8g
c8g.medium 2.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
Performance speciﬁcations 180
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8g.large 4.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
c8g.xlarge 8.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
c8g.2xlarge 16.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
c8g.4xlarge 32.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
c8g.8xlarge 64.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
c8g.12xlarge 96.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
c8g.16xlarge 128.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
c8g.24xlarge 192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8g.48xlarge 384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
c8g.metal 
-24xl
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8g.metal 
-48xl
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
C8gb
Performance speciﬁcations 181

## Network speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8gb.medium 2.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
c8gb.large 4.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
c8gb.xlarge 8.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
c8gb.2xlarge 16.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
c8gb.4xlarge 32.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
c8gb.8xlarge 64.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
c8gb.12xl 
arge
96.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
c8gb.16xl 
arge
128.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
c8gb.24xl 
arge
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8gb.48xl 
arge
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
c8gb.meta 
l-24xl
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8gb.meta 
l-48xl
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Performance speciﬁcations 182
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
C8gd
c8gd.medium 2.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
c8gd.large 4.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
c8gd.xlarge 8.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
c8gd.2xlarge 16.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
c8gd.4xlarge 32.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
c8gd.8xlarge 64.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
c8gd.12xl 
arge
96.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
c8gd.16xl 
arge
128.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
c8gd.24xl 
arge
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8gd.48xl 
arge
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
c8gd.meta 
l-24xl
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
Performance speciﬁcations 183
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8gd.meta 
l-48xl
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
C8gn
c8gn.medium 2.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
c8gn.large 4.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
c8gn.xlarge 8.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
c8gn.2xlarge 16.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
c8gn.4xlarge 32.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
c8gn.8xlarge 64.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
c8gn.12xl 
arge
96.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
c8gn.16xl 
arge
128.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
c8gn.24xl 
arge
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8gn.48xl 
arge
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Performance speciﬁcations 184
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8gn.meta 
l-24xl
192.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
c8gn.meta 
l-48xl
384.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
C8i
c8i.large 4.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
c8i.xlarge 8.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
c8i.2xlarge 16.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
c8i.4xlarge 32.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
c8i.8xlarge 64.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
c8i.12xlarge 96.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
c8i.16xlarge 128.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
c8i.24xlarge 192.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
c8i.32xlarge 256.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
Performance speciﬁcations 185
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8i.48xlarge 384.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
c8i.96xlarge 768.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
c8i.metal 
-48xl
384.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
c8i.metal 
-96xl
768.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
C8id
c8id.large 4.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
c8id.xlarge 8.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
c8id.2xlarge 16.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
c8id.4xlarge 32.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
c8id.8xlarge 64.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
c8id.12xlarge 96.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
c8id.16xlarge 128.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
Performance speciﬁcations 186
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8id.24xlarge 192.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
c8id.32xlarge 256.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
c8id.48xlarge 384.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
c8id.96xlarge 768.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
c8id.meta 
l-48xl
384.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
c8id.meta 
l-96xl
768.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
C8i-ﬂex
c8i-ﬂex.large 4.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
c8i-ﬂex. 
xlarge
8.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
c8i-ﬂex. 
2xlarge
16.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
c8i-ﬂex. 
4xlarge
32.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
c8i-ﬂex. 
8xlarge
64.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
Performance speciﬁcations 187
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c8i-ﬂex. 
12xlarge
96.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
c8i-ﬂex. 
16xlarge
128.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
Network speciﬁcations
Note
C8a, C8g, C8gd, C8i, C8id, C8i-ﬂex instance types support conﬁgurable bandwidth 
weightings. With these instance types, you can optimize an instance's bandwidth for either 
networking performance or Amazon EBS performance. The following table shows the 
default networking bandwidth performance for these instance types. For the supported 
conﬁgurable weightings, see  Conﬁgurable bandwidth weighting preferences.
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
C5
c5.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c5.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 188
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c5.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5.9xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5.18xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C5a
c5a.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c5a.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5a.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5a.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5a.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 189
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c5a.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5a.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5a.24xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C5ad
c5ad.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c5ad.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5ad.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5ad.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5ad.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5ad.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5ad.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5ad.24xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Network speciﬁcations 190
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
C5d
c5d.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c5d.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5d.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5d.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5d.9xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5d.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5d.18xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5d.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5d.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C5n
c5n.large 1 3.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 191
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c5n.xlarge 1 5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5n.2xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c5n.4xlarge 1 15.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5n.9xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c5n.18xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c5n.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C6a
c6a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 192
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6a.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C6g
c6g.medium 1 0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c6g.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6g.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6g.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6g.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 193
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6g.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6g.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6g.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c6g.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C6gd
c6gd.medium
1
0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c6gd.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6gd.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6gd.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6gd.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6gd.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6gd.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 194
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6gd.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
c6gd.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C6gn
c6gn.medium
1
1.6 / 16.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c6gn.large 1 3.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6gn.xlarge 1 6.3 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6gn.2xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6gn.4xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6gn.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6gn.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6gn.16xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C6i
Network speciﬁcations 195
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6i.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6i.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C6id
c6id.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 196
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6id.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6id.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6id.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6id.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6id.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6id.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6id.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6id.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6id.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C6in
c6in.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c6in.xlarge 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 197
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c6in.2xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c6in.4xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c6in.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6in.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c6in.16xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6in.24xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c6in.32xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
c6in.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
C7a
c7a.medium 1 0.39 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c7a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c7a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 198
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c7a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7a.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C7g
c7g.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c7g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 199
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c7g.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7g.16xlarge 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7g.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C7gd
c7gd.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c7gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c7gd.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7gd.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 200
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c7gd.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7gd.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7gd.16xlarge 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7gd.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C7gn
c7gn.medium
1
3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c7gn.large 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c7gn.xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7gn.2xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7gn.4xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7gn.8xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
Network speciﬁcations 201
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c7gn.12xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7gn.16xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7gn.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C7i
c7i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c7i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c7i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 202
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c7i.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7i.metal-24xl 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c7i.metal-48xl 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C7i-ﬂex
c7i-ﬂex.large 1 0.39 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c7i-ﬂex.xlarge
1
0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7i-ﬂex. 
2xlarge 1
1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c7i-ﬂex. 
4xlarge 1
3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7i-ﬂex. 
8xlarge 1
6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7i-ﬂex. 
12xlarge 1
9.375 / 18.75 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c7i-ﬂex. 
16xlarge 1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
C8a
Network speciﬁcations 203
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8a.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c8a.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
c8a.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
c8a.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 40 ✓ 
Yes
c8a.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
c8a.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 40 ✓ 
Yes
c8a.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 64 ✓ 
Yes
c8a.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
c8a.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
c8a.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8a.metal 
-24xl
40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
Network speciﬁcations 204
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8a.metal 
-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
C8g
c8g.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c8g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c8g.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c8g.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8g.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8g.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 205
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8g.metal 
-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8g.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C8gb
c8gb.medium
1
2.083 / 
16.666
✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c8gb.large 1 4.166 / 20.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c8gb.xlarge 1 8.333 / 
26.666
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gb.2xlarge 1 16.666 / 
33.333
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gb.4xlarge 33.33 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8gb.8xlarge 66.66 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
c8gb.12xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
c8gb.16xlarge 133.33 
Gigabit
✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
c8gb.24xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
Network speciﬁcations 206

## Amazon EBS speciﬁcations

Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8gb.48xlarge 400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
c8gb.meta 
l-24xl
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
c8gb.meta 
l-48xl
400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
C8gd
c8gd.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c8gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c8gd.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gd.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gd.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8gd.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
c8gd.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 207
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8gd.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8gd.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8gd.meta 
l-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
c8gd.meta 
l-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
C8gn
c8gn.medium
1
3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
c8gn.large 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
c8gn.xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gn.2xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
c8gn.4xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
c8gn.8xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
c8gn.12xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
Network speciﬁcations 208
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8gn.16xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
c8gn.24xlarge 300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
c8gn.48xlarge 600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
c8gn.meta 
l-24xl
300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
c8gn.meta 
l-48xl
600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
C8i
c8i.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
c8i.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
c8i.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
c8i.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
c8i.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
c8i.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
Network speciﬁcations 209
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8i.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
c8i.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
c8i.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8i.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8i.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8i.metal-48xl 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8i.metal-96xl 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
C8id
c8id.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
c8id.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
c8id.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
c8id.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
Network speciﬁcations 210
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8id.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
c8id.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
c8id.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
c8id.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
c8id.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8id.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8id.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8id.meta 
l-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
c8id.meta 
l-96xl
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
C8i-ﬂex
c8i-ﬂex.large 1 0.468 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
c8i-ﬂex.xlarge
1
0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
Network speciﬁcations 211
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c8i-ﬂex. 
2xlarge 1
1.875 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
c8i-ﬂex. 
4xlarge 1
3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
c8i-ﬂex. 
8xlarge 1
7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
c8i-ﬂex. 
12xlarge 1
11.25 / 22.5 ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
c8i-ﬂex. 
16xlarge 1
15.0 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
For c6in.32xlarge, c6in.metal, you must attach at least 2 ENIs, to separate network 
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up 
to 170 Gbps.
For c8gn.48xlarge, c8gn.metal-48xl, you must attach at least 2 ENIs, to separate 
network cards, to achieve 600 Gbps throughput. Each ENI attached to a network card can 
achieve up to 300 Gbps.
Network speciﬁcations 212
Amazon EC2 Instance Types
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Note
C8a, C8g, C8gd, C8i, C8id, C8i-ﬂex instance types support conﬁgurable bandwidth 
weightings. With these instance types, you can optimize an instance's bandwidth for either 
networking performance or Amazon EBS performance. The following table shows the 
default networking bandwidth performance for these instance types. For the supported 
conﬁgurable weightings, see  Conﬁgurable bandwidth weighting preferences.
Amazon EBS speciﬁcations 213
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
C5
c5.large 1 650.00 / 
4750.00
81.25 / 
593.75
4000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.xlarge 1 1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.2xlarge
1
2300.00 / 
4750.00
287.50 / 
593.75
10000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.4xlarge 4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.9xlarge 9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.12xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.18xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 214
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c5.24xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C5a
c5a.large 1 200.00 / 
3170.00
25.00 / 
396.25
800.00 / 
13300.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.xlarge
1
400.00 / 
3170.00
50.00 / 
396.25
1600.00 / 
13300.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.2xlar 
ge 1
800.00 / 
3170.00
100.00 / 
396.25
3200.00 / 
13300.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.4xlar 
ge 1
1580.00 / 
3170.00
197.50 / 
396.25
6600.00 / 
13300.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.8xlar 
ge
3170.00 396.25 13300.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 215
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c5a.12xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.16xla 
rge
6300.00 787.50 26700.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5a.24xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
C5ad
c5ad.large
1
200.00 / 
3170.00
25.00 / 
396.25
800.00 / 
13300.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5ad.xlar 
ge 1
400.00 / 
3170.00
50.00 / 
396.25
1600.00 / 
13300.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5ad.2xla 
rge 1
800.00 / 
3170.00
100.00 / 
396.25
3200.00 / 
13300.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5ad.4xla 
rge 1
1580.00 / 
3170.00
197.50 / 
396.25
6600.00 / 
13300.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 216
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c5ad.8xla 
rge
3170.00 396.25 13300.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c5ad.12xl 
arge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c5ad.16xl 
arge
6300.00 787.50 26700.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c5ad.24xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
C5d
c5d.large 1 650.00 / 
4750.00
81.25 / 
593.75
4000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5d.xlarge
1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5d.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
10000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 217
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c5d.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5d.9xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
c5d.12xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c5d.18xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c5d.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
c5d.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C5n
c5n.large 1 650.00 / 
4750.00
81.25 / 
593.75
4000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 218
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c5n.xlarge
1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5n.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
10000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5n.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5n.9xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5n.18xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c5n.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6a
c6a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 219
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 220
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6a.metal 40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6g
c6g.mediu 
m 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.large 1 630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.xlarge
1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.2xlar 
ge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 221
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6g.8xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.12xla 
rge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.16xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6g.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6gd
c6gd.medi 
um 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6gd.large
1
630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6gd.xlar 
ge 1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 222
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6gd.2xla 
rge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6gd.4xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6gd.8xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6gd.12xl 
arge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c6gd.16xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c6gd.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6gn
c6gn.medi 
um 1
760.00 / 
9500.00
95.00 / 
1187.50
2500.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 223
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6gn.large
1
1235.00 / 
9500.00
154.38 / 
1187.50
5000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.xlar 
ge 1
2375.00 / 
9500.00
296.88 / 
1187.50
10000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.2xla 
rge 1
4750.00 / 
9500.00
593.75 / 
1187.50
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.4xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.8xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.12xl 
arge
28500.00 3562.50 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6gn.16xl 
arge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
C6i
Amazon EBS speciﬁcations 224
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 225
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6i.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6id
c6id.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6id.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c6id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 226
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c6id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c6id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
c6id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
c6id.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C6in
c6in.large 1 1562.00 / 
25000.00
195.31 / 
3125.00
6250.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.xlarge
1
3125.00 / 
25000.00
390.62 / 
3125.00
12500.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 227
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c6in.2xla 
rge 1
6250.00 / 
25000.00
781.25 / 
3125.00
25000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.4xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
50000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.8xla 
rge
25000.00 3125.00 100000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.12xl 
arge
37500.00 4687.50 150000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.16xl 
arge
50000.00 6250.00 200000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.24xl 
arge
75000.00 9375.00 300000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.32xl 
arge
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c6in.metal 100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 228
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
C7a
c7a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c7a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 229
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c7a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c7a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
c7a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c7a.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C7g
c7g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.large 1 630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 230
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7g.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7g.metal 20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C7gd
Amazon EBS speciﬁcations 231
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
c7gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
c7gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 232
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7gd.metal 20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C7gn
c7gn.medi 
um 1
521.00 / 
10000.00
65.12 / 
1250.00
2083.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.large
1
1042.00 / 
10000.00
130.25 / 
1250.00
4167.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.xlar 
ge 1
2083.00 / 
10000.00
260.38 / 
1250.00
8333.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.2xla 
rge 1
4167.00 / 
10000.00
520.88 / 
1250.00
16667.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.4xla 
rge 1
8333.00 / 
10000.00
1041.62 / 
1250.00
33333.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.8xla 
rge 1
16667.00 / 
20000.00
2083.38 / 
2500.00
66667.00 / 
80000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 233
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7gn.12xl 
arge 1
25000.00 / 
30000.00
3125.00 / 
3750.00
100000.00 / 
120000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.16xl 
arge 1
33333.00 / 
40000.00
4166.62 / 
5000.00
133333.00 / 
160000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
c7gn.meta 
l 1
33333.00 / 
40000.00
4166.62 / 
5000.00
133333.00 / 
160000.00
✓  Yes ✗  No Up to 31 
(Shared 
limit)
C7i
c7i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 234
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c7i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c7i.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c7i.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
c7i.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C7i-ﬂex
Amazon EBS speciﬁcations 235
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c7i-ﬂex. 
large 1
312.00 / 
10000.00
39.06 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
xlarge 1
625.00 / 
10000.00
78.12 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
2xlarge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
4xlarge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
8xlarge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
12xlarge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c7i-ﬂex. 
16xlarge 1
10000.00 / 
20000.00
1250.00 / 
2500.00
40000.00 / 
80000.00
✓  Yes ✗  No 48 
(Dedicated 
limit)
C8a
Amazon EBS speciﬁcations 236
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 237
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8a.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8a.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8a.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C8g
c8g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.large 1 630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 238
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c8g.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8g.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8g.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
Amazon EBS speciﬁcations 239
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8g.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C8gb
c8gb.medi 
um 1
1562.00 / 
25000.00
195.31 / 
3125.00
7500.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.large
1
3125.00 / 
25000.00
390.62 / 
3125.00
15000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.xlar 
ge 1
6250.00 / 
25000.00
781.25 / 
3125.00
30000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.2xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
60000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.4xla 
rge
25000.00 3125.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.8xla 
rge
50000.00 6250.00 240000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 240
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8gb.12xl 
arge
75000.00 9375.00 360000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gb.16xl 
arge
100000.00 12500.00 480000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c8gb.24xl 
arge
150000.00 18750.00 720000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8gb.48xl 
arge
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
128 
(Dedicated 
limit)
c8gb.meta 
l-24xl
150000.00 18750.00 720000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
c8gb.meta 
l-48xl
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
78 
(Dedicated 
limit)
C8gd
c8gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 241
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8gd.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c8gd.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Amazon EBS speciﬁcations 242

## Instance store speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8gd.48xl 
arge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8gd.meta 
l-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
c8gd.meta 
l-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C8gn
c8gn.medi 
um 1
760.00 / 
10000.00
95.00 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.large
1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.2xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 243
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8gn.4xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.8xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.12xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8gn.16xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c8gn.24xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8gn.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8gn.meta 
l-24xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
c8gn.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
Amazon EBS speciﬁcations 244
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
C8i
c8i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 245
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
c8i.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8i.96xla 
rge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8i.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8i.metal 
-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C8id
c8id.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 246
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8id.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
c8id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
c8id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
Amazon EBS speciﬁcations 247
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8id.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8id.96xl 
arge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
c8id.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
c8id.meta 
l-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
C8i-ﬂex
c8i-ﬂex. 
large 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i-ﬂex. 
xlarge 1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i-ﬂex. 
2xlarge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 248
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c8i-ﬂex. 
4xlarge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i-ﬂex. 
8xlarge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i-ﬂex. 
12xlarge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
c8i-ﬂex. 
16xlarge 1
10000.00 / 
20000.00
1250.00 / 
2500.00
40000.00 / 
80000.00
✓  Yes ✗  No 48 
(Dedicated 
limit)
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance store speciﬁcations 249

## Security speciﬁcations

Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
C5ad
c5ad.large 1 x 75 GB NVMe 
SSD
16,283 / 7,105 ✓  Yes
c5ad.xlarge 1 x 150 GB NVMe 
SSD
32,566 / 14,211 ✓  Yes
c5ad.2xlarge 1 x 300 GB NVMe 
SSD
65,132 / 28,421 ✓  Yes
c5ad.4xlarge 2 x 300 GB NVMe 
SSD
130,262 / 56,842 ✓  Yes
c5ad.8xlarge 2 x 600 GB NVMe 
SSD
260,526 / 113,684 ✓  Yes
c5ad.12xlarge 2 x 900 GB NVMe 
SSD
412,500 / 180,000 ✓  Yes
c5ad.16xlarge 2 x 1200 GB NVMe 
SSD
521,052 / 227,368 ✓  Yes
c5ad.24xlarge 2 x 1900 GB NVMe 
SSD
825,000 / 360,000 ✓  Yes
C5d
c5d.large 1 x 50 GB NVMe 
SSD
20,000 / 9,000 ✓  Yes
c5d.xlarge 1 x 100 GB NVMe 
SSD
40,000 / 18,000 ✓  Yes
Instance store speciﬁcations 250
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c5d.2xlarge 1 x 200 GB NVMe 
SSD
80,000 / 37,000 ✓  Yes
c5d.4xlarge 1 x 400 GB NVMe 
SSD
175,000 / 75,000 ✓  Yes
c5d.9xlarge 1 x 900 GB NVMe 
SSD
350,000 / 170,000 ✓  Yes
c5d.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
c5d.18xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
c5d.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
c5d.metal 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
C6gd
c6gd.medium 1 x 59 GB NVMe 
SSD
13,438 / 5,625 ✓  Yes
c6gd.large 1 x 118 GB NVMe 
SSD
26,875 / 11,250 ✓  Yes
c6gd.xlarge 1 x 237 GB NVMe 
SSD
53,750 / 22,500 ✓  Yes
c6gd.2xlarge 1 x 474 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
Instance store speciﬁcations 251
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c6gd.4xlarge 1 x 950 GB NVMe 
SSD
215,000 / 90,000 ✓  Yes
c6gd.8xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
c6gd.12xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
c6gd.16xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
c6gd.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
C6id
c6id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
c6id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
c6id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
c6id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
c6id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
c6id.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
Instance store speciﬁcations 252
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c6id.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
c6id.24xlarge 4 x 1425 GB NVMe 
SSD
1,609,996 / 
805,000
✓  Yes
c6id.32xlarge 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
c6id.metal 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
C7gd
c7gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
c7gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
c7gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
c7gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
c7gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
c7gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
c7gd.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
Instance store speciﬁcations 253
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c7gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
c7gd.metal 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
C8gd
c8gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
c8gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
c8gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
c8gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
c8gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
c8gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
c8gd.12xlarge 3 x 950 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
c8gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
c8gd.24xlarge 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
Instance store speciﬁcations 254
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c8gd.48xlarge 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
c8gd.metal-24xl 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
c8gd.metal-48xl 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
C8id
c8id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
c8id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
c8id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
c8id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
c8id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
c8id.12xlarge 1 x 2850 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
c8id.16xlarge 1 x 3800 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
c8id.24xlarge 2 x 2850 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
Instance store speciﬁcations 255
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
c8id.32xlarge 2 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
c8id.48xlarge 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
c8id.96xlarge 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
c8id.metal-48xl 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
c8id.metal-96xl 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
C5
c5.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
Security speciﬁcations 256
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c5.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.9xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.18xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c5.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
C5a
Security speciﬁcations 257
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c5a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c5a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
C5ad
Security speciﬁcations 258
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c5ad.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
c5ad.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c5ad.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
C5d
c5d.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
c5d.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.9xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.18xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.24xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c5d.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
C5n
Security speciﬁcations 259
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c5n.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c5n.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5n.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5n.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5n.9xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5n.18xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c5n.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C6a
c6a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✗  No
Security speciﬁcations 260
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
c6a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 261
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6a.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C6g
c6g.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
c6g.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 262
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6g.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
c6g.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
C6gd
c6gd.medium ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
c6gd.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
c6gd.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
C6gn
Security speciﬁcations 263
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6gn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c6gn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6gn.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
C6i
Security speciﬁcations 264
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c6i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 265
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6i.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C6id
c6id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
c6id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c6id.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
C6in
c6in.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 266
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6in.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c6in.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 267
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c6in.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C7a
c7a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 268
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C7g
c7g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 269
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7g.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C7gd
c7gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
c7gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 270
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c7gd.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
C7gn
c7gn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 271
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7gn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7gn.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C7i
c7i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 272
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c7i.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
c7i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C7i-ﬂex
c7i-ﬂex.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 273
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c7i-ﬂex.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i-ﬂex.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i-ﬂex.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i-ﬂex.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i-ﬂex.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c7i-ﬂex.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
C8a
c8a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 274
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 275
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8a.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
c8a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C8g
c8g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 276
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8g.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
c8g.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C8gb
c8gb.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8gb.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 277
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8gb.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gb.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 278

## Memory optimized


## Instance families and instance types

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8gb.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
c8gb.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C8gd
c8gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
c8gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8gd.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
c8gd.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
C8gn
Security speciﬁcations 279
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8gn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8gn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 280
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8gn.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8gn.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
c8gn.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C8i
c8i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 281
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
c8i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 282
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8i.metal-96xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
C8id
c8id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
c8id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.96xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
c8id.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
c8id.metal-96xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
C8i-ﬂex
Security speciﬁcations 283

## Instance family summary

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c8i-ﬂex.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
c8i-ﬂex.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 284
Amazon EC2 Instance Types
Speciﬁcations for Amazon EC2 memory optimized instances
End of sale notice
The U-9tb1, U-12tb1, U-18tb1, and U-24tb1 instance types are no longer available for new 
instance launches. If your workload requires a high-memory instance, we recommend that 
you use a U7i instance type instead.
Memory optimized instances are designed to deliver fast performance for workloads that process 
large data sets in memory.
For information on previous generation instance types of this category, such as R4 instances, see
Speciﬁcations for Amazon EC2 previous generation instances.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Instance families and instance types
Instance 
family
Available instance types
R5 r5.large | r5.xlarge  | r5.2xlarge  | r5.4xlarge  | r5.8xlarge  |
r5.12xlarge  | r5.16xlarge  | r5.24xlarge  | r5.metal
Memory optimized 285
Amazon EC2 Instance Types
Instance 
family
Available instance types
R5a r5a.large  | r5a.xlarge  | r5a.2xlarge  | r5a.4xlarge  | r5a.8xlar 
ge  | r5a.12xlarge  | r5a.16xlarge  | r5a.24xlarge
R5ad r5ad.large  | r5ad.xlarge  | r5ad.2xlarge  | r5ad.4xlarge  |
r5ad.8xlarge  | r5ad.12xlarge  | r5ad.16xlarge  | r5ad.24xlarge
R5b r5b.large  | r5b.xlarge  | r5b.2xlarge  | r5b.4xlarge  | r5b.8xlar 
ge  | r5b.12xlarge  | r5b.16xlarge  | r5b.24xlarge  | r5b.metal
R5d r5d.large  | r5d.xlarge  | r5d.2xlarge  | r5d.4xlarge  | r5d.8xlar 
ge  | r5d.12xlarge  | r5d.16xlarge  | r5d.24xlarge  | r5d.metal
R5dn r5dn.large  | r5dn.xlarge  | r5dn.2xlarge  | r5dn.4xlarge  |
r5dn.8xlarge  | r5dn.12xlarge  | r5dn.16xlarge  | r5dn.24xlarge  |
r5dn.metal
R5n r5n.large  | r5n.xlarge  | r5n.2xlarge  | r5n.4xlarge  | r5n.8xlar 
ge  | r5n.12xlarge  | r5n.16xlarge  | r5n.24xlarge  | r5n.metal
R6a r6a.large  | r6a.xlarge  | r6a.2xlarge  | r6a.4xlarge  | r6a.8xlar 
ge  | r6a.12xlarge  | r6a.16xlarge  | r6a.24xlarge  | r6a.32xlarge  |
r6a.48xlarge  | r6a.metal
R6g r6g.medium  | r6g.large  | r6g.xlarge  | r6g.2xlarge  | r6g.4xlarge
| r6g.8xlarge  | r6g.12xlarge  | r6g.16xlarge  | r6g.metal
R6gd r6gd.medium  | r6gd.large  | r6gd.xlarge  | r6gd.2xlarge  |
r6gd.4xlarge  | r6gd.8xlarge  | r6gd.12xlarge  | r6gd.16xlarge  |
r6gd.metal
R6i r6i.large  | r6i.xlarge  | r6i.2xlarge  | r6i.4xlarge  | r6i.8xlar 
ge  | r6i.12xlarge  | r6i.16xlarge  | r6i.24xlarge  | r6i.32xlarge  |
r6i.metal
Instance families and instance types 286
Amazon EC2 Instance Types
Instance 
family
Available instance types
R6id r6id.large  | r6id.xlarge  | r6id.2xlarge  | r6id.4xlarge  |
r6id.8xlarge  | r6id.12xlarge  | r6id.16xlarge  | r6id.24xlarge  |
r6id.32xlarge  | r6id.metal
R6idn r6idn.large  | r6idn.xlarge  | r6idn.2xlarge  | r6idn.4xlarge
| r6idn.8xlarge  | r6idn.12xlarge  | r6idn.16xlarge  | r6idn.24x 
large  | r6idn.32xlarge  | r6idn.metal
R6in r6in.large  | r6in.xlarge  | r6in.2xlarge  | r6in.4xlarge  |
r6in.8xlarge  | r6in.12xlarge  | r6in.16xlarge  | r6in.24xlarge  |
r6in.32xlarge  | r6in.metal
R7a r7a.medium  | r7a.large  | r7a.xlarge  | r7a.2xlarge  | r7a.4xlar 
ge  | r7a.8xlarge  | r7a.12xlarge  | r7a.16xlarge  | r7a.24xlarge  |
r7a.32xlarge  | r7a.48xlarge  | r7a.metal-48xl
R7g r7g.medium  | r7g.large  | r7g.xlarge  | r7g.2xlarge  | r7g.4xlarge
| r7g.8xlarge  | r7g.12xlarge  | r7g.16xlarge  | r7g.metal
R7gd r7gd.medium  | r7gd.large  | r7gd.xlarge  | r7gd.2xlarge  |
r7gd.4xlarge  | r7gd.8xlarge  | r7gd.12xlarge  | r7gd.16xlarge  |
r7gd.metal
R7i r7i.large  | r7i.xlarge  | r7i.2xlarge  | r7i.4xlarge  | r7i.8xlar 
ge  | r7i.12xlarge  | r7i.16xlarge  | r7i.24xlarge  | r7i.48xlarge  |
r7i.metal-24xl  | r7i.metal-48xl
R7iz r7iz.large  | r7iz.xlarge  | r7iz.2xlarge  | r7iz.4xlarge  |
r7iz.8xlarge  | r7iz.12xlarge  | r7iz.16xlarge  | r7iz.32xlarge  |
r7iz.metal-16xl  | r7iz.metal-32xl
R8a r8a.medium  | r8a.large  | r8a.xlarge  | r8a.2xlarge  | r8a.4xlar 
ge  | r8a.8xlarge  | r8a.12xlarge  | r8a.16xlarge  | r8a.24xlarge  |
r8a.48xlarge  | r8a.metal-24xl  | r8a.metal-48xl
Instance families and instance types 287
Amazon EC2 Instance Types
Instance 
family
Available instance types
R8g r8g.medium  | r8g.large  | r8g.xlarge  | r8g.2xlarge  | r8g.4xlar 
ge  | r8g.8xlarge  | r8g.12xlarge  | r8g.16xlarge  | r8g.24xlarge  |
r8g.48xlarge  | r8g.metal-24xl  | r8g.metal-48xl
R8gb r8gb.medium  | r8gb.large  | r8gb.xlarge  | r8gb.2xlarge  |
r8gb.4xlarge  | r8gb.8xlarge  | r8gb.12xlarge  | r8gb.16xlarge
| r8gb.24xlarge  | r8gb.48xlarge  | r8gb.metal-24xl  | r8gb.meta 
l-48xl
R8gd r8gd.medium  | r8gd.large  | r8gd.xlarge  | r8gd.2xlarge  |
r8gd.4xlarge  | r8gd.8xlarge  | r8gd.12xlarge  | r8gd.16xlarge
| r8gd.24xlarge  | r8gd.48xlarge  | r8gd.metal-24xl  | r8gd.meta 
l-48xl
R8gn r8gn.medium  | r8gn.large  | r8gn.xlarge  | r8gn.2xlarge  |
r8gn.4xlarge  | r8gn.8xlarge  | r8gn.12xlarge  | r8gn.16xlarge
| r8gn.24xlarge  | r8gn.48xlarge  | r8gn.metal-24xl  | r8gn.meta 
l-48xl
R8i r8i.large  | r8i.xlarge  | r8i.2xlarge  | r8i.4xlarge  | r8i.8xlar 
ge  | r8i.12xlarge  | r8i.16xlarge  | r8i.24xlarge  | r8i.32xlarge  |
r8i.48xlarge  | r8i.96xlarge  | r8i.metal-48xl  | r8i.metal-96xl
R8id r8id.large  | r8id.xlarge  | r8id.2xlarge  | r8id.4xlarge  |
r8id.8xlarge  | r8id.12xlarge  | r8id.16xlarge  | r8id.24xlarge  |
r8id.32xlarge  | r8id.48xlarge  | r8id.96xlarge  | r8id.metal-48xl
| r8id.metal-96xl
R8i-ﬂex r8i-flex.large  | r8i-flex.xlarge  | r8i-flex.2xlarge  | r8i-flex. 
4xlarge  | r8i-flex.8xlarge  | r8i-flex.12xlarge  | r8i-flex. 
16xlarge
U-3tb1 u-3tb1.56xlarge
U-6tb1 u-6tb1.56xlarge  | u-6tb1.112xlarge  | u-6tb1.metal
Instance families and instance types 288

## Performance speciﬁcations

Amazon EC2 Instance Types
Instance 
family
Available instance types
U-9tb1 u-9tb1.112xlarge  | u-9tb1.metal
U-12tb1 u-12tb1.112xlarge  | u-12tb1.metal
U-18tb1 u-18tb1.112xlarge  | u-18tb1.metal
U-24tb1 u-24tb1.112xlarge  | u-24tb1.metal
U7i-6tb u7i-6tb.112xlarge
U7i-8tb u7i-8tb.112xlarge
U7i-12tb u7i-12tb.224xlarge
U7in-16tb u7in-16tb.224xlarge
U7in-24tb u7in-24tb.224xlarge
U7in-32tb u7in-32tb.224xlarge
U7inh-32t 
b
u7inh-32tb.480xlarge
X1 x1.16xlarge  | x1.32xlarge
X1e x1e.xlarge  | x1e.2xlarge  | x1e.4xlarge  | x1e.8xlarge  | x1e.16xla 
rge  | x1e.32xlarge
X2gd x2gd.medium  | x2gd.large  | x2gd.xlarge  | x2gd.2xlarge  |
x2gd.4xlarge  | x2gd.8xlarge  | x2gd.12xlarge  | x2gd.16xlarge  |
x2gd.metal
X2idn x2idn.16xlarge  | x2idn.24xlarge  | x2idn.32xlarge  | x2idn.metal
X2iedn x2iedn.xlarge  | x2iedn.2xlarge  | x2iedn.4xlarge  | x2iedn.8x 
large  | x2iedn.16xlarge  | x2iedn.24xlarge  | x2iedn.32xlarge  |
x2iedn.metal
Instance families and instance types 289
Amazon EC2 Instance Types
Instance 
family
Available instance types
X2iezn x2iezn.2xlarge  | x2iezn.4xlarge  | x2iezn.6xlarge  | x2iezn.8x 
large  | x2iezn.12xlarge  | x2iezn.metal
X8g x8g.medium  | x8g.large  | x8g.xlarge  | x8g.2xlarge  | x8g.4xlar 
ge  | x8g.8xlarge  | x8g.12xlarge  | x8g.16xlarge  | x8g.24xlarge  |
x8g.48xlarge  | x8g.metal-24xl  | x8g.metal-48xl
X8aedz x8aedz.large  | x8aedz.xlarge  | x8aedz.3xlarge  | x8aedz.6x 
large  | x8aedz.12xlarge  | x8aedz.24xlarge  | x8aedz.metal-12xl  |
x8aedz.metal-24xl
X8i x8i.large  | x8i.xlarge  | x8i.2xlarge  | x8i.4xlarge  | x8i.8xlar 
ge  | x8i.12xlarge  | x8i.16xlarge  | x8i.24xlarge  | x8i.32xlarge
| x8i.48xlarge  | x8i.64xlarge  | x8i.96xlarge  | x8i.metal-48xl  |
x8i.metal-96xl
z1d z1d.large  | z1d.xlarge  | z1d.2xlarge  | z1d.3xlarge  | z1d.6xlar 
ge  | z1d.12xlarge  | z1d.metal
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
R5 Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R5a Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
R5ad Nitro v2 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 290
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
R5b Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R5d Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R5dn Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R5n Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R6a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R6g Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R6gd Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R6i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R6id Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R6idn Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R6in Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 291
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
R7a Nitro v4 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R7g Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R7gd Nitro v4 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R7i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R7iz Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R8a Nitro v6 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R8g Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R8gb Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R8gd Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
Instance family summary 292
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
R8gn Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
R8i Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R8id Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R8i-ﬂex Nitro v6 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✓  Yes Windows | 
Linux
U-3tb1 Nitro v3 Intel 
(x86_64)
✗  No ✗  No ✗  No ✗  No Windows | 
Linux
U-6tb1 Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✗  No ✗  No Windows | 
Linux
U-9tb1 Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✗  No ✗  No Windows | 
Linux
U-12tb1 Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✗  No ✗  No Windows | 
Linux
U-18tb1 Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✗  No ✗  No Windows | 
Linux
U-24tb1 Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✗  No ✗  No Windows | 
Linux
U7i-6tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
Instance family summary 293
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
U7i-8tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
U7i-12tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
U7in-16tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
U7in-24tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
U7in-32tb Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Windows | 
Linux
U7inh-32t 
b
Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✗  No ✗  No Linux
X1 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
X1e Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
X2gd Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
X2idn Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
X2iedn Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Instance family summary 294
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
X2iezn Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
X8g Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✗  No Linux
X8aedz Nitro v6 AMD 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
X8i Nitro v6 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
z1d Nitro v2 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
R5
r5.large 16.00 Intel Xeon Platinum 
8175
2 1 2 ✗  No ✗  No
r5.xlarge 32.00 Intel Xeon Platinum 
8175
4 2 2 ✗  No ✗  No
r5.2xlarge 64.00 Intel Xeon Platinum 
8175
8 4 2 ✗  No ✗  No
Performance speciﬁcations 295
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r5.4xlarge 128.00 Intel Xeon Platinum 
8175
16 8 2 ✗  No ✗  No
r5.8xlarge 256.00 Intel Xeon Platinum 
8175
32 16 2 ✗  No ✗  No
r5.12xlarge 384.00 Intel Xeon Platinum 
8175
48 24 2 ✗  No ✗  No
r5.16xlarge 512.00 Intel Xeon Platinum 
8175
64 32 2 ✗  No ✗  No
r5.24xlarge 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
r5.metal 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
R5a
r5a.large 16.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
r5a.xlarge 32.00 AMD EPYC 7571 4 2 2 ✗  No ✗  No
r5a.2xlarge 64.00 AMD EPYC 7571 8 4 2 ✗  No ✗  No
r5a.4xlarge 128.00 AMD EPYC 7571 16 8 2 ✗  No ✗  No
r5a.8xlarge 256.00 AMD EPYC 7571 32 16 2 ✗  No ✗  No
r5a.12xlarge 384.00 AMD EPYC 7571 48 24 2 ✗  No ✗  No
r5a.16xlarge 512.00 AMD EPYC 7571 64 32 2 ✗  No ✗  No
r5a.24xlarge 768.00 AMD EPYC 7571 96 48 2 ✗  No ✗  No
R5ad
Performance speciﬁcations 296
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r5ad.large 16.00 AMD EPYC 7571 2 1 2 ✗  No ✗  No
r5ad.xlarge 32.00 AMD EPYC 7571 4 2 2 ✗  No ✗  No
r5ad.2xlarge 64.00 AMD EPYC 7571 8 4 2 ✗  No ✗  No
r5ad.4xlarge 128.00 AMD EPYC 7571 16 8 2 ✗  No ✗  No
r5ad.8xlarge 256.00 AMD EPYC 7571 32 16 2 ✗  No ✗  No
r5ad.12xlarge 384.00 AMD EPYC 7571 48 24 2 ✗  No ✗  No
r5ad.16xlarge 512.00 AMD EPYC 7571 64 32 2 ✗  No ✗  No
r5ad.24xlarge 768.00 AMD EPYC 7571 96 48 2 ✗  No ✗  No
R5b
r5b.large 16.00 Intel Xeon Platinum 
8259
2 1 2 ✗  No ✗  No
r5b.xlarge 32.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
r5b.2xlarge 64.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
r5b.4xlarge 128.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
r5b.8xlarge 256.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
r5b.12xlarge 384.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
Performance speciﬁcations 297
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r5b.16xlarge 512.00 Intel Xeon Platinum 
8259
64 32 2 ✗  No ✗  No
r5b.24xlarge 768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
r5b.metal 768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
R5d
r5d.large 16.00 Intel Xeon Platinum 
8175
2 1 2 ✗  No ✗  No
r5d.xlarge 32.00 Intel Xeon Platinum 
8175
4 2 2 ✗  No ✗  No
r5d.2xlarge 64.00 Intel Xeon Platinum 
8175
8 4 2 ✗  No ✗  No
r5d.4xlarge 128.00 Intel Xeon Platinum 
8175
16 8 2 ✗  No ✗  No
r5d.8xlarge 256.00 Intel Xeon Platinum 
8175
32 16 2 ✗  No ✗  No
r5d.12xlarge 384.00 Intel Xeon Platinum 
8175
48 24 2 ✗  No ✗  No
r5d.16xlarge 512.00 Intel Xeon Platinum 
8175
64 32 2 ✗  No ✗  No
r5d.24xlarge 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
Performance speciﬁcations 298
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r5d.metal 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
R5dn
r5dn.large 16.00 Intel Xeon Platinum 
8259
2 1 2 ✗  No ✗  No
r5dn.xlarge 32.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
r5dn.2xlarge 64.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
r5dn.4xlarge 128.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
r5dn.8xlarge 256.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
r5dn.12xl 
arge
384.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
r5dn.16xl 
arge
512.00 Intel Xeon Platinum 
8259
64 32 2 ✗  No ✗  No
r5dn.24xl 
arge
768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
r5dn.metal 768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
R5n
r5n.large 16.00 Intel Xeon Platinum 
8259
2 1 2 ✗  No ✗  No
Performance speciﬁcations 299
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r5n.xlarge 32.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
r5n.2xlarge 64.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
r5n.4xlarge 128.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
r5n.8xlarge 256.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
r5n.12xlarge 384.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
r5n.16xlarge 512.00 Intel Xeon Platinum 
8259
64 32 2 ✗  No ✗  No
r5n.24xlarge 768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
r5n.metal 768.00 Intel Xeon Platinum 
8259
96 48 2 ✗  No ✗  No
R6a
r6a.large 16.00 AMD EPYC 7R13 2 1 2 ✗  No ✗  No
r6a.xlarge 32.00 AMD EPYC 7R13 4 2 2 ✗  No ✗  No
r6a.2xlarge 64.00 AMD EPYC 7R13 8 4 2 ✗  No ✗  No
r6a.4xlarge 128.00 AMD EPYC 7R13 16 8 2 ✗  No ✗  No
r6a.8xlarge 256.00 AMD EPYC 7R13 32 16 2 ✗  No ✗  No
Performance speciﬁcations 300
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r6a.12xlarge 384.00 AMD EPYC 7R13 48 24 2 ✗  No ✗  No
r6a.16xlarge 512.00 AMD EPYC 7R13 64 32 2 ✗  No ✗  No
r6a.24xlarge 768.00 AMD EPYC 7R13 96 48 2 ✗  No ✗  No
r6a.32xlarge 1024.00 AMD EPYC 7R13 128 64 2 ✗  No ✗  No
r6a.48xlarge 1536.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
r6a.metal 1536.00 AMD EPYC 7R13 192 96 2 ✗  No ✗  No
R6g
r6g.medium 8.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
r6g.large 16.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
r6g.xlarge 32.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
r6g.2xlarge 64.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
r6g.4xlarge 128.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
r6g.8xlarge 256.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
r6g.12xlarge 384.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
Performance speciﬁcations 301
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r6g.16xlarge 512.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
r6g.metal 512.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
R6gd
r6gd.medium 8.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
r6gd.large 16.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
r6gd.xlarge 32.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
r6gd.2xlarge 64.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
r6gd.4xlarge 128.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
r6gd.8xlarge 256.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
r6gd.12xl 
arge
384.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
r6gd.16xl 
arge
512.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
r6gd.metal 512.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
R6i
Performance speciﬁcations 302
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r6i.large 16.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
r6i.xlarge 32.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
r6i.2xlarge 64.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
r6i.4xlarge 128.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
r6i.8xlarge 256.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
r6i.12xlarge 384.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
r6i.16xlarge 512.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
r6i.24xlarge 768.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
r6i.32xlarge 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
r6i.metal 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
R6id
r6id.large 16.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
r6id.xlarge 32.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
r6id.2xlarge 64.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
r6id.4xlarge 128.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
r6id.8xlarge 256.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
r6id.12xlarge 384.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
r6id.16xlarge 512.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
r6id.24xlarge 768.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
Performance speciﬁcations 303
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r6id.32xlarge 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
r6id.metal 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
R6idn
r6idn.large 16.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
r6idn.xlarge 32.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
r6idn.2xlarge 64.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
r6idn.4xlarge 128.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
r6idn.8xlarge 256.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
r6idn.12x 
large
384.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
r6idn.16x 
large
512.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
r6idn.24x 
large
768.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
r6idn.32x 
large
1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
r6idn.metal 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
R6in
r6in.large 16.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
r6in.xlarge 32.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
r6in.2xlarge 64.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
Performance speciﬁcations 304
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r6in.4xlarge 128.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
r6in.8xlarge 256.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
r6in.12xlarge 384.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
r6in.16xlarge 512.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
r6in.24xlarge 768.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
r6in.32xlarge 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
r6in.metal 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
R7a
r7a.medium 8.00 AMD EPYC 9R14 1 1 1 ✗  No ✗  No
r7a.large 16.00 AMD EPYC 9R14 2 2 1 ✗  No ✗  No
r7a.xlarge 32.00 AMD EPYC 9R14 4 4 1 ✗  No ✗  No
r7a.2xlarge 64.00 AMD EPYC 9R14 8 8 1 ✗  No ✗  No
r7a.4xlarge 128.00 AMD EPYC 9R14 16 16 1 ✗  No ✗  No
r7a.8xlarge 256.00 AMD EPYC 9R14 32 32 1 ✗  No ✗  No
r7a.12xlarge 384.00 AMD EPYC 9R14 48 48 1 ✗  No ✗  No
r7a.16xlarge 512.00 AMD EPYC 9R14 64 64 1 ✗  No ✗  No
r7a.24xlarge 768.00 AMD EPYC 9R14 96 96 1 ✗  No ✗  No
r7a.32xlarge 1024.00 AMD EPYC 9R14 128 128 1 ✗  No ✗  No
r7a.48xlarge 1536.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
Performance speciﬁcations 305
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r7a.metal 
-48xl
1536.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
R7g
r7g.medium 8.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
r7g.large 16.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
r7g.xlarge 32.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
r7g.2xlarge 64.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
r7g.4xlarge 128.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
r7g.8xlarge 256.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
r7g.12xlarge 384.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
r7g.16xlarge 512.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
r7g.metal 512.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
R7gd
r7gd.medium 8.00 AWS Graviton3 
Processor
1 1 1 ✗  No ✗  No
Performance speciﬁcations 306
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r7gd.large 16.00 AWS Graviton3 
Processor
2 2 1 ✗  No ✗  No
r7gd.xlarge 32.00 AWS Graviton3 
Processor
4 4 1 ✗  No ✗  No
r7gd.2xlarge 64.00 AWS Graviton3 
Processor
8 8 1 ✗  No ✗  No
r7gd.4xlarge 128.00 AWS Graviton3 
Processor
16 16 1 ✗  No ✗  No
r7gd.8xlarge 256.00 AWS Graviton3 
Processor
32 32 1 ✗  No ✗  No
r7gd.12xl 
arge
384.00 AWS Graviton3 
Processor
48 48 1 ✗  No ✗  No
r7gd.16xl 
arge
512.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
r7gd.metal 512.00 AWS Graviton3 
Processor
64 64 1 ✗  No ✗  No
R7i
r7i.large 16.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
r7i.xlarge 32.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
r7i.2xlarge 64.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
Performance speciﬁcations 307
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r7i.4xlarge 128.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
r7i.8xlarge 256.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
r7i.12xlarge 384.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
r7i.16xlarge 512.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
r7i.24xlarge 768.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
r7i.48xlarge 1536.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
r7i.metal 
-24xl
768.00 Intel Xeon Sapphire 
Rapids
96 48 2 ✗  No ✗  No
r7i.metal 
-48xl
1536.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
R7iz
r7iz.large 16.00 Intel Xeon Sapphire 
Rapids
2 1 2 ✗  No ✗  No
r7iz.xlarge 32.00 Intel Xeon Sapphire 
Rapids
4 2 2 ✗  No ✗  No
r7iz.2xlarge 64.00 Intel Xeon Sapphire 
Rapids
8 4 2 ✗  No ✗  No
Performance speciﬁcations 308
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r7iz.4xlarge 128.00 Intel Xeon Sapphire 
Rapids
16 8 2 ✗  No ✗  No
r7iz.8xlarge 256.00 Intel Xeon Sapphire 
Rapids
32 16 2 ✗  No ✗  No
r7iz.12xlarge 384.00 Intel Xeon Sapphire 
Rapids
48 24 2 ✗  No ✗  No
r7iz.16xlarge 512.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
r7iz.32xlarge 1024.00 Intel Xeon Sapphire 
Rapids
128 64 2 ✗  No ✗  No
r7iz.meta 
l-16xl
512.00 Intel Xeon Sapphire 
Rapids
64 32 2 ✗  No ✗  No
r7iz.meta 
l-32xl
1024.00 Intel Xeon Sapphire 
Rapids
128 64 2 ✗  No ✗  No
R8a
r8a.medium 8.00 AMD EPYC 9R45 1 1 1 ✗  No ✗  No
r8a.large 16.00 AMD EPYC 9R45 2 2 1 ✗  No ✗  No
r8a.xlarge 32.00 AMD EPYC 9R45 4 4 1 ✗  No ✗  No
r8a.2xlarge 64.00 AMD EPYC 9R45 8 8 1 ✗  No ✗  No
r8a.4xlarge 128.00 AMD EPYC 9R45 16 16 1 ✗  No ✗  No
r8a.8xlarge 256.00 AMD EPYC 9R45 32 32 1 ✗  No ✗  No
r8a.12xlarge 384.00 AMD EPYC 9R45 48 48 1 ✗  No ✗  No
Performance speciﬁcations 309
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8a.16xlarge 512.00 AMD EPYC 9R45 64 64 1 ✗  No ✗  No
r8a.24xlarge 768.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
r8a.48xlarge 1536.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
r8a.metal 
-24xl
768.00 AMD EPYC 9R45 96 96 1 ✗  No ✗  No
r8a.metal 
-48xl
1536.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
R8g
r8g.medium 8.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
r8g.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
r8g.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
r8g.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
r8g.4xlarge 128.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
r8g.8xlarge 256.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
r8g.12xlarge 384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
Performance speciﬁcations 310
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8g.16xlarge 512.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
r8g.24xlarge 768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8g.48xlarge 1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
r8g.metal 
-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8g.metal 
-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
R8gb
r8gb.medium 8.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
r8gb.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
r8gb.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
r8gb.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
r8gb.4xlarge 128.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
r8gb.8xlarge 256.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
Performance speciﬁcations 311
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8gb.12xl 
arge
384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
r8gb.16xl 
arge
512.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
r8gb.24xl 
arge
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gb.48xl 
arge
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
r8gb.meta 
l-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gb.meta 
l-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
R8gd
r8gd.medium 8.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
r8gd.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
r8gd.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
r8gd.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
r8gd.4xlarge 128.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
Performance speciﬁcations 312
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8gd.8xlarge 256.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
r8gd.12xl 
arge
384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
r8gd.16xl 
arge
512.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
r8gd.24xl 
arge
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gd.48xl 
arge
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
r8gd.meta 
l-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gd.meta 
l-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
R8gn
r8gn.medium 8.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
r8gn.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
r8gn.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
r8gn.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
Performance speciﬁcations 313
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8gn.4xlarge 128.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
r8gn.8xlarge 256.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
r8gn.12xl 
arge
384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
r8gn.16xl 
arge
512.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
r8gn.24xl 
arge
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gn.48xl 
arge
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
r8gn.meta 
l-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
r8gn.meta 
l-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
R8i
r8i.large 16.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
r8i.xlarge 32.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
r8i.2xlarge 64.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
Performance speciﬁcations 314
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8i.4xlarge 128.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
r8i.8xlarge 256.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
r8i.12xlarge 384.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
r8i.16xlarge 512.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
r8i.24xlarge 768.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
r8i.32xlarge 1024.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
r8i.48xlarge 1536.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
r8i.96xlarge 3072.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
r8i.metal 
-48xl
1536.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
r8i.metal 
-96xl
3072.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
R8id
r8id.large 16.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
Performance speciﬁcations 315
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r8id.xlarge 32.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
r8id.2xlarge 64.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
r8id.4xlarge 128.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
r8id.8xlarge 256.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
r8id.12xlarge 384.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
r8id.16xlarge 512.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
r8id.24xlarge 768.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
r8id.32xlarge 1024.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
r8id.48xlarge 1536.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
r8id.96xlarge 3072.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
r8id.meta 
l-48xl
1536.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
r8id.meta 
l-96xl
3072.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
Performance speciﬁcations 316
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
R8i-ﬂex
r8i-ﬂex.large 16.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
r8i-ﬂex. 
xlarge
32.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
r8i-ﬂex. 
2xlarge
64.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
r8i-ﬂex. 
4xlarge
128.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
r8i-ﬂex. 
8xlarge
256.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
r8i-ﬂex. 
12xlarge
384.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
r8i-ﬂex. 
16xlarge
512.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
U-3tb1
u-3tb1.56 
xlarge
3072.00 Intel Xeon Platinum 
8176M
224 112 2 ✗  No ✗  No
U-6tb1
u-6tb1.56 
xlarge
6144.00 Intel Xeon Platinum 
8176M
224 224 1 ✗  No ✗  No
u-6tb1.11 
2xlarge
6144.00 Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
Performance speciﬁcations 317
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
u-6tb1.metal 6144.00 Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
U-9tb1
u-9tb1.11 
2xlarge
9216.00 Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
u-9tb1.metal 9216.00 Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
U-12tb1
u-12tb1.1 
12xlarge
12288.00Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
u-12tb1.m 
etal
12288.00Intel Xeon Platinum 
8176M
448 224 2 ✗  No ✗  No
U-18tb1
u-18tb1.1 
12xlarge
18432.00Intel Xeon Platinum 
8280L
448 224 2 ✗  No ✗  No
u-18tb1.m 
etal
18432.00Intel Xeon Platinum 
8280L
448 224 2 ✗  No ✗  No
U-24tb1
u-24tb1.1 
12xlarge
24576.00Intel Xeon Platinum 
8280L
448 224 2 ✗  No ✗  No
u-24tb1.m 
etal
24576.00Intel Xeon Platinum 
8280L
448 224 2 ✗  No ✗  No
U7i-6tb
Performance speciﬁcations 318
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
u7i-6tb.1 
12xlarge
6144.00 Intel Xeon Sapphire 
Rapids
448 224 2 ✗  No ✗  No
U7i-8tb
u7i-8tb.1 
12xlarge
8192.00 Intel Xeon Sapphire 
Rapids
448 224 2 ✗  No ✗  No
U7i-12tb
u7i-12tb. 
224xlarge
12288.00Intel Xeon Sapphire 
Rapids
896 448 2 ✗  No ✗  No
U7in-16tb
u7in-16tb 
.224xlarge
16384.00Intel Xeon Sapphire 
Rapids
896 448 2 ✗  No ✗  No
U7in-24tb
u7in-24tb 
.224xlarge
24576.00Intel Xeon Sapphire 
Rapids
896 448 2 ✗  No ✗  No
U7in-32tb
u7in-32tb 
.224xlarge
32768.00Intel Xeon Sapphire 
Rapids
896 448 2 ✗  No ✗  No
U7inh-32tb
u7inh-32t 
b.480xlarge
32768.00Intel Xeon Sapphire 
Rapids
1920 960 2 ✗  No ✗  No
X1
Performance speciﬁcations 319

## Network speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x1.16xlarge 976.00 Intel Xeon E7 8880 
v3
64 32 2 ✗  No ✗  No
x1.32xlarge 1952.00 Intel Xeon E7 8880 
v3
128 64 2 ✗  No ✗  No
X1e
x1e.xlarge 122.00 Intel Haswell E7 
8880v3
4 2 2 ✗  No ✗  No
x1e.2xlarge 244.00 Intel Haswell E7 
8880v3
8 4 2 ✗  No ✗  No
x1e.4xlarge 488.00 Intel Haswell E7 
8880v3
16 8 2 ✗  No ✗  No
x1e.8xlarge 976.00 Intel Haswell E7 
8880v3
32 16 2 ✗  No ✗  No
x1e.16xlarge 1952.00 Intel Haswell E7 
8880v3
64 32 2 ✗  No ✗  No
x1e.32xlarge 3904.00 Intel Haswell E7 
8880v3
128 64 2 ✗  No ✗  No
X2gd
x2gd.medium 16.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
x2gd.large 32.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
x2gd.xlarge 64.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
Performance speciﬁcations 320
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x2gd.2xlarge 128.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
x2gd.4xlarge 256.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
x2gd.8xlarge 512.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
x2gd.12xl 
arge
768.00 AWS Graviton2 
Processor
48 48 1 ✗  No ✗  No
x2gd.16xl 
arge
1024.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
x2gd.metal 1024.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
X2idn
x2idn.16x 
large
1024.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
x2idn.24x 
large
1536.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
x2idn.32x 
large
2048.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
x2idn.metal 2048.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
X2iedn
x2iedn.xlarge 128.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
Performance speciﬁcations 321
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x2iedn.2x 
large
256.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
x2iedn.4x 
large
512.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
x2iedn.8x 
large
1024.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
x2iedn.16 
xlarge
2048.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
x2iedn.24 
xlarge
3072.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
x2iedn.32 
xlarge
4096.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
x2iedn.metal 4096.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
X2iezn
x2iezn.2x 
large
256.00 Intel Xeon Platinum 
8252
8 4 2 ✗  No ✗  No
x2iezn.4x 
large
512.00 Intel Xeon Platinum 
8252
16 8 2 ✗  No ✗  No
x2iezn.6x 
large
768.00 Intel Xeon Platinum 
8252
24 12 2 ✗  No ✗  No
x2iezn.8x 
large
1024.00 Intel Xeon Platinum 
8252
32 16 2 ✗  No ✗  No
x2iezn.12 
xlarge
1536.00 Intel Xeon Platinum 
8252
48 24 2 ✗  No ✗  No
Performance speciﬁcations 322
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x2iezn.metal 1536.00 Intel Xeon Platinum 
8252
48 24 2 ✗  No ✗  No
X8g
x8g.medium 16.00 AWS Graviton4 
Processor
1 1 1 ✗  No ✗  No
x8g.large 32.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
x8g.xlarge 64.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
x8g.2xlarge 128.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
x8g.4xlarge 256.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
x8g.8xlarge 512.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
x8g.12xlarge 768.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
x8g.16xlarge 1024.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
x8g.24xlarge 1536.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
x8g.48xlarge 3072.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Performance speciﬁcations 323
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x8g.metal 
-24xl
1536.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
x8g.metal 
-48xl
3072.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
X8aedz
x8aedz.large 64.00 AMD EPYC 9R05 2 2 1 ✗  No ✗  No
x8aedz.xlarge 128.00 AMD EPYC 9R05 4 4 1 ✗  No ✗  No
x8aedz.3x 
large
384.00 AMD EPYC 9R05 12 12 1 ✗  No ✗  No
x8aedz.6x 
large
768.00 AMD EPYC 9R05 24 24 1 ✗  No ✗  No
x8aedz.12 
xlarge
1536.00 AMD EPYC 9R05 48 48 1 ✗  No ✗  No
x8aedz.24 
xlarge
3072.00 AMD EPYC 9R05 96 96 1 ✗  No ✗  No
x8aedz.me 
tal-12xl
1536.00 AMD EPYC 9R05 48 48 1 ✗  No ✗  No
x8aedz.me 
tal-24xl
3072.00 AMD EPYC 9R05 96 96 1 ✗  No ✗  No
X8i
x8i.large 32.00 Intel Xeon Granite 
Rapids
2 1 2 ✗  No ✗  No
Performance speciﬁcations 324
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x8i.xlarge 64.00 Intel Xeon Granite 
Rapids
4 2 2 ✗  No ✗  No
x8i.2xlarge 128.00 Intel Xeon Granite 
Rapids
8 4 2 ✗  No ✗  No
x8i.4xlarge 256.00 Intel Xeon Granite 
Rapids
16 8 2 ✗  No ✗  No
x8i.8xlarge 512.00 Intel Xeon Granite 
Rapids
32 16 2 ✗  No ✗  No
x8i.12xlarge 768.00 Intel Xeon Granite 
Rapids
48 24 2 ✗  No ✗  No
x8i.16xlarge 1024.00 Intel Xeon Granite 
Rapids
64 32 2 ✗  No ✗  No
x8i.24xlarge 1536.00 Intel Xeon Granite 
Rapids
96 48 2 ✗  No ✗  No
x8i.32xlarge 2048.00 Intel Xeon Granite 
Rapids
128 64 2 ✗  No ✗  No
x8i.48xlarge 3072.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
x8i.64xlarge 4096.00 Intel Xeon Granite 
Rapids
256 128 2 ✗  No ✗  No
x8i.96xlarge 6144.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
x8i.metal 
-48xl
3072.00 Intel Xeon Granite 
Rapids
192 96 2 ✗  No ✗  No
Performance speciﬁcations 325
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
x8i.metal 
-96xl
6144.00 Intel Xeon Granite 
Rapids
384 192 2 ✗  No ✗  No
z1d
z1d.large 16.00 Intel Xeon Platinum 
8151
2 1 2 ✗  No ✗  No
z1d.xlarge 32.00 Intel Xeon Platinum 
8151
4 2 2 ✗  No ✗  No
z1d.2xlarge 64.00 Intel Xeon Platinum 
8151
8 4 2 ✗  No ✗  No
z1d.3xlarge 96.00 Intel Xeon Platinum 
8151
12 6 2 ✗  No ✗  No
z1d.6xlarge 192.00 Intel Xeon Platinum 
8151
24 12 2 ✗  No ✗  No
z1d.12xlarge 384.00 Intel Xeon Platinum 
8151
48 24 2 ✗  No ✗  No
z1d.metal 384.00 Intel Xeon Platinum 
8151
48 24 2 ✗  No ✗  No
Network speciﬁcations
Note
R8a, R8g, R8gd, R8i, R8id, R8i-ﬂex, X8g, X8aedz, X8i instance types support conﬁgurable 
bandwidth weightings. With these instance types, you can optimize an instance's 
bandwidth for either networking performance or Amazon EBS performance. The following 
table shows the default networking bandwidth performance for these instance types. 
Network speciﬁcations 326
Amazon EC2 Instance Types
For the supported conﬁgurable weightings, see  Conﬁgurable bandwidth weighting 
preferences.
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
R5
r5.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5a
Network speciﬁcations 327
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r5a.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5a.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5a.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5a.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5a.8xlarge 1 7.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5a.12xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5a.16xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5a.24xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5ad
r5ad.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5ad.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5ad.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 328
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r5ad.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5ad.8xlarge 1 7.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5ad.12xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5ad.16xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5ad.24xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5b
r5b.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5b.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5b.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5b.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5b.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5b.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 329
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r5b.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5b.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5b.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5d
r5d.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5d.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5d.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5d.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5d.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5d.12xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5d.16xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5d.24xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Network speciﬁcations 330
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r5d.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5dn
r5dn.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5dn.xlarge 1 4.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5dn.2xlarge 1 8.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5dn.4xlarge 1 16.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5dn.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5dn.12xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5dn.16xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5dn.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5dn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R5n
Network speciﬁcations 331
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r5n.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r5n.xlarge 1 4.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5n.2xlarge 1 8.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r5n.4xlarge 1 16.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5n.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5n.12xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r5n.16xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5n.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r5n.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R6a
r6a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 332
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6a.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R6g
r6g.medium 1 0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r6g.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 333
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6g.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6g.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6g.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6g.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6g.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6g.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r6g.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R6gd
r6gd.medium
1
0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r6gd.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6gd.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6gd.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 334
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6gd.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6gd.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6gd.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6gd.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
r6gd.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
R6i
r6i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
Network speciﬁcations 335
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6i.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6i.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R6id
r6id.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6id.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6id.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6id.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6id.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6id.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6id.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 336
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6id.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6id.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6id.metal 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R6idn
r6idn.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6idn.xlarge 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6idn.2xlarge
1
12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6idn.4xlarge
1
25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6idn.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6idn.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6idn.16xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6idn.24xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 337
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6idn.32xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
r6idn.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
R6in
r6in.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r6in.xlarge 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6in.2xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r6in.4xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r6in.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6in.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r6in.16xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6in.24xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r6in.32xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
Network speciﬁcations 338
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r6in.metal 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
R7a
r7a.medium 1 0.39 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r7a.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r7a.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7a.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7a.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7a.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7a.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7a.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7a.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7a.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 339
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r7a.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7a.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R7g
r7g.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r7g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r7g.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7g.16xlarge 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7g.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 340
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
R7gd
r7gd.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r7gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r7gd.xlarge 1 1.876 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7gd.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7gd.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7gd.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7gd.16xlarge 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7gd.metal 30 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R7i
r7i.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 341
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r7i.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7i.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7i.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7i.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7i.12xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7i.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7i.24xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7i.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7i.metal-24xl 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7i.metal-48xl 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R7iz
r7iz.large 1 0.781 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 342
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r7iz.xlarge 1 1.562 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7iz.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r7iz.4xlarge 1 6.25 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r7iz.8xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7iz.12xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r7iz.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7iz.32xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7iz.meta 
l-16xl
25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r7iz.meta 
l-32xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R8a
r8a.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r8a.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
Network speciﬁcations 343
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8a.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
r8a.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 40 ✓ 
Yes
r8a.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
r8a.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 40 ✓ 
Yes
r8a.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 64 ✓ 
Yes
r8a.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
r8a.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
r8a.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8a.metal 
-24xl
40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
r8a.metal 
-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
R8g
r8g.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
Network speciﬁcations 344
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r8g.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r8g.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8g.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8g.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8g.metal 
-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8g.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R8gb
Network speciﬁcations 345
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8gb.medium
1
2.083 / 
16.667
✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r8gb.large 1 4.166 / 20.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r8gb.xlarge 1 8.333 / 
26.667
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gb.2xlarge 1 16.666 / 
33.333
✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gb.4xlarge 33.33 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8gb.8xlarge 66.66 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
r8gb.12xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
r8gb.16xlarge 133.33 
Gigabit
✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
r8gb.24xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
r8gb.48xlarge 400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
r8gb.meta 
l-24xl
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
Network speciﬁcations 346
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8gb.meta 
l-48xl
400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
R8gd
r8gd.medium
1
0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r8gd.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r8gd.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gd.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gd.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8gd.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8gd.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
r8gd.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8gd.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8gd.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 347
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8gd.meta 
l-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
r8gd.meta 
l-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
R8gn
r8gn.medium
1
3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
r8gn.large 1 6.25 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r8gn.xlarge 1 12.5 / 40.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gn.2xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r8gn.4xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r8gn.8xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
r8gn.12xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
r8gn.16xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
r8gn.24xlarge 300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
Network speciﬁcations 348
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8gn.48xlarge 600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
r8gn.meta 
l-24xl
300 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
r8gn.meta 
l-48xl
600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 24 50 ✓ 
Yes
R8i
r8i.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
r8i.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8i.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8i.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
r8i.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
r8i.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
r8i.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
r8i.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
Network speciﬁcations 349
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8i.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8i.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8i.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8i.metal-48xl 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8i.metal-96xl 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
R8id
r8id.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
r8id.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8id.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8id.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
r8id.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
r8id.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
Network speciﬁcations 350
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8id.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
r8id.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
r8id.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8id.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8id.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8id.meta 
l-48xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
r8id.meta 
l-96xl
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
R8i-ﬂex
r8i-ﬂex.large 1 0.468 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
r8i-ﬂex.xlarge
1
0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8i-ﬂex. 
2xlarge 1
1.875 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
r8i-ﬂex. 
4xlarge 1
3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
Network speciﬁcations 351
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r8i-ﬂex. 
8xlarge 1
7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
r8i-ﬂex. 
12xlarge 1
11.25 / 22.5 ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
r8i-ﬂex. 
16xlarge 1
15.0 / 30.0 ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
U-3tb1
u-3tb1.56 
xlarge
50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
U-6tb1
u-6tb1.56 
xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-6tb1.11 
2xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-6tb1.metal 100 ✗ 
No
✓ 
Yes
✗  No 1 5 30 ✓ 
Yes
U-9tb1
u-9tb1.11 
2xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-9tb1.metal 100 ✗ 
No
✓ 
Yes
✗  No 1 5 30 ✓ 
Yes
U-12tb1
Network speciﬁcations 352
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
u-12tb1.1 
12xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-12tb1.metal 100 ✗ 
No
✓ 
Yes
✗  No 1 5 30 ✓ 
Yes
U-18tb1
u-18tb1.1 
12xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-18tb1.metal 100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
U-24tb1
u-24tb1.1 
12xlarge
100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
u-24tb1.metal 100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
U7i-6tb
u7i-6tb.1 
12xlarge
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
U7i-8tb
u7i-8tb.1 
12xlarge
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
U7i-12tb
Network speciﬁcations 353
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
u7i-12tb. 
224xlarge
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
U7in-16tb
u7in-16tb 
.224xlarge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
U7in-24tb
u7in-24tb 
.224xlarge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
U7in-32tb
u7in-32tb 
.224xlarge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
U7inh-32tb
u7inh-32t 
b.480xlarge
200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 16 50 ✓ 
Yes
X1
x1.16xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x1.32xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
X1e
x1e.xlarge 1 0.625 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 354
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x1e.2xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x1e.4xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x1e.8xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x1e.16xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x1e.32xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
X2gd
x2gd.medium
1
0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
x2gd.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
x2gd.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x2gd.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x2gd.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x2gd.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 355

## Amazon EBS speciﬁcations

Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x2gd.12xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x2gd.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
x2gd.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
X2idn
x2idn.16x 
large
50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2idn.24x 
large
75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2idn.32x 
large
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2idn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
X2iedn
x2iedn.xlarge
1
1.875 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x2iedn.2x 
large 1
5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x2iedn.4x 
large 1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 356
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x2iedn.8x 
large
25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
x2iedn.16 
xlarge
50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2iedn.24 
xlarge
75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2iedn.32 
xlarge
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x2iedn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
X2iezn
x2iezn.2xlarge
1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x2iezn.4xlarge
1
15.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x2iezn.6xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x2iezn.8xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x2iezn.12 
xlarge
100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
x2iezn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Network speciﬁcations 357
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
X8g
x8g.medium 1 0.52 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
x8g.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
x8g.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x8g.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
x8g.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x8g.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
x8g.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
x8g.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x8g.24xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x8g.48xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
x8g.metal 
-24xl
40 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 358
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x8g.metal 
-48xl
50 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
X8aedz
x8aedz.large 1 1.562 / 18.75 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
x8aedz.xlarge
1
3.125 / 18.75 ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
x8aedz.3x 
large 1
9.375 / 18.75 ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
x8aedz.6x 
large
18.75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 40 ✓ 
Yes
x8aedz.12 
xlarge
37.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
x8aedz.24 
xlarge
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
x8aedz.me 
tal-12xl
37.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
x8aedz.me 
tal-24xl
75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
X8i
x8i.large 1 0.937 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
Network speciﬁcations 359
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x8i.xlarge 1 1.875 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
x8i.2xlarge 1 3.75 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 30 ✓ 
Yes
x8i.4xlarge 1 7.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
x8i.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 50 ✓ 
Yes
x8i.12xlarge 22.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 12 50 ✓ 
Yes
x8i.16xlarge 30 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 16 64 ✓ 
Yes
x8i.24xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 64 ✓ 
Yes
x8i.32xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
x8i.48xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
x8i.64xlarge 80 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
x8i.96xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
Network speciﬁcations 360
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
x8i.metal-48xl 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
x8i.metal-96xl 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 64 ✓ 
Yes
z1d
z1d.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
z1d.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
z1d.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
z1d.3xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
z1d.6xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
z1d.12xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
z1d.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
Network speciﬁcations 361
Amazon EC2 Instance Types
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
For r6in.32xlarge, r6in.metal, r6idn.32xlarge, r6idn.metal, you must attach at 
least 2 ENIs, to separate network cards, to achieve 200 Gbps throughput. Each ENI attached 
to a network card can achieve up to 170 Gbps.
For u7in-16tb.224xlarge, u7in-24tb.224xlarge, u7in-32tb.224xlarge,
u7inh-32tb.480xlarge, you must attach at least 2 ENIs, to separate network cards, to 
achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 100 
Gbps.
For r8gn.48xlarge, r8gn.metal-48xl, you must attach at least 2 ENIs, to separate 
network cards, to achieve 600 Gbps throughput. Each ENI attached to a network card can 
achieve up to 300 Gbps.
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Amazon EBS speciﬁcations 362
Amazon EC2 Instance Types
Note
• R8a, R8g, R8gd, R8i, R8id, R8i-ﬂex, X8g, X8aedz, X8i virtualized instance types support 
conﬁgurable bandwidth weightings. With these instance types, you can optimize an 
instance's bandwidth for either networking performance or Amazon EBS performance. 
The following table shows the default networking bandwidth performance for these 
instance types. Bare metal instance types are not supported. For the supported 
conﬁgurable weightings, see  Conﬁgurable bandwidth weighting preferences.
• For maximum IOPS performance with U7i instances, we recommend that you use io2 
BlockExpress volumes.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R5
r5.large 1 650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.xlarge 1 1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.2xlarge
1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.4xlarge 4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 363
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5.8xlarge 6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.12xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.16xlar 
ge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.24xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R5a
r5a.large 1 650.00 / 
2880.00
81.25 / 
360.00
3600.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.xlarge
1
1085.00 / 
2880.00
135.62 / 
360.00
6000.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 364
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5a.2xlarge
1
1580.00 / 
2880.00
197.50 / 
360.00
8333.00 / 
16000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.4xlarge 2880.00 360.00 16000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.8xlarge 4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.12xla 
rge
6780.00 847.50 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.16xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5a.24xla 
rge
13570.00 1696.25 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
R5ad
r5ad.large
1
650.00 / 
2880.00
81.25 / 
360.00
3600.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 365
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5ad.xlarge
1
1085.00 / 
2880.00
135.62 / 
360.00
6000.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5ad.2xla 
rge 1
1580.00 / 
2880.00
197.50 / 
360.00
8333.00 / 
16000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5ad.4xla 
rge
2880.00 360.00 16000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5ad.8xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5ad.12xl 
arge
6780.00 847.50 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5ad.16xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r5ad.24xl 
arge
13570.00 1696.25 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
R5b
Amazon EBS speciﬁcations 366
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5b.large 1 1250.00 / 
10000.00
156.25 / 
1250.00
5417.00 / 
43333.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
10833.00 / 
43333.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.2xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
21667.00 / 
43333.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.4xlar 
ge
10000.00 1250.00 43333.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.8xlar 
ge
20000.00 2500.00 86667.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.12xla 
rge
30000.00 3750.00 130000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.16xla 
rge
40000.00 5000.00 173333.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5b.24xla 
rge
60000.00 7500.00 260000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 367
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5b.metal 60000.00 7500.00 260000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R5d
r5d.large 1 650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5d.xlarge
1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5d.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5d.4xlar 
ge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5d.8xlar 
ge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5d.12xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 368
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5d.16xla 
rge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r5d.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r5d.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R5dn
r5dn.large
1
650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5dn.xlar 
ge 1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5dn.2xla 
rge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r5dn.4xla 
rge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 369
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5dn.8xla 
rge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5dn.12xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r5dn.16xl 
arge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r5dn.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r5dn.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R5n
r5n.large 1 650.00 / 
4750.00
81.25 / 
593.75
3600.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.xlarge
1
1150.00 / 
4750.00
143.75 / 
593.75
6000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 370
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r5n.2xlar 
ge 1
2300.00 / 
4750.00
287.50 / 
593.75
12000.00 / 
18750.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.4xlar 
ge
4750.00 593.75 18750.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.8xlar 
ge
6800.00 850.00 30000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.12xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.16xla 
rge
13600.00 1700.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r5n.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6a
Amazon EBS speciﬁcations 371
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 372
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6a.metal 40000.00 5000.00 240000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6g
r6g.mediu 
m 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.large 1 630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.xlarge
1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.2xlar 
ge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 373
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6g.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.8xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.12xla 
rge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.16xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6g.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6gd
r6gd.medi 
um 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6gd.large
1
630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 374
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6gd.xlar 
ge 1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6gd.2xla 
rge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6gd.4xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6gd.8xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6gd.12xl 
arge
14250.00 1781.25 50000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6gd.16xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6gd.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6i
Amazon EBS speciﬁcations 375
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 376
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6i.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6id
r6id.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6id.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 377
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r6id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r6id.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R6idn
r6idn.large
1
1562.00 / 
25000.00
195.31 / 
3125.00
6250.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6idn.xla 
rge 1
3125.00 / 
25000.00
390.62 / 
3125.00
12500.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 378
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6idn.2xl 
arge 1
6250.00 / 
25000.00
781.25 / 
3125.00
25000.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6idn.4xl 
arge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
50000.00 / 
100000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6idn.8xl 
arge
25000.00 3125.00 100000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
r6idn.12x 
large
37500.00 4687.50 150000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6idn.16x 
large
50000.00 6250.00 200000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r6idn.24x 
large
75000.00 9375.00 300000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r6idn.32x 
large
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
r6idn.met 
al
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 379
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R6in
r6in.large 1 1562.00 / 
25000.00
195.31 / 
3125.00
6250.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.xlarge
1
3125.00 / 
25000.00
390.62 / 
3125.00
12500.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.2xla 
rge 1
6250.00 / 
25000.00
781.25 / 
3125.00
25000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.4xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
50000.00 / 
100000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.8xla 
rge
25000.00 3125.00 100000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.12xl 
arge
37500.00 4687.50 150000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.16xl 
arge
50000.00 6250.00 200000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 380
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r6in.24xl 
arge
75000.00 9375.00 300000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.32xl 
arge
100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r6in.metal 100000.00 12500.00 400000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R7a
r7a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 381
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r7a.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r7a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r7a.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
r7a.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r7a.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 382
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R7g
r7g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.large 1 630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 383
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r7g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
r7g.metal 20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R7gd
r7gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r7gd.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r7gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r7gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
r7gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 384
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r7gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
r7gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r7gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
r7gd.metal 20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
R7i
r7i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 385
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r7i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r7i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r7i.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r7i.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r7i.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 386
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R7iz
r7iz.large 1 792.00 / 
10000.00
99.00 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.xlarge
1
1584.00 / 
10000.00
198.00 / 
1250.00
6667.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.2xla 
rge 1
3168.00 / 
10000.00
396.00 / 
1250.00
13333.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.12xl 
arge
19000.00 2375.00 76000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r7iz.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 387
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r7iz.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
r7iz.meta 
l-16xl
20000.00 2500.00 80000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r7iz.meta 
l-32xl
40000.00 5000.00 160000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
R8a
r8a.mediu 
m 1
325.00 / 
10000.00
40.62 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 388
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8a.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8a.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8a.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8a.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8a.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8a.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 389
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R8g
r8g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.large 1 630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 390
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8g.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8g.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8g.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r8g.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
R8gb
r8gb.medi 
um 1
1562.00 / 
25000.00
195.31 / 
3125.00
7500.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.large
1
3125.00 / 
25000.00
390.62 / 
3125.00
15000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 391
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8gb.xlar 
ge 1
6250.00 / 
25000.00
781.25 / 
3125.00
30000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.2xla 
rge 1
12500.00 / 
25000.00
1562.50 / 
3125.00
60000.00 / 
120000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.4xla 
rge
25000.00 3125.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.8xla 
rge
50000.00 6250.00 240000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.12xl 
arge
75000.00 9375.00 360000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gb.16xl 
arge
100000.00 12500.00 480000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8gb.24xl 
arge
150000.00 18750.00 720000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8gb.48xl 
arge
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
128 
(Dedicated 
limit)
Amazon EBS speciﬁcations 392
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8gb.meta 
l-24xl
150000.00 18750.00 720000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r8gb.meta 
l-48xl
300000.00 37500.00 1440000.0 
0
✓  Yes ✓  Yes (2 
EBS cards)
78 
(Dedicated 
limit)
R8gd
r8gd.medi 
um 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.large
1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.xlar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 393
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8gd.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gd.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8gd.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8gd.48xl 
arge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8gd.meta 
l-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r8gd.meta 
l-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
R8gn
Amazon EBS speciﬁcations 394
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8gn.medi 
um 1
760.00 / 
10000.00
95.00 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.large
1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.2xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.4xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.8xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.12xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8gn.16xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
Amazon EBS speciﬁcations 395
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8gn.24xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8gn.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8gn.meta 
l-24xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
r8gn.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
R8i
r8i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 396
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
r8i.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8i.96xla 
rge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
Amazon EBS speciﬁcations 397
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8i.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8i.metal 
-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
R8id
r8id.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8id.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8id.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8id.4xla 
rge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8id.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 398
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r8id.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
r8id.16xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
r8id.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8id.32xl 
arge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
r8id.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8id.96xl 
arge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
r8id.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
r8id.meta 
l-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 399
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
R8i-ﬂex
r8i-ﬂex. 
large 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
xlarge 1
630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
2xlarge 1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
4xlarge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
8xlarge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
12xlarge 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
r8i-ﬂex. 
16xlarge 1
10000.00 / 
20000.00
1250.00 / 
2500.00
40000.00 / 
80000.00
✓  Yes ✗  No 48 
(Dedicated 
limit)
U-3tb1
Amazon EBS speciﬁcations 400
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
u-3tb1.56 
xlarge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
U-6tb1
u-6tb1.56 
xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-6tb1.11 
2xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-6tb1.me 
tal
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
U-9tb1
u-9tb1.11 
2xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-9tb1.me 
tal
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
U-12tb1
Amazon EBS speciﬁcations 401
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
u-12tb1.1 
12xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-12tb1.m 
etal
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
U-18tb1
u-18tb1.1 
12xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-18tb1.m 
etal
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
U-24tb1
u-24tb1.1 
12xlarge
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
u-24tb1.m 
etal
38000.00 4750.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
U7i-6tb
Amazon EBS speciﬁcations 402
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
u7i-6tb.1 
12xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7i-8tb
u7i-8tb.1 
12xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7i-12tb
u7i-12tb. 
224xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7in-16tb
u7in-16tb 
.224xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7in-24tb
u7in-24tb 
.224xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7in-32tb
Amazon EBS speciﬁcations 403
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
u7in-32tb 
.224xlarge
100000.00 12500.00 560000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
U7inh-32tb
u7inh-32t 
b.480xlar 
ge
160000.00 20000.00 840000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
X1
x1.16xlar 
ge
7000.00 875.00 40000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
x1.32xlar 
ge
14000.00 1750.00 80000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
X1e
x1e.xlarge 500.00 62.50 3700.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
x1e.2xlar 
ge
1000.00 125.00 7400.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
Amazon EBS speciﬁcations 404
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x1e.4xlar 
ge
1750.00 218.75 10000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
x1e.8xlar 
ge
3500.00 437.50 20000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
x1e.16xla 
rge
7000.00 875.00 40000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
x1e.32xla 
rge
14000.00 1750.00 80000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
X2gd
x2gd.medi 
um 1
315.00 / 
4750.00
39.38 / 
593.75
2500.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2gd.large
1
630.00 / 
4750.00
78.75 / 
593.75
3600.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2gd.xlar 
ge 1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 405
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x2gd.2xla 
rge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2gd.4xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2gd.8xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2gd.12xl 
arge
14250.00 1781.25 60000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2gd.16xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2gd.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
X2idn
x2idn.16x 
large
40000.00 5000.00 173333.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 406
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x2idn.24x 
large
60000.00 7500.00 260000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2idn.32x 
large
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2idn.met 
al
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
X2iedn
x2iedn.xl 
arge 1
2500.00 / 
20000.00
312.50 / 
2500.00
8125.00 / 
65000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2iedn.2x 
large 1
5000.00 / 
20000.00
625.00 / 
2500.00
16250.00 / 
65000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2iedn.4x 
large 1
10000.00 / 
20000.00
1250.00 / 
2500.00
32500.00 / 
65000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2iedn.8x 
large
20000.00 2500.00 65000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 407
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x2iedn.16 
xlarge
40000.00 5000.00 130000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
x2iedn.24 
xlarge
60000.00 7500.00 195000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2iedn.32 
xlarge
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
x2iedn.me 
tal
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
X2iezn
x2iezn.2x 
large
3170.00 396.25 13333.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
x2iezn.4x 
large
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
x2iezn.6x 
large
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 408

## Instance store speciﬁcations

Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x2iezn.8x 
large
12000.00 1500.00 55000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
x2iezn.12 
xlarge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
x2iezn.me 
tal
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
X8g
x8g.mediu 
m 1
315.00 / 
10000.00
39.38 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.large 1 630.00 / 
10000.00
78.75 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.2xlar 
ge 1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 409
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x8g.4xlar 
ge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.8xlar 
ge
10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
x8g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
x8g.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
x8g.48xla 
rge
40000.00 5000.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
x8g.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
x8g.metal 
-48xl
40000.00 5000.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 410
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
X8aedz
x8aedz.la 
rge 1
1250.00 / 
15000.00
156.25 / 
1875.00
5000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8aedz.xl 
arge 1
2500.00 / 
15000.00
312.50 / 
1875.00
10000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8aedz.3x 
large 1
7500.00 / 
15000.00
937.50 / 
1875.00
30000.00 / 
60000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8aedz.6x 
large
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
x8aedz.12 
xlarge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
x8aedz.24 
xlarge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
x8aedz.me 
tal-12xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Amazon EBS speciﬁcations 411
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x8aedz.me 
tal-24xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
X8i
x8i.large 1 650.00 / 
10000.00
81.25 / 
1250.00
3600.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
12000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
x8i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
x8i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 412
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
x8i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
x8i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
x8i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No 88 
(Dedicated 
limit)
x8i.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
x8i.64xla 
rge
70000.00 8750.00 320000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
x8i.96xla 
rge
80000.00 10000.00 480000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
x8i.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
x8i.metal 
-96xl
80000.00 10000.00 480000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Amazon EBS speciﬁcations 413
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
z1d
z1d.large 1 800.00 / 
3170.00
100.00 / 
396.25
3333.00 / 
13333.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
z1d.xlarge
1
1580.00 / 
3170.00
197.50 / 
396.25
6667.00 / 
13333.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
z1d.2xlar 
ge
3170.00 396.25 13333.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
z1d.3xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
z1d.6xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
z1d.12xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
z1d.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
Amazon EBS speciﬁcations 414
Amazon EC2 Instance Types
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
R5ad
r5ad.large 1 x 75 GB NVMe 
SSD
30,000 / 15,000 ✓  Yes
r5ad.xlarge 1 x 150 GB NVMe 
SSD
59,000 / 29,000 ✓  Yes
r5ad.2xlarge 1 x 300 GB NVMe 
SSD
117,000 / 57,000 ✓  Yes
r5ad.4xlarge 2 x 300 GB NVMe 
SSD
234,000 / 114,000 ✓  Yes
r5ad.8xlarge 2 x 600 GB NVMe 
SSD
466,666 / 233,334 ✓  Yes
r5ad.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
r5ad.16xlarge 4 x 600 GB NVMe 
SSD
933,332 / 466,668 ✓  Yes
Instance store speciﬁcations 415
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r5ad.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
R5d
r5d.large 1 x 75 GB NVMe 
SSD
30,000 / 15,000 ✓  Yes
r5d.xlarge 1 x 150 GB NVMe 
SSD
59,000 / 29,000 ✓  Yes
r5d.2xlarge 1 x 300 GB NVMe 
SSD
117,000 / 57,000 ✓  Yes
r5d.4xlarge 2 x 300 GB NVMe 
SSD
234,000 / 114,000 ✓  Yes
r5d.8xlarge 2 x 600 GB NVMe 
SSD
466,666 / 233,334 ✓  Yes
r5d.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
r5d.16xlarge 4 x 600 GB NVMe 
SSD
933,332 / 466,668 ✓  Yes
r5d.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
r5d.metal 4 x 900 GB NVMe 
SSD
1,400,000 / 
680,000
✓  Yes
R5dn
r5dn.large 1 x 75 GB NVMe 
SSD
29,000 / 14,500 ✓  Yes
Instance store speciﬁcations 416
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r5dn.xlarge 1 x 150 GB NVMe 
SSD
58,000 / 29,000 ✓  Yes
r5dn.2xlarge 1 x 300 GB NVMe 
SSD
116,000 / 58,000 ✓  Yes
r5dn.4xlarge 2 x 300 GB NVMe 
SSD
232,000 / 116,000 ✓  Yes
r5dn.8xlarge 2 x 600 GB NVMe 
SSD
464,000 / 232,000 ✓  Yes
r5dn.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 350,000 ✓  Yes
r5dn.16xlarge 4 x 600 GB NVMe 
SSD
930,000 / 465,000 ✓  Yes
r5dn.24xlarge 4 x 900 GB NVMe 
SSD
1,400,000 / 
700,000
✓  Yes
r5dn.metal 4 x 900 GB NVMe 
SSD
1,400,000 / 
700,000
✓  Yes
R6gd
r6gd.medium 1 x 59 GB NVMe 
SSD
13,438 / 5,625 ✓  Yes
r6gd.large 1 x 118 GB NVMe 
SSD
26,875 / 11,250 ✓  Yes
r6gd.xlarge 1 x 237 GB NVMe 
SSD
53,750 / 22,500 ✓  Yes
Instance store speciﬁcations 417
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r6gd.2xlarge 1 x 474 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
r6gd.4xlarge 1 x 950 GB NVMe 
SSD
215,000 / 90,000 ✓  Yes
r6gd.8xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
r6gd.12xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
r6gd.16xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
r6gd.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
R6id
r6id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
r6id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
r6id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
r6id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
r6id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
Instance store speciﬁcations 418
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r6id.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
r6id.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
r6id.24xlarge 4 x 1425 GB NVMe 
SSD
1,609,996 / 
805,000
✓  Yes
r6id.32xlarge 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
r6id.metal 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
R6idn
r6idn.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
r6idn.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
r6idn.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
r6idn.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
r6idn.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
r6idn.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
Instance store speciﬁcations 419
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r6idn.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
r6idn.24xlarge 4 x 1425 GB NVMe 
SSD
1,609,996 / 
805,000
✓  Yes
r6idn.32xlarge 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
r6idn.metal 4 x 1900 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
R7gd
r7gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
r7gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
r7gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
r7gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
r7gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
r7gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
r7gd.12xlarge 2 x 1425 GB NVMe 
SSD
804,998 / 402,500 ✓  Yes
Instance store speciﬁcations 420

## Security speciﬁcations

Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r7gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
r7gd.metal 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
R8gd
r8gd.medium 1 x 59 GB NVMe 
SSD
16,771 / 8,385 ✓  Yes
r8gd.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
r8gd.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
r8gd.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
r8gd.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
r8gd.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
r8gd.12xlarge 3 x 950 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
r8gd.16xlarge 2 x 1900 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
r8gd.24xlarge 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
Instance store speciﬁcations 421
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r8gd.48xlarge 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
r8gd.metal-24xl 3 x 1900 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
r8gd.metal-48xl 6 x 1900 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
R8id
r8id.large 1 x 118 GB NVMe 
SSD
33,542 / 16,771 ✓  Yes
r8id.xlarge 1 x 237 GB NVMe 
SSD
67,083 / 33,542 ✓  Yes
r8id.2xlarge 1 x 474 GB NVMe 
SSD
134,167 / 67,084 ✓  Yes
r8id.4xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
r8id.8xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
r8id.12xlarge 1 x 2850 GB NVMe 
SSD
804,999 / 402,501 ✓  Yes
r8id.16xlarge 1 x 3800 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
r8id.24xlarge 2 x 2850 GB NVMe 
SSD
1,609,998 / 
805,002
✓  Yes
Instance store speciﬁcations 422
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
r8id.32xlarge 2 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
r8id.48xlarge 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
r8id.96xlarge 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
r8id.metal-48xl 3 x 3800 GB NVMe 
SSD
3,219,996 / 
1,610,004
✓  Yes
r8id.metal-96xl 6 x 3800 GB NVMe 
SSD
6,439,992 / 
3,220,008
✓  Yes
X1
x1.16xlarge 1 x 1920 GB SSD   ✓  Yes
x1.32xlarge 2 x 1920 GB SSD   ✓  Yes
X1e
x1e.xlarge 1 x 120 GB SSD   ✓  Yes
x1e.2xlarge 1 x 240 GB SSD   ✓  Yes
x1e.4xlarge 1 x 480 GB SSD   ✓  Yes
x1e.8xlarge 1 x 960 GB SSD   ✓  Yes
x1e.16xlarge 1 x 1920 GB SSD   ✓  Yes
x1e.32xlarge 2 x 1920 GB SSD   ✓  Yes
X2gd
Instance store speciﬁcations 423
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
x2gd.medium 1 x 59 GB NVMe 
SSD
13,438 / 5,625 ✓  Yes
x2gd.large 1 x 118 GB NVMe 
SSD
26,875 / 11,250 ✓  Yes
x2gd.xlarge 1 x 237 GB NVMe 
SSD
53,750 / 22,500 ✓  Yes
x2gd.2xlarge 1 x 475 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
x2gd.4xlarge 1 x 950 GB NVMe 
SSD
215,000 / 90,000 ✓  Yes
x2gd.8xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
x2gd.12xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
x2gd.16xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
x2gd.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
X2idn
x2idn.16xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
x2idn.24xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
Instance store speciﬁcations 424
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
x2idn.32xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
x2idn.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
X2iedn
x2iedn.xlarge 1 x 118 GB NVMe 
SSD
26,875 / 11,250 ✓  Yes
x2iedn.2xlarge 1 x 237 GB NVMe 
SSD
53,750 / 22,500 ✓  Yes
x2iedn.4xlarge 1 x 475 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
x2iedn.8xlarge 1 x 950 GB NVMe 
SSD
215,000 / 90,000 ✓  Yes
x2iedn.16xlarge 1 x 1900 GB NVMe 
SSD
430,000 / 180,000 ✓  Yes
x2iedn.24xlarge 2 x 1425 GB NVMe 
SSD
645,000 / 270,000 ✓  Yes
x2iedn.32xlarge 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
x2iedn.metal 2 x 1900 GB NVMe 
SSD
860,000 / 360,000 ✓  Yes
X8aedz
x8aedz.large 1 x 158 GB NVMe 
SSD
44,722 / 22,361 ✓  Yes
Instance store speciﬁcations 425
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
x8aedz.xlarge 1 x 316 GB NVMe 
SSD
89,444 / 44,722 ✓  Yes
x8aedz.3xlarge 1 x 950 GB NVMe 
SSD
268,333 / 134,167 ✓  Yes
x8aedz.6xlarge 1 x 1900 GB NVMe 
SSD
536,666 / 268,334 ✓  Yes
x8aedz.12xlarge 1 x 3800 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
x8aedz.24xlarge 2 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
x8aedz.me 
tal-12xl
1 x 3800 GB NVMe 
SSD
1,073,332 / 
536,668
✓  Yes
x8aedz.me 
tal-24xl
2 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
z1d
z1d.large 1 x 75 GB NVMe 
SSD
30,000 / 15,000 ✓  Yes
z1d.xlarge 1 x 150 GB NVMe 
SSD
59,000 / 29,000 ✓  Yes
z1d.2xlarge 1 x 300 GB NVMe 
SSD
117,000 / 57,000 ✓  Yes
z1d.3xlarge 1 x 450 GB NVMe 
SSD
175,000 / 75,000 ✓  Yes
Instance store speciﬁcations 426
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
z1d.6xlarge 1 x 900 GB NVMe 
SSD
350,000 / 170,000 ✓  Yes
z1d.12xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
z1d.metal 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
R5
r5.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
r5.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 427
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
R5a
r5a.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
r5a.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 428
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5a.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5a.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5a.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5a.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5a.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5a.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
R5ad
r5ad.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
r5ad.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5ad.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5ad.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 429
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5ad.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5ad.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5ad.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5ad.24xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
R5b
r5b.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
r5b.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 430
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5b.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.24xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r5b.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
R5d
r5d.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
r5d.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.24xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r5d.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
R5dn
r5dn.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 431
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5dn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r5dn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R5n
r5n.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r5n.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 432
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r5n.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r5n.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R6a
r6a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✗  No
r6a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
r6a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
Security speciﬁcations 433
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✓  Yes ✓  Yes ✓  Yes
r6a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6a.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R6g
Security speciﬁcations 434
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6g.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✗  No
r6g.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.12xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
r6g.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 435
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6g.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
R6gd
r6gd.medium ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
r6gd.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
r6gd.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
R6i
r6i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r6i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 436
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6i.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R6id
Security speciﬁcations 437
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
r6id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6id.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R6idn
r6idn.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
r6idn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 438
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6idn.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r6idn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R6in
r6in.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r6in.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 439
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r6in.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r6in.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R7a
r7a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r7a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r7a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 440
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R7g
r7g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 441
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7g.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R7gd
Security speciﬁcations 442
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
r7gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r7gd.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R7i
r7i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r7i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 443
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7i.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
r7i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R7iz
r7iz.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 444
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7iz.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r7iz.metal-16xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 445
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r7iz.metal-32xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8a
r8a.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8a.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 446
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8a.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8a.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
r8a.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8g
r8g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 447
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8g.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 448
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8g.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8gb
r8gb.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8gb.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 449
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8gb.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gb.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
r8gb.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8gd
r8gd.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
r8gd.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 450
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8gd.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8gd.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
r8gd.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R8gn
r8gn.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8gn.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 451
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8gn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8gn.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
r8gn.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8i
r8i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 452
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 453
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
r8i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
r8i.metal-96xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
R8id
r8id.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
r8id.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 454
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8id.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.96xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
r8id.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
r8id.metal-96xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
R8i-ﬂex
r8i-ﬂex.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8i-ﬂex.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8i-ﬂex.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8i-ﬂex.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8i-ﬂex.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
r8i-ﬂex.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 455
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r8i-ﬂex.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U-3tb1
u-3tb1.56xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
U-6tb1
u-6tb1.56xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-6tb1.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-6tb1.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
U-9tb1
u-9tb1.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-9tb1.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 456
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
U-12tb1
u-12tb1.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-12tb1.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
U-18tb1
u-18tb1.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-18tb1.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
U-24tb1
u-24tb1.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
u-24tb1.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
U7i-6tb
Security speciﬁcations 457
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
u7i-6tb.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U7i-8tb
u7i-8tb.112xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U7i-12tb
u7i-12tb. 
224xlarge
✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U7in-16tb
u7in-16tb 
.224xlarge
✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U7in-24tb
u7in-24tb 
.224xlarge
✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
U7in-32tb
u7in-32tb 
.224xlarge
✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 458
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
U7inh-32tb
u7inh-32t 
b.480xlarge
✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
X1
x1.16xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1.32xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
X1e
x1e.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1e.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1e.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1e.8xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1e.16xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
x1e.32xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
X2gd
x2gd.medium ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
x2gd.large ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
Security speciﬁcations 459

## Storage optimized


## Instance families and instance types

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
x2gd.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✓  Yes
x2gd.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
X2idn
x2idn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2idn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2idn.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2idn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
X2iedn
x2iedn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x2iedn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 460
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
X2iezn
x2iezn.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x2iezn.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x2iezn.6xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x2iezn.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x2iezn.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x2iezn.metal ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
X8g
x8g.medium ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 461

## Instance family summary

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
x8g.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 462

## Performance speciﬁcations

Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
x8g.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8g.metal-24xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
x8g.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
X8aedz
x8aedz.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.3xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
x8aedz.metal-12xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
x8aedz.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
X8i
x8i.large ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 463
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
x8i.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.32xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 464
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
x8i.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.64xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
x8i.metal-48xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
x8i.metal-96xl ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
z1d
z1d.large ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✗  No
z1d.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
z1d.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
z1d.3xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
z1d.6xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
z1d.12xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes ✓  Yes
z1d.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 465
Amazon EC2 Instance Types
Speciﬁcations for Amazon EC2 storage optimized instances
Storage optimized instances are designed for workloads that require high, sequential read 
and write access to very large data sets on local storage. They are optimized to deliver tens of 
thousands of low-latency, random I/O operations per second (IOPS) to applications.
For information on previous generation instance types of this category, such as I2 instances, see
Speciﬁcations for Amazon EC2 previous generation instances.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Instance families and instance types
Instance 
family
Available instance types
D2 d2.xlarge  | d2.2xlarge  | d2.4xlarge  | d2.8xlarge
D3 d3.xlarge  | d3.2xlarge  | d3.4xlarge  | d3.8xlarge
D3en d3en.xlarge  | d3en.2xlarge  | d3en.4xlarge  | d3en.6xlarge  |
d3en.8xlarge  | d3en.12xlarge
H1 h1.2xlarge  | h1.4xlarge  | h1.8xlarge  | h1.16xlarge
Storage optimized 466
Amazon EC2 Instance Types
Instance 
family
Available instance types
I3 i3.large | i3.xlarge  | i3.2xlarge  | i3.4xlarge  | i3.8xlarge  |
i3.16xlarge  | i3.metal
I3en i3en.large  | i3en.xlarge  | i3en.2xlarge  | i3en.3xlarge  |
i3en.6xlarge  | i3en.12xlarge  | i3en.24xlarge  | i3en.metal
I4g i4g.large  | i4g.xlarge  | i4g.2xlarge  | i4g.4xlarge  | i4g.8xlar 
ge  | i4g.16xlarge
I4i i4i.large  | i4i.xlarge  | i4i.2xlarge  | i4i.4xlarge  | i4i.8xlar 
ge  | i4i.12xlarge  | i4i.16xlarge  | i4i.24xlarge  | i4i.32xlarge  |
i4i.metal
I7i i7i.large  | i7i.xlarge  | i7i.2xlarge  | i7i.4xlarge  | i7i.8xlar 
ge  | i7i.12xlarge  | i7i.16xlarge  | i7i.24xlarge  | i7i.48xlarge  |
i7i.metal-24xl  | i7i.metal-48xl
I7ie i7ie.large  | i7ie.xlarge  | i7ie.2xlarge  | i7ie.3xlarge  |
i7ie.6xlarge  | i7ie.12xlarge  | i7ie.18xlarge  | i7ie.24xlarge  |
i7ie.48xlarge  | i7ie.metal-24xl  | i7ie.metal-48xl
I8g i8g.large  | i8g.xlarge  | i8g.2xlarge  | i8g.4xlarge  | i8g.8xlar 
ge  | i8g.12xlarge  | i8g.16xlarge  | i8g.24xlarge  | i8g.48xlarge  |
i8g.metal-24xl  | i8g.metal-48xl
I8ge i8ge.large  | i8ge.xlarge  | i8ge.2xlarge  | i8ge.3xlarge  |
i8ge.6xlarge  | i8ge.12xlarge  | i8ge.18xlarge  | i8ge.24xlarge  |
i8ge.48xlarge  | i8ge.metal-24xl  | i8ge.metal-48xl
Im4gn im4gn.large  | im4gn.xlarge  | im4gn.2xlarge  | im4gn.4xlarge  |
im4gn.8xlarge  | im4gn.16xlarge
Is4gen is4gen.medium  | is4gen.large  | is4gen.xlarge  | is4gen.2xlarge  |
is4gen.4xlarge  | is4gen.8xlarge
Instance families and instance types 467
Amazon EC2 Instance Types
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
D2 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
D3 Nitro v3 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
D3en Nitro v3 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
H1 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
I3 Xen * Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
I3en Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
I4g Nitro v4 AWS 
Graviton 
(arm64)
✗  No ✓  Yes ✓  Yes ✓  Yes Linux
I4i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
I7i Nitro v4 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
I7ie Nitro v5 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 468
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
I8g Nitro v5 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
I8ge Nitro v6 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✓  Yes Linux
Im4gn Nitro v4 AWS 
Graviton 
(arm64)
✗  No ✓  Yes ✓  Yes ✓  Yes Linux
Is4gen Nitro v4 AWS 
Graviton 
(arm64)
✗  No ✗  No ✓  Yes ✓  Yes Linux
Note
* i3.metal instances are built on the AWS Nitro System.
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
D2
d2.xlarge 30.50 Intel Xeon 
E52676v3
4 2 2 ✗  No ✗  No
Performance speciﬁcations 469
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
d2.2xlarge 61.00 Intel Xeon 
E52676v3
8 4 2 ✗  No ✗  No
d2.4xlarge 122.00 Intel Xeon 
E52676v3
16 8 2 ✗  No ✗  No
d2.8xlarge 244.00 Intel Xeon 
E52676v3
36 18 2 ✗  No ✗  No
D3
d3.xlarge 32.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
d3.2xlarge 64.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
d3.4xlarge 128.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
d3.8xlarge 256.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
D3en
d3en.xlarge 16.00 Intel Xeon Platinum 
8259
4 2 2 ✗  No ✗  No
d3en.2xlarge 32.00 Intel Xeon Platinum 
8259
8 4 2 ✗  No ✗  No
d3en.4xlarge 64.00 Intel Xeon Platinum 
8259
16 8 2 ✗  No ✗  No
d3en.6xlarge 96.00 Intel Xeon Platinum 
8259
24 12 2 ✗  No ✗  No
Performance speciﬁcations 470
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
d3en.8xlarge 128.00 Intel Xeon Platinum 
8259
32 16 2 ✗  No ✗  No
d3en.12xl 
arge
192.00 Intel Xeon Platinum 
8259
48 24 2 ✗  No ✗  No
H1
h1.2xlarge 32.00 Intel Broadwell 
E5-2686v4
8 4 2 ✗  No ✗  No
h1.4xlarge 64.00 Intel Broadwell 
E5-2686v4
16 8 2 ✗  No ✗  No
h1.8xlarge 128.00 Intel Broadwell 
E5-2686v4
32 16 2 ✗  No ✗  No
h1.16xlarge 256.00 Intel Broadwell 
E5-2686v4
64 32 2 ✗  No ✗  No
I3
i3.large 15.25 Intel Broadwell 
E5-2686v4
2 1 2 ✗  No ✗  No
i3.xlarge 30.50 Intel Broadwell 
E5-2686v4
4 2 2 ✗  No ✗  No
i3.2xlarge 61.00 Intel Broadwell 
E5-2686v4
8 4 2 ✗  No ✗  No
i3.4xlarge 122.00 Intel Broadwell 
E5-2686v4
16 8 2 ✗  No ✗  No
i3.8xlarge 244.00 Intel Broadwell 
E5-2686v4
32 16 2 ✗  No ✗  No
Performance speciﬁcations 471
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i3.16xlarge 488.00 Intel Broadwell 
E5-2686v4
64 32 2 ✗  No ✗  No
i3.metal 512.00 Intel Broadwell 
E5-2686v4
72 36 2 ✗  No ✗  No
I3en
i3en.large 16.00 Intel Xeon Platinum 
8175
2 1 2 ✗  No ✗  No
i3en.xlarge 32.00 Intel Xeon Platinum 
8175
4 2 2 ✗  No ✗  No
i3en.2xlarge 64.00 Intel Xeon Platinum 
8175
8 4 2 ✗  No ✗  No
i3en.3xlarge 96.00 Intel Xeon Platinum 
8175
12 6 2 ✗  No ✗  No
i3en.6xlarge 192.00 Intel Xeon Platinum 
8175
24 12 2 ✗  No ✗  No
i3en.12xlarge 384.00 Intel Xeon Platinum 
8175
48 24 2 ✗  No ✗  No
i3en.24xlarge 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
i3en.metal 768.00 Intel Xeon Platinum 
8175
96 48 2 ✗  No ✗  No
I4g
i4g.large 16.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
Performance speciﬁcations 472
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i4g.xlarge 32.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
i4g.2xlarge 64.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
i4g.4xlarge 128.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
i4g.8xlarge 256.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
i4g.16xlarge 512.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
I4i
i4i.large 16.00 Intel Xeon Ice Lake 2 1 2 ✗  No ✗  No
i4i.xlarge 32.00 Intel Xeon Ice Lake 4 2 2 ✗  No ✗  No
i4i.2xlarge 64.00 Intel Xeon Ice Lake 8 4 2 ✗  No ✗  No
i4i.4xlarge 128.00 Intel Xeon Ice Lake 16 8 2 ✗  No ✗  No
i4i.8xlarge 256.00 Intel Xeon Ice Lake 32 16 2 ✗  No ✗  No
i4i.12xlarge 384.00 Intel Xeon Ice Lake 48 24 2 ✗  No ✗  No
i4i.16xlarge 512.00 Intel Xeon Ice Lake 64 32 2 ✗  No ✗  No
i4i.24xlarge 768.00 Intel Xeon Ice Lake 96 48 2 ✗  No ✗  No
i4i.32xlarge 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
i4i.metal 1024.00 Intel Xeon Ice Lake 128 64 2 ✗  No ✗  No
Performance speciﬁcations 473
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
I7i
i7i.large 16.00 Intel Emerald 
Rapids
2 1 2 ✗  No ✗  No
i7i.xlarge 32.00 Intel Emerald 
Rapids
4 2 2 ✗  No ✗  No
i7i.2xlarge 64.00 Intel Emerald 
Rapids
8 4 2 ✗  No ✗  No
i7i.4xlarge 128.00 Intel Emerald 
Rapids
16 8 2 ✗  No ✗  No
i7i.8xlarge 256.00 Intel Emerald 
Rapids
32 16 2 ✗  No ✗  No
i7i.12xlarge 384.00 Intel Emerald 
Rapids
48 24 2 ✗  No ✗  No
i7i.16xlarge 512.00 Intel Emerald 
Rapids
64 32 2 ✗  No ✗  No
i7i.24xlarge 768.00 Intel Emerald 
Rapids
96 48 2 ✗  No ✗  No
i7i.48xlarge 1536.00 Intel Emerald 
Rapids
192 96 2 ✗  No ✗  No
i7i.metal 
-24xl
768.00 Intel Emerald 
Rapids
96 48 2 ✗  No ✗  No
i7i.metal 
-48xl
1536.00 Intel Emerald 
Rapids
192 96 2 ✗  No ✗  No
I7ie
Performance speciﬁcations 474
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i7ie.large 16.00 Intel Emerald 
Rapids
2 1 2 ✗  No ✗  No
i7ie.xlarge 32.00 Intel Emerald 
Rapids
4 2 2 ✗  No ✗  No
i7ie.2xlarge 64.00 Intel Emerald 
Rapids
8 4 2 ✗  No ✗  No
i7ie.3xlarge 96.00 Intel Emerald 
Rapids
12 6 2 ✗  No ✗  No
i7ie.6xlarge 192.00 Intel Emerald 
Rapids
24 12 2 ✗  No ✗  No
i7ie.12xlarge 384.00 Intel Emerald 
Rapids
48 24 2 ✗  No ✗  No
i7ie.18xlarge 576.00 Intel Emerald 
Rapids
72 36 2 ✗  No ✗  No
i7ie.24xlarge 768.00 Intel Emerald 
Rapids
96 48 2 ✗  No ✗  No
i7ie.48xlarge 1536.00 Intel Emerald 
Rapids
192 96 2 ✗  No ✗  No
i7ie.meta 
l-24xl
768.00 Intel Emerald 
Rapids
96 48 2 ✗  No ✗  No
i7ie.meta 
l-48xl
1536.00 Intel Emerald 
Rapids
192 96 2 ✗  No ✗  No
I8g
Performance speciﬁcations 475
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i8g.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
i8g.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
i8g.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
i8g.4xlarge 128.00 AWS Graviton4 
Processor
16 16 1 ✗  No ✗  No
i8g.8xlarge 256.00 AWS Graviton4 
Processor
32 32 1 ✗  No ✗  No
i8g.12xlarge 384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
i8g.16xlarge 512.00 AWS Graviton4 
Processor
64 64 1 ✗  No ✗  No
i8g.24xlarge 768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
i8g.48xlarge 1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
i8g.metal 
-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
i8g.metal 
-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
I8ge
Performance speciﬁcations 476
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i8ge.large 16.00 AWS Graviton4 
Processor
2 2 1 ✗  No ✗  No
i8ge.xlarge 32.00 AWS Graviton4 
Processor
4 4 1 ✗  No ✗  No
i8ge.2xlarge 64.00 AWS Graviton4 
Processor
8 8 1 ✗  No ✗  No
i8ge.3xlarge 96.00 AWS Graviton4 
Processor
12 12 1 ✗  No ✗  No
i8ge.6xlarge 192.00 AWS Graviton4 
Processor
24 24 1 ✗  No ✗  No
i8ge.12xlarge 384.00 AWS Graviton4 
Processor
48 48 1 ✗  No ✗  No
i8ge.18xlarge 576.00 AWS Graviton4 
Processor
72 72 1 ✗  No ✗  No
i8ge.24xlarge 768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
i8ge.48xlarge 1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
i8ge.meta 
l-24xl
768.00 AWS Graviton4 
Processor
96 96 1 ✗  No ✗  No
i8ge.meta 
l-48xl
1536.00 AWS Graviton4 
Processor
192 192 1 ✗  No ✗  No
Im4gn
Performance speciﬁcations 477
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
im4gn.large 8.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
im4gn.xlarge 16.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
im4gn.2xl 
arge
32.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
im4gn.4xl 
arge
64.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
im4gn.8xl 
arge
128.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
im4gn.16x 
large
256.00 AWS Graviton2 
Processor
64 64 1 ✗  No ✗  No
Is4gen
is4gen.me 
dium
6.00 AWS Graviton2 
Processor
1 1 1 ✗  No ✗  No
is4gen.large 12.00 AWS Graviton2 
Processor
2 2 1 ✗  No ✗  No
is4gen.xlarge 24.00 AWS Graviton2 
Processor
4 4 1 ✗  No ✗  No
is4gen.2x 
large
48.00 AWS Graviton2 
Processor
8 8 1 ✗  No ✗  No
is4gen.4x 
large
96.00 AWS Graviton2 
Processor
16 16 1 ✗  No ✗  No
Performance speciﬁcations 478
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
is4gen.8x 
large
192.00 AWS Graviton2 
Processor
32 32 1 ✗  No ✗  No
Network speciﬁcations
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
D2
d2.xlarge Moderate ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
d2.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
d2.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
d2.8xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
D3
d3.xlarge 1 3.0 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 3 ✓ 
Yes
d3.2xlarge 1 6.0 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 5 ✓ 
Yes
d3.4xlarge 1 12.5 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 10 ✓ 
Yes
Network speciﬁcations 479
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
d3.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 3 20 ✓ 
Yes
D3en
d3en.xlarge 1 6.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 3 ✓ 
Yes
d3en.2xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 5 ✓ 
Yes
d3en.4xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 10 ✓ 
Yes
d3en.6xlarge 40 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
d3en.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 20 ✓ 
Yes
d3en.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 3 30 ✓ 
Yes
H1
h1.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
h1.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
h1.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 480
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
h1.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
I3
i3.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i3.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i3.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i3.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i3.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i3.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
i3.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
I3en
i3en.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i3en.xlarge 1 4.2 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 481
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
i3en.2xlarge 1 8.4 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i3en.3xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i3en.6xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i3en.12xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i3en.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
i3en.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
I4g
i4g.large 1 0.781 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i4g.xlarge 1 1.875 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i4g.2xlarge 1 4.687 / 12.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i4g.4xlarge 1 9.375 / 25.0 ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
i4g.8xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
Network speciﬁcations 482
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
i4g.16xlarge 37.5 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
I4i
i4i.large 1 0.781 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i4i.xlarge 1 1.875 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i4i.2xlarge 1 4.687 / 12.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i4i.4xlarge 1 9.375 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i4i.8xlarge 18.75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
i4i.12xlarge 28.12 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
i4i.16xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i4i.24xlarge 56.25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 30 ✓ 
Yes
i4i.32xlarge 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i4i.metal 75 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 483
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
I7i
i7i.large 1 1.171 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i7i.xlarge 1 2.343 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i7i.2xlarge 1 4.687 / 12.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i7i.4xlarge 1 9.375 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i7i.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i7i.12xlarge 28.12 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
i7i.16xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7i.24xlarge 56.25 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7i.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7i.metal-24xl 56.25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7i.metal-48xl 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 484
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
I7ie
i7ie.large 1 2.083 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i7ie.xlarge 1 4.166 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i7ie.2xlarge 1 8.333 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i7ie.3xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i7ie.6xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i7ie.12xlarge 1 25.0 / 50.0 ✗ 
No
✓ 
Yes
✓  Yes 1 8 50 ✓ 
Yes
i7ie.18xlarge 1 37.5 / 75.0 ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7ie.24xlarge 1 50.0 / 100.0 ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7ie.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7ie.meta 
l-24xl 1
50.0 / 100.0 ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i7ie.meta 
l-48xl
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 485
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
I8g
i8g.large 1 1.172 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i8g.xlarge 1 2.344 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i8g.2xlarge 1 4.688 / 12.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i8g.4xlarge 1 9.375 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i8g.8xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
i8g.12xlarge 28.12 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
i8g.16xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i8g.24xlarge 56.25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i8g.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i8g.metal-24xl 56.25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
i8g.metal-48xl
1
90.0 / 100.0 ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Network speciﬁcations 486
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
I8ge
i8ge.large 1 2.1 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
i8ge.xlarge 1 4.2 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i8ge.2xlarge 1 8.4 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
i8ge.3xlarge 1 12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 6 30 ✓ 
Yes
i8ge.6xlarge 37.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 10 30 ✓ 
Yes
i8ge.12xlarge 75 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 12 30 ✓ 
Yes
i8ge.18xlarge 112.5 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
i8ge.24xlarge 150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
i8ge.48xlarge 180 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
i8ge.meta 
l-24xl
150 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 16 50 ✓ 
Yes
i8ge.meta 
l-48xl
180 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 24 50 ✓ 
Yes
Network speciﬁcations 487
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
Im4gn
im4gn.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
im4gn.xlarge 1 6.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
im4gn.2xlarge
1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
im4gn.4xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
im4gn.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✓  Yes 1 8 30 ✓ 
Yes
im4gn.16x 
large
100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
Is4gen
is4gen.me 
dium 1
1.562 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
is4gen.large 1 3.125 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
is4gen.xlarge
1
6.25 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
is4gen.2xlarge
1
12.5 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 488
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
is4gen.4xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
is4gen.8xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
2 These instances support enhanced networking using the Intel 82599 VF interface.
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
Amazon EBS speciﬁcations 489
Amazon EC2 Instance Types
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
D2
d2.xlarge 750.00 93.75 6000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
d2.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
d2.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
d2.8xlarge 4000.00 500.00 32000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
D3
d3.xlarge 1 850.00 / 
2800.00
106.25 / 
350.00
5000.00 / 
15000.00
✓  Yes ✗  No Up to 24 
(Shared 
limit)
Amazon EBS speciﬁcations 490
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
d3.2xlarge
1
1700.00 / 
2800.00
212.50 / 
350.00
10000.00 / 
15000.00
✓  Yes ✗  No Up to 21 
(Shared 
limit)
d3.4xlarge 2800.00 350.00 15000.00 ✓  Yes ✗  No Up to 15 
(Shared 
limit)
d3.8xlarge 5000.00 625.00 30000.00 ✓  Yes ✗  No Up to 3 
(Shared 
limit)
D3en
d3en.xlar 
ge 1
850.00 / 
2800.00
106.25 / 
350.00
5000.00 / 
15000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
d3en.2xla 
rge 1
1700.00 / 
2800.00
212.50 / 
350.00
10000.00 / 
15000.00
✓  Yes ✗  No Up to 23 
(Shared 
limit)
d3en.4xla 
rge
2800.00 350.00 15000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
d3en.6xla 
rge
4000.00 500.00 25000.00 ✓  Yes ✗  No Up to 15 
(Shared 
limit)
Amazon EBS speciﬁcations 491
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
d3en.8xla 
rge
5000.00 625.00 30000.00 ✓  Yes ✗  No Up to 11 
(Shared 
limit)
d3en.12xl 
arge
7000.00 875.00 40000.00 ✓  Yes ✗  No Up to 3 
(Shared 
limit)
H1
h1.2xlarge 1750.00 218.75 12000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
h1.4xlarge 3500.00 437.50 20000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
h1.8xlarge 7000.00 875.00 40000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
h1.16xlar 
ge
14000.00 1750.00 80000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
I3
i3.large 425.00 53.12 3000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
Amazon EBS speciﬁcations 492
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i3.xlarge 850.00 106.25 6000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i3.2xlarge 1700.00 212.50 12000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i3.4xlarge 3500.00 437.50 16000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i3.8xlarge 7000.00 875.00 32500.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i3.16xlarge 14000.00 1750.00 65000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i3.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
I3en
i3en.large
1
576.00 / 
4750.00
72.10 / 
593.75
3000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 493
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i3en.xlarge
1
1153.00 / 
4750.00
144.20 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i3en.2xla 
rge 1
2307.00 / 
4750.00
288.39 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
i3en.3xla 
rge 1
3800.00 / 
4750.00
475.00 / 
593.75
15000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i3en.6xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
i3en.12xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
i3en.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
i3en.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
I4g
Amazon EBS speciﬁcations 494
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i4g.large 1 625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4g.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4g.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4g.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4g.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
i4g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
I4i
i4i.large 1 625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 495
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i4i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
i4i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
i4i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No Up to 24 
(Shared 
limit)
i4i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
i4i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 21 
(Shared 
limit)
i4i.32xla 
rge
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
Amazon EBS speciﬁcations 496
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i4i.metal 40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
I7i
i7i.large 1 625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7i.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7i.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7i.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7i.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
i7i.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 497
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i7i.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
i7i.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
i7i.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
i7i.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
i7i.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
I7ie
i7ie.large 1 625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7ie.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 498
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i7ie.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7ie.3xla 
rge 1
3750.00 / 
10000.00
468.75 / 
1250.00
15000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7ie.6xla 
rge 1
7500.00 / 
10000.00
937.50 / 
1250.00
30000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i7ie.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
i7ie.18xl 
arge
22500.00 2812.50 90000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
i7ie.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
i7ie.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
i7ie.meta 
l-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
Amazon EBS speciﬁcations 499
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i7ie.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
I8g
i8g.large 1 625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8g.xlarge 1 1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8g.2xlarge
1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8g.4xlarge
1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8g.8xlarge 10000.00 1250.00 40000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
i8g.12xla 
rge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 500
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i8g.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
i8g.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
i8g.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
i8g.metal 
-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
i8g.metal 
-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
I8ge
i8ge.large
1
625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8ge.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 501
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i8ge.2xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8ge.3xla 
rge 1
3750.00 / 
10000.00
468.75 / 
1250.00
15000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8ge.6xla 
rge 1
7500.00 / 
10000.00
937.50 / 
1250.00
30000.00 / 
40000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
i8ge.12xl 
arge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
i8ge.18xl 
arge
22500.00 2812.50 90000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
i8ge.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
i8ge.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
i8ge.meta 
l-24xl
30000.00 3750.00 120000.00 ✓  Yes ✗  No 39 
(Dedicated 
limit)
Amazon EBS speciﬁcations 502
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i8ge.meta 
l-48xl
60000.00 7500.00 240000.00 ✓  Yes ✗  No 79 
(Dedicated 
limit)
Im4gn
im4gn.lar 
ge 1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
im4gn.xla 
rge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
im4gn.2xl 
arge 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
im4gn.4xl 
arge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
im4gn.8xl 
arge
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
im4gn.16x 
large
40000.00 5000.00 160000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
Is4gen
Amazon EBS speciﬁcations 503
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
is4gen.me 
dium 1
625.00 / 
10000.00
78.12 / 
1250.00
2500.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
is4gen.la 
rge 1
1250.00 / 
10000.00
156.25 / 
1250.00
5000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
is4gen.xl 
arge 1
2500.00 / 
10000.00
312.50 / 
1250.00
10000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
is4gen.2x 
large 1
5000.00 / 
10000.00
625.00 / 
1250.00
20000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
is4gen.4x 
large
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
is4gen.8x 
large
20000.00 2500.00 80000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Amazon EBS speciﬁcations 504
Amazon EC2 Instance Types
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
D2
d2.xlarge 3 x 2048 GB HDD   ✓  Yes
d2.2xlarge 6 x 2048 GB HDD   ✓  Yes
d2.4xlarge 12 x 2048 
GB
HDD   ✓  Yes
d2.8xlarge 24 x 2048 
GB
HDD   ✓  Yes
D3
d3.xlarge 3 x 1980 GB NVMe 
HDD
  ✓  Yes
d3.2xlarge 6 x 1980 GB NVMe 
HDD
  ✓  Yes
d3.4xlarge 12 x 1980 
GB
NVMe 
HDD
  ✓  Yes
d3.8xlarge 24 x 1980 
GB
NVMe 
HDD
  ✓  Yes
D3en
d3en.xlarge 2 x 13980 
GB
NVMe 
HDD
  ✓  Yes
Instance store speciﬁcations 505
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
d3en.2xlarge 4 x 13980 
GB
NVMe 
HDD
  ✓  Yes
d3en.4xlarge 8 x 13980 
GB
NVMe 
HDD
  ✓  Yes
d3en.6xlarge 12 x 13980 
GB
NVMe 
HDD
  ✓  Yes
d3en.8xlarge 16 x 13980 
GB
NVMe 
HDD
  ✓  Yes
d3en.12xlarge 24 x 13980 
GB
NVMe 
HDD
  ✓  Yes
H1
h1.2xlarge 1 x 2000 GB HDD   ✓  Yes
h1.4xlarge 2 x 2000 GB HDD   ✓  Yes
h1.8xlarge 4 x 2000 GB HDD   ✓  Yes
h1.16xlarge 8 x 2000 GB HDD   ✓  Yes
I3
i3.large 1 x 475 GB NVMe 
SSD
103,125 / 35,000 ✓  Yes
i3.xlarge 1 x 950 GB NVMe 
SSD
206,250 / 70,000 ✓  Yes
i3.2xlarge 1 x 1900 GB NVMe 
SSD
412,500 / 180,000 ✓  Yes
Instance store speciﬁcations 506
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i3.4xlarge 2 x 1900 GB NVMe 
SSD
825,000 / 360,000 ✓  Yes
i3.8xlarge 4 x 1900 GB NVMe 
SSD
1,650,000 / 
720,000
✓  Yes
i3.16xlarge 8 x 1900 GB NVMe 
SSD
3,300,000 / 
1,440,000
✓  Yes
i3.metal 8 x 1900 GB NVMe 
SSD
3,300,000 / 
1,440,000
✓  Yes
I3en
i3en.large 1 x 1250 GB NVMe 
SSD
42,500 / 32,500 ✓  Yes
i3en.xlarge 1 x 2500 GB NVMe 
SSD
85,000 / 65,000 ✓  Yes
i3en.2xlarge 2 x 2500 GB NVMe 
SSD
170,000 / 130,000 ✓  Yes
i3en.3xlarge 1 x 7500 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
i3en.6xlarge 2 x 7500 GB NVMe 
SSD
500,000 / 400,000 ✓  Yes
i3en.12xlarge 4 x 7500 GB NVMe 
SSD
1,000,000 / 
800,000
✓  Yes
i3en.24xlarge 8 x 7500 GB NVMe 
SSD
2,000,000 / 
1,600,000
✓  Yes
Instance store speciﬁcations 507
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i3en.metal 8 x 7500 GB NVMe 
SSD
2,000,000 / 
1,600,000
✓  Yes
I4g
i4g.large 1 x 468 GB NVMe 
SSD
31,250 / 25,000 ✓  Yes
i4g.xlarge 1 x 937 GB NVMe 
SSD
62,500 / 50,000 ✓  Yes
i4g.2xlarge 1 x 1875 GB NVMe 
SSD
125,000 / 100,000 ✓  Yes
i4g.4xlarge 1 x 3750 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
i4g.8xlarge 2 x 3750 GB NVMe 
SSD
500,000 / 400,000 ✓  Yes
i4g.16xlarge 4 x 3750 GB NVMe 
SSD
1,000,000 / 
800,000
✓  Yes
I4i
i4i.large 1 x 468 GB NVMe 
SSD
50,000 / 27,500 ✓  Yes
i4i.xlarge 1 x 937 GB NVMe 
SSD
100,000 / 55,000 ✓  Yes
i4i.2xlarge 1 x 1875 GB NVMe 
SSD
200,000 / 110,000 ✓  Yes
i4i.4xlarge 1 x 3750 GB NVMe 
SSD
400,000 / 220,000 ✓  Yes
Instance store speciﬁcations 508
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i4i.8xlarge 2 x 3750 GB NVMe 
SSD
800,000 / 440,000 ✓  Yes
i4i.12xlarge 3 x 3750 GB NVMe 
SSD
1,200,000 / 
660,000
✓  Yes
i4i.16xlarge 4 x 3750 GB NVMe 
SSD
1,600,000 / 
880,000
✓  Yes
i4i.24xlarge 6 x 3750 GB NVMe 
SSD
2,400,000 / 
1,320,000
✓  Yes
i4i.32xlarge 8 x 3750 GB NVMe 
SSD
3,200,000 / 
1,760,000
✓  Yes
i4i.metal 8 x 3750 GB NVMe 
SSD
3,200,000 / 
1,760,000
✓  Yes
I7i
i7i.large 1 x 468 GB NVMe 
SSD
75,000 / 41,250 ✓  Yes
i7i.xlarge 1 x 937 GB NVMe 
SSD
150,000 / 82,500 ✓  Yes
i7i.2xlarge 1 x 1875 GB NVMe 
SSD
300,000 / 165,000 ✓  Yes
i7i.4xlarge 1 x 3750 GB NVMe 
SSD
600,000 / 330,000 ✓  Yes
i7i.8xlarge 2 x 3750 GB NVMe 
SSD
1,200,000 / 
660,000
✓  Yes
Instance store speciﬁcations 509
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i7i.12xlarge 3 x 3750 GB NVMe 
SSD
1,800,000 / 
990,000
✓  Yes
i7i.16xlarge 4 x 3750 GB NVMe 
SSD
2,400,000 / 
1,320,000
✓  Yes
i7i.24xlarge 6 x 3750 GB NVMe 
SSD
3,600,000 / 
1,980,000
✓  Yes
i7i.48xlarge 12 x 3750 
GB
NVMe 
SSD
7,200,000 / 
3,960,000
✓  Yes
i7i.metal-24xl 6 x 3750 GB NVMe 
SSD
3,600,000 / 
1,980,000
✓  Yes
i7i.metal-48xl 12 x 3750 
GB
NVMe 
SSD
7,200,000 / 
3,960,000
✓  Yes
I7ie
i7ie.large 1 x 1250 GB NVMe 
SSD
54,166 / 43,333 ✓  Yes
i7ie.xlarge 1 x 2500 GB NVMe 
SSD
108,333 / 86,666 ✓  Yes
i7ie.2xlarge 2 x 2500 GB NVMe 
SSD
216,666 / 173,332 ✓  Yes
i7ie.3xlarge 1 x 7500 GB NVMe 
SSD
325,000 / 260,000 ✓  Yes
i7ie.6xlarge 2 x 7500 GB NVMe 
SSD
650,000 / 520,000 ✓  Yes
Instance store speciﬁcations 510
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i7ie.12xlarge 4 x 7500 GB NVMe 
SSD
1,300,000 / 
1,040,000
✓  Yes
i7ie.18xlarge 6 x 7500 GB NVMe 
SSD
1,950,000 / 
1,560,000
✓  Yes
i7ie.24xlarge 8 x 7500 GB NVMe 
SSD
2,600,000 / 
2,080,000
✓  Yes
i7ie.48xlarge 16 x 7500 
GB
NVMe 
SSD
5,200,000 / 
4,160,000
✓  Yes
i7ie.metal-24xl 8 x 7500 GB NVMe 
SSD
2,600,000 / 
2,080,000
✓  Yes
i7ie.metal-48xl 16 x 7500 
GB
NVMe 
SSD
5,200,000 / 
4,160,000
✓  Yes
I8g
i8g.large 1 x 468 GB NVMe 
SSD
75,000 / 41,250 ✓  Yes
i8g.xlarge 1 x 937 GB NVMe 
SSD
150,000 / 82,500 ✓  Yes
i8g.2xlarge 1 x 1875 GB NVMe 
SSD
300,000 / 165,000 ✓  Yes
i8g.4xlarge 1 x 3750 GB NVMe 
SSD
600,000 / 330,000 ✓  Yes
i8g.8xlarge 2 x 3750 GB NVMe 
SSD
1,200,000 / 
660,000
✓  Yes
Instance store speciﬁcations 511
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i8g.12xlarge 3 x 3750 GB NVMe 
SSD
1,800,000 / 
990,000
✓  Yes
i8g.16xlarge 4 x 3750 GB NVMe 
SSD
2,400,000 / 
1,320,000
✓  Yes
i8g.24xlarge 6 x 3750 GB NVMe 
SSD
3,600,000 / 
1,980,000
✓  Yes
i8g.48xlarge 12 x 3750 
GB
NVMe 
SSD
7,200,000 / 
3,960,000
✓  Yes
i8g.metal-24xl 6 x 3750 GB NVMe 
SSD
3,600,000 / 
1,980,000
✓  Yes
i8g.metal-48xl 12 x 3750 
GB
NVMe 
SSD
7,200,000 / 
3,960,000
✓  Yes
I8ge
i8ge.large 1 x 1250 GB NVMe 
SSD
54,166 / 43,333 ✓  Yes
i8ge.xlarge 1 x 2500 GB NVMe 
SSD
108,333 / 86,666 ✓  Yes
i8ge.2xlarge 2 x 2500 GB NVMe 
SSD
216,666 / 173,332 ✓  Yes
i8ge.3xlarge 1 x 7500 GB NVMe 
SSD
325,000 / 260,000 ✓  Yes
i8ge.6xlarge 2 x 7500 GB NVMe 
SSD
650,000 / 520,000 ✓  Yes
Instance store speciﬁcations 512
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
i8ge.12xlarge 4 x 7500 GB NVMe 
SSD
1,300,000 / 
1,040,000
✓  Yes
i8ge.18xlarge 6 x 7500 GB NVMe 
SSD
1,950,000 / 
1,560,000
✓  Yes
i8ge.24xlarge 8 x 7500 GB NVMe 
SSD
2,600,000 / 
2,080,000
✓  Yes
i8ge.48xlarge 16 x 7500 
GB
NVMe 
SSD
5,200,000 / 
4,160,000
✓  Yes
i8ge.metal-24xl 8 x 7500 GB NVMe 
SSD
2,600,000 / 
2,080,000
✓  Yes
i8ge.metal-48xl 16 x 7500 
GB
NVMe 
SSD
5,200,000 / 
4,160,000
✓  Yes
Im4gn
im4gn.large 1 x 937 GB NVMe 
SSD
31,250 / 25,000 ✓  Yes
im4gn.xlarge 1 x 1875 GB NVMe 
SSD
62,500 / 50,000 ✓  Yes
im4gn.2xlarge 1 x 3750 GB NVMe 
SSD
125,000 / 100,000 ✓  Yes
im4gn.4xlarge 1 x 7500 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
im4gn.8xlarge 2 x 7500 GB NVMe 
SSD
500,000 / 400,000 ✓  Yes
Instance store speciﬁcations 513
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
im4gn.16xlarge 4 x 7500 GB NVMe 
SSD
1,000,000 / 
800,000
✓  Yes
Is4gen
is4gen.medium 1 x 937 GB NVMe 
SSD
31,250 / 25,000 ✓  Yes
is4gen.large 1 x 1875 GB NVMe 
SSD
62,500 / 50,000 ✓  Yes
is4gen.xlarge 1 x 3750 GB NVMe 
SSD
125,000 / 100,000 ✓  Yes
is4gen.2xlarge 1 x 7500 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
is4gen.4xlarge 2 x 7500 GB NVMe 
SSD
500,000 / 400,000 ✓  Yes
is4gen.8xlarge 4 x 7500 GB NVMe 
SSD
1,000,000 / 
800,000
✓  Yes
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Instance store speciﬁcations 514
Amazon EC2 Instance Types
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
D2
d2.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
d2.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
d2.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
d2.8xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
D3
d3.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
D3en
d3en.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3en.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3en.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3en.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3en.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
d3en.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 515
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
H1
h1.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
h1.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
h1.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
h1.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
I3
i3.large ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.8xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
i3.metal ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
I3en
i3en.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
i3en.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i3en.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i3en.3xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i3en.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 516
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
i3en.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i3en.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i3en.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
I4g
i4g.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
i4g.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
i4g.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
i4g.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
i4g.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
i4g.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
I4i
i4i.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
i4i.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 517
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
i4i.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i4i.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
I7i
i7i.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
i7i.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7i.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
i7i.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
I7ie
i7ie.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
i7ie.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.3xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 518
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
i7ie.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.18xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i7ie.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
i7ie.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
I8g
i8g.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8g.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
i8g.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 519
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
I8ge
i8ge.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.3xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.18xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
i8ge.metal-24xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
i8ge.metal-48xl ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Im4gn
im4gn.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
im4gn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
im4gn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
im4gn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
im4gn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
im4gn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
Security speciﬁcations 520
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
Is4gen
is4gen.medium ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
is4gen.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
is4gen.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
is4gen.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
is4gen.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
is4gen.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Speciﬁcations for Amazon EC2 accelerated computing instances
Accelerated computing instances use hardware accelerators, or co-processors, to perform 
functions, such as ﬂoating point number calculations, graphics processing, or data pattern 
matching, more eﬃciently than is possible in software running on CPUs.
For information on previous generation instance types of this category, such as G3 instances, see
Speciﬁcations for Amazon EC2 previous generation instances.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Accelerated computing 521
Amazon EC2 Instance Types
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Instance families and instance types
Instance 
family
Available instance types
DL1 dl1.24xlarge
DL2q dl2q.24xlarge
F1 f1.2xlarge  | f1.4xlarge  | f1.16xlarge
F2 f2.6xlarge  | f2.12xlarge  | f2.48xlarge
G4ad g4ad.xlarge  | g4ad.2xlarge  | g4ad.4xlarge  | g4ad.8xlarge  |
g4ad.16xlarge
G4dn g4dn.xlarge  | g4dn.2xlarge  | g4dn.4xlarge  | g4dn.8xlarge  |
g4dn.12xlarge  | g4dn.16xlarge  | g4dn.metal
G5 g5.xlarge  | g5.2xlarge  | g5.4xlarge  | g5.8xlarge  | g5.12xlarge  |
g5.16xlarge  | g5.24xlarge  | g5.48xlarge
G5g g5g.xlarge  | g5g.2xlarge  | g5g.4xlarge  | g5g.8xlarge  | g5g.16xla 
rge  | g5g.metal
G6 g6.xlarge  | g6.2xlarge  | g6.4xlarge  | g6.8xlarge  | g6.12xlarge  |
g6.16xlarge  | g6.24xlarge  | g6.48xlarge
G6e g6e.xlarge  | g6e.2xlarge  | g6e.4xlarge  | g6e.8xlarge  | g6e.12xla 
rge  | g6e.16xlarge  | g6e.24xlarge  | g6e.48xlarge
G6f g6f.large  | g6f.xlarge  | g6f.2xlarge  | g6f.4xlarge
Gr6 gr6.4xlarge  | gr6.8xlarge
Gr6f gr6f.4xlarge
Instance families and instance types 522
Amazon EC2 Instance Types
Instance 
family
Available instance types
G7e g7e.2xlarge  | g7e.4xlarge  | g7e.8xlarge  | g7e.12xlarge  |
g7e.24xlarge  | g7e.48xlarge
Inf1 inf1.xlarge  | inf1.2xlarge  | inf1.6xlarge  | inf1.24xlarge
Inf2 inf2.xlarge  | inf2.8xlarge  | inf2.24xlarge  | inf2.48xlarge
P4d p4d.24xlarge
P4de p4de.24xlarge
P5 p5.4xlarge  | p5.48xlarge
P5e p5e.48xlarge
P5en p5en.48xlarge
P6-B200 p6-b200.48xlarge
P6-B300 p6-b300.48xlarge
P6e-
GB200
p6e-gb200.36xlarge
Trn1 trn1.2xlarge  | trn1.32xlarge
Trn1n trn1n.32xlarge
Trn2 trn2.3xlarge  | trn2.48xlarge
Trn2u trn2u.48xlarge
VT1 vt1.3xlarge  | vt1.6xlarge  | vt1.24xlarge
Instance families and instance types 523
Amazon EC2 Instance Types
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
DL1 Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
DL2q Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
F1 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
F2 Nitro v4 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
G4ad Nitro v3 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
G4dn Nitro v3 Intel 
(x86_64)
✓  Yes ✓  Yes ✓  Yes ✗  No Windows | 
Linux
G5 Nitro v3 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
G5g Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✗  No Linux
G6 Nitro v4 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
G6e Nitro v4 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Instance family summary 524
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
G6f Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
Gr6 Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
Gr6f Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
G7e Nitro v6 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
Inf1 Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
Inf2 Nitro v4 AMD 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
P4d Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
P4de Nitro v3 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
P5 Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows 
(p5.4xlarg 
e  only) | 
Linux 1
P5e Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
P5en Nitro v5 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
Instance family summary 525
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
P6-
B200
Nitro v6 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
P6-
B300
Nitro v6 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
P6e-
GB200
Nitro v5 NVIDIA 
Grace 
(arm64)
✗  No ✗  No ✗  No ✗  No Linux
Trn1 Nitro v4 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
Trn1n Nitro v4 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
Trn2 Nitro v5 Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Linux
Trn2u Nitro v5 Intel 
(x86_64)
✗  No ✗  No ✗  No ✗  No Linux
VT1 Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Linux
Note
1 p5.4xlarge supports both Windows and Linux operating systems. p5.48xlarge
supports Linux operating systems only.
Instance family summary 526
Amazon EC2 Instance Types
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
DL1
dl1.24xlarge 768.00 Intel Xeon 
P-8275CL
96 48 2 8 x Habana 
Gaudi 
HL-205 
GPU
256 
GiB (8 
x 32 
GiB)
DL2q
dl2q.24xlarge 768.00 Intel Xeon Cascade 
Lake
96 48 2 8 x 
Qualcomm 
Qualcomm 
AI100 
inference 
accelerator
125 
GiB (8 
x 15 
GiB)
F1
f1.2xlarge 122.00 Intel Xeon 
E5-2686v4
8 4 2 1 x Xilinx 
Virtex 
UltraScal 
e (VU9P) 
FPGA
64 
GiB (1 
x 64 
GiB)
f1.4xlarge 244.00 Intel Xeon 
E5-2686v4
16 8 2 2 x Xilinx 
Virtex 
UltraScal 
e (VU9P) 
FPGA
128 
GiB (2 
x 64 
GiB)
f1.16xlarge 976.00 Intel Xeon 
E5-2686v4
64 32 2 8 x Xilinx 
Virtex 
512 
GiB (8 
Performance speciﬁcations 527
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
UltraScal 
e (VU9P) 
FPGA
x 64 
GiB)
F2
f2.6xlarge 256.00 AMD EPYC 7R13 24 12 2 1 x Xilinx 
Virtex 
UltraScale
+ (VU47P) 
FPGA
80 
GiB (1 
x 80 
GiB)
f2.12xlarge 512.00 AMD EPYC 7R13 48 24 2 2 x Xilinx 
Virtex 
UltraScale
+ (VU47P) 
FPGA
160 
GiB (2 
x 80 
GiB)
f2.48xlarge 2048.00 AMD EPYC 7R13 192 96 2 8 x Xilinx 
Virtex 
UltraScale
+ (VU47P) 
FPGA
640 
GiB (8 
x 80 
GiB)
G4ad
g4ad.xlarge 16.00 2nd Gen AMD EPYC 
7R32
4 2 2 1 x AMD 
Radeon Pro 
V520 GPU
8 GiB 
(1 x 8 
GiB)
g4ad.2xlarge 32.00 2nd Gen AMD EPYC 
7R32
8 4 2 1 x AMD 
Radeon Pro 
V520 GPU
8 GiB 
(1 x 8 
GiB)
Performance speciﬁcations 528
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g4ad.4xlarge 64.00 2nd Gen AMD EPYC 
7R32
16 8 2 1 x AMD 
Radeon Pro 
V520 GPU
8 GiB 
(1 x 8 
GiB)
g4ad.8xlarge 128.00 2nd Gen AMD EPYC 
7R32
32 16 2 2 x AMD 
Radeon Pro 
V520 GPU
16 
GiB 
(2 x 8 
GiB)
g4ad.16xl 
arge
256.00 2nd Gen AMD EPYC 
7R32
64 32 2 4 x AMD 
Radeon Pro 
V520 GPU
32 
GiB 
(4 x 8 
GiB)
G4dn
g4dn.xlarge 16.00 Intel Xeon P-8259L 4 2 2 1 x NVIDIA 
T4 GPU
16 
GiB (1 
x 16 
GiB)
g4dn.2xlarge 32.00 Intel Xeon P-8259L 8 4 2 1 x NVIDIA 
T4 GPU
16 
GiB (1 
x 16 
GiB)
g4dn.4xlarge 64.00 Intel Xeon P-8259L 16 8 2 1 x NVIDIA 
T4 GPU
16 
GiB (1 
x 16 
GiB)
Performance speciﬁcations 529
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g4dn.8xlarge 128.00 Intel Xeon P-8259L 32 16 2 1 x NVIDIA 
T4 GPU
16 
GiB (1 
x 16 
GiB)
g4dn.12xl 
arge
192.00 Intel Xeon P-8259L 48 24 2 4 x NVIDIA 
T4 GPU
64 
GiB (4 
x 16 
GiB)
g4dn.16xl 
arge
256.00 Intel Xeon P-8259L 64 32 2 1 x NVIDIA 
T4 GPU
16 
GiB (1 
x 16 
GiB)
g4dn.metal 384.00 Intel Xeon P-8259L 96 48 2 8 x NVIDIA 
T4 GPU
128 
GiB (8 
x 16 
GiB)
G5
g5.xlarge 16.00 2nd Gen AMD EPYC 
7R32
4 2 2 1 x NVIDIA 
A10G GPU
22 
GiB (1 
x 22 
GiB)
g5.2xlarge 32.00 2nd Gen AMD EPYC 
7R32
8 4 2 1 x NVIDIA 
A10G GPU
22 
GiB (1 
x 22 
GiB)
Performance speciﬁcations 530
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g5.4xlarge 64.00 2nd Gen AMD EPYC 
7R32
16 8 2 1 x NVIDIA 
A10G GPU
22 
GiB (1 
x 22 
GiB)
g5.8xlarge 128.00 2nd Gen AMD EPYC 
7R32
32 16 2 1 x NVIDIA 
A10G GPU
22 
GiB (1 
x 22 
GiB)
g5.12xlarge 192.00 2nd Gen AMD EPYC 
7R32
48 24 2 4 x NVIDIA 
A10G GPU
89 
GiB (4 
x 22 
GiB)
g5.16xlarge 256.00 2nd Gen AMD EPYC 
7R32
64 32 2 1 x NVIDIA 
A10G GPU
22 
GiB (1 
x 22 
GiB)
g5.24xlarge 384.00 2nd Gen AMD EPYC 
7R32
96 48 2 4 x NVIDIA 
A10G GPU
89 
GiB (4 
x 22 
GiB)
g5.48xlarge 768.00 2nd Gen AMD EPYC 
7R32
192 96 2 8 x NVIDIA 
A10G GPU
178 
GiB (8 
x 22 
GiB)
G5g
Performance speciﬁcations 531
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g5g.xlarge 8.00 AWS Graviton2 
Processor
4 4 1 1 x NVIDIA 
T4g GPU
16 
GiB (1 
x 16 
GiB)
g5g.2xlarge 16.00 AWS Graviton2 
Processor
8 8 1 1 x NVIDIA 
T4g GPU
16 
GiB (1 
x 16 
GiB)
g5g.4xlarge 32.00 AWS Graviton2 
Processor
16 16 1 1 x NVIDIA 
T4g GPU
16 
GiB (1 
x 16 
GiB)
g5g.8xlarge 64.00 AWS Graviton2 
Processor
32 32 1 1 x NVIDIA 
T4g GPU
16 
GiB (1 
x 16 
GiB)
g5g.16xlarge 128.00 AWS Graviton2 
Processor
64 64 1 2 x NVIDIA 
T4g GPU
32 
GiB (2 
x 16 
GiB)
g5g.metal 128.00 AWS Graviton2 
Processor
64 64 1 2 x NVIDIA 
T4g GPU
32 
GiB (2 
x 16 
GiB)
G6
Performance speciﬁcations 532
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g6.xlarge 16.00 AMD EPYC 7R13 4 2 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
g6.2xlarge 32.00 AMD EPYC 7R13 8 4 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
g6.4xlarge 64.00 AMD EPYC 7R13 16 8 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
g6.8xlarge 128.00 AMD EPYC 7R13 32 16 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
g6.12xlarge 192.00 AMD EPYC 7R13 48 24 2 4 x NVIDIA 
L4 GPU
89 
GiB (4 
x 22 
GiB)
g6.16xlarge 256.00 AMD EPYC 7R13 64 32 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
g6.24xlarge 384.00 AMD EPYC 7R13 96 48 2 4 x NVIDIA 
L4 GPU
89 
GiB (4 
x 22 
GiB)
Performance speciﬁcations 533
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g6.48xlarge 768.00 AMD EPYC 7R13 192 96 2 8 x NVIDIA 
L4 GPU
178 
GiB (8 
x 22 
GiB)
G6e
g6e.xlarge 32.00 AMD EPYC 7R13 4 2 2 1 x NVIDIA 
L40S GPU
44 
GiB (1 
x 44 
GiB)
g6e.2xlarge 64.00 AMD EPYC 7R13 8 4 2 1 x NVIDIA 
L40S GPU
44 
GiB (1 
x 44 
GiB)
g6e.4xlarge 128.00 AMD EPYC 7R13 16 8 2 1 x NVIDIA 
L40S GPU
44 
GiB (1 
x 44 
GiB)
g6e.8xlarge 256.00 AMD EPYC 7R13 32 16 2 1 x NVIDIA 
L40S GPU
44 
GiB (1 
x 44 
GiB)
g6e.12xlarge 384.00 AMD EPYC 7R13 48 24 2 4 x NVIDIA 
L40S GPU
178 
GiB (4 
x 44 
GiB)
Performance speciﬁcations 534
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g6e.16xlarge 512.00 AMD EPYC 7R13 64 32 2 1 x NVIDIA 
L40S GPU
44 
GiB (1 
x 44 
GiB)
g6e.24xlarge 768.00 AMD EPYC 7R13 96 48 2 4 x NVIDIA 
L40S GPU
178 
GiB (4 
x 44 
GiB)
g6e.48xlarge 1536.00 AMD EPYC 7R13 192 96 2 8 x NVIDIA 
L40S GPU
357 
GiB (8 
x 44 
GiB)
G6f
g6f.large 8.00 AMD EPYC 7R13 2 1 2 0 x NVIDIA 
L4 GPU
2 GiB 
(0 x 2 
GiB)
g6f.xlarge 16.00 AMD EPYC 7R13 4 2 2 0 x NVIDIA 
L4 GPU
2 GiB 
(0 x 2 
GiB)
g6f.2xlarge 32.00 AMD EPYC 7R13 8 4 2 0 x NVIDIA 
L4 GPU
5 GiB 
(0 x 5 
GiB)
g6f.4xlarge 64.00 AMD EPYC 7R13 16 8 2 0 x NVIDIA 
L4 GPU
11 
GiB (0 
x 11 
GiB)
Gr6
Performance speciﬁcations 535
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
gr6.4xlarge 128.00 AMD EPYC 7R13 16 8 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
gr6.8xlarge 256.00 AMD EPYC 7R13 32 16 2 1 x NVIDIA 
L4 GPU
22 
GiB (1 
x 22 
GiB)
Gr6f
gr6f.4xlarge 128.00 AMD EPYC 7R13 16 8 2 0 x NVIDIA 
L4 GPU
11 
GiB (0 
x 11 
GiB)
G7e
g7e.2xlarge 64.00 Intel Xeon Emerald 
Rapids
8 4 2 1 x NVIDIA 
RTX PRO 
Server 6000 
GPU
96 
GiB (1 
x 96 
GiB)
g7e.4xlarge 128.00 Intel Xeon Emerald 
Rapids
16 8 2 1 x NVIDIA 
RTX PRO 
Server 6000 
GPU
96 
GiB (1 
x 96 
GiB)
g7e.8xlarge 256.00 Intel Xeon Emerald 
Rapids
32 16 2 1 x NVIDIA 
RTX PRO 
Server 6000 
GPU
96 
GiB (1 
x 96 
GiB)
Performance speciﬁcations 536
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
g7e.12xlarge 512.00 Intel Xeon Emerald 
Rapids
48 24 2 2 x NVIDIA 
RTX PRO 
Server 6000 
GPU
192 
GiB (2 
x 96 
GiB)
g7e.24xlarge 1024.00 Intel Xeon Emerald 
Rapids
96 48 2 4 x NVIDIA 
RTX PRO 
Server 6000 
GPU
384 
GiB (4 
x 96 
GiB)
g7e.48xlarge 2048.00 Intel Xeon Emerald 
Rapids
192 96 2 8 x NVIDIA 
RTX PRO 
Server 6000 
GPU
768 
GiB (8 
x 96 
GiB)
Inf1
inf1.xlarge 8.00 Intel Xeon P-8259L 4 2 2 1 x AWS 
Inferentia 
inference 
accelerator
8 GiB 
(1 x 8 
GiB)
inf1.2xlarge 16.00 Intel Xeon P-8259L 8 4 2 1 x AWS 
Inferentia 
inference 
accelerator
8 GiB 
(1 x 8 
GiB)
inf1.6xlarge 48.00 Intel Xeon P-8259L 24 12 2 4 x AWS 
Inferentia 
inference 
accelerator
32 
GiB 
(4 x 8 
GiB)
Performance speciﬁcations 537
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
inf1.24xlarge 192.00 Intel Xeon P-8259L 96 48 2 16 x AWS 
Inferentia 
inference 
accelerator
128 
GiB 
(16 x 
8 GiB)
Inf2
inf2.xlarge 16.00 AMD EPYC 7R13 4 2 2 1 x AWS 
Inferentia2 
inference 
accelerator
32 
GiB (1 
x 32 
GiB)
inf2.8xlarge 128.00 AMD EPYC 7R13 32 16 2 1 x AWS 
Inferentia2 
inference 
accelerator
32 
GiB (1 
x 32 
GiB)
inf2.24xlarge 384.00 AMD EPYC 7R13 96 48 2 6 x AWS 
Inferentia2 
inference 
accelerator
192 
GiB (6 
x 32 
GiB)
inf2.48xlarge 768.00 AMD EPYC 7R13 192 96 2 12 x AWS 
Inferentia2 
inference 
accelerator
384 
GiB 
(12 
x 32 
GiB)
P4d
p4d.24xlarge 1152.00 Intel Xeon Platinum 
8175
96 48 2 8 x NVIDIA 
A100 GPU
320 
GiB (8 
x 40 
GiB)
Performance speciﬁcations 538
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
P4de
p4de.24xl 
arge
1152.00 Intel Xeon Platinum 
8175
96 48 2 8 x NVIDIA 
A100 GPU
640 
GiB (8 
x 80 
GiB)
P5
p5.4xlarge 256.00 AMD EPYC 7R13 16 8 2 1 x NVIDIA 
H100 GPU
80 
GiB (1 
x 80 
GiB)
p5.48xlarge 2048.00 AMD EPYC 7R13 192 96 2 8 x NVIDIA 
H100 GPU
640 
GiB (8 
x 80 
GiB)
P5e
p5e.48xlarge 2048.00 AMD EPYC 7R13 192 96 2 8 x NVIDIA 
H200 GPU
1128 
GiB (8 
x 141 
GiB)
P5en
p5en.48xl 
arge
2048.00 Intel Xeon Sapphire 
Rapids
192 96 2 8 x NVIDIA 
H200 GPU
1128 
GiB (8 
x 141 
GiB)
P6-B200
Performance speciﬁcations 539
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
p6-b200.4 
8xlarge
2048.00 Intel Xeon Emerald 
Rapids
192 96 2 8 x NVIDIA 
B200 GPU
1432 
GiB (8 
x 179 
GiB)
P6-B300
p6-b300.4 
8xlarge
4096.00 Intel Xeon Emerald 
Rapids
192 96 2 8 x NVIDIA 
B300 GPU
2148 
GiB (8 
x 268 
GiB)
P6e-GB200
p6e-gb200 
.36xlarge
960.00 Nvidia Grace CPU 144 144 1 4 x NVIDIA 
B200 GPU
740 
GiB (4 
x 185 
GiB)
Trn1
trn1.2xlarge 32.00 Intel Xeon Ice Lake 
8375C
8 4 2 1 x AWS 
Trainium 
accelerators
32 
GiB (1 
x 32 
GiB)
trn1.32xlarge 512.00 Intel Xeon Ice Lake 
8375C
128 64 2 16 x AWS 
Trainium 
accelerators
512 
GiB 
(16 
x 32 
GiB)
Trn1n
Performance speciﬁcations 540
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
trn1n.32x 
large
512.00 Intel Xeon Ice Lake 128 64 2 16 x AWS 
Trainium 
accelerators
512 
GiB 
(16 
x 32 
GiB)
Trn2
trn2.3xlarge 128.00 Intel Xeon Sapphire 
Rapids
12 6 2 1 x AWS 
Trainium2 
accelerators
512 
GiB (1 
x 512 
GiB)
trn2.48xlarge 2048.00 Intel Xeon Sapphire 
Rapids
192 96 2 16 x AWS 
Trainium2 
accelerators
8192 
GiB 
(16 x 
512 
GiB)
Trn2u
trn2u.48x 
large
2048.00 Intel Xeon Sapphire 
Rapids
192 96 2 ✗  No ✗  No
VT1
vt1.3xlarge 24.00 Intel Cascade Lake 
P-8259CL
12 6 2 1 x Xilinx 
U30 media 
accelerator
24 
GiB (1 
x 24 
GiB)
vt1.6xlarge 48.00 Intel Cascade Lake 
P-8259CL
24 12 2 2 x Xilinx 
U30 media 
accelerator
48 
GiB (2 
x 24 
GiB)
Performance speciﬁcations 541
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
vt1.24xlarge 192.00 Intel Cascade Lake 
P-8259CL
96 48 2 8 x Xilinx 
U30 media 
accelerator
192 
GiB (8 
x 24 
GiB)
Network speciﬁcations
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
DL1
dl1.24xlarge 4x 100 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 4 60 50 ✓ 
Yes
DL2q
dl2q.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
F1
f1.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
f1.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
f1.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 50 ✓ 
Yes
F2
Network speciﬁcations 542
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
f2.6xlarge 12.5 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
f2.12xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
f2.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
G4ad
g4ad.xlarge 1 2.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
g4ad.2xlarge 1 4.167 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
g4ad.4xlarge 1 8.333 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
g4ad.8xlarge 15 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g4ad.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
G4dn
g4dn.xlarge 1 5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
g4dn.2xlarge
1
10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 543
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
g4dn.4xlarge
1
20.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
g4dn.8xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g4dn.12xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g4dn.16xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g4dn.metal 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
G5
g5.xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g5.2xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g5.4xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g5.8xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g5.12xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g5.16xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 544
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
g5.24xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g5.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 7 50 ✓ 
Yes
G5g
g5g.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g5g.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g5g.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g5g.8xlarge 12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g5g.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g5g.metal 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
G6
g6.xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g6.2xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 545
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
g6.4xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g6.8xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g6.12xlarge 40 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g6.16xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g6.24xlarge 50 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g6.48xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 15 50 ✓ 
Yes
G6e
g6e.xlarge 1 2.5 / 20.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g6e.2xlarge 1 5.0 / 20.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g6e.4xlarge 20 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g6e.8xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g6e.12xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 10 30 ✓ 
Yes
Network speciﬁcations 546
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
g6e.16xlarge 35 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
g6e.24xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 20 50 ✓ 
Yes
g6e.48xlarge 400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 4 40 50 ✓ 
Yes
G6f
g6f.large 1 1.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 10 ✓ 
Yes
g6f.xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g6f.2xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
g6f.4xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Gr6
gr6.4xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
gr6.8xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Gr6f
gr6f.4xlarge 1 10.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 547
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
G7e
g7e.2xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 64 ✓ 
Yes
g7e.4xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 64 ✓ 
Yes
g7e.8xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 8 64 ✓ 
Yes
g7e.12xlarge 400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 10 64 ✓ 
Yes
g7e.24xlarge 800 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 2 20 64 ✓ 
Yes
g7e.48xlarge 1600 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 4 40 64 ✓ 
Yes
Inf1
inf1.xlarge 1 5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 10 ✓ 
Yes
inf1.2xlarge 1 5.0 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 4 10 ✓ 
Yes
inf1.6xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
inf1.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 11 30 ✓ 
Yes
Inf2
Network speciﬁcations 548
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
inf2.xlarge 1 2.083 / 15.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
inf2.8xlarge 1 16.667 / 25.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
inf2.24xlarge 50 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
inf2.48xlarge 100 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
P4d
p4d.24xlarge 4x 100 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 4 60 50 ✓ 
Yes
P4de
p4de.24xlarge 4x 100 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 4 60 50 ✓ 
Yes
P5
p5.4xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 1 4 30 ✓ 
Yes
p5.48xlarge 3200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 32 64 50 ✓ 
Yes
P5e
p5e.48xlarge 3200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 32 64 50 ✓ 
Yes
Network speciﬁcations 549
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
P5en
p5en.48xlarge 3200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 16 64 50 ✓ 
Yes
P6-B200
p6-b200.4 
8xlarge
3200 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 8 32 50 ✓ 
Yes
P6-B300
p6-b300.4 
8xlarge
6400 Gigabit ✓ 
Yes
✓ 
Yes
✓  Yes 17 68 50 ✓ 
Yes
P6e-GB200
p6e-gb200 
.36xlarge
3200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 17 39 50 ✓ 
Yes
Trn1
trn1.2xlarge 1 3.125 / 12.5 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
trn1.32xlarge 8x 100 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 8 40 50 ✓ 
Yes
Trn1n
trn1n.32x 
large
16x 100 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 16 80 50 ✓ 
Yes
Trn2
Network speciﬁcations 550
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
trn2.3xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 2 15 ✓ 
Yes
trn2.48xlarge 16x 200 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 16 32 50 ✓ 
Yes
Trn2u
trn2u.48x 
large
16x 200 
Gigabit
✓ 
Yes
✓ 
Yes
✗  No 16 32 50 ✓ 
Yes
VT1
vt1.3xlarge 3.12 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
vt1.6xlarge 6.25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
vt1.24xlarge 25 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
Network speciﬁcations 551
Amazon EC2 Instance Types
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
DL1
dl1.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 28 
(Shared 
limit)
DL2q
Amazon EBS speciﬁcations 552
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
dl2q.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 19 
(Shared 
limit)
F1
f1.2xlarge 1700.00 212.50 12000.00 ✗  No ✗  No Up to 26 
(Xen-based 
limit)
f1.4xlarge 3500.00 437.50 44000.00 ✗  No ✗  No Up to 25 
(Xen-based 
limit)
f1.16xlar 
ge
14000.00 1750.00 75000.00 ✗  No ✗  No Up to 19 
(Xen-based 
limit)
F2
f2.6xlarge 7500.00 937.50 30000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
f2.12xlar 
ge
15000.00 1875.00 60000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
f2.48xlar 
ge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
Amazon EBS speciﬁcations 553
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
G4ad
g4ad.xlar 
ge 1
400.00 / 
3170.00
50.00 / 
396.25
1700.00 / 
13333.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4ad.2xla 
rge 1
800.00 / 
3170.00
100.00 / 
396.25
3400.00 / 
13333.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4ad.4xla 
rge 1
1580.00 / 
3170.00
197.50 / 
396.25
6700.00 / 
13333.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4ad.8xla 
rge
3170.00 396.25 13333.00 ✓  Yes ✗  No Up to 24 
(Shared 
limit)
g4ad.16xl 
arge
6300.00 787.50 26667.00 ✓  Yes ✗  No Up to 21 
(Shared 
limit)
G4dn
g4dn.xlar 
ge 1
950.00 / 
3500.00
118.75 / 
437.50
3000.00 / 
20000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4dn.2xla 
rge 1
1150.00 / 
3500.00
143.75 / 
437.50
6000.00 / 
20000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 554
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g4dn.4xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4dn.8xla 
rge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4dn.12xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 22 
(Shared 
limit)
g4dn.16xl 
arge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g4dn.meta 
l
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
G5
g5.xlarge 1 700.00 / 
3500.00
87.50 / 
437.50
3000.00 / 
15000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
g5.2xlarge
1
850.00 / 
3500.00
106.25 / 
437.50
3500.00 / 
15000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
Amazon EBS speciﬁcations 555
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g5.4xlarge 4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g5.8xlarge 16000.00 2000.00 65000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g5.12xlar 
ge
16000.00 2000.00 65000.00 ✓  Yes ✗  No Up to 22 
(Shared 
limit)
g5.16xlar 
ge
16000.00 2000.00 65000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g5.24xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 22 
(Shared 
limit)
g5.48xlar 
ge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 9 
(Shared 
limit)
G5g
g5g.xlarge
1
1188.00 / 
4750.00
148.50 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 556
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g5g.2xlar 
ge 1
2375.00 / 
4750.00
296.88 / 
593.75
12000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
g5g.4xlar 
ge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
g5g.8xlar 
ge
9500.00 1187.50 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
g5g.16xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 25 
(Shared 
limit)
g5g.metal 19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
G6
g6.xlarge 1 1000.00 / 
5000.00
125.00 / 
625.00
4000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g6.2xlarge
1
2000.00 / 
5000.00
250.00 / 
625.00
8000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 557
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g6.4xlarge 8000.00 1000.00 32000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6.8xlarge 16000.00 2000.00 64000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6.12xlar 
ge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6.16xlar 
ge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
g6.24xlar 
ge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
g6.48xlar 
ge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
G6e
g6e.xlarge
1
1000.00 / 
5000.00
125.00 / 
625.00
4000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 558
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g6e.2xlar 
ge 1
2000.00 / 
5000.00
250.00 / 
625.00
8000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g6e.4xlar 
ge
8000.00 1000.00 32000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6e.8xlar 
ge
16000.00 2000.00 64000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6e.12xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g6e.16xla 
rge
20000.00 2500.00 80000.00 ✓  Yes ✗  No 48 
(Dedicated 
limit)
g6e.24xla 
rge
30000.00 3750.00 120000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
g6e.48xla 
rge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
G6f
Amazon EBS speciﬁcations 559
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
g6f.large 1 936.00 / 
5000.00
117.00 / 
625.00
3750.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g6f.xlarge
1
1000.00 / 
5000.00
125.00 / 
625.00
4000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g6f.2xlarge
1
2000.00 / 
5000.00
250.00 / 
625.00
8000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g6f.4xlarge 6000.00 750.00 24000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Gr6
gr6.4xlar 
ge
8000.00 1000.00 32000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
gr6.8xlar 
ge
16000.00 2000.00 64000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Gr6f
gr6f.4xla 
rge
8000.00 1000.00 32000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
Amazon EBS speciﬁcations 560
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
G7e
g7e.2xlar 
ge 1
2000.00 / 
5000.00
250.00 / 
625.00
8000.00 / 
20000.00
✓  Yes ✗  No 32 
(Dedicated 
limit)
g7e.4xlar 
ge
8000.00 1000.00 32000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g7e.8xlar 
ge
16000.00 2000.00 64000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g7e.12xla 
rge
25000.00 3125.00 100000.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
g7e.24xla 
rge
50000.00 6250.00 200000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
g7e.48xla 
rge
100000.00 12500.00 400000.00 ✓  Yes ✗  No 128 
(Dedicated 
limit)
Inf1
inf1.xlarge
1
1190.00 / 
4750.00
148.75 / 
593.75
4000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
Amazon EBS speciﬁcations 561
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
inf1.2xla 
rge 1
1190.00 / 
4750.00
148.75 / 
593.75
6000.00 / 
20000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
inf1.6xla 
rge
4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
inf1.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 11 
(Shared 
limit)
Inf2
inf2.xlarge
1
1250.00 / 
10000.00
156.25 / 
1250.00
6000.00 / 
40000.00
✓  Yes ✗  No Up to 26 
(Shared 
limit)
inf2.8xla 
rge
10000.00 1250.00 40000.00 ✓  Yes ✗  No Up to 26 
(Shared 
limit)
inf2.24xl 
arge
30000.00 3750.00 120000.00 ✓  Yes ✗  No Up to 28 
(Shared 
limit)
inf2.48xl 
arge
60000.00 7500.00 240000.00 ✓  Yes ✗  No Up to 28 
(Shared 
limit)
P4d
Amazon EBS speciﬁcations 562
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
p4d.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No 28 
(Dedicated 
limit)
P4de
p4de.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No 28 
(Dedicated 
limit)
P5
p5.4xlarge 10000.00 1250.00 32500.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
p5.48xlar 
ge
80000.00 10000.00 260000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
P5e
p5e.48xla 
rge
80000.00 10000.00 260000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
P5en
p5en.48xl 
arge
100000.00 12500.00 400000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Amazon EBS speciﬁcations 563
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
P6-B200
p6-b200.4 
8xlarge
100000.00 12500.00 400000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
P6-B300
p6-b300.4 
8xlarge
100000.00 12500.00 400000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
P6e-GB200
p6e-gb200 
.36xlarge
60000.00 7500.00 240000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Trn1
trn1.2xla 
rge 1
5000.00 / 
20000.00
625.00 / 
2500.00
16250.00 / 
65000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
trn1.32xl 
arge
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 28 
(Shared 
limit)
Trn1n
Amazon EBS speciﬁcations 564
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
trn1n.32x 
large
80000.00 10000.00 260000.00 ✓  Yes ✗  No Up to 28 
(Shared 
limit)
Trn2
trn2.3xla 
rge
5000.00 625.00 16250.00 ✓  Yes ✗  No 32 
(Dedicated 
limit)
trn2.48xl 
arge
80000.00 10000.00 260000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
Trn2u
trn2u.48x 
large
80000.00 10000.00 260000.00 ✓  Yes ✗  No 64 
(Dedicated 
limit)
VT1
vt1.3xlarge
1
2375.00 / 
4750.00
296.88 / 
593.75
10000.00 / 
20000.00
✓  Yes ✗  No Up to 25 
(Shared 
limit)
vt1.6xlarge 4750.00 593.75 20000.00 ✓  Yes ✗  No Up to 23 
(Shared 
limit)
Amazon EBS speciﬁcations 565
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
vt1.24xla 
rge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
DL1
dl1.24xlarge 4 x 1000 GB NVMe 
SSD
1,000,000 / 
800,000
✓  Yes
F1
f1.2xlarge 1 x 470 GB NVMe 
SSD
  ✓  Yes
Instance store speciﬁcations 566
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
f1.4xlarge 1 x 940 GB NVMe 
SSD
  ✓  Yes
f1.16xlarge 4 x 940 GB NVMe 
SSD
  ✓  Yes
F2
f2.6xlarge 1 x 940 GB NVMe 
SSD
400,000 / 125,000 ✓  Yes
f2.12xlarge 2 x 940 GB NVMe 
SSD
800,000 / 250,000 ✓  Yes
f2.48xlarge 8 x 940 GB NVMe 
SSD
3,200,000 / 
1,000,000
✓  Yes
G4ad
g4ad.xlarge 1 x 150 GB NVMe 
SSD
10,417 / 8,333 ✓  Yes
g4ad.2xlarge 1 x 300 GB NVMe 
SSD
20,833 / 16,667 ✓  Yes
g4ad.4xlarge 1 x 600 GB NVMe 
SSD
41,667 / 33,333 ✓  Yes
g4ad.8xlarge 1 x 1200 GB NVMe 
SSD
83,333 / 66,667 ✓  Yes
g4ad.16xlarge 2 x 1200 GB NVMe 
SSD
166,666 / 133,332 ✓  Yes
G4dn
Instance store speciﬁcations 567
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
g4dn.xlarge 1 x 125 GB NVMe 
SSD
42,500 / 32,500 ✓  Yes
g4dn.2xlarge 1 x 225 GB NVMe 
SSD
42,500 / 32,500 ✓  Yes
g4dn.4xlarge 1 x 225 GB NVMe 
SSD
85,000 / 65,000 ✓  Yes
g4dn.8xlarge 1 x 900 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
g4dn.12xlarge 1 x 900 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
g4dn.16xlarge 1 x 900 GB NVMe 
SSD
250,000 / 200,000 ✓  Yes
g4dn.metal 2 x 900 GB NVMe 
SSD
500,000 / 400,000 ✓  Yes
G5
g5.xlarge 1 x 250 GB NVMe 
SSD
40,625 / 20,313 ✓  Yes
g5.2xlarge 1 x 450 GB NVMe 
SSD
40,625 / 20,313 ✓  Yes
g5.4xlarge 1 x 600 GB NVMe 
SSD
125,000 / 62,500 ✓  Yes
g5.8xlarge 1 x 900 GB NVMe 
SSD
250,000 / 125,000 ✓  Yes
Instance store speciﬁcations 568
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
g5.12xlarge 1 x 3800 GB NVMe 
SSD
312,500 / 156,250 ✓  Yes
g5.16xlarge 1 x 1900 GB NVMe 
SSD
250,000 / 125,000 ✓  Yes
g5.24xlarge 1 x 3800 GB NVMe 
SSD
312,500 / 156,250 ✓  Yes
g5.48xlarge 2 x 3800 GB NVMe 
SSD
625,000 / 312,500 ✓  Yes
G6
g6.xlarge 1 x 250 GB NVMe 
SSD
40,625 / 20,000 ✓  Yes
g6.2xlarge 1 x 450 GB NVMe 
SSD
40,625 / 20,000 ✓  Yes
g6.4xlarge 1 x 600 GB NVMe 
SSD
125,000 / 40,000 ✓  Yes
g6.8xlarge 2 x 450 GB NVMe 
SSD
250,000 / 80,000 ✓  Yes
g6.12xlarge 4 x 940 GB NVMe 
SSD
312,500 / 125,000 ✓  Yes
g6.16xlarge 2 x 940 GB NVMe 
SSD
250,000 / 80,000 ✓  Yes
g6.24xlarge 4 x 940 GB NVMe 
SSD
312,500 / 156,248 ✓  Yes
Instance store speciﬁcations 569
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
g6.48xlarge 8 x 940 GB NVMe 
SSD
625,000 / 312,496 ✓  Yes
G6e
g6e.xlarge 1 x 250 GB NVMe 
SSD
40,625 / 20,000 ✓  Yes
g6e.2xlarge 1 x 450 GB NVMe 
SSD
40,625 / 20,000 ✓  Yes
g6e.4xlarge 1 x 600 GB NVMe 
SSD
125,000 / 40,000 ✓  Yes
g6e.8xlarge 2 x 450 GB NVMe 
SSD
250,000 / 80,000 ✓  Yes
g6e.12xlarge 2 x 1900 GB NVMe 
SSD
312,500 / 125,000 ✓  Yes
g6e.16xlarge 2 x 950 GB NVMe 
SSD
250,000 / 80,000 ✓  Yes
g6e.24xlarge 2 x 1900 GB NVMe 
SSD
312,500 / 156,250 ✓  Yes
g6e.48xlarge 4 x 1900 GB NVMe 
SSD
625,000 / 312,500 ✓  Yes
G6f
g6f.large 1 x 100 GB NVMe 
SSD
16,250 / 8,000 ✓  Yes
g6f.xlarge 1 x 100 GB NVMe 
SSD
27,100 / 13,333 ✓  Yes
Instance store speciﬁcations 570
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
g6f.2xlarge 1 x 200 GB NVMe 
SSD
40,625 / 20,000 ✓  Yes
g6f.4xlarge 1 x 450 GB NVMe 
SSD
125,000 / 40,000 ✓  Yes
Gr6
gr6.4xlarge 1 x 600 GB NVMe 
SSD
125,000 / 40,000 ✓  Yes
gr6.8xlarge 2 x 450 GB NVMe 
SSD
250,000 / 80,000 ✓  Yes
Gr6f
gr6f.4xlarge 1 x 450 GB NVMe 
SSD
125,000 / 40,000 ✓  Yes
G7e
g7e.2xlarge 1 x 1900 GB NVMe 
SSD
275,000 / 137,500 ✓  Yes
g7e.4xlarge 1 x 1900 GB NVMe 
SSD
275,000 / 137,500 ✓  Yes
g7e.8xlarge 1 x 1900 GB NVMe 
SSD
275,000 / 137,500 ✓  Yes
g7e.12xlarge 1 x 3800 GB NVMe 
SSD
550,000 / 275,000 ✓  Yes
g7e.24xlarge 2 x 3800 GB NVMe 
SSD
1,100,000 / 
550,000
✓  Yes
Instance store speciﬁcations 571
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
g7e.48xlarge 4 x 3800 GB NVMe 
SSD
2,200,000 / 
1,100,000
✓  Yes
P4d
p4d.24xlarge 8 x 1000 GB NVMe 
SSD
2,000,000 / 
1,600,000
✓  Yes
P4de
p4de.24xlarge 8 x 1000 GB NVMe 
SSD
2,000,000 / 
1,600,000
✓  Yes
P5
p5.4xlarge 1 x 3800 GB NVMe 
SSD
550,000 / 275,000 ✓  Yes
p5.48xlarge 8 x 3800 GB NVMe 
SSD
4,400,000 / 
2,200,000
✓  Yes
P5e
p5e.48xlarge 8 x 3800 GB NVMe 
SSD
4,400,000 / 
2,200,000
✓  Yes
P5en
p5en.48xlarge 8 x 3800 GB NVMe 
SSD
4,400,000 / 
2,200,000
✓  Yes
P6-B200
p6-b200.4 
8xlarge
8 x 3800 GB NVMe 
SSD
4,400,000 / 
2,200,000
✓  Yes
Instance store speciﬁcations 572
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
P6-B300
p6-b300.4 
8xlarge
8 x 3800 GB NVMe 
SSD
4,400,000 / 
2,200,000
✓  Yes
P6e-GB200
p6e-gb200 
.36xlarge
3 x 7500 GB NVMe 
SSD
2,550,000 / 
2,400,000
✓  Yes
Trn1
trn1.2xlarge 1 x 474 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
trn1.32xlarge 4 x 1900 GB NVMe 
SSD
1,720,000 / 
720,000
✓  Yes
Trn1n
trn1n.32xlarge 4 x 1900 GB NVMe 
SSD
1,720,000 / 
720,000
✓  Yes
Trn2
trn2.3xlarge 1 x 470 GB NVMe 
SSD
107,500 / 45,000 ✓  Yes
trn2.48xlarge 4 x 1900 GB NVMe 
SSD
1,720,000 / 
720,000
✓  Yes
Trn2u
trn2u.48xlarge 4 x 1900 GB NVMe 
SSD
1,720,000 / 
720,000
✓  Yes
Instance store speciﬁcations 573
Amazon EC2 Instance Types
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
DL1
dl1.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
DL2q
dl2q.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✓  Yes
F1
f1.2xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
f1.4xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
f1.16xlarge ✓  Yes ✓  Yes ✗  No ✗  No ✗  No ✗  No
F2
f2.6xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
f2.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
f2.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
G4ad
g4ad.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 574
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
g4ad.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
g4ad.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
g4ad.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
g4ad.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
G4dn
g4dn.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g4dn.metal ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
G5
g5.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 575
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
g5.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g5.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
G5g
g5g.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g5g.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g5g.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g5g.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g5g.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g5g.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
G6
g6.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 576
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
g6.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
G6e
g6e.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.16xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6e.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
G6f
g6f.large ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
g6f.xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 577
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
g6f.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g6f.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Gr6
gr6.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
gr6.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Gr6f
gr6f.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
G7e
g7e.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g7e.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g7e.8xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g7e.12xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g7e.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
g7e.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Inf1
inf1.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Security speciﬁcations 578
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
inf1.2xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
inf1.6xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
inf1.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
Inf2
inf2.xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
inf2.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
inf2.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
inf2.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✓  Yes
P4d
p4d.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
Security speciﬁcations 579
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
P4de
p4de.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
P5
p5.4xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
p5.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
P5e
p5e.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
P5en
p5en.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
P6-B200
p6-b200.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
P6-B300
p6-b300.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
P6e-GB200
p6e-gb200 
.36xlarge
✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Trn1
trn1.2xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
trn1.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 580
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
Trn1n
trn1n.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✗  No
Trn2
trn2.3xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
trn2.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
Trn2u
trn2u.48xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✓  Yes
VT1
vt1.3xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
vt1.6xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
vt1.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Speciﬁcations for Amazon EC2 high-performance computing 
instances
High-performance computing instances are purpose built to oﬀer the best price performance 
for running HPC workloads at scale on AWS. These instances are ideal for applications that 
High-performance computing 581
Amazon EC2 Instance Types
beneﬁt from high-performance processors, such as large, complex simulations and deep learning 
workloads.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Instance families and instance types
Instance 
family
Available instance types
Hpc6a hpc6a.48xlarge
Hpc6id hpc6id.32xlarge
Hpc7a hpc7a.12xlarge  | hpc7a.24xlarge  | hpc7a.48xlarge  | hpc7a.96x 
large
Hpc7g hpc7g.4xlarge  | hpc7g.8xlarge  | hpc7g.16xlarge
Hpc8a hpc8a.96xlarge
Instance families and instance types 582
Amazon EC2 Instance Types
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
Hpc6a Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✗  No ✗  No Linux
Hpc6id Nitro v4 Intel 
(x86_64)
✗  No ✗  No ✗  No ✗  No Windows | 
Linux
Hpc7a Nitro v4 AMD 
(x86_64)
✗  No ✗  No ✗  No ✗  No Windows | 
Linux
Hpc7g Nitro v5 AWS 
Graviton 
(arm64)
✗  No ✗  No ✗  No ✗  No Linux
Hpc8a Nitro v6 AMD 
(x86_64)
✗  No ✗  No ✗  No ✗  No Windows | 
Linux
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
Hpc6a
hpc6a.48x 
large
384.00 AMD EPYC 7R13 96 96 1 ✗  No ✗  No
Hpc6id
Instance family summary 583
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
hpc6id.32 
xlarge
1024.00 Intel Xeon Ice Lake 64 64 1 ✗  No ✗  No
Hpc7a
hpc7a.12x 
large
768.00 AMD EPYC 9R14 24 24 1 ✗  No ✗  No
hpc7a.24x 
large
768.00 AMD EPYC 9R14 48 48 1 ✗  No ✗  No
hpc7a.48x 
large
768.00 AMD EPYC 9R14 96 96 1 ✗  No ✗  No
hpc7a.96x 
large
768.00 AMD EPYC 9R14 192 192 1 ✗  No ✗  No
Hpc7g
hpc7g.4xl 
arge
128.00 AWS Graviton3E 
Processor
16 16 1 ✗  No ✗  No
hpc7g.8xl 
arge
128.00 AWS Graviton3E 
Processor
32 32 1 ✗  No ✗  No
hpc7g.16x 
large
128.00 AWS Graviton3E 
Processor
64 64 1 ✗  No ✗  No
Hpc8a
hpc8a.96x 
large
768.00 AMD EPYC 9R45 192 192 1 ✗  No ✗  No
Performance speciﬁcations 584
Amazon EC2 Instance Types
Network speciﬁcations
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
Hpc6a
hpc6a.48x 
large
100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 2 50 ✓ 
Yes
Hpc6id
hpc6id.32 
xlarge
200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 2 50 ✓ 
Yes
Hpc7a
hpc7a.12x 
large
300 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 4 50 ✓ 
Yes
hpc7a.24x 
large
300 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 4 50 ✓ 
Yes
hpc7a.48x 
large
300 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 4 50 ✓ 
Yes
hpc7a.96x 
large
300 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 4 50 ✓ 
Yes
Hpc7g
hpc7g.4xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 4 50 ✓ 
Yes
hpc7g.8xlarge 200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 4 50 ✓ 
Yes
Network speciﬁcations 585
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
hpc7g.16x 
large
200 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 4 50 ✓ 
Yes
Hpc8a
hpc8a.96x 
large
300 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 2 4 50 ✓ 
Yes
Note
For hpc6id.32xlarge, you must attach at least 2 ENIs, to separate network cards, to 
achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 170 
Gbps.
For hpc7a.12xlarge, hpc7a.24xlarge, hpc7a.48xlarge, hpc7a.96xlarge, you 
must attach at least 2 ENIs, to separate network cards, to achieve 300 Gbps throughput. 
Each ENI attached to a network card can achieve up to 150 Gbps.
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
Amazon EBS speciﬁcations 586
Amazon EC2 Instance Types
combined performance equal to or greater than the maximum instance performance. For 
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
Hpc6a
hpc6a.48x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Hpc6id
hpc6id.32 
xlarge 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No Up to 23 
(Shared 
limit)
Hpc7a
hpc7a.12x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No 27 
(Dedicated 
limit)
hpc7a.24x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No 27 
(Dedicated 
limit)
Amazon EBS speciﬁcations 587
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
hpc7a.48x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No 27 
(Dedicated 
limit)
hpc7a.96x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No 27 
(Dedicated 
limit)
Hpc7g
hpc7g.4xl 
arge 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
hpc7g.8xl 
arge 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
hpc7g.16x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
Hpc8a
hpc8a.96x 
large 1
87.00 / 
2085.00
10.88 / 
260.62
500.00 / 
11000.00
✓  Yes ✗  No 27 
(Dedicated 
limit)
Amazon EBS speciﬁcations 588
Amazon EC2 Instance Types
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
Instance store speciﬁcations
The following table shows the instance store volume conﬁguration for supported instance types, 
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
Hpc6id
hpc6id.32xlarge 4 x 3800 GB NVMe 
SSD
2,146,664 / 
1,073,336
✓  Yes
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
Hpc6a
hpc6a.48xlarge ✓  Yes Instance 
store not 
✓  Yes ✗  No ✓  Yes ✗  No
Instance store speciﬁcations 589
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
supported
Hpc6id
hpc6id.32xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✓  Yes ✗  No
Hpc7a
hpc7a.12xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
hpc7a.24xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
hpc7a.48xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
hpc7a.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Hpc7g
hpc7g.4xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
hpc7g.8xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Security speciﬁcations 590
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
hpc7g.16xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✗  No ✗  No
Hpc8a
hpc8a.96xlarge ✓  Yes Instance 
store not 
supported
✓  Yes ✗  No ✓  Yes ✗  No
Speciﬁcations for Amazon EC2 previous generation instances
AWS oﬀers previous generation instance types for users who have optimized their applications 
around them and have yet to upgrade. We encourage you to use current generation instance 
types to get the best performance, but we continue to support the following previous generation 
instance types.
Contents
• Instance families and instance types
• Instance family summary
• Performance speciﬁcations
• Network speciﬁcations
• Amazon EBS speciﬁcations
• Instance store speciﬁcations
• Security speciﬁcations
Pricing
For pricing information, see Amazon EC2 On-Demand Pricing.
Previous generation 591
Amazon EC2 Instance Types
Instance families and instance types
Instance 
family
Available instance types
A1 a1.medium  | a1.large | a1.xlarge  | a1.2xlarge  | a1.4xlarge  |
a1.metal
C1 c1.medium  | c1.xlarge
C3 c3.large | c3.xlarge  | c3.2xlarge  | c3.4xlarge  | c3.8xlarge
C4 c4.large | c4.xlarge  | c4.2xlarge  | c4.4xlarge  | c4.8xlarge
G3 g3.4xlarge  | g3.8xlarge  | g3.16xlarge
I2 i2.xlarge  | i2.2xlarge  | i2.4xlarge  | i2.8xlarge
M1 m1.small | m1.medium  | m1.large | m1.xlarge
M2 m2.xlarge  | m2.2xlarge  | m2.4xlarge
M3 m3.medium  | m3.large | m3.xlarge  | m3.2xlarge
M4 m4.large | m4.xlarge  | m4.2xlarge  | m4.4xlarge  | m4.10xlarge  |
m4.16xlarge
P2 p2.xlarge  | p2.8xlarge  | p2.16xlarge
P3 p3.2xlarge  | p3.8xlarge  | p3.16xlarge
P3dn p3dn.24xlarge
R3 r3.large | r3.xlarge  | r3.2xlarge  | r3.4xlarge  | r3.8xlarge
R4 r4.large | r4.xlarge  | r4.2xlarge  | r4.4xlarge  | r4.8xlarge  |
r4.16xlarge
T1 t1.micro
Instance families and instance types 592
Amazon EC2 Instance Types
Instance family summary
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
A1 Nitro v2 AWS 
Graviton 
(arm64)
✓  Yes ✓  Yes ✓  Yes ✗  No Linux
C1 Xen Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
C3 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
C4 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
G3 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
I2 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
M1 Xen Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
M2 Xen Intel 
(x86_64)
✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
M3 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
M4 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
Instance family summary 593
Amazon EC2 Instance Types
Instance 
family
Hyperviso 
r
Processor 
type 
(architec 
ture)
Metal 
instances 
available
Dedicated 
Hosts 
support
Spot 
support
Hibernati 
on 
support
Supported 
operating 
systems
P2 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
P3 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
P3dn Nitro v3 Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✗  No Windows | 
Linux
R3 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
R4 Xen Intel 
(x86_64)
✗  No ✓  Yes ✓  Yes ✓  Yes Windows | 
Linux
T1 Xen Intel (i386) ✗  No ✗  No ✓  Yes ✗  No Windows | 
Linux
Performance speciﬁcations
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
A1
a1.medium 2.00 AWS Graviton 
Processor
1 1 1 ✗  No ✗  No
a1.large 4.00 AWS Graviton 
Processor
2 2 1 ✗  No ✗  No
Performance speciﬁcations 594
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
a1.xlarge 8.00 AWS Graviton 
Processor
4 4 1 ✗  No ✗  No
a1.2xlarge 16.00 AWS Graviton 
Processor
8 8 1 ✗  No ✗  No
a1.4xlarge 32.00 AWS Graviton 
Processor
16 16 1 ✗  No ✗  No
a1.metal 32.00 AWS Graviton 
Processor
16 16 1 ✗  No ✗  No
C1
c1.medium 1.70 Intel Xeon Family 2 2 1 ✗  No ✗  No
c1.xlarge 7.00 Intel Xeon Family 8 8 1 ✗  No ✗  No
C3
c3.large 3.75 Intel Xeon 
E5-2680v2
2 1 2 ✗  No ✗  No
c3.xlarge 7.50 Intel Xeon 
E5-2680v2
4 2 2 ✗  No ✗  No
c3.2xlarge 15.00 Intel Xeon 
E5-2680v2
8 4 2 ✗  No ✗  No
c3.4xlarge 30.00 Intel Xeon 
E5-2680v2
16 8 2 ✗  No ✗  No
c3.8xlarge 60.00 Intel Xeon 
E5-2680v2
32 16 2 ✗  No ✗  No
C4
Performance speciﬁcations 595
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
c4.large 3.75 Intel Xeon 
E5-2666v3
2 1 2 ✗  No ✗  No
c4.xlarge 7.50 Intel Xeon 
E5-2666v3
4 2 2 ✗  No ✗  No
c4.2xlarge 15.00 Intel Xeon 
E5-2666v3
8 4 2 ✗  No ✗  No
c4.4xlarge 30.00 Intel Xeon 
E5-2666v3
16 8 2 ✗  No ✗  No
c4.8xlarge 60.00 Intel Xeon 
E5-2666v3
36 18 2 ✗  No ✗  No
G3
g3.4xlarge 122.00 Intel Xeon E5-2686 
v4
16 8 2 1 x NVIDIA 
M60 GPU
8 GiB 
(1 x 8 
GiB)
g3.8xlarge 244.00 Intel Xeon E5-2686 
v4
32 16 2 2 x NVIDIA 
M60 GPU
16 
GiB 
(2 x 8 
GiB)
g3.16xlarge 488.00 Intel Xeon E5-2686 
v4
64 32 2 4 x NVIDIA 
M60 GPU
32 
GiB 
(4 x 8 
GiB)
I2
i2.xlarge 30.50 Intel Xeon 
E5-2670v2
4 2 2 ✗  No ✗  No
Performance speciﬁcations 596
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
i2.2xlarge 61.00 Intel Xeon 
E5-2670v2
8 4 2 ✗  No ✗  No
i2.4xlarge 122.00 Intel Xeon 
E5-2670v2
16 8 2 ✗  No ✗  No
i2.8xlarge 244.00 Intel Xeon 
E5-2670v2
32 16 2 ✗  No ✗  No
M1
m1.small 1.70 Intel Xeon Family 1 1 1 ✗  No ✗  No
m1.medium 3.70 Intel Xeon Family 1 1 1 ✗  No ✗  No
m1.large 7.50 Intel Xeon Family 2 2 1 ✗  No ✗  No
m1.xlarge 15.00 Intel Xeon Family 4 4 1 ✗  No ✗  No
M2
m2.xlarge 17.10 Intel Xeon Family 2 2 1 ✗  No ✗  No
m2.2xlarge 34.20 Intel Xeon Family 4 4 1 ✗  No ✗  No
m2.4xlarge 68.40 Intel Xeon Family 8 8 1 ✗  No ✗  No
M3
m3.medium 3.75 Intel Xeon 
E5-2670v2
1 1 1 ✗  No ✗  No
m3.large 7.50 Intel Xeon 
E5-2670v2
2 1 2 ✗  No ✗  No
m3.xlarge 15.00 Intel Xeon 
E5-2670v2
4 2 2 ✗  No ✗  No
Performance speciﬁcations 597
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
m3.2xlarge 30.00 Intel Xeon 
E5-2670v2
8 4 2 ✗  No ✗  No
M4
m4.large 8.00 Intel Xeon 
E5-2676v3
2 1 2 ✗  No ✗  No
m4.xlarge 16.00 Intel Xeon 
E5-2676v3
4 2 2 ✗  No ✗  No
m4.2xlarge 32.00 Intel Xeon 
E5-2676v3
8 4 2 ✗  No ✗  No
m4.4xlarge 64.00 Intel Xeon 
E5-2676v3
16 8 2 ✗  No ✗  No
m4.10xlarge 160.00 Intel Xeon 
E5-2676v3
40 20 2 ✗  No ✗  No
m4.16xlarge 256.00 Intel Xeon 
E5-2686v4
64 32 2 ✗  No ✗  No
P2
p2.xlarge 61.00 Intel Xeon 
E5-2686v4
4 2 2 1 x NVIDIA 
K80 GPU
12 
GiB (1 
x 12 
GiB)
p2.8xlarge 488.00 Intel Xeon 
E5-2686v4
32 16 2 8 x NVIDIA 
K80 GPU
96 
GiB (8 
x 12 
GiB)
Performance speciﬁcations 598
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
p2.16xlarge 732.00 Intel Xeon E5-2686 
v4
64 32 2 16 x NVIDIA 
K80 GPU
192 
GiB 
(16 
x 12 
GiB)
P3
p3.2xlarge 61.00 Intel Xeon E5-2686 
v4
8 4 2 1 x NVIDIA 
V100 GPU
16 
GiB (1 
x 16 
GiB)
p3.8xlarge 244.00 Intel Xeon E5-2686 
v4
32 16 2 4 x NVIDIA 
V100 GPU
64 
GiB (4 
x 16 
GiB)
p3.16xlarge 488.00 Intel Xeon E5-2686 
v4
64 32 2 8 x NVIDIA 
V100 GPU
128 
GiB (8 
x 16 
GiB)
P3dn
p3dn.24xl 
arge
768.00 Intel Xeon Platinum 
8175
96 48 2 8 x NVIDIA 
V100 GPU
256 
GiB (8 
x 32 
GiB)
R3
r3.large 15.00 Intel Xeon 
E5-2670v2
2 1 2 ✗  No ✗  No
Performance speciﬁcations 599
Amazon EC2 Instance Types
Instance 
type
Memory 
(GiB)
Processor vCPUs CPU 
cores
Threads 
per 
core
Accelerat 
ors
Accelerat 
or 
memory
r3.xlarge 30.50 Intel Xeon 
E5-2670v2
4 2 2 ✗  No ✗  No
r3.2xlarge 61.00 Intel Xeon 
E5-2670v2
8 4 2 ✗  No ✗  No
r3.4xlarge 122.00 Intel Xeon 
E5-2670v2
16 8 2 ✗  No ✗  No
r3.8xlarge 244.00 Intel Xeon 
E5-2670v2
32 16 2 ✗  No ✗  No
R4
r4.large 15.25 Intel Broadwell 
E5-2686v4
2 1 2 ✗  No ✗  No
r4.xlarge 30.50 Intel Broadwell 
E5-2686v4
4 2 2 ✗  No ✗  No
r4.2xlarge 61.00 Intel Broadwell 
E5-2686v4
8 4 2 ✗  No ✗  No
r4.4xlarge 122.00 Intel Broadwell 
E5-2686v4
16 8 2 ✗  No ✗  No
r4.8xlarge 244.00 Intel Broadwell 
E5-2686v4
32 16 2 ✗  No ✗  No
r4.16xlarge 488.00 Intel Broadwell 
E5-2686v4
64 32 2 ✗  No ✗  No
T1
t1.micro 0.61 Intel E5-2650 1 1 1 ✗  No ✗  No
Performance speciﬁcations 600
Amazon EC2 Instance Types
Network speciﬁcations
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
A1
a1.medium 1 0.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 2 4 ✓ 
Yes
a1.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
a1.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
a1.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
a1.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
a1.metal 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
C1
c1.medium Moderate ✗ 
No
✗ 
No
✗  No 1 2 6 ✗ 
No
c1.xlarge High ✗ 
No
✗ 
No
✗  No 1 4 15 ✗ 
No
C3
c3.large Moderate ✗ 
No
✗ 
No 2
✗  No 1 3 10 ✓ 
Yes
Network speciﬁcations 601
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
c3.xlarge Moderate ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
c3.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
c3.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
c3.8xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
C4
c4.large Moderate ✗ 
No
✗ 
No 2
✗  No 1 3 10 ✓ 
Yes
c4.xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
c4.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
c4.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
c4.8xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
G3
g3.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 602
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
g3.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
g3.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
I2
i2.xlarge Moderate ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
i2.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
i2.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
i2.8xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
M1
m1.small Low ✗ 
No
✗ 
No
✗  No 1 2 4 ✗ 
No
m1.medium Moderate ✗ 
No
✗ 
No
✗  No 1 2 6 ✗ 
No
m1.large Moderate ✗ 
No
✗ 
No
✗  No 1 3 10 ✗ 
No
m1.xlarge High ✗ 
No
✗ 
No
✗  No 1 4 15 ✗ 
No
M2
Network speciﬁcations 603
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m2.xlarge Moderate ✗ 
No
✗ 
No
✗  No 1 4 15 ✗ 
No
m2.2xlarge Moderate ✗ 
No
✗ 
No
✗  No 1 4 30 ✗ 
No
m2.4xlarge High ✗ 
No
✗ 
No
✗  No 1 8 30 ✗ 
No
M3
m3.medium Moderate ✗ 
No
✗ 
No
✗  No 1 2 6 ✗ 
No
m3.large Moderate ✗ 
No
✗ 
No
✗  No 1 3 10 ✗ 
No
m3.xlarge High ✗ 
No
✗ 
No
✗  No 1 4 15 ✗ 
No
m3.2xlarge High ✗ 
No
✗ 
No
✗  No 1 4 30 ✗ 
No
M4
m4.large Moderate ✗ 
No
✗ 
No 2
✗  No 1 2 10 ✓ 
Yes
m4.xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
m4.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
Network speciﬁcations 604
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
m4.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
m4.10xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
m4.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
P2
p2.xlarge High ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
p2.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
p2.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
P3
p3.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
p3.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
p3.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
P3dn
p3dn.24xlarge 100 Gigabit ✓ 
Yes
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
Network speciﬁcations 605
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
R3
r3.large Moderate ✗ 
No
✗ 
No 2
✗  No 1 3 10 ✓ 
Yes
r3.xlarge Moderate ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
r3.2xlarge High ✗ 
No
✗ 
No 2
✗  No 1 4 15 ✓ 
Yes
r3.4xlarge High ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
r3.8xlarge 10 Gigabit ✗ 
No
✗ 
No 2
✗  No 1 8 30 ✓ 
Yes
R4
r4.large 1 0.75 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 3 10 ✓ 
Yes
r4.xlarge 1 1.25 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r4.2xlarge 1 2.5 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 4 15 ✓ 
Yes
r4.4xlarge 1 5.0 / 10.0 ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
r4.8xlarge 10 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 8 30 ✓ 
Yes
Network speciﬁcations 606
Amazon EC2 Instance Types
Instance type Baseline / 
Burst 
bandwidth 
(Gbps)
EFA ENA ENA 
Express
Network 
cards
Max. 
network 
interface 
s
IP 
addresses 
per 
interface
IPv6
r4.16xlarge 25 Gigabit ✗ 
No
✓ 
Yes
✗  No 1 15 50 ✓ 
Yes
T1
t1.micro Very Low ✗ 
No
✗ 
No
✗  No 1 2 2 ✗ 
No
Note
1 These instances have a baseline bandwidth and can use a network I/O credit mechanism 
to burst beyond their baseline bandwidth on a best eﬀort basis. Other instances types 
can sustain their maximum performance indeﬁnitely. For more information, see  instance 
network bandwidth.
2 These instances support enhanced networking using the Intel 82599 VF interface.
Amazon EBS speciﬁcations
The following table indicates which instance types are Amazon EBS optimized by default and 
which optionally support it. It also describes their EBS-optimized performance, including dedicated 
bandwidth to Amazon EBS, the typical maximum aggregate throughput that can be achieved on 
that dedicated connection with a streaming read workload and 128 KiB I/O size, and the maximum 
IOPS the instance type can support when using a 16 KiB I/O size. Instance types not listed do not 
support Amazon EBS optimization.
Important
An instance's EBS performance is bounded by the instance's performance limits, or 
the aggregated performance of its attached volumes, whichever is smaller. To achieve 
maximum EBS performance, an instance must have attached volumes that provide a 
combined performance equal to or greater than the maximum instance performance. For 
Amazon EBS speciﬁcations 607
Amazon EC2 Instance Types
example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5
gp3 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000
IOPS).
We recommend that you choose an EBS–optimized instance type that provides more 
dedicated Amazon EBS throughput than your application needs; otherwise, the connection 
between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
A1
a1.medium
1
300.00 / 
3500.00
37.50 / 
437.50
2500.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
a1.large 1 525.00 / 
3500.00
65.62 / 
437.50
4000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
a1.xlarge 1 800.00 / 
3500.00
100.00 / 
437.50
6000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
a1.2xlarge
1
1750.00 / 
3500.00
218.75 / 
437.50
10000.00 / 
20000.00
✓  Yes ✗  No Up to 27 
(Shared 
limit)
a1.4xlarge 3500.00 437.50 20000.00 ✓  Yes ✗  No Up to 27 
(Shared 
limit)
Amazon EBS speciﬁcations 608
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
a1.metal 3500.00 437.50 20000.00 ✓  Yes ✗  No Up to 31 
(Shared 
limit)
C1
c1.xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
C3
c3.xlarge 500.00 62.50 4000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
c3.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
c3.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
C4
c4.large 500.00 62.50 4000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
Amazon EBS speciﬁcations 609
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
c4.xlarge 750.00 93.75 6000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
c4.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
c4.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
c4.8xlarge 4000.00 500.00 32000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
G3
g3.4xlarge 3500.00 437.50 20000.00 ✗  No ✗  No Up to 26 
(Xen-based 
limit)
g3.8xlarge 7000.00 875.00 40000.00 ✗  No ✗  No Up to 25 
(Xen-based 
limit)
g3.16xlar 
ge
14000.00 1750.00 80000.00 ✗  No ✗  No Up to 23 
(Xen-based 
limit)
I2
Amazon EBS speciﬁcations 610
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
i2.xlarge 500.00 62.50 4000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i2.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
i2.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
M1
m1.large 500.00 62.50 4000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
m1.xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
M2
m2.2xlarge 500.00 62.50 4000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
m2.4xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
Amazon EBS speciﬁcations 611
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
M3
m3.xlarge 500.00 62.50 4000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
m3.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
M4
m4.large 450.00 56.25 3600.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
m4.xlarge 750.00 93.75 6000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
m4.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
m4.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
m4.10xlar 
ge
4000.00 500.00 32000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
Amazon EBS speciﬁcations 612
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
m4.16xlar 
ge
10000.00 1250.00 65000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
P2
p2.xlarge 750.00 93.75 6000.00 ✗  No ✗  No Up to 26 
(Xen-based 
limit)
p2.8xlarge 5000.00 625.00 32500.00 ✗  No ✗  No Up to 19 
(Xen-based 
limit)
p2.16xlar 
ge
10000.00 1250.00 65000.00 ✗  No ✗  No Up to 11 
(Xen-based 
limit)
P3
p3.2xlarge 1750.00 218.75 10000.00 ✗  No ✗  No Up to 26 
(Xen-based 
limit)
p3.8xlarge 7000.00 875.00 40000.00 ✗  No ✗  No Up to 23 
(Xen-based 
limit)
p3.16xlar 
ge
14000.00 1750.00 80000.00 ✗  No ✗  No Up to 19 
(Xen-based 
limit)
Amazon EBS speciﬁcations 613
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
P3dn
p3dn.24xl 
arge
19000.00 2375.00 80000.00 ✓  Yes ✗  No Up to 17 
(Shared 
limit)
R3
r3.xlarge 500.00 62.50 4000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
r3.2xlarge 1000.00 125.00 8000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
r3.4xlarge 2000.00 250.00 16000.00 ✗  No ✗  No Up to 39 
(Xen-based 
limit)
R4
r4.large 425.00 53.12 3000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
r4.xlarge 850.00 106.25 6000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
Amazon EBS speciﬁcations 614
Amazon EC2 Instance Types
Instance 
type
Baseline / 
Maximum 
bandwidth 
(Mbps)
Baseline / 
Maximum 
throughpu 
t (MB/s, 
128 KiB I/
O)
Baseline / 
Maximum 
IOPS (16 
KiB I/O)
NVMe Multiple 
EBS cards
EBS 
volume 
limit
r4.2xlarge 1700.00 212.50 12000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
r4.4xlarge 3500.00 437.50 18750.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
r4.8xlarge 7000.00 875.00 37500.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
r4.16xlar 
ge
14000.00 1750.00 75000.00 ✗  No ✗  No Up to 40 
(Xen-based 
limit)
T1
Note
1 These instances can support maximum performance for 30 minutes at least once every 24 
hours, after which they revert to their baseline performance. Other instances can sustain 
the maximum performance indeﬁnitely. If your workload requires sustained maximum 
performance for longer than 30 minutes, use one of these instances.
C1, C3, I2, M1, M2, M3, and R3 instances are not Amazon EBS optimized by default. You can 
optionally enable Amazon EBS optimization for these instances during or after launch for 
an additional hourly fee.
Amazon EBS speciﬁcations 615
Amazon EC2 Instance Types
Instance store speciﬁcations
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
C1
c1.medium 1 x 350 GB HDD   ✓  Yes
c1.xlarge 4 x 420 GB HDD   ✓  Yes
C3
c3.large 2 x 16 GB SSD   ✓  Yes
c3.xlarge 2 x 40 GB SSD   ✓  Yes
c3.2xlarge 2 x 80 GB SSD   ✓  Yes
c3.4xlarge 2 x 160 GB SSD   ✓  Yes
c3.8xlarge 2 x 320 GB SSD   ✓  Yes
I2
i2.xlarge 1 x 800 GB SSD   ✓  Yes
i2.2xlarge 2 x 800 GB SSD   ✓  Yes
i2.4xlarge 4 x 800 GB SSD   ✓  Yes
i2.8xlarge 8 x 800 GB SSD   ✓  Yes
M1
m1.small 1 x 160 GB HDD   ✓  Yes
m1.medium 1 x 410 GB HDD   ✓  Yes
m1.large 2 x 420 GB HDD   ✓  Yes
Instance store speciﬁcations 616
Amazon EC2 Instance Types
Instance type Instance 
store 
volumes
Instance 
store 
type
100% random read 
IOPS / Write IOPS
Needs 
initializ 
ation 1
TRIM 
support
2
m1.xlarge 4 x 420 GB HDD   ✓  Yes
M2
m2.xlarge 1 x 420 GB HDD   ✓  Yes
m2.2xlarge 1 x 850 GB HDD   ✓  Yes
m2.4xlarge 2 x 840 GB HDD   ✓  Yes
M3
m3.medium 1 x 4 GB SSD   ✓  Yes
m3.large 1 x 32 GB SSD   ✓  Yes
m3.xlarge 2 x 40 GB SSD   ✓  Yes
m3.2xlarge 2 x 80 GB SSD   ✓  Yes
P3dn
p3dn.24xlarge 2 x 900 GB NVMe 
SSD
700,000 / 340,000 ✓  Yes
R3
r3.large 1 x 32 GB SSD   ✓  Yes
r3.xlarge 1 x 80 GB SSD   ✓  Yes
r3.2xlarge 1 x 160 GB SSD   ✓  Yes
r3.4xlarge 1 x 320 GB SSD   ✓  Yes
r3.8xlarge 2 x 320 GB SSD   ✓  Yes
Instance store speciﬁcations 617
Amazon EC2 Instance Types
1 Volumes attached to certain instances suﬀer a ﬁrst-write penalty unless initialized. For more 
information, see Optimize disk performance for instance store volumes.
2 For more information, see Instance store volume TRIM support.
Security speciﬁcations
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
A1
a1.medium ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
a1.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
a1.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
a1.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
a1.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
a1.metal ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
C1
Security speciﬁcations 618
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c1.medium ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
c1.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
C3
c3.large ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
c3.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
c3.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
c3.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
c3.8xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
C4
c4.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
c4.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
c4.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
c4.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 619
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
c4.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
G3
g3.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g3.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
g3.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
I2
i2.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
i2.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
i2.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
i2.8xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
M1
m1.small ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m1.medium ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m1.large ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 620
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m1.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
M2
m2.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m2.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m2.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
M3
m3.medium ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m3.large ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m3.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
m3.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
M4
m4.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
m4.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
m4.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 621
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
m4.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
m4.10xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
m4.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
P2
p2.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
p2.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
p2.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
P3
p3.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 622
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
p3.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
p3.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
P3dn
p3dn.24xlarge ✓  Yes ✓  Yes ✓  Yes ✗  No ✗  No ✓  Yes
R3
r3.large ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
r3.xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
r3.2xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
r3.4xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
r3.8xlarge ✓  Yes ✗  No ✗  No ✗  No ✗  No ✗  No
R4
r4.large ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
r4.xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 623
Amazon EC2 Instance Types
Instance type EBS 
encryptio 
n
Instance 
store 
encryptio 
n
Encryptio 
n in 
transit
AMD 
SEV-SNP
NitroTPM Nitro 
Enclaves
r4.2xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
r4.4xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
r4.8xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
r4.16xlarge ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
T1
t1.micro ✓  Yes Instance 
store not 
supported
✗  No ✗  No ✗  No ✗  No
Security speciﬁcations 624
Amazon EC2 Instance Types
Amazon EC2 instance types by Region
An Amazon EC2 instance is tied to the zone in which it was launched. The ID of an instance is tied 
to the Region for the instance, and can only be used in this Region.
Considerations
• When you create your AWS account, we set default quotas on these resources on a per-Region 
basis. We monitor your usage within each Region and raise your quotas automatically based on 
your use of Amazon EC2. For more information, see Quotas.
• Each Region supports a subset of the available instance types. An instance type that is supported 
in a Region might not be supported in all of the Availability Zones for that Region.
• Each Local Zone supports a subset of the available instance types. For more information, see
AWS Local Zones Features.
• Each Wavelength Zone supports a subset of the available instance types. For more information, 
see Amazon EC2 considerations.
US East (N. Virginia) — us-east-1
The following instance types are available in US East (N. Virginia).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | 
M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8azn | M8g 
| M8gb | M8gd | M8gn | M8i | M8id | M8i-ﬂex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-
m2pro | Mac-m4 | Mac-m4pro | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8a | C8g | C8gb | C8gd | C8gn | C8i | C8id | 
C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i 
| R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gb | R8gd | R8gn | R8i | R8id | 
R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | X1 | X1e | X2gd 
| X2idn | X2iedn | X2iezn | X8g | X8i | z1d
• Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | 
Is4gen
US East (N. Virginia) 625
Amazon EC2 Instance Types
• Accelerated Computing: DL1 | F1 | F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | G7e | Inf1 | 
Inf2 | P3 | P4d | P4de | P5 | P5en | P6-B200 | Trn1 | Trn1n | VT1
• High Performance Computing: Hpc7g
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | R3 | R4 | T1
US East (Ohio) — us-east-2
The following instance types are available in US East (Ohio).
• General Purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i 
| M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8g | M8gd | M8i | M8id | M8i-
ﬂex | Mac1 | Mac2 | Mac2-m2 | Mac2-m2pro | Mac-m4 | T2 | T3 | T3a | T4g
• Compute Optimized: C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | 
C7a | C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8a | C8g | C8gd | C8gn | C8i | C8id | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | 
R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gd | R8i | R8id | R8i-ﬂex | U-3tb1 
| U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-24tb | X1 | X1e | X2gd | X2idn | X2iedn | X8g | X8i | 
z1d
• Storage Optimized: D2 | D3 | H1 | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | Is4gen
• Accelerated Computing: G4ad | G4dn | G5 | G6 | G6e | G6f | Gr6 | Gr6f | G7e | Inf1 | Inf2 | P3 | 
P4d | P5 | P5e | P5en | P6-B200 | Trn1 | Trn1n | Trn2
• High Performance Computing: Hpc6a | Hpc6id | Hpc7a | Hpc8a
• Previous Generation: A1 | C4 | I2 | M4 | P3 | R3 | R4
US West (N. California) — us-west-1
The following instance types are available in US West (N. California).
• General Purpose: M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd | M6i | 
M6id | M6idn | M6in | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8i | M8i-ﬂex | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6in | 
C7g | C7gd | C7i | C7i-ﬂex | C8g | C8gn | C8i | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5d | R5n | R6a | R6g | R6gd | R6i | R7g | R7gd | 
R7i | R8g | R8i | R8i-ﬂex | X2idn | X2iedn | z1d
US East (Ohio) 626
Amazon EC2 Instance Types
• Storage Optimized: D2 | I2 | I3 | I3en | I4i | I7i | I7ie
• Accelerated Computing: G4dn | Inf1 | P5 | P5en
• Previous Generation: C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | R3 | R4 | T1
US West (Oregon) — us-west-2
The following instance types are available in US West (Oregon).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | 
M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8azn | M8g 
| M8gb | M8gd | M8gn | M8i | M8id | M8i-ﬂex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-
m2pro | Mac-m4 | Mac-m4pro | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8a | C8g | C8gb | C8gd | C8gn | C8i | C8id | 
C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i 
| R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gb | R8gd | R8gn | R8i | R8id | 
R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | X1 | X1e | X2gd 
| X2idn | X2iedn | X2iezn | X8g | X8aedz | X8i | z1d
• Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | 
Is4gen
• Accelerated Computing: DL1 | DL2q | F1 | F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | G7e 
| Inf1 | Inf2 | P3 | P4d | P4de | P5 | P5e | P5en | P6-B200 | Trn1 | Trn1n | VT1
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | R3 | R4 | T1
Africa (Cape Town) — af-south-1
The following instance types are available in Africa (Cape Town).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | M7i | M8g | M8i | M8i-ﬂex | T3 | T4g
• Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6gd | C6i | C6in | C7g | C7i | C7i-ﬂex | 
C8gn
• Memory Optimized: R5 | R5d | R5dn | R5n | R6g | R6gd | R6i | R6id | R7g | R7gd | R8i | R8i-ﬂex | 
U-6tb1 | X1 | X1e | X2idn | X2iedn
US West (Oregon) 627
Amazon EC2 Instance Types
• Storage Optimized: D2 | I3 | I3en | I4i | I7i | I7ie
• Accelerated Computing: G4dn | Inf1
Asia Paciﬁc (Hong Kong) — ap-east-1
The following instance types are available in Asia Paciﬁc (Hong Kong).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | M7i | M7i-ﬂex | M8g | T3 | T4g
• Compute Optimized: C5 | C5a | C5d | C5n | C6a | C6g | C6gn | C6i | C6in | C7g | C7i | C7i-ﬂex | C8g
• Memory Optimized: R5 | R5d | R5n | R6g | R6i | R7g | R7gd | R8g | U-3tb1 | X1
• Storage Optimized: D2 | I3 | I3en | I4i | I7i
• Accelerated Computing: G4dn | G5 | Inf1
Asia Paciﬁc (Hyderabad) — ap-south-2
The following instance types are available in Asia Paciﬁc (Hyderabad).
• General Purpose: M5 | M5d | M6a | M6g | M6gd | M6i | M7g | M8g | M8i | M8i-ﬂex | T3 | T4g
• Compute Optimized: C5 | C5d | C6a | C6g | C6i | C6in | C7g | C7i | C8g
• Memory Optimized: R5 | R5d | R6a | R6g | R6i | R7a | R7g | R7gd | R7i | R8g | R8i | R8i-ﬂex | 
U-6tb1 | U7i-12tb | X2idn | X2iedn
• Storage Optimized: I3 | I3en | I4i | I7i
Asia Paciﬁc (Jakarta) — ap-southeast-3
The following instance types are available in Asia Paciﬁc (Jakarta).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | M7i | M7i-ﬂex | M8g | T3 | T4g
• Compute Optimized: C5 | C5d | C5n | C6g | C6gd | C6gn | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g
• Memory Optimized: R5 | R5d | R6g | R6gd | R7g | R7gd | R7i | R8g | U-6tb1 | U7i-6tb | X2idn | 
X2iedn
• Storage Optimized: D3en | I3 | I3en | I4i | I7i | I7ie
• Accelerated Computing: G5 | G5g | P5 | P5e | P5en
Asia Paciﬁc (Hong Kong) 628
Amazon EC2 Instance Types
Asia Paciﬁc (Malaysia) — ap-southeast-5
The following instance types are available in Asia Paciﬁc (Malaysia).
• General Purpose: M6g | M6gd | M6i | M6id | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8gd | M8i | 
M8i-ﬂex | T3 | T4g
• Compute Optimized: C6g | C6gn | C6i | C6id | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g | C8gd | 
C8gn | C8i | C8i-ﬂex
• Memory Optimized: R6g | R6i | R6id | R7g | R7gd | R7i | R8g | R8gd | R8i | R8i-ﬂex | U7i-8tb | 
X2idn | X2iedn
• Storage Optimized: I3en | I4i | I7i | I7ie
• Accelerated Computing: G6 | Gr6
Asia Paciﬁc (Melbourne) — ap-southeast-4
The following instance types are available in Asia Paciﬁc (Melbourne).
• General Purpose: M5 | M5d | M6g | M6gd | M7g | M7i | M7i-ﬂex | M8g | T3 | T4g
• Compute Optimized: C5 | C5d | C6g | C6in | C7i | C8g | C8gn
• Memory Optimized: R5 | R5d | R6g | R7g | R7i | R8g | X2idn
• Storage Optimized: I3 | I3en | I4i | I7i
• Accelerated Computing: Trn1 | Trn2
Asia Paciﬁc (Mumbai) — ap-south-1
The following instance types are available in Asia Paciﬁc (Mumbai).
• General Purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M6idn | 
M6in | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8i | M8i-ﬂex | Mac1 | T2 | T3 | T3a | T4g
• Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6in | C7g | C7gd | 
C7i | C7i-ﬂex | C8g | C8gn | C8i | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5d | R5n | R6a | R6g | R6gd | R6i | R6id | R7g | 
R7gd | R7i | R8g | R8i | R8i-ﬂex | U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | X1 | X1e | 
X2idn | X2iedn | X8aedz | z1d
Asia Paciﬁc (Malaysia) 629
Amazon EC2 Instance Types
• Storage Optimized: D2 | D3 | I2 | I3 | I3en | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: G4dn | G5 | G6 | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P4d | P5 | P5en | Trn1
• Previous Generation: A1 | C4 | I2 | M4 | R3 | R4
Asia Paciﬁc (New Zealand) — ap-southeast-6
The following instance types are available in Asia Paciﬁc (New Zealand).
• General Purpose: M6g | M6gd | M6i | M6id | M7g | M7gd | M7i | M7i-ﬂex | T3 | T4g
• Compute Optimized: C6g | C6gn | C6i | C6id | C7g | C7i | C7i-ﬂex
• Memory Optimized: R6g | R6i | R6id | R7g | R7gd | R7i | R8i | R8i-ﬂex
• Storage Optimized: I3en | I4i
Asia Paciﬁc (Osaka) — ap-northeast-3
The following instance types are available in Asia Paciﬁc (Osaka).
• General Purpose: M4 | M5 | M5d | M6g | M6gd | M6i | M7g | M7i | M7i-ﬂex | M8g | T2 | T3 | T4g
• Compute Optimized: C4 | C5 | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in | C7g | C7gd | C7i | C8g
• Memory Optimized: R4 | R5 | R5d | R6g | R6gd | R6i | R7g | R7gd | R7i | R8g | U-6tb1 | X1 | X1e | 
X2idn | X2iedn
• Storage Optimized: D2 | I3 | I3en | I4i | I7i | I8g
• Accelerated Computing: G4dn
• Previous Generation: C4 | M4 | R4
Asia Paciﬁc (Seoul) — ap-northeast-2
The following instance types are available in Asia Paciﬁc (Seoul).
• General Purpose: M4 | M5 | M5a | M5ad | M5d | M5zn | M6g | M6gd | M6i | M6id | M6idn | M6in | 
M7g | M7gd | M7i | M7i-ﬂex | M8g | M8i | M8i-ﬂex | Mac1 | T2 | T3 | T3a | T4g
• Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g | C7gd 
| C7i | C7i-ﬂex | C8g | C8gn | C8i | C8i-ﬂex
Asia Paciﬁc (New Zealand) 630
Amazon EC2 Instance Types
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6g | R6gd | R6i | R6id | 
R7g | R7gd | R7i | R8g | R8i | R8i-ﬂex | U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | X1 | X1e 
| X2idn | X2iedn | X8aedz | z1d
• Storage Optimized: D2 | I2 | I3 | I3en | I4i | I7i | I8g
• Accelerated Computing: F2 | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P3 | P4d | 
P5 | P5en
• Previous Generation: C4 | I2 | M4 | P3 | R3 | R4
Asia Paciﬁc (Singapore) — ap-southeast-1
The following instance types are available in Asia Paciﬁc (Singapore).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | 
M6g | M6gd | M6i | M6id | M6idn | M6in | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8i | M8i-ﬂex | Mac1 
| Mac2 | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g | C8gn | C8i | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | 
R6id | R6idn | R6in | R7g | R7gd | R7i | R8g | R8i | R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | U7in-16tb | 
X1 | X1e | X2idn | X2iedn | z1d
• Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: G4dn | G5g | Inf1 | Inf2 | P3 | P4de
• High Performance Computing: Hpc6a
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | R3 | R4 | T1
Asia Paciﬁc (Sydney) — ap-southeast-2
The following instance types are available in Asia Paciﬁc (Sydney).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd | 
M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8gd | M8i | M8i-ﬂex | Mac1 
| Mac2-m2 | Mac2-m2pro | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g | C8gd | C8gn | C8i | C8i-ﬂex
Asia Paciﬁc (Singapore) 631
Amazon EC2 Instance Types
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i 
| R6id | R6idn | R6in | R7g | R7gd | R7i | R8g | R8gd | R8i | R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | 
U7in-16tb | X1 | X1e | X2idn | X2iedn | X8g | z1d
• Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: F1 | F2 | G4dn | G5 | G6 | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P3 | P4d | P5 | 
P5e | Trn1
• High Performance Computing: Hpc6a
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | R3 | R4 | T1
Asia Paciﬁc (Taipei) — ap-east-2
The following instance types are available in Asia Paciﬁc (Taipei).
• General Purpose: M6g | M6gd | M6i | M6id | M7g | M7gd | M7i | M7i-ﬂex | T3 | T4g
• Compute Optimized: C6g | C6gn | C6i | C6id | C7g | C7i | C7i-ﬂex
• Memory Optimized: R6g | R6i | R6id | R7g | R7gd | R7i
• Storage Optimized: I3en | I4i
Asia Paciﬁc (Thailand) — ap-southeast-7
The following instance types are available in Asia Paciﬁc (Thailand).
• General Purpose: M6g | M6gd | M6i | M6id | M7g | M7gd | M7i | M7i-ﬂex | M8g | T3 | T4g
• Compute Optimized: C6g | C6gn | C6i | C6id | C6in | C7g | C7i | C7i-ﬂex | C8g | C8gn
• Memory Optimized: R6g | R6i | R6id | R7g | R7gd | R7i | U7i-6tb | X2idn | X2iedn
• Storage Optimized: I3en | I4i
Asia Paciﬁc (Tokyo) — ap-northeast-1
The following instance types are available in Asia Paciﬁc (Tokyo).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | 
M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8azn | M8g | 
M8gd | M8i | M8id | M8i-ﬂex | Mac1 | T1 | T2 | T3 | T3a | T4g
Asia Paciﬁc (Taipei) 632
Amazon EC2 Instance Types
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | 
C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8g | C8gd | C8i | C8id | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i 
| R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8g | R8gd | R8i | R8id | R8i-ﬂex | U-3tb1 | 
U-6tb1 | U7i-6tb | X1 | X1e | X2idn | X2iedn | X2iezn | X8aedz | z1d
• Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f | G7e | Inf1 | 
Inf2 | P3 | P3dn | P4d | P4de | P5 | P5en | VT1
• High Performance Computing: Hpc7g
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | P3dn | R3 | R4 | T1
Canada (Central) — ca-central-1
The following instance types are available in Canada (Central).
• General Purpose: M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M6idn | M6in | 
M7g | M7i | M7i-ﬂex | M8g | M8gd | M8i | M8i-ﬂex | Mac2-m2 | T2 | T3 | T3a | T4g
• Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g | 
C7gd | C7i | C7i-ﬂex | C8g | C8gd | C8gn | C8i | C8i-ﬂex
• Memory Optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6a | R6g | R6gd | R6i | R7g | R7i | 
R8g | R8gd | R8i | R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | X1 | X1e | X2idn | X2iedn
• Storage Optimized: D2 | D3 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: F2 | G4ad | G4dn | G5 | G6 | G6f | Gr6 | Gr6f | Inf1 | P3 | P4d | P5
• Previous Generation: C4 | M4 | P3 | R4
Canada West (Calgary) — ca-west-1
The following instance types are available in Canada West (Calgary).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | M8g | T3 | T4g
• Compute Optimized: C5 | C6g | C6gn | C6i | C6id | C6in | C7g | C8gn
• Memory Optimized: R5 | R6g | R6i | R6id | R7g
• Storage Optimized: I3en | I4i | I7i | I7ie
Canada (Central) 633
Amazon EC2 Instance Types
China (Beijing) — cn-north-1
The following instance types are available in China (Beijing).
• General Purpose: M1 | M3 | M4 | M5 | M5a | M5d | M6g | M6i | M7g | M8g | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C3 | C4 | C5 | C5a | C5d | C6g | C6gn | C6i | C7g | C8g
• Memory Optimized: R3 | R4 | R5 | R5a | R5d | R6g | R6gd | R6i | R7g | R8g | U-6tb1 | X1 | X2idn | 
X2iedn
• Storage Optimized: D2 | I2 | I3 | I3en | I4i
• Accelerated Computing: G4dn | G5 | Inf1 | P3
• Previous Generation: C3 | C4 | I2 | M1 | M3 | M4 | P3 | R3 | R4 | T1
China (Ningxia) — cn-northwest-1
The following instance types are available in China (Ningxia).
• General Purpose: M4 | M5 | M5a | M5d | M6g | M6i | M7g | M8g | T2 | T3 | T3a | T4g
• Compute Optimized: C4 | C5 | C5a | C5d | C6g | C6gd | C6gn | C6i | C6in | C7g | C8g
• Memory Optimized: R4 | R5 | R5a | R5d | R6g | R6gd | R6i | R7g | R8g | U-6tb1 | X1 | X2idn | 
X2iedn | z1d
• Storage Optimized: D2 | I3 | I3en | I4i
• Accelerated Computing: G4dn | G5 | Inf1 | P3
• Previous Generation: C4 | M4 | P3 | R4
Europe (Frankfurt) — eu-central-1
The following instance types are available in Europe (Frankfurt).
• General Purpose: A1 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd 
| M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8a | M8azn | M8g | M8gd | M8i | 
M8id | M8i-ﬂex | Mac1 | Mac2-m2 | Mac-m4 | T2 | T3 | T3a | T4g
• Compute Optimized: C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | 
C6in | C7a | C7g | C7gd | C7i | C7i-ﬂex | C8a | C8g | C8gd | C8gn | C8i | C8id | C8i-ﬂex
China (Beijing) 634
Amazon EC2 Instance Types
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | 
R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gd | R8i | R8id | R8i-ﬂex | U-3tb1 
| U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | X1 | X1e | X2idn | X2iedn | X8g | 
X8i | z1d
• Storage Optimized: D2 | D3 | D3en | I2 | I3 | I3en | I4i | I7i | I7ie | I8g | I8ge | Im4gn | Is4gen
• Accelerated Computing: DL2q | F1 | F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f | 
Inf1 | Inf2 | P3 | P4d | P4de
• Previous Generation: A1 | C3 | C4 | I2 | M3 | M4 | P3 | R3 | R4
Europe (Ireland) — eu-west-1
The following instance types are available in Europe (Ireland).
• General Purpose: A1 | M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | 
M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | M8g | Mac1 | Mac2 | 
T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7a | C7g | C7gd | C7gn | C7i | C7i-ﬂex | C8a | C8g | C8gd | C8gn
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i 
| R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gd | R8i | R8i-ﬂex | U-3tb1 | 
U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | X1 | X1e | X2gd | X2idn | X2iedn | X2iezn | z1d
• Storage Optimized: D2 | D3 | D3en | H1 | I2 | I3 | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | 
Is4gen
• Accelerated Computing: F1 | G4ad | G4dn | G5 | Inf1 | Inf2 | P3 | P3dn | P4d | VT1
• High Performance Computing: Hpc7a | Hpc7g
• Previous Generation: A1 | C1 | C3 | C4 | I2 | M1 | M2 | M3 | M4 | P3 | P3dn | R3 | R4 | T1
Europe (London) — eu-west-2
The following instance types are available in Europe (London).
• General Purpose: M4 | M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M6id | M7a | M7g | M7i 
| M7i-ﬂex | M8g | M8gd | Mac1 | T2 | T3 | T3a | T4g
Europe (Ireland) 635
Amazon EC2 Instance Types
• Compute Optimized: C4 | C5 | C5a | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7a | 
C7g | C7gd | C7i | C7i-ﬂex | C8g | C8gd | C8gn | C8i
• Memory Optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6g | R6gd | R6i | R6id | R7g | R7gd | 
R7i | R8g | R8gd | R8i | R8i-ﬂex | U-6tb1 | U7i-6tb | U7i-8tb | U7in-16tb | X1 | X2idn | X2iedn | z1d
• Storage Optimized: D2 | D3 | I3 | I3en | I4i | I7i | I7ie | I8g | Im4gn | Is4gen
• Accelerated Computing: F1 | F2 | G4ad | G4dn | G5 | G6 | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P3 | P4d | 
P5 | P5e
• Previous Generation: C4 | M4 | P3 | R4
Europe (Milan) — eu-south-1
The following instance types are available in Europe (Milan).
• General Purpose: M5 | M5a | M5d | M6a | M6g | M6gd | M6i | M7i | M8g | T3 | T3a | T4g
• Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6gn | C6i | C6id | C6in | C7g | C8g
• Memory Optimized: R5 | R5a | R5b | R5d | R5dn | R5n | R6g | R6i | R7g | R7gd | R7i | U-3tb1 | 
U-6tb1 | U7i-6tb | X2idn | X2iedn
• Storage Optimized: D2 | I3 | I3en | I4i | I7i | Im4gn
• Accelerated Computing: G4dn | Inf1
Europe (Paris) — eu-west-3
The following instance types are available in Europe (Paris).
• General Purpose: M5 | M5a | M5ad | M5d | M6a | M6g | M6gd | M6i | M7g | M7gd | M7i | M7i-ﬂex | 
M8g | M8i | M8i-ﬂex | T2 | T3 | T3a | T4g
• Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g | C7gd | C7i 
| C7i-ﬂex | C8i | C8i-ﬂex
• Memory Optimized: R4 | R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | R6i | R7g | R7gd | R7i | 
R8g | R8i | R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | X1 | X2idn | X2iedn
• Storage Optimized: D2 | D3 | I3 | I3en | I4i | I7ie | Im4gn | Is4gen
• Accelerated Computing: G4dn | G6 | Gr6 | Inf1 | Inf2
• High Performance Computing: Hpc6id | Hpc7a
Europe (Milan) 636
Amazon EC2 Instance Types
• Previous Generation: R4
Europe (Spain) — eu-south-2
The following instance types are available in Europe (Spain).
• General Purpose: M5 | M5d | M6g | M6gd | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-
ﬂex | M8a | M8g | M8gd | M8i | M8id | M8i-ﬂex | T3 | T4g
• Compute Optimized: C5 | C5d | C6g | C6gd | C6in | C7a | C7g | C7gd | C7i | C7i-ﬂex | C8a | C8g | 
C8gd | C8gn | C8i | C8i-ﬂex
• Memory Optimized: R5 | R5d | R6g | R6gd | R6id | R7a | R7g | R7gd | R7i | R8a | R8g | R8gd | R8i | 
R8id | R8i-ﬂex | U-6tb1 | X2idn | X2iedn
• Storage Optimized: I3 | I3en | I4i | I7i | I7ie | I8g | Im4gn
• Accelerated Computing: G5g | G6 | G6e | G6f | Gr6 | Gr6f | P5en
Europe (Stockholm) — eu-north-1
The following instance types are available in Europe (Stockholm).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex 
| M8g | Mac1 | T3 | T4g
• Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in | C7a | C7g | C7gd | C7i | 
C7i-ﬂex | C8g | C8gn
• Memory Optimized: R5 | R5b | R5d | R5dn | R5n | R6g | R6gd | R6i | R6idn | R6in | R7a | R7g | 
R7gd | R7i | R8g | U-6tb1 | U7i-6tb | U7i-12tb | X2idn | X2iedn | X8g | X8i
• Storage Optimized: D2 | I3 | I3en | I4i | I7i | I7ie | I8g
• Accelerated Computing: G4dn | G5 | G6 | G6e | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P4d | P5 | P5e | P5en
• High Performance Computing: Hpc6a | Hpc6id | Hpc7a | Hpc8a
Europe (Zurich) — eu-central-2
The following instance types are available in Europe (Zurich).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | M6idn | M6in | M7g | M7i | M8g | T3 | T4g
Europe (Spain) 637
Amazon EC2 Instance Types
• Compute Optimized: C5 | C5d | C6g | C6gd | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g
• Memory Optimized: R5 | R5d | R6g | R6gd | R6i | R7g | R8g | U-3tb1 | U-6tb1 | X2idn | X2iedn
• Storage Optimized: D3 | I3 | I3en | I4i | I7i
• Accelerated Computing: G6 | Gr6
Israel (Tel Aviv) — il-central-1
The following instance types are available in Israel (Tel Aviv).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M6id | M7g | M7i | T3 | T3a | T4g
• Compute Optimized: C5 | C5d | C6g | C6gn | C6i | C6id | C6in | C7g
• Memory Optimized: R5 | R5d | R6g | R6i | R6id | R7g | R7gd | U-6tb1 | X2idn
• Storage Optimized: D3 | I3 | I3en | I4i
• Accelerated Computing: G5 | P4de
Mexico (Central) — mx-central-1
The following instance types are available in Mexico (Central).
• General Purpose: M6g | M6gd | M6i | M6id | M7g | M7gd | M7i | M7i-ﬂex | T3 | T4g
• Compute Optimized: C6g | C6gn | C6i | C6id | C6in | C7g | C7i | C7i-ﬂex
• Memory Optimized: R6g | R6i | R6id | R7g | R7gd | R7i | R8g
• Storage Optimized: I3en | I4i
Middle East (Bahrain) — me-south-1
The following instance types are available in Middle East (Bahrain).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | M8g | T3 | T4g
• Compute Optimized: C5 | C5a | C5ad | C5d | C5n | C6g | C6gn | C6i | C6in | C7g
• Memory Optimized: R5 | R5d | R6g | R6i | R7g | X2idn
• Storage Optimized: D2 | I3 | I3en | I4i
• Accelerated Computing: G4dn | Inf1
Israel (Tel Aviv) 638
Amazon EC2 Instance Types
Middle East (UAE) — me-central-1
The following instance types are available in Middle East (UAE).
• General Purpose: M5 | M5d | M6g | M6gd | M6i | M7g | M7gd | M7i | M8g | T3 | T4g
• Compute Optimized: C5 | C5d | C6g | C6in | C7i | C7i-ﬂex | C8gn
• Memory Optimized: R5 | R5d | R6g | R6i | R7g | R7gd | R8g | R8i | R8i-ﬂex | X2idn | X2iezn
• Storage Optimized: I3 | I3en | I4i | I7i
• Accelerated Computing: G5 | G6 | G6e | P5en
South America (Sao Paulo) — sa-east-1
The following instance types are available in South America (Sao Paulo).
• General Purpose: M1 | M2 | M3 | M4 | M5 | M5a | M5ad | M5d | M5zn | M6a | M6g | M6gd | M6i | 
M6id | M7g | M7gd | M7i | M7i-ﬂex | M8g | M8gd | M8i | M8i-ﬂex | T1 | T2 | T3 | T3a | T4g
• Compute Optimized: C1 | C3 | C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | 
C6id | C6in | C7g | C7gd | C7i | C7i-ﬂex | C8g | C8i | C8i-ﬂex
• Memory Optimized: R3 | R4 | R5 | R5a | R5ad | R5b | R5d | R5n | R6g | R6gd | R6i | R7g | R7i | R8g 
| R8gd | R8i | R8i-ﬂex | U-3tb1 | U-6tb1 | U7i-6tb | U7i-8tb | U7i-12tb | X1 | X1e | X2idn | X2iedn
• Storage Optimized: I3 | I3en | I4g | I4i | I7i | I7ie | I8g
• Accelerated Computing: G4dn | G5 | G6 | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P4d | P5 | P5e | Trn2
• Previous Generation: C1 | C3 | C4 | M1 | M2 | M3 | M4 | R3 | R4 | T1
AWS GovCloud (US-East) — us-gov-east-1
The following instance types are available in AWS GovCloud (US-East).
• General Purpose: M5 | M5a | M5d | M5dn | M5n | M6g | M6gd | M6i | M7g | M7i | M7i-ﬂex | T3 | 
T3a | T4g
• Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6in | C7g | C7gd | C7i
• Memory Optimized: R5 | R5a | R5d | R5dn | R5n | R6g | R6gd | R6i | R7g | R7gd | R7i | U-6tb1 | 
U7in-24tb | X1 | X1e | X2idn | X2iedn
• Storage Optimized: I3 | I3en | I4i | I7ie
Middle East (UAE) 639
Amazon EC2 Instance Types
• Accelerated Computing: G4dn | G6 | Gr6 | Inf1 | P3dn
• High Performance Computing: Hpc6a
AWS GovCloud (US-West) — us-gov-west-1
The following instance types are available in AWS GovCloud (US-West).
• General Purpose: M5 | M5a | M5ad | M5d | M5dn | M5n | M6g | M6gd | M6i | M6id | M6idn | M6in | 
M7g | M7i | M7i-ﬂex | T2 | T3 | T3a | T4g
• Compute Optimized: C5 | C5a | C5d | C5n | C6g | C6gd | C6gn | C6i | C6id | C6in | C7g | C7gd | C7i 
| C7i-ﬂex
• Memory Optimized: R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | R6i | R6id | R6idn | R6in | 
R7g | R7gd | R7i | R8g | U-3tb1 | U-6tb1 | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | X1 | X1e | 
X2idn | X2iedn
• Storage Optimized: D3 | I3 | I3en | I3p | I4i | I7i | I7ie
• Accelerated Computing: F1 | G4dn | G6 | Gr6 | Inf1 | P2 | P3 | P3dn | P4d | P5 | P5en
• High Performance Computing: Hpc6a | Hpc6id | Hpc7a | Hpc7g
• Previous Generation: C4 | G3 | M4 | R4
AWS GovCloud (US-West) 640
Amazon EC2 Instance Types
Instances built on the AWS Nitro System
End of sale notice
The U-9tb1, U-12tb1, U-18tb1, and U-24tb1 instance types are no longer available for new 
instance launches. If your workload requires a high-memory instance, we recommend that 
you use a U7i instance type instead.
The Nitro System is a collection of hardware and software components built by AWS that enable 
high performance, high availability, and high security.
The Nitro System provides bare metal capabilities that eliminate virtualization overhead and 
support workloads that require full access to host hardware. Bare metal instances are well suited 
for the following:
• Workloads that require access to low-level hardware features (for example, Intel VT) that are not 
available or fully supported in virtualized environments
• Applications that require a non-virtualized environment for licensing or support
Nitro components
The following components are part of the Nitro System:
• Nitro card
• Local NVMe storage volumes
• Networking hardware support
• Management
• Monitoring
• Security
• Nitro security chip, integrated into the motherboard
• Nitro hypervisor - A lightweight hypervisor that manages memory and CPU allocation and 
delivers performance that is indistinguishable from bare metal for most workloads.
For more information, see AWS Nitro System.
Nitro components 641
Amazon EC2 Instance Types
Network feature support
The following content summarizes key networking capabilities for each version of the Nitro 
System. Versions are shown in descending version release order. If you know the instance type 
family that your instance belongs to, you can expand the Speciﬁcations section and select your 
instance family. The Platform summary table for your instance family shows the Nitro version for 
your instance type in the Hypervisor column.
If you're not sure which instance family applies, see the Naming conventions section.
Note
Features are cumulative, meaning that newer versions of the Nitro system support the 
features that are listed in all prior versions, except where explicitly stated otherwise.
See the Nitro instance requirements section for the minimum ENA driver and Linux kernel 
versions for optimal performance of Nitro v4 and later instance types.
Nitro v6
• Traﬃc Mirroring is not supported.
• Up to 400 Gbps* per network card.
Nitro v5
• Traﬃc Mirroring is not supported.
• Up to 200 Gbps* per network card.
Nitro v4
• GPU accelerated and Trainium based instance types support up to 100 Gbps* per network card 
for consistency. Other instance types support up to 170 Gbps* per network card.
• Supports ENA Express. For more information about ENA Express, including what speciﬁc instance 
types support it see Improve network performance with ENA Express on your EC2 instances in 
the Amazon EC2 User Guide.
• Supports RDMA read and RDMA write for select instance types. For more information, see  Elastic 
Fabric Adapter.
Network feature support 642
Amazon EC2 Instance Types
• Traﬃc Mirroring is supported.
Nitro v3
• Up to 100 Gbps* per network card.
• Encryption in transit.
• Traﬃc Mirroring is supported.
Nitro v2
• Enhanced networking with Elastic Network Adapter (ENA).
• Traﬃc Mirroring is supported.
* Your instance type might support a lower maximum bandwidth. For more information, refer to the 
network speciﬁcations for your instance type in the instance family pages.
Virtualized instances
The following virtualized instances are built on the Nitro System:
Nitro v6
• General Purpose: M8a | M8azn | M8gb | M8gn | M8i | M8id | M8i-ﬂex
• Compute Optimized: C8a | C8gb | C8gn | C8i | C8id | C8i-ﬂex
• Memory Optimized: R8a | R8gb | R8gn | R8i | R8id | R8i-ﬂex | X8aedz | X8i
• Storage Optimized: I8ge
• Accelerated Computing: G7e | P6-B200 | P6-B300
• High Performance Computing: Hpc8a
Nitro v5
• General Purpose: M8g | M8gd
• Compute Optimized: C7gn | C8g | C8gd
• Memory Optimized: R8g | R8gd | X8g
Virtualized instances 643
Amazon EC2 Instance Types
• Storage Optimized: I7ie | I8g
• Accelerated Computing: P5en | P6e-GB200 | Trn2 | Trn2u
• High Performance Computing: Hpc7g
Nitro v4
• General Purpose: M6a | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex
• Compute Optimized: C6a | C6gn | C6i | C6id | C6in | C7a | C7g | C7gd | C7i | C7i-ﬂex
• Memory Optimized: R6a | R6i | R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | U7i-6tb | 
U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X2idn | X2iedn
• Storage Optimized: I4g | I4i | I7i | Im4gn | Is4gen
• Accelerated Computing: F2 | G6 | G6e | G6f | Gr6 | Gr6f | Inf2 | P5 | P5e | Trn1 | Trn1n
• High Performance Computing: Hpc6a | Hpc6id | Hpc7a
Nitro v3
• General Purpose: M5dn | M5n | M5zn
• Compute Optimized: C5n
• Memory Optimized: R5dn | R5n | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | 
X2iezn
• Storage Optimized: D3 | D3en | I3en
• Accelerated Computing: DL1 | DL2q | G4ad | G4dn | G5 | Inf1 | P4d | P4de | VT1 | P3dn
• Previous Generation: P3dn
Nitro v2
• General Purpose: M5 | M5a | M5ad | M5d | M6g | M6gd | T3 | T3a | T4g | A1
• Compute Optimized: C5 | C5a | C5ad | C5d | C6g | C6gd
• Memory Optimized: R5 | R5a | R5ad | R5b | R5d | R6g | R6gd | X2gd | z1d
• Accelerated Computing: G5g
• Previous Generation: A1
Virtualized instances 644
Amazon EC2 Instance Types
Bare metal instances
The following bare metal instances are built on the Nitro System:
Nitro v6
• General Purpose: M8a | M8azn | M8gb | M8gn | M8i | M8id
• Compute Optimized: C8a | C8gb | C8gn | C8i | C8id
• Memory Optimized: R8a | R8gb | R8gn | R8i | R8id | X8aedz | X8i
• Storage Optimized: I8ge
Nitro v5
• General Purpose: M8g | M8gd | Mac-m4 | Mac-m4pro
• Compute Optimized: C7gn | C8g | C8gd
• Memory Optimized: R8g | R8gd | X8g
• Storage Optimized: I7ie | I8g
Nitro v4
• General Purpose: M6a | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i
• Compute Optimized: C6a | C6i | C6id | C6in | C7a | C7g | C7gd | C7i
• Memory Optimized: R6a | R6i | R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | X2idn | 
X2iedn
• Storage Optimized: I4i | I7i
Nitro v3
• General Purpose: M5dn | M5n | M5zn
• Compute Optimized: C5n
• Memory Optimized: R5dn | R5n | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | X2iezn
• Storage Optimized: I3en
• Accelerated Computing: G4dn
Bare metal instances 645
Amazon EC2 Instance Types
Nitro v2
• General Purpose: M5 | M5d | M6g | M6gd | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-
m2pro | A1
• Compute Optimized: C5 | C5d | C6g | C6gd
• Memory Optimized: R5 | R5b | R5d | R6g | R6gd | X2gd | z1d
• Storage Optimized: I3
• Accelerated Computing: G5g
• Previous Generation: A1
In most cases, when you launch a bare metal instance, the underlying server goes through its boot 
process, during which it veriﬁes all hardware and ﬁrmware components. This means that it can 
take up to 20 minutes or more from the time the instance enters the running state until it becomes 
available over the network.
Nitro instance requirements
Instances built on the AWS Nitro System use ENA for enhanced networking, and storage volumes 
exposed as NVMe block devices. For more information about NVMe drivers, see Install or upgrade 
the NVMe driver in the Amazon EBS User Guide for Linux instances, or AWS NVMe drivers for 
Windows instances in the Amazon EC2 User Guide. For more information about ENA drivers, see
Requirements for enhanced networking with ENA in the Amazon EC2 User Guide.
The following tabs show details about which driver or kernel versions are recommended for your 
operating system.
Linux
The ENA Linux kernel driver version 2.2.9g or later, from the Amazon Drivers GitHub repository 
is recommended for Nitro v4 instance types and required for Nitro v5 (or later) instance types 
for Linux distributions that expose the version information. ENA drivers for Linux are available 
on GitHub. For more information, see Linux kernel driver for Elastic Network Adapter (ENA) 
family. For release notes, see ENA Linux Kernel Driver Release notes.
Linux distributions can also incorporate ENA driver features within the kernel. However, the 
timing may vary for implementation within the diﬀerent distributions. The Amazon Linux 2023 
Nitro instance requirements 646
Amazon EC2 Instance Types
and Bottlerocket Linux distributions support ENA features for Nitro v4 and newer instance types 
by default.
Some Linux distributions might require a minimum kernel version to prevent suboptimal 
performance of ENA driver features on Nitro v4 and newer instance types. If your Linux 
distribution appears in the following table, you can verify the kernel version for your instance 
with the uname command as follows:
uname -r
Linux distribution Minimum kernel version
Linux upstream Kernel version 5.9
Amazon Linux 2 Kernel 4.14.186
Red Hat Enterprise Linux (RHEL) RHEL 8.4 kernel 4.18.0-305
SUSE Linux Enterprise Server (SLES)
•
SLE 12 SP4 kernel 4.12.14-95.99.3
•
SLE 12 SP5 kernel 4.12.14-122.116.1
•
SLE 15 kernel 4.12.14-150000.150.92.2
•
SLE 15 SP1 kernel 4.12.14-150100.197 
.114.2
•
SLE 15 SP2 kernel 5.3.18-24.15.1
Linux Ubuntu 20.04 kernel 5.4.0-1025-aws
Debian 11 (Bullseye) kernel 5.10.0
DPDK v20.11
Nitro instance requirements 647
Amazon EC2 Instance Types
Note
The following ENA Linux driver versions are not supported, and will result in elastic 
network interface attachment failures:
• ENA Linux
• Nitro v5 – Earlier than 2.2.9
• All Nitro versions prior to v5 – Earlier than v1.2.0
• ENA DPDK
• Nitro v5 – Earlier than 20.11
• All Nitro versions prior to v5 – Earlier than v1.1.1
Windows
ENA Windows driver version: 2.2.3 or later for Windows instances.
Note
The following ENA Windows drivers are not supported:
• ENA Windows: v2.2.0 or earlier
All of the current AWS Windows AMIs meet these requirements. For more information about 
AMI versions and release notes, see the AWS Windows AMI reference.
FreeBSD
ENA FreeBSD driver version: 2.3.1 or later for FreeBSD instances.
Note
ENA FreeBSD driver versions earlier than v2.3.1 are not supported, and will result in 
elastic network interface attachment failures.
Nitro instance requirements 648
Amazon EC2 Instance Types
Linux instances with AWS Graviton processors
Linux instances with AWS Graviton processors have the following additional requirements:
• An AMI with 64-bit ARM architecture.
• Support for UEFI boot with ACPI tables and ACPI hot-plug of PCI devices.
Note
AWS Graviton processors only support Linux operating systems.
Linux instances with AWS Graviton processors 649
Amazon EC2 Instance Types
Amazon EC2 instance type quotas
Your AWS account has quotas that aﬀect the number of instances that you can run in each Region. 
These quotas are grouped by purchasing option.
Quotas
• On-Demand Instance quotas
• Spot Instance quotas
• Dedicated Host quotas
• Capacity Blocks quotas
On-Demand Instance quotas
The following table shows the maximum number of vCPUs that you can provision for On-Demand 
Instances. Amazon EC2 automatically increases your On-Demand Instance quotas based on your 
usage. You can also request a quota increase. For more information, see On-Demand Instance 
quotas in the Amazon EC2 User Guide.
Name Default Adjustable
Running On-Demand DL instances 0 Yes
Running On-Demand F instances 0 Yes
Running On-Demand G and VT instances 0 Yes
Running On-Demand HPC instances 0 Yes
Running On-Demand High Memory instances 0 Yes
Running On-Demand Inf instances 0 Yes
Running On-Demand P instances 0 Yes
Running On-Demand Standard (A, C, D, H, I, M, R, T, 
Z) instances
5 Yes
On-Demand Instance quotas 650
Amazon EC2 Instance Types
Name Default Adjustable
Running On-Demand Trn instances 0 Yes
Running On-Demand X instances 0 Yes
Spot Instance quotas
The following table shows the maximum number of vCPUs that you can provision for Spot 
Instances. Amazon EC2 automatically increases your Spot Instance quotas based on your usage. 
You can also request a quota increase. For more information, see Spot Instance quotas in the
Amazon EC2 User Guide.
Name Default Adjustable
All DL Spot Instance Requests 0 Yes
All F Spot Instance Requests 0 Yes
All G and VT Spot Instance Requests 0 Yes
All Inf Spot Instance Requests 0 Yes
All P Spot Instance Requests 0 Yes
All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance 
Requests
5 Yes
All Trn Spot Instance Requests 0 Yes
All X Spot Instance Requests 0 Yes
Dedicated Host quotas
The following table shows the maximum number of running Dedicated Hosts that you can allocate.
Spot Instance quotas 651
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated a1 Hosts 0 Yes
Running Dedicated c1 Hosts 0 Yes
Running Dedicated c3 Hosts 0 Yes
Running Dedicated c4 Hosts 0 Yes
Running Dedicated c5 Hosts 0 Yes
Running Dedicated c5a Hosts 0 Yes
Running Dedicated c5d Hosts 0 Yes
Running Dedicated c5n Hosts 0 Yes
Running Dedicated c6a Hosts 0 Yes
Running Dedicated c6g Hosts 0 Yes
Running Dedicated c6gd Hosts 0 Yes
Running Dedicated c6gn Hosts 0 Yes
Running Dedicated c6i Hosts 0 Yes
Running Dedicated c6id Hosts 0 Yes
Running Dedicated c6in Hosts 0 Yes
Running Dedicated c7a Hosts 0 Yes
Running Dedicated c7g Hosts 0 Yes
Running Dedicated c7gd Hosts 0 Yes
Running Dedicated c7gn Hosts 0 Yes
Running Dedicated c7i Hosts 0 Yes
Dedicated Host quotas 652
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated c7i-ﬂex Hosts 0 Yes
Running Dedicated c8a Hosts 0 Yes
Running Dedicated c8g Hosts 0 Yes
Running Dedicated c8gb Hosts 0 Yes
Running Dedicated c8gd Hosts 0 Yes
Running Dedicated c8gn Hosts 0 Yes
Running Dedicated c8i Hosts 0 Yes
Running Dedicated c8i-ﬂex Hosts 0 Yes
Running Dedicated c8id Hosts 0 Yes
Running Dedicated d2 Hosts 0 Yes
Running Dedicated dl1 Hosts 0 Yes
Running Dedicated f1 Hosts 0 Yes
Running Dedicated f2 Hosts 0 Yes
Running Dedicated g4ad Hosts 0 Yes
Running Dedicated g4dn Hosts 0 Yes
Running Dedicated g5 Hosts 0 Yes
Running Dedicated g5g Hosts 0 Yes
Running Dedicated g6 Hosts 0 Yes
Running Dedicated g6e Hosts 0 Yes
Running Dedicated g6f Hosts 0 Yes
Dedicated Host quotas 653
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated g7e Hosts 0 Yes
Running Dedicated gr6 Hosts 0 Yes
Running Dedicated gr6f Hosts 0 Yes
Running Dedicated h1 Hosts 0 Yes
Running Dedicated i2 Hosts 0 Yes
Running Dedicated i3 Hosts 0 Yes
Running Dedicated i3en Hosts 0 Yes
Running Dedicated i4g Hosts 0 Yes
Running Dedicated i4i Hosts 0 Yes
Running Dedicated i7i Hosts 0 Yes
Running Dedicated i7ie Hosts 0 Yes
Running Dedicated i8g Hosts 0 Yes
Running Dedicated i8ge Hosts 0 Yes
Running Dedicated im4gn Hosts 0 Yes
Running Dedicated inf Hosts 0 Yes
Running Dedicated inf2 Hosts 0 Yes
Running Dedicated is4gen Hosts 0 Yes
Running Dedicated m1 Hosts 0 Yes
Running Dedicated m2 Hosts 0 Yes
Running Dedicated m3 Hosts 0 Yes
Dedicated Host quotas 654
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated m4 Hosts 0 Yes
Running Dedicated m5 Hosts 0 Yes
Running Dedicated m5a Hosts 0 Yes
Running Dedicated m5ad Hosts 0 Yes
Running Dedicated m5d Hosts 0 Yes
Running Dedicated m5dn Hosts 0 Yes
Running Dedicated m5n Hosts 0 Yes
Running Dedicated m5zn Hosts 0 Yes
Running Dedicated m6a Hosts 0 Yes
Running Dedicated m6g Hosts 0 Yes
Running Dedicated m6gd Hosts 0 Yes
Running Dedicated m6i Hosts 0 Yes
Running Dedicated m6id Hosts 0 Yes
Running Dedicated m6idn Hosts 0 Yes
Running Dedicated m6in Hosts 0 Yes
Running Dedicated m7a Hosts 0 Yes
Running Dedicated m7g Hosts 0 Yes
Running Dedicated m7gd Hosts 0 Yes
Running Dedicated m7i Hosts 0 Yes
Running Dedicated m8a Hosts 0 Yes
Dedicated Host quotas 655
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated m8azn Hosts 0 Yes
Running Dedicated m8g Hosts 0 Yes
Running Dedicated m8gb Hosts 0 Yes
Running Dedicated m8gd Hosts 0 Yes
Running Dedicated m8gn Hosts 0 Yes
Running Dedicated m8i Hosts 0 Yes
Running Dedicated m8id Hosts 0 Yes
Running Dedicated mac-m4 Hosts 0 Yes
Running Dedicated mac-m4max Hosts 0 Yes
Running Dedicated mac-m4pro Hosts 0 Yes
Running Dedicated mac1 Hosts 0 Yes
Running Dedicated mac2 Hosts 0 Yes
Running Dedicated mac2-m1ultra Hosts 0 Yes
Running Dedicated mac2-m2 Hosts 0 Yes
Running Dedicated mac2-m2pro Hosts 0 Yes
Running Dedicated p3 Hosts 0 Yes
Running Dedicated p3dn Hosts 0 Yes
Running Dedicated p4d Hosts 0 Yes
Running Dedicated p4de Hosts 0 Yes
Running Dedicated p5 Hosts 0 Yes
Dedicated Host quotas 656
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated p5en Hosts 0 Yes
Running Dedicated r3 Hosts 0 Yes
Running Dedicated r4 Hosts 0 Yes
Running Dedicated r5 Hosts 0 Yes
Running Dedicated r5a Hosts 0 Yes
Running Dedicated r5ad Hosts 0 Yes
Running Dedicated r5b Hosts 0 Yes
Running Dedicated r5d Hosts 0 Yes
Running Dedicated r5dn Hosts 0 Yes
Running Dedicated r5n Hosts 0 Yes
Running Dedicated r6a Hosts 0 Yes
Running Dedicated r6g Hosts 0 Yes
Running Dedicated r6gd Hosts 0 Yes
Running Dedicated r6i Hosts 0 Yes
Running Dedicated r6id Hosts 0 Yes
Running Dedicated r6idn Hosts 0 Yes
Running Dedicated r6in Hosts 0 Yes
Running Dedicated r7a Hosts 0 Yes
Running Dedicated r7g Hosts 0 Yes
Running Dedicated r7gd Hosts 0 Yes
Dedicated Host quotas 657
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated r7i Hosts 0 Yes
Running Dedicated r7iz Hosts 0 Yes
Running Dedicated r8a Hosts 0 Yes
Running Dedicated r8g Hosts 0 Yes
Running Dedicated r8gb Hosts 0 Yes
Running Dedicated r8gd Hosts 0 Yes
Running Dedicated r8gn Hosts 0 Yes
Running Dedicated r8i Hosts 0 Yes
Running Dedicated r8i-ﬂex Hosts 0 Yes
Running Dedicated r8id Hosts 0 Yes
Running Dedicated t1 Hosts 0 Yes
Running Dedicated t2 Hosts 0 Yes
Running Dedicated t3 Hosts 0 Yes
Running Dedicated trn1 Hosts 0 Yes
Running Dedicated trn1n Hosts 0 Yes
Running Dedicated u-3tb1 Hosts 0 Yes
Running Dedicated u-6tb1 Hosts 0 Yes
Running Dedicated u7i-12tb Hosts 0 Yes
Running Dedicated u7i-6tb Hosts 0 Yes
Running Dedicated u7i-8tb Hosts 0 Yes
Dedicated Host quotas 658
Amazon EC2 Instance Types
Name Default Adjustable
Running Dedicated u7in-16tb Hosts 0 Yes
Running Dedicated u7in-24tb Hosts 0 Yes
Running Dedicated u7in-32tb Hosts 0 Yes
Running Dedicated vt1 Hosts 0 Yes
Running Dedicated x1 Hosts 0 Yes
Running Dedicated x1e Hosts 0 Yes
Running Dedicated x2gd Hosts 0 Yes
Running Dedicated x2idn Hosts 0 Yes
Running Dedicated x2iedn Hosts 0 Yes
Running Dedicated x2iezn Hosts 0 Yes
Running Dedicated x8g Hosts 0 Yes
Running Dedicated x8i Hosts 0 Yes
Running Dedicated z1d Hosts 0 Yes
Capacity Blocks quotas
The following table shows the maximum number of vCPUs for concurrently active Capacity Blocks.
Name Default Adjustable
Concurrent P4d Capacity Blocks per account 0 Yes
Concurrent P4d Capacity Blocks per organization 0 Yes
Concurrent P5 Capacity Blocks per account 0 Yes
Capacity Blocks quotas 659
Amazon EC2 Instance Types
Name Default Adjustable
Concurrent P5 Capacity Blocks per organization 0 Yes
Concurrent P5e Capacity Blocks per account 0 Yes
Concurrent P5e Capacity Blocks per organization 0 Yes
Concurrent P5en Capacity Blocks per account 0 Yes
Concurrent P5en Capacity Blocks per organization 0 Yes
Concurrent Trn1 Capacity Blocks per account 0 Yes
Concurrent Trn1 Capacity Blocks per organization 0 Yes
Concurrent Trn2 Capacity Blocks per account 0 Yes
Concurrent Trn2 Capacity Blocks per organization 0 Yes
Capacity Blocks quotas 660
Amazon EC2 Instance Types
Document history for the Amazon EC2 Instance Types 
Guide
The following table describes the instance type releases for Amazon EC2.
Change Description Date
I8g bare metal instances New metal-48xl  bare 
metal instance type for I8g, 
powered by AWS Graviton4 
processors.
February 26, 2026
M8gn and M8gb bare metal 
instances
New metal-24xl  and
metal-48xl  bare metal 
instance types for M8gn and 
M8gb.
February 25, 2026
Hpc8a instances New high performance 
computing optimized 
instances powered by ﬁfth 
generation AMD EPYC 
Processors (Turin) with a 
maximum CPU frequency of 
4.5 GHz.
February 16, 2026
M8azn instances New general purpose instance 
types powered by ﬁfth 
generation AMD EPYC 
Processors (Turin) with a 
maximum CPU frequency of 
5 GHz. These instance types 
feature improved network 
performance, with up to 200 
Gbps network throughput.
February 12, 2026
M8id, C8id, and R8id 
instances
New general purpose, 
compute optimized, and 
February 4, 2026
661
Amazon EC2 Instance Types
memory optimized instances 
that feature custom sixth 
generation Intel Xeon 
Scalable Processors (Granite 
Rapids) and up to 22.8 TB of 
SSD instance storage.
G7e instances New accelerated computing 
instances that feature Intel 
Xeon (Emerald Rapids) 
processors, up to 2048 GiB 
memory, and up to 8 NVIDIA 
RTX PRO Server 6000 GPUs 
with up to 768 GiB GPU 
memory.
January 20, 2026
X8i instances New memory optimized 
virtualized and bare metal 
instances types that feature 
custom sixth generation Intel 
Xeon Scalable Processors 
(Granite Rapids).
January 15, 2026
M8gn instances New general purpose 
instances types powered by 
AWS Graviton4 processors 
and the AWS Nitro v6 card. 
These instance types feature 
improved network performan 
ce, with up to 600 Gbps 
network throughput.
December 17, 2025
662
Amazon EC2 Instance Types
M8gb instances New general purpose 
instances types powered by 
AWS Graviton4 processor 
s and the AWS Nitro v6 
card. These instance types 
provide improved Amazon 
EBS performance, with up to 
150 Gbps EBS throughput 
and 720,00 IOPS.
December 17, 2025
C8gb instances New compute optimized 
instance types powered by 
AWS Graviton4 processors, 
and that deliver up to 150 
Gbps Amazon EBS throughpu 
t.
December 10, 2025
X8aedz instances New memory optimized 
instance types powered by 
ﬁfth generation AMD EPYC 
Processors (Turin), with a 
maximum CPU frequency 
of 5 GHz, up to 3072 GiB 
of memory, and up to 7600 
GB of NVMe SSD instance 
storage.
December 2, 2025
C8a instances New compute optimized 
instance types powered by 
ﬁfth generation AMD EPYC 
Processors (Turin), with a 
maximum CPU frequency of 
4.5 GHz, and up to 384 GiB of 
memory.
December 2, 2025
663
Amazon EC2 Instance Types
P6-B300 instances Latest generation GPU 
instances featuring Nvidia 
B300 GPUs for large scale ML 
training, Inference and HPC 
workloads.
November 18, 2025
R8a instances New memory optimized 
instance types powered by 
ﬁfth generation AMD EPYC 
Processors (Turin), with a 
maximum CPU frequency of 
4.5 GHz, and up to 1,536 GiB 
of memory.
November 4, 2025
M8a instances New general purpose instance 
types powered by ﬁfth 
generation AMD EPYC 
Processors (Turin) with a 
maximum CPU frequency of 
4.5 GHz.
October 8, 2025
C8i-ﬂex instances New compute optimized Flex 
instances that feature custom 
sixth generation Intel Xeon 
Scalable Processors (Granite 
Rapids). Flex instances deliver 
a baseline CPU performan 
ce of 40 percent with the 
ability to deliver up to 100 
percent CPU performance for 
95 percent of the time over a 
24-hour period.
October 6, 2025
664
Amazon EC2 Instance Types
C8i instances New compute optimized 
instance types that feature 
custom sixth generation Intel 
Xeon Scalable Processors 
(Granite Rapids).
October 6, 2025
Updated network performan 
ce for I7i and I8g
I7i and I8g instance types
.8xlarge and larger no 
longer use the network 
I/O credit mechanism to 
burst beyond their baseline 
bandwidth. They now sustain 
their maximum performance 
indeﬁnitely.
September 24, 2025
R8gb instances New memory optimized 
instance types powered by 
AWS Graviton4 processors, 
and that feature improved 
Amazon EBS performance 
with up to 300 Gbps EBS 
throughput and 1,440,000 
IOPS.
September 23, 2025
R8gn instances New memory optimized 
instance types powered by 
AWS Graviton4 processors, 
and that feature up to 1536 
GiB of memory.
September 15, 2025
665
Amazon EC2 Instance Types
M4 Pro Mac instances New general purpose Mac 
instances built on 2024 Mac 
mini hardware powered 
by Apple silicon M4 Pro 
processors, 14 CPU cores, 20 
GPU cores, 48 GiB of memory, 
and the 16-core Apple Neural 
Engine.
September 11, 2025
M4 Mac instances New general purpose Mac 
instances built on 2024 Mac 
mini hardware powered by 
Apple silicon M4 processors, 
10 CPU cores, 10 GPU cores, 
24 GiB of memory, and the 
16-core Apple Neural Engine.
September 11, 2025
I8ge instances New storage optimized 
instance family based on 
the latest third generation 
AWS Nitro SSDs and AWS 
Graviton4 Processor. I8ge 
oﬀers up to 192 vCPUs, 
1536 GB memory, and up to 
120TB storage. I8ge instances 
are optimized for storage 
intensive workloads such as 
NoSQL databases, distributed 
ﬁle systems, search engines, 
and data analytics.
August 29, 2025
666
Amazon EC2 Instance Types
M8i-ﬂex instances New general purpose Flex 
instances that feature custom 
sixth generation Intel Xeon 
Scalable Processors (Granite 
Rapids). Flex instances deliver 
a baseline CPU performan 
ce of 40 percent with the 
ability to deliver up to 100 
percent CPU performance for 
95 percent of the time over a 
24-hour period.
August 28, 2025
M8i instances New general purpose instance 
types that feature custom 
sixth generation Intel Xeon 
Scalable Processors (Granite 
Rapids).
August 28, 2025
R8i-ﬂex instances New memory optimized 
Flex instances that feature 
custom sixth generation Intel 
Xeon Scalable Processors 
(Granite Rapids) and up to 
512 GiB of memory. Flex 
instances deliver a baseline 
CPU performance of 40 
percent with the ability to 
deliver up to 100 percent CPU 
performance for 95 percent 
of the time over a 24-hour 
period.
August 19, 2025
667
Amazon EC2 Instance Types
R8i instances New memory optimized 
instance types that feature 
custom sixth generation Intel 
Xeon Scalable Processors 
(Granite Rapids) and up to 3 
TiB of memory.
August 19, 2025
P5 instance new size New p5.4xlarge  instance 
type enables smaller size with 
one GPU.
August 12, 2025
G6f, Gr6f instances New G6f and Gr6f instance 
types can lower GPU 
computing costs by oﬀering 
fractional GPU proﬁles that 
better match your workload 
requirements, making GPU-
accelerated workstations and 
graphics applications more 
cost-eﬀective for use cases 
that don't require full GPU 
capacity.
July 29, 2025
P6e-GB200 instances New GPU instances featuring 
NVIDIA GB200 superchip 
s for the highest available 
GPU-based AI training and 
inference performance.
July 10, 2025
C8gn instances New compute optimized 
instances types powered by 
AWS Graviton4 processors, 
and that support up to to 600 
Gbps networking.
June 30, 2025
668
Amazon EC2 Instance Types
U-9tb1, U-12tb1, U-18tb1, 
and U-24tb1 end of sale
The U-9tb1, U-12tb1, 
U-18tb1, and U-24tb1 
instance types are no longer 
available for new instance 
launches. If your workload 
requires a high-memory 
instance, we recommend that 
you use a U7i instance type 
instead.
June 20, 2025
P6-B200 instances New GPU instances featuring 
NVIDIA B200 GPUs for large 
scale ML Training/inference 
and HPC.
May 15, 2025
I7i instances New storage optimized 
virtualized and bare 
metal instance types that 
feature Intel Emerald 
Rapids processors and third 
generation AWS Nitro SSD-
based instance storage.
April 25, 2025
M8gd, C8gd, R8gd instances New general purpose (M8gd), 
compute optimized (C8gd), 
and memory optimized 
(R8gd) virtualized and bare 
metal instances powered by 
AWS Graviton4 processors, 
and that feature NVMe SSD 
instance storage.
April 21, 2025
669
Amazon EC2 Instance Types
I7ie bare metal instances New i7ie.metal-24xl
and i7ie.metal-48xl
bare metal instance types 
that feature the 5th generatio 
n Intel Xeon Scalable 
processors (Emerald Rapids), 
and the 3rd generation AWS 
Nitro SSDs.
April 10, 2025
GovCloud now supports R8g The GovCloud Regions now 
support the R8g instance 
type.
March 31, 2025
GovCloud now supports R8g The GovCloud Regions now 
support the R8g instance 
type.
March 31, 2025
New F2 instance type F2 is now available in the 
following instance size:
6xlarge.
February 5, 2025
New C7i-ﬂex and M7i-ﬂex 
instance types
C7i-ﬂex and M7i-ﬂex are now 
available in 12xlarge and
16xlarge instance sizes.
January 16, 2025
U7inh-32tb instances New high memory instance 
types that feature 1,920 
vCPUs of 4th generation Intel 
Xeon Scalable Processors 
(Sapphire Rapids) with 32 TiB 
of memory.
December 16, 2024
670
Amazon EC2 Instance Types
F2 instances New accelerated computing 
instance type for the latest 
generation FPGA instances 
that feature AMD-Xilinx 
VU47P HBM FPGA accelerat 
ors for genomics and 
multimedia processing.
December 11, 2024
U7i-6tb, and U7i-8tb 
instances
New high memory instance 
types that feature 4th 
generation Intel Xeon 
Scalable processors.
December 9, 2024
Trn2 instances New accelerated instance 
types that feature up to 
16x Trainium2 chips and 
deliver up to 4 times faster 
performance than Trn1 
instances.
December 3, 2024
P5en instances GPU instances featuring 
NVIDIA H200 GPUs for large 
scale ML Training/inference 
and HPC.
December 2, 2024
I8g instances New storage optimized 
instances powered by AWS 
Graviton4 processors.
December 1, 2024
I7ie instances New storage optimized 
instances that feature the 
5th generation Intel Xeon 
Scalable processors (Emerald 
Rapids), and the 3rd generatio 
n AWS Nitro SSDs.
December 1, 2024
671
Amazon EC2 Instance Types
M8g instances New general purpose 
instances powered by AWS 
Graviton4 processors.
September 25, 2024
C8g instances New compute optimized 
instances powered by AWS 
Graviton4 processors.
September 25, 2024
X8g instances New memory optimized 
instances powered by AWS 
Graviton4 processors.
September 18, 2024
P5e instances New accelerated computing 
instance type for the latest 
generation GPU instances 
featuring NVIDIA H200 GPUs 
for large scale ML Training/ 
inference and HPC.
September 9, 2024
G6e instances New accelerated computing 
instances that feature up to 
8 NVIDIA L40S GPUs, which 
oﬀer 48 GB of GPU memory.
August 15, 2024
Nitro version features Updated Nitro page to include 
features and instance types 
by Nitro version. Added Nitro 
version to the Hyperviso 
r column in the Platform 
summary tables also.
July 22, 2024
R8g instances New memory optimized 
instances powered by AWS 
Graviton4 processors and up 
to 1.5 TiB memory.
July 9, 2024
672
Amazon EC2 Instance Types
Mac2-m1ultra instances New general purpose instance 
type that features Apple M1 
Ultra processors.
June 17, 2024
U7i-12tb, U7in-16tb, 
U7in-24tb, and U7in-32tb 
instances
New high memory instance 
types that feature 4th 
generation Intel Xeon 
Scalable processors.
May 28, 2024
C7i-ﬂex instances New compute optimized 
instances featuring Intel Xeon 
Scalable processors (Sapphire 
Rapids). They deliver a 
baseline CPU performance of 
40 percent with the ability to 
deliver up to 100 percent CPU 
performance for 95 percent 
of the time over a 24-hour 
period.
May 14, 2024
G6 and Gr6 instances New high performance GPU-
based instance types for 
deep learning inference and 
graphics-intensive applicati 
ons.
April 4, 2024
C7gn bare metal instances New c7gn.metal  bare 
metal instance type powered 
by the latest generation AWS 
Graviton3E processors and 
the new AWS Nitro cards.
March 26, 2024
C7gd, M7gd, and R7gd bare 
metal instances
New bare metal instances. March 6, 2024
673
Amazon EC2 Instance Types
DL2q instances New instances that use 
Qualcomm AI100 inference 
accelerators, which feature 
7th generation Qualcomm 
Edge AI cores. These instances 
can be used to cost-eﬃciently 
deploy deep learning (DL) 
workloads in the cloud or 
validate performance and 
accuracy of DL workloads 
that will be deployed on 
Qualcomm edge devices.
November 15, 2023
Mac2-m2 instances New general purpose instance 
type that features Apple M2 
processors.
October 25, 2023
R7i instances New memory optimized 
instance types that feature 
4th generation Intel Xeon 
Scalable processors.
October 16, 2023
C7a instances New compute optimized 
instances powered by 4th 
generation AMD EPYC 
processors.
October 4, 2023
Mac2-m2pro instances New general purpose instance 
type that features Apple M2 
Pro processors.
September 18, 2023
C7i instances New compute optimized 
instance types that feature 
4th generation Intel Xeon 
Scalable processors.
September 14, 2023
674
Amazon EC2 Instance Types
R7a instances New memory optimized 
instance types featuring 4th 
generation AMD EPYC 9R14 
processors and up to 1536 
GiB of system memory.
September 11, 2023
R7iz instances New high-frequency and high 
memory instances powered 
by 4th generation Intel Xeon 
processors.
September 7, 2023
Hpc7a instances New compute optimized 
instance types that feature 
4th generation AMD EPYC 
processors. These instances 
support up to 300 Gbps 
networking bandwidth, and 
up to 192 CPU cores with up 
to 768 GB of system memory.
August 17, 2023
M7a instances New general purpose 
instances powered by 4th 
generation AMD EPYC 
processors.
August 15, 2023
M7i-ﬂex instances New general purpose 
instances that oﬀer a balance 
of compute, memory, and 
network resources for a broad 
spectrum of general purpose 
applications. They deliver a 
baseline CPU performance of 
40 percent with the ability to 
deliver up to 100 percent CPU 
performance for 95 percent 
of the time over a 24-hour 
period.
August 2, 2023
675
Amazon EC2 Instance Types
M7i instances New general purpose 
instance types that feature 
4th generation Intel Xeon 
Scalable processors.
August 2, 2023
R7gd instances New memory optimized 
instances featuring the latest 
AWS Graviton3 processors.
July 28, 2023
M7gd instances New general purpose 
instances featuring the latest 
AWS Graviton3 processors.
July 28, 2023
C7gd instances New compute optimized 
instances featuring the latest 
AWS Graviton3 processors.
July 28, 2023
P5 instances New accelerated computing 
instances that feature 8 
NVIDIA H100 GPUs with 640 
GB high-bandwidth GPU 
memory, 3rd generation AMD 
EPYC processors, and 2 TB 
system memory.
July 26, 2023
Hpc7g instances New high-performance 
computing instances powered 
by AWS Graviton3E processor 
s that provide up to 35 
percent higher vector-
instruction processing 
performance than Graviton3 
processors.
June 20, 2023
676
Amazon EC2 Instance Types
C7gn instances New compute optimized 
instances powered by the 
latest generation AWS 
Graviton3E processors and 
the new AWS Nitro cards. 
These instances oﬀer up to 
200 Gbps network bandwidth.
June 20, 2023
I4g instances New storage optimized 
instances that features the 
AWS Graviton2 processor and 
AWS Nitro SSDs.
May 9, 2023
Trn1n instances New accelerated computing 
instances optimized for 
machine learning training 
powered by AWS Trainium 
accelerators.
April 13, 2023
Inf2 instances New instances featuring AWS 
Inferentia2 accelerators, the 
latest machine learning chip 
designed by AWS.
April 13, 2023
M7g and R7g instances New instances featuring AWS 
Graviton3 processors.
February 12, 2023
Hpc6id instance New memory optimized 
instance featuring 3rd 
generation Intel Xeon 
Scalable processors (Ice Lake).
November 29, 2022
R6in and R6idn instances New memory optimized 
instances for network-i 
ntensive workloads.
November 28, 2022
M6in and M6idn instances New general computing 
instances types.
November 28, 2022
677
Amazon EC2 Instance Types
C6in instances New compute optimized 
instances ideal for running 
high performance computing.
November 28, 2022
Trn1 instances New accelerated computing 
instances optimized for deep 
learning powered by AWS 
Trainium chips.
October 10, 2022
R6a instances New memory optimized 
instances featuring 3rd 
generation AMD EPYC 
processors.
July 19, 2022
R6id instances New memory optimized 
instances featuring 3rd 
generation Intel Xeon 
Scalable processors (Ice Lake).
June 9, 2022
P4de instances New accelerated computing 
instances featuring 640GB of 
GPU memory.
May 26, 2022
M6id instances New general purpose 
instances featuring 3rd 
generation Intel Xeon 
Scalable processors (Ice Lake).
May 26, 2022
C6id instances New compute optimized 
instances featuring 3rd 
generation Intel Xeon 
Scalable processors (Ice Lake).
May 26, 2022
C7g instances New compute optimized 
instances featuring AWS 
Graviton3 processors.
May 23, 2022
678
Amazon EC2 Instance Types
I4i instances New storage optimized 
instances featuring 3rd 
generation Intel Xeon 
Scalable processors (Ice Lake).
April 27, 2022
X2idn and X2iedn instances New memory optimized 
instances featuring Intel Xeon 
Scalable processors (Ice Lake).
March 10, 2022
C6a instances New compute optimized 
instances featuring 3rd 
generation AMD EPYC 
processors (Milan).
February 14, 2022
X2iezn instances New memory optimized 
instances featuring Intel Xeon 
Platinum processors (Cascade 
Lake).
January 26, 2022
Hpc6a instances New compute optimized 
instances featuring AMD EPYC 
processors.
January 10, 2022
Im4gn and Is4gen instances New storage optimized 
instances.
November 30, 2021
M6a instances New general purpose 
instances powered by 
AMD 3rd Generation EPYC 
processors.
November 29, 2021
G5g instances New accelerated computing 
instances featuring AWS 
Graviton2 processors based 
on 64-bit Arm architecture.
November 29, 2021
R6i instances New memory optimized 
instances.
November 22, 2021
679
Amazon EC2 Instance Types
G5 instances New accelerated computing 
instances featuring up to 
8 NVIDIA A10G GPUs and 
second generation AMD EPY 
processors.
November 11, 2021
C6i instances New compute optimized 
instances featuring Intel Xeon 
Scalable processors (Ice Lake).
October 28, 2021
DL1 instances New accelerated computing 
instances featuring Habana 
Gaudi accelerators and Intel 
Xeon Platinum processors 
(Cascade Lake).
October 26, 2021
VT1 instances New accelerated computing 
instances that use Xilinx Alveo 
U30 media accelerators and 
are designed for live video 
transcoding workloads.
September 13, 2021
M6i instances New general purpose 
instances featuring third 
generation Intel Xeon 
Scalable processors (Ice Lake).
August 16, 2021
High memory virtualized 
instances
Virtualized high memory 
instances purpose-built 
to run large in-memory 
databases. The new types are 
u-6tb1.56xlarge, u-6tb1.11 
2xlarge, u-9tb1.112xlarge, 
and u-12tb1.112xlarge.
May 11, 2021
680
Amazon EC2 Instance Types
X2gd instances New memory optimized 
instances featuring an AWS 
Graviton2 processor based on 
64-bit Arm architecture.
March 16, 2021
C6gn instances New computed optimized 
instances featuring an AWS 
Graviton2 processor based 
on 64-bit Arm architecture. 
These instances can utilize 
up to 100 Gbps of network 
bandwidth.
December 18, 2020
G4ad instances New instances powered by 
AMD Radeon Pro V520 GPUs 
and AMD 2nd Generation 
EPYC processors.
December 9, 2020
D3, D3en, M5zn, and R5b 
instances
New instance types built on 
the Nitro System.
December 1, 2020
Mac1 instances New instances built on Apple 
Mac mini computers that 
support running macOS 
workloads on Amazon EC2.
November 30, 2020
P4d instances New accelerated computing 
instances that provide a high-
performance platform for 
machine learning and HPC 
workloads.
November 2, 2020
681
Amazon EC2 Instance Types
T4g instances New general purpose 
instances powered by AWS 
Graviton2 processors, which 
are based on 64-bit Arm 
Neoverse cores and custom 
silicon designed by AWS for 
optimized performance and 
cost.
September 14, 2020
C5ad instances New compute optimized 
instances featuring second-ge 
neration AMD EPYC processor 
s.
August 13, 2020
C6gd, M6gd, and R6gd 
instances
New general purpose 
instances powered by AWS 
Graviton2 processors, which 
are based on 64-bit Arm 
Neoverse cores and custom 
silicon designed by AWS for 
optimized performance and 
cost.
July 27, 2020
C6g and R6g instances New general purpose 
instances powered by AWS 
Graviton2 processors, which 
are based on 64-bit Arm 
Neoverse cores and custom 
silicon designed by AWS for 
optimized performance and 
cost.
June 10, 2020
C5a instances New compute optimized 
instances featuring second-ge 
neration AMD EPYC processor 
s.
June 4, 2020
682
Amazon EC2 Instance Types
M6g instances New general purpose 
instances powered by AWS 
Graviton2 processors, which 
are based on 64-bit Arm 
Neoverse cores and custom 
silicon designed by AWS for 
optimized performance and 
cost.
May 11, 2020
Inf1 instances New instances featuring AWS 
Inferentia, a machine learning 
inference chip designed to 
deliver high performance at a 
low cost.
December 3, 2019
M5dn, M5n, R5dn, and R5n 
instances
New instances featuring 100 
Gbps of network bandwidth.
October 9, 2019
G4dn instances New instances featuring 
NVIDIA Tesla GPUs.
September 19, 2019
I3en instances New I3en instances can utilize 
up to 100 Gbps of network 
bandwidth.
May 8, 2019
T3a instances New instances featuring AMD 
EPYC processors.
April 24, 2019
M5ad and R5ad instances New instances featuring AMD 
EPYC processors.
March 27, 2019
p3dn.24xlarge instances New instances that provide 
100 Gbps of network 
bandwidth.
December 7, 2018
C5n instances New instances that provide 
up to 100 Gbps of network 
bandwidth.
November 26, 2018
683
Amazon EC2 Instance Types
A1 instances New instances featuring Arm-
based processors.
November 26, 2018
R5a instances New instances featuring AMD 
EPYC processors.
November 6, 2018
M5a instances New instances featuring AMD 
EPYC processors.
November 6, 2018
T3 instances New instances featuring AMD 
EPYC processors.
August 21, 2018
z1d instances New memory optimized 
instances.
July 25, 2018
R5 and R5d instances New memory optimized 
instances.
July 25, 2018
M5d instances New compute optimized 
instances.
June 4, 2018
C5d instances New compute optimized 
instances.
May 17, 2018
X1e instances New memory optimized 
instances.
November 28, 2017
M5 instances New general purpose 
instances.
November 28, 2017
H1 instances New storage optimized 
instances.
November 28, 2017
C5 instances New compute optimized 
instances.
November 6, 2017
P3 instances New accelerated computing 
instances.
October 25, 2017
684
Amazon EC2 Instance Types
G3 instances New accelerated computing 
instances.
July 13, 2017
F1 instances New accelerated computing 
instances.
April 19, 2017
I3 instances New storage optimized 
instances.
February 23, 2017
R4 instances New memory optimized 
instances.
November 30, 2016
P2 instances New accelerated computing 
instances.
September 29, 2016
X1 instances New memory optimized 
instances.
May 18, 2016
M4 instances New general purpose 
instances.
June 11, 2015
D2 instances New storage optimized 
instances.
March 24, 2015
C4 instances New compute optimized 
instances.
January 11, 2015
T2 instances New general purpose 
instances.
June 30, 2014
685

