# Pre-commit hooks
- pre-commit or husky
- pre-commit should call linters
- they should also call sonarlint
- Identify secrets such as usernames, passwords, and access keys in code. Examples of secret detection tools include but are not limited to GitGuardian, gitleaks, Yelp Detect Secrets, AWS Git Secrets. Secrets should not be committed to local repository and/or pushed to remote repository. If hacker gets access to code repository, they could read the secrets from commit history.
- if we change something in pre-commit we need to run unit tests again. so unit tests should be last step of pre-commit.
<br><br>

# Pre-checkout initialize variables
<br><br>

# Checkout
- Application component source code
    - Code that is compiled, transpiled or interpreted for the purpose of delivering business capabilities through applications and/or services.
- Test source code
    - Code that verifies the expected functionality of the Application component source code and the Infrastructure source code. 
    - This includes source code for unit, integration, end-to-end, capacity, chaos, and synthetic testing. 
    - All Test source code is required to be stored in the same repository as the app to allow tests to be created and updated on the same lifecycle as the Application component source code.
- Infrastructure source code
    - Code that defines the infrastructure necessary to run the Application component source code. 
    - Examples of infrastructure source code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform. 
    - All Infrastructure source code is required to be stored in the same repository as the app to allow infrastructure to be created and updated on the same lifecycle as the Application component source code.
- Static Assets
    - Assets used by the Application component source code such as html, css, and images.
- Dependency Manifests
    - References to third-party code that is used by the Application component source code. 
    - This could be libraries created by the same team, a separate team within the same organization, or from an external entity.
- Static Configuration
    - Files (e.g. JSON, XML, YAML or HCL) used to configure the behavior of the Application component source code. 
    - Any configuration that is environment specific should not be included in Application component source code. 
    - Environment specific configuration should be defined in the Infrastructure source code and injected into the application component at runtime through some mechanism. Environment variables is not a good idea because then the underlying middleware could get access to sensitive data. Application component should connect to configuration provider using tokens and get the configuration similar to how it calls rest api of other application components.
- Database source code
    - Code that defines the schema and reference data of the database used by the Application component source code. 
    - Examples of database source code include but are not limited to Liquibase. 
    - If the Application component source code uses a private database that no other application component accesses, then the database source code is required to be stored in the same repository as the Application component source code. This allows the Application component source code and Database source code to be updated on the same lifecycle. 
    - However, if the database is shared by multiple application components then the Database source code should be maintained in a separate repository and managed by separate pipeline. It should be noted that this is undesireable as it introduces coupling between application components.
<br><br>

# Post-checkout initialize variables
<br><br>

# Container file security and compliance scanning ( Pre-build test ) ( Security scan )
- Checkov
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Build
- Convert code into artifacts that can be promoted through environments. 
- Examples include but are not limited to Maven and tsc.
- Mandatory to cache the dependencies for faster build
<br><br>

# Unit tests ( Post-build test )
- Run the test code to verify that individual functions and methods of classes, components or modules of the Application source code are performing according to expectations. 
- These tests are fast-running tests with zero dependencies on external systems returning results in seconds. 
- Examples of unit testing frameworks include but are not limited to JUnit, Jest, and pytest. 
<br><br>

# Package
- While the Build Code action will package most of the relevant artifacts, there may be additional steps to automate for packaging the code artifacts. 
- Artifacts should only be built and packaged once and then deployed to various environments to validate the artifact. Artifacts should never be rebuilt during subsequent deploy stages.
- Packages should be signed with a digital-signature to allow deployment processes to confirm the code being deployed is from a trusted publisher and has not been altered. AWS Signer can be used to cryptographically sign code for AWS Lambda applications and AWS-supported IoT devices.
- Get the version number from the release branch tag.
<br><br>

# Software bill of materials (SBOM) ( Post-package test )
- Generate a software bill of materials (SBOM) report detailing all the dependencies used. Examples of SBOM formats include SPDX and CycloneDX
- SBOM should be published to somewhere like JIRA for updating issues and ITSM for attaching to Change Requests.
<br><br>

# Software composition analysis (SCA) ( Post-package test ) ( Security scan )
- Run software composition analysis (SCA) tools to find vulnerabilities to package repositories related to open source use, licensing, and security vulnerabilities. SCA tools also launch workflows to fix these vulnerabilities. 
- These tools also require a software bill of materials (SBOM) exist. 
- Example SCA tools include but are not limited to Dependabot, Snyk, Blackduck, OWASP Dependency Check
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Secrets scanning ( Post-package test ) ( Security scan )
- Identify secrets such as usernames, passwords, and access keys in artifacts.
- Examples of secret detection tools include but are not limited to GitGuardian, gitleaks, Yelp Detect Secrets, AWS Git Secrets
- Secrets scanning should be part of pre-commit and so secrets should not be committed to local repository and/or pushed to remote repository.
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Static application security testing (SAST) ( Post-package test ) ( Security scan )
- Analyze code for application security violations such as XML External Entity Processing, SQL Injection, and Cross Site Scripting. 
- Examples of tools to perform static application security testing include but are not limited to SonarQube, Checkmarx and Amazon CodeGuru.
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Infrastructure code security and compliance scanning ( Post-package test ) ( Security scan )
- tfsec(trivy) for Terraform, trivy(cfsec) for CloudFormation, Checkov for Terraform, Helm Charts, Cloudformation, Azure Resource Manager, Serverless Framework, Kubernetes, Docker
- Policy as code
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Container image and other build artifacts security scanning ( Post-package test ) ( Security scan )
- trivy for containers
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Anti-virus Scanning ( Post-package test ) ( Security scan )
- ClamAV
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Static code analysis ( Post-package test )
- Run various automated static analysis tools that generate reports on readability, maintainability, code quality, coding standards, code coverage, and other aspects according to the team and/or organization’s best practices. 
- Examples of tools to measure code quality include but are not limited to SonarQube, black, ESLint, Amazon CodeGuru.
<br><br>

# Database changes quality checks ( Post-package test )
- Liquibase 
<br><br>

# Push Artifacts
- Examples of artifact repositories include but are not limited to Nexus, JFrog Artifactory, AWS CodeArtifact, Amazon ECR.
- When artifacts are published to Artifact repository tools like Sonatype nexus, jfrog artifactory, etc. they can run security scans like SCA and reject the publish if the security scans fail.
- It is recommended to use security platform like Checkmarx or Veracode for security scans and only use better tool if available.
<br><br>

# Deploy and test in simulated testing environment
- Pull artifacts
    - Artifacts to be deployed should include digital signatures to verify that the artifact came from a trusted source and that no changes were made to the artifact.
- Environment should be in a different cloud account from the tools used to run the CI/CD pipeline. For Infrastructure deployment, access to environment should be handled via cross-account IAM roles rather than long lived credentials from IAM users. For other deployments, access should be handled using mechanisms like oauth.
- Create consumer/downstream application component simulated testing environment kubernetes namespace or cloud account
- Deploy middleware infrastructure
    - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
- Deploy middleware changes like database changes
    - Changes to the database should be incremental, only applying the changes since the prior deployment. Examples of tools that apply incremental database changes include but are not limited to Liquibase, VS Database Project, and Flyway.
- Deploy simulated testing data for consumer/downstream application component
- Deploy simulated producer/upstream application components infrastructure
- Deploy simulated producer/upstream application components code
- Deploy consumer/downstream application component infrastructure
    - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
- Deploy consumer/downstream application component code
    - Examples of tools to deploy application component code include but are not limited to AWS CodeDeploy, Octopus Deploy, and Spinnaker.
- Rollback testing
    - Examples of automated rollback include AWS CloudFormation monitor & rollback, AWS CodeDeploy rollback and Flagger.
- Deployed infrastructure security and compliance scanning
- Simulated testing
    - Tests may come in the form of behavior-driven tests, automated acceptance tests, or automated tests linked to requirements and/or stories in a tracking system.
    - Examples of tools to define integration tests include but are not limited to Cucumber, vRest, and SoapUI.
    - Run dynamic application security testing in parallel to simulated testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
    - Run observability testing in parallel to simulated testing
        - Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
        - Monitor deployments across regions and fail when threshold breached. 
        - The thresholds for metric alarms should be defined in the Infrastructure Source Code and deployed along with the rest of the infrastructure in an environment. 
        - Ideally, deployments should be automatically failed and rolled back when error thresholds are breached.
- Destroy consumer/downstream application component simulated testing environment kubernetes namespace or cloud account
<br><br>

# Deploy and test in end to end testing environment
- Pull artifacts
    - Artifacts to be deployed should include digital signatures to verify that the artifact came from a trusted source and that no changes were made to the artifact.
- Environment should be in a different cloud account from the tools used to run the CI/CD pipeline. For Infrastructure deployment, access to environment should be handled via cross-account IAM roles rather than long lived credentials from IAM users. For other deployments, access should be handled using mechanisms like oauth.
- Contract testing
- Deploy middleware infrastructure
    - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
- Deploy middleware changes like database changes
    - Changes to the database should be incremental, only applying the changes since the prior deployment. Examples of tools that apply incremental database changes include but are not limited to Liquibase, VS Database Project, and Flyway.
- Cleanup and deploy end to end testing data for all application components
- Deploy application component infrastructure
    - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
- Deploy application component code
    - Examples of tools to deploy application component code include but are not limited to AWS CodeDeploy, Octopus Deploy, and Spinnaker.
- Deployed infrastructure security and compliance scanning
- Synthetic / End to end testing journeys
    - These tests verify the user workflow, including when performed through a UI. 
    - These tests are the slowest to run and hardest to maintain and therefore it is recommended to only have a few end-to-end tests that cover the most important application workflows.
    - Examples of tools to define end-to-end tests include but are not limited to Cypress, Selenium, and Telerik Test Studio.
    - Synthetic Tests run continuously in the background in a given environment to generate traffic and verify the system is healthy.   
        - These tests serve two purposes: 
            - Ensure there is always adequate traffic in the environment to trigger alarms if a deployment is unhealthy
            - Test specific workflows and assert that the system is functioning correctly. 
        - Examples of tools that can be used for synthetic tests include but are not limited to Amazon CloudWatch Synthetics,Dynatrace Synthetic Monitoring, and Datadog Synthetic Monitoring.
    - Run dynamic application security testing in parallel to synthetic or end to end testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
    - Run observability testing in parallel to synthetic or end to end testing
        - Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
        - Monitor deployments across regions and fail when threshold breached. 
        - The thresholds for metric alarms should be defined in the Infrastructure Source Code and deployed along with the rest of the infrastructure in an environment. 
        - Ideally, deployments should be automatically failed and rolled back when error thresholds are breached.
- In case of failures, rollback and create bug issue
    - Examples of automated rollback include AWS CloudFormation monitor & rollback, AWS CodeDeploy rollback and Flagger.
<br><br>

# Deploy and test in performance testing environment
- Pull artifacts
    - Artifacts to be deployed should include digital signatures to verify that the artifact came from a trusted source and that no changes were made to the artifact.
- Environment should be in a different cloud account from the tools used to run the CI/CD pipeline. For Infrastructure deployment, access to environment should be handled via cross-account IAM roles rather than long lived credentials from IAM users. For other deployments, access should be handled using mechanisms like oauth.
- Environment is as production-like as possible including configuration, monitoring, and traffic. 
- Environment should match the same regions that the production environment uses. 
- Contract testing
- Progressive delivery testing
    - Software should be deployed using one of progressive deployment involving controlled rollout of a change through techniques such as canary deployments, feature flags, and traffic shifting. 
    - Deploy middleware infrastructure
        - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
    - Deploy middleware changes like database changes
        - Changes to the database should be incremental, only applying the changes since the prior deployment. Examples of tools that apply incremental database changes include but are not limited to Liquibase, VS Database Project, and Flyway.
    - Cleanup and deploy performance testing data for all application components
    - Deploy application component infrastructure
        - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
    - Deploy application component code
        - Examples of tools to deploy application component code include but are not limited to AWS CodeDeploy, Octopus Deploy, and Spinnaker.
- Deployed infrastructure security and compliance scanning
- Synthetic / End to end testing journeys
    - These tests verify the user workflow, including when performed through a UI. 
    - These tests are the slowest to run and hardest to maintain and therefore it is recommended to only have a few end-to-end tests that cover the most important application workflows.
    - Examples of tools to define end-to-end tests include but are not limited to Cypress, Selenium, and Telerik Test Studio.
    - Synthetic Tests run continuously in the background in a given environment to generate traffic and verify the system is healthy.   
        - These tests serve two purposes: 
            - Ensure there is always adequate traffic in the environment to trigger alarms if a deployment is unhealthy
            - Test specific workflows and assert that the system is functioning correctly. 
        - Examples of tools that can be used for synthetic tests include but are not limited to Amazon CloudWatch Synthetics,Dynatrace Synthetic Monitoring, and Datadog Synthetic Monitoring.
    - Run dynamic application security testing in parallel to synthetic or end to end testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
    - Run observability testing in parallel to synthetic or end to end testing
        - Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
        - Monitor deployments across regions and fail when threshold breached. 
        - The thresholds for metric alarms should be defined in the Infrastructure Source Code and deployed along with the rest of the infrastructure in an environment. 
        - Ideally, deployments should be automatically failed and rolled back when error thresholds are breached.
- Performance testing
    - Run longer-running automated capacity tests against environments that simulate production capacity. 
    - Measure metrics such as the transaction success rates, response time and throughput. 
    - Determine if application meets performance requirements and compare metrics to past performance to look for performance degredation. 
    - Examples of tools that can be used for performance tests include but are not limited to JMeter, Locust, and Gatling.
    - Run dynamic application security testing in parallel to performance testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
    - Run observability testing in parallel to performance testing
        - Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
        - Monitor deployments across regions and fail when threshold breached. 
        - The thresholds for metric alarms should be defined in the Infrastructure Source Code and deployed along with the rest of the infrastructure in an environment. 
        - Ideally, deployments should be automatically failed and rolled back when error thresholds are breached.
- Resilience testing
    - Inject failures into environments to identify areas of the application that are susceptible to failure. 
    - Tests are defined as code and applied to the environment while the system is under load. 
    - The success rate, response time and throughput are measured during the periods when the failures are injected and compared to periods without the failures. Any significant deviation should fail the pipeline. 
    - Examples of tools that can be used for chaos/resilience testing include but are not limited to AWS Fault Injection Simulator, Gremlin, and ChaosToolkit.
    - Run dynamic application security testing in parallel to resilience testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
    - Run observability testing in parallel to resilience testing
        - Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
        - Monitor deployments across regions and fail when threshold breached. 
        - The thresholds for metric alarms should be defined in the Infrastructure Source Code and deployed along with the rest of the infrastructure in an environment. 
        - Ideally, deployments should be automatically failed and rolled back when error thresholds are breached.
- In case of failures, rollback and create bug issue
    - Examples of automated rollback include AWS CloudFormation monitor & rollback, AWS CodeDeploy rollback and Flagger.
<br><br>

# Create release OR
- Pull artifacts
- Manual approval
    - As part of an automated workflow, obtain authorized human approval.
    - Need to provide RFC and change request number
<br><br>

# OR Deploy to production environment
- Pull artifacts
    - Artifacts to be deployed should include digital signatures to verify that the artifact came from a trusted source and that no changes were made to the artifact.
- Manual approval
    - As part of an automated workflow, obtain authorized human approval.
    - Need to provide RFC and change request number
- Environment should be in a different cloud account from the tools used to run the CI/CD pipeline. For Infrastructure deployment, access to environment should be handled via cross-account IAM roles rather than long lived credentials from IAM users. For other deployments, access should be handled using mechanisms like oauth.
- Contract testing
- Progressive delivery
    - Software should be deployed using one of progressive deployment involving controlled rollout of a change through techniques such as canary deployments, feature flags, and traffic shifting.
    - Deploy middleware infrastructure
        - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
    - Deploy middleware changes like database changes
        - Changes to the database should be incremental, only applying the changes since the prior deployment. Examples of tools that apply incremental database changes include but are not limited to Liquibase, VS Database Project, and Flyway.
    - Deploy application component infrastructure
        - Example tools for defining infrastructure code include but are not limited to AWS Cloud Development Kit, AWS CloudFormation and HashiCorp Terraform.
    - Deploy application component code
        - Examples of tools to deploy application component code include but are not limited to AWS CodeDeploy, Octopus Deploy, and Spinnaker.
- Synthetic / End to end testing journeys
    - Synthetic Tests run continuously in the background in a given environment to generate traffic and verify the system is healthy.   
        - These tests serve two purposes: 
            - Ensure there is always adequate traffic in the environment to trigger alarms if a deployment is unhealthy
            - Test specific workflows and assert that the system is functioning correctly. 
        - Examples of tools that can be used for synthetic tests include but are not limited to Amazon CloudWatch Synthetics,Dynatrace Synthetic Monitoring, and Datadog Synthetic Monitoring.
    - Run dynamic application security testing in parallel to synthetic or end to end testing
        - Perform testing of web applications and APIs by running automated scans against it to identify vulnerabilities through techniques such as cross-site scripting (XSS) and SQL injection(SQLi). 
        - Examples of tools that can be used for dynamic application security testing include but are not limited to OWASP ZAP, StackHawk, and AppScan.
- Test if metrics, logs and traces are generated and we can understand the internal state of the system by examining this telemetry data
- Deployed infrastructure security and compliance scanning
- In case of failures, rollback and create problem issue
    - Examples of automated rollback include AWS CloudFormation monitor & rollback, AWS CodeDeploy rollback and Flagger.
<br><br>

# Always
- Publish testing and security scanning results to somewhere like 
    - JIRA for updating issues
    - ITSM for attaching to Change Requests and RFCs for testing proof.
    - SIEM tool for security scanning results
- Documentation
    - Update Confluence Documentation for the Application Component/Service
- CMDB 
    - Call CMDB Webhook which will use the Infrastructure Resource Tags to update CMDB
- Communication and Collaboration 
    - Update JIRA Issue. Send Notification via email,sms,etc.
- Cleanup
    - Docker logout