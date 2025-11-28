# TODO: Address PR #65 Review Comments

## Critical (Must Fix)

- [ ] **Security: Remove command injection risk in AgentCore discovery**
  - Replace `execSync` with AWS SDK for CloudFormation API calls
  - Validate region parameter format before use
  - Location: `discoverAgentCoreRuntimes()` function

- [ ] **Security: Avoid exposing credentials in logs**
  - Option 1: Use Cognito's built-in email delivery for temporary password
  - Option 2: Store credentials in AWS Secrets Manager and provide ARN
  - Option 3: Add warning about sensitive data in logs
  - Location: User creation section in build phase

- [ ] **Fix silent error suppression**
  - Capture error output from `admin-create-user` command
  - Log specific error messages for troubleshooting
  - Distinguish between "user exists" vs other failures
  - Location: Cognito user creation command

## Important (Should Fix)

- [ ] **Optimize N+1 query pattern**
  - Fetch all stack outputs in single query
  - Change query to: `Stacks[?Tags[?Key=='Integration' && Value=='GenU']].[StackName,Outputs]`
  - Location: `discoverAgentCoreRuntimes()` function

- [ ] **Add JSON parsing error handling**
  - Check for empty/invalid output before parsing
  - Add try-catch for JSON.parse operations
  - Location: `discoverAgentCoreRuntimes()` function

- [ ] **Improve error messages**
  - Differentiate "no runtimes found" vs "error discovering"
  - Check for specific error codes (ResourceNotFoundException)
  - Location: catch block in `discoverAgentCoreRuntimes()`

## Minor (Nice to Have)

- [ ] **Fix grammar in deployment message**
  - "access to Cognito" → "access the Cognito"
  - "referring registration guide" → "referring to the registration guide"
  - Location: deployment-info.txt generation

- [ ] **Improve default USER_NOTE message**
  - Change to: "User creation was not successful. Please create user manually or check if user already exists."
  - Location: User credentials default values

- [ ] **Add JSDoc documentation**
  - Document `discoverAgentCoreRuntimes()` function
  - Explain tag criteria, expected outputs, and return format
  - Location: Before function definition

- [ ] **Remove trailing whitespace**
  - Clean up line ending after User Registration Guide URL
  - Location: deployment-info.txt generation

## Implementation Order

1. Fix critical security issues first (command injection, credentials exposure)
2. Address error handling and logging improvements
3. Optimize performance (N+1 queries)
4. Polish with grammar fixes and documentation
