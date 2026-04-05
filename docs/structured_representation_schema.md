# Structured Representation Schema

## Overview

This document defines the JSON/YAML schemas used to store the output of the AKU Extraction and Topic Extraction modules. By enforcing strict schemas with cross-linking capabilities, we ensure that Factual, Procedural, and Conceptual knowledge can be programmatically queried, loaded into vector databases, connected into a rich knowledge graph, or injected into prompt contexts.

---

## 1. Entity Tables (Factual Knowledge)

Used to store discrete facts, configurations, limits, and component definitions.

### Schema

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "title": "AWS Entity",
  "description": "Schema representing a factual AWS entity (service, component, configuration, or limit).",
  "type": "object",
  "properties": {
    "entity_id": {
      "type": "string",
      "description": "Unique machine-friendly identifier (e.g., 'aws_lambda_function')"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string",
      "description": "Human-readable summary and context for the entity."
    },
    "category": {
      "type": "string",
      "enum": ["Service", "Component", "Configuration", "Limit"]
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Taxonomy tags for semantic indexing and retrieval."
    },
    "attributes": {
      "type": "object",
      "description": "Flexible key-value pairs of factual AKUs. Values can be strings, numbers, booleans, arrays, or nested objects.",
      "additionalProperties": true
    },
    "governed_by": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of principle_ids that govern this entity."
    },
    "related_entities": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of related entity_ids for flat cross-referencing."
    },
    "relationships": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "target_entity": { "type": "string" },
          "relation_type": { 
            "type": "string", 
            "enum": [
              "DEPENDS_ON", "PART_OF", "CONFIGURES", "COMMUNICATES_WITH",
              "USES", "TRIGGERS", "SECURED_BY", "SCALES_WITH", "LIMITS"
            ] 
          }
        },
        "required": ["target_entity", "relation_type"]
      }
    }
  },
  "required": ["entity_id", "name", "description", "category", "attributes"],
  "additionalProperties": true
}
```

### Example Payload

```json
{
  "entity_id": "aws_lambda_timeout",
  "name": "Lambda Execution Timeout",
  "description": "The maximum duration that an AWS Lambda function can run before it is terminated.",
  "category": "Limit",
  "tags": ["compute", "serverless", "limits", "execution"],
  "attributes": {
    "default_value_seconds": 3,
    "maximum_value_seconds": 900,
    "is_adjustable": false
  },
  "governed_by": ["principle_cost_optimization", "principle_fail_fast"],
  "related_entities": ["aws_lambda_memory", "aws_iam_execution_role"],
  "relationships": [
    { "target_entity": "aws_lambda_function", "relation_type": "LIMITS" },
    { "target_entity": "aws_step_functions", "relation_type": "TRIGGERS" }
  ]
}
```

---

## 2. Step Summaries (Procedural Knowledge)

Used to capture sequential "How-To" guides and operational workflows.

### Schema

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "title": "Procedural Workflow",
  "description": "Schema representing a sequential operational workflow or tutorial.",
  "type": "object",
  "properties": {
    "workflow_id": { "type": "string" },
    "target_service": { "type": "string" },
    "goal": { "type": "string", "description": "The objective of the procedure." },
    "description": { "type": "string", "description": "Human-readable context summarizing the workflow." },
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    },
    "related_entities": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of entity_ids interacted with or created during this workflow."
    },
    "applies_principles": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of principle_ids demonstrated or required by this workflow."
    },
    "prerequisites": {
      "type": "array",
      "items": { "type": "string" }
    },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step_number": { "type": "integer" },
          "step_type": { 
            "type": "string",
            "enum": ["CLI", "Console", "API", "Validation", "Conceptual"]
          },
          "action_aku": { "type": "string", "description": "The core action as a procedural AKU." },
          "inputs": { 
            "type": "array", 
            "items": { "type": "string" }
          },
          "outputs": {
            "type": "array",
            "items": { "type": "string" }
          },
          "code_snippet": { "type": "string" },
          "validation": { "type": "string" },
          "error_handling": { "type": "string" }
        },
        "required": ["step_number", "step_type", "action_aku"]
      }
    }
  },
  "required": ["workflow_id", "target_service", "goal", "description", "steps"],
  "additionalProperties": true
}
```

### Example Payload

```json
{
  "workflow_id": "deploy_lambda_function_cli",
  "target_service": "AWS Lambda",
  "goal": "Deploy a basic Lambda function via CLI",
  "description": "A terminal-based workflow for packaging code and creating a Lambda function using the AWS CLI.",
  "tags": ["deployment", "cli", "serverless", "automation"],
  "related_entities": ["aws_lambda_function", "aws_iam_execution_role"],
  "applies_principles": ["least_privilege"],
  "prerequisites": ["AWS CLI installed", "IAM Execution Role created"],
  "steps": [
    {
      "step_number": 1,
      "step_type": "CLI",
      "action_aku": "Zip the deployment package containing the function code and dependencies.",
      "inputs": ["index.js file", "node_modules/"],
      "outputs": ["function.zip"],
      "code_snippet": "zip -r function.zip index.js node_modules/"
    },
    {
      "step_number": 2,
      "step_type": "CLI",
      "action_aku": "Execute the 'aws lambda create-function' CLI command, passing the zip file and IAM execution role ARN.",
      "inputs": ["function.zip", "IAM Role ARN"],
      "code_snippet": "aws lambda create-function --function-name myFunc --runtime nodejs18.x --role arn:aws:iam::123:role/exRole --handler index.handler --zip-file fileb://function.zip",
      "validation": "Check for a 200 HTTP response and the function ARN in the CLI output.",
      "error_handling": "If 'InvalidParameterValueException' occurs, ensure the IAM role has been fully propagated (wait 10 seconds)."
    }
  ]
}
```

---

## 3. Principle Statements (Conceptual Knowledge)

Used to capture "Why" things are designed a certain way, architectural patterns, and historical context.

### Schema

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "title": "Conceptual Principle",
  "description": "Schema representing a conceptual principle, architecture pattern, or rationale.",
  "type": "object",
  "properties": {
    "principle_id": { "type": "string" },
    "domain": { "type": "string" },
    "statement": { "type": "string" },
    "description": { "type": "string" },
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    },
    "rationale": { "type": "string" },
    "impact_level": { 
      "type": "string",
      "enum": ["Low", "Medium", "High", "Critical"]
    },
    "applicable_services": {
      "type": "array",
      "items": { "type": "string" }
    },
    "related_principles": {
      "type": "array",
      "items": { "type": "string" }
    },
    "anti_pattern": {
      "type": "string"
    },
    "examples": {
      "type": "array",
      "items": { "type": "string" }
    },
    "tradeoffs": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["principle_id", "domain", "statement", "description", "rationale", "impact_level"],
  "additionalProperties": true
}
```

### Example Payload

```json
{
  "principle_id": "least_privilege",
  "domain": "Security",
  "statement": "Grant only the minimum permissions required to perform a specific task.",
  "description": "A foundational security concept dictating that users, systems, and applications should only have access to the specific resources necessary for their function.",
  "tags": ["iam", "access-control", "zero-trust", "compliance"],
  "rationale": "Prevents accidental or malicious resource modification by restricting the blast radius of compromised credentials.",
  "impact_level": "Critical",
  "applicable_services": ["AWS IAM", "Amazon S3", "AWS KMS", "AWS Lambda"],
  "related_principles": ["defense_in_depth", "separation_of_duties"],
  "anti_pattern": "Using 'AdministratorAccess' for an EC2 instance profile just to read from a single S3 bucket.",
  "examples": [
    "Attaching an IAM policy to a Lambda function that only allows 's3:GetObject' on a specific bucket ARN, rather than 's3:*' on all buckets."
  ],
  "tradeoffs": [
    "Increases administrative overhead to carefully craft and maintain granular policies.",
    "Can slow down development speed initially as engineers must determine exact permissions needed."
  ]
}
```

---

Source: 
