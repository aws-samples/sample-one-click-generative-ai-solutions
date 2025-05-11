import pytest
import subprocess
import json
from pathlib import Path

# Get the repository root directory
REPO_ROOT = Path(__file__).parent.parent

# Define template configurations
TEMPLATES = [
    {
        "name": "GenU",
        "path": REPO_ROOT / "deployments" / "genu" / "GenUDeploymentStack.yaml"
    },
    {
        "name": "Dify",
        "path": REPO_ROOT / "deployments" / "dify" / "DifyDeploymentStack.yaml"
    },
    {
        "name": "BrChat",
        "path": REPO_ROOT / "deployments" / "brchat" / "BrChatDeploymentStack.yaml"
    }
]

@pytest.mark.parametrize("template_config", TEMPLATES)
def test_template_exists(template_config):
    """Test that the CloudFormation template file exists."""
    template_path = template_config["path"]
    assert template_path.exists(), f"Template file not found at {template_path}"

@pytest.mark.parametrize("template_config", TEMPLATES)
def test_template_validates_with_aws_cli(template_config):
    """Test that the template validates with the AWS CloudFormation validate-template command."""
    template_path = template_config["path"]
    template_name = template_config["name"]
    
    try:
        # Run the AWS CLI command to validate the template
        result = subprocess.run(
            ["aws", "cloudformation", "validate-template", "--template-body", f"file://{template_path}"],
            capture_output=True,
            text=True,
            check=False
        )
        
        # Check if the command was successful
        if result.returncode != 0:
            pytest.fail(f"Template validation failed for {template_name}: {result.stderr}")

        # Parse the output to verify it's valid JSON
        validation_result = json.loads(result.stdout)
        
        # Check that the Parameters section was properly parsed
        assert "Parameters" in validation_result, f"Template validation for {template_name} did not return Parameters section"
        
        # Print success message
        print(f"Template validation successful for {template_name}: {template_path}")
        
    except Exception as e:
        pytest.fail(f"Error validating template {template_name}: {str(e)}")
