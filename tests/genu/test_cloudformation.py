import pytest
import subprocess
import json
from pathlib import Path

# Get the repository root directory
REPO_ROOT = Path(__file__).parent.parent.parent
TEMPLATE_PATH = REPO_ROOT / "build" / "genu" / "genu_deployment.yaml"

def test_template_exists():
    """Test that the CloudFormation template file exists."""
    assert TEMPLATE_PATH.exists(), f"Template file not found at {TEMPLATE_PATH}"

def test_template_validates_with_aws_cli():
    """Test that the template validates with the AWS CloudFormation validate-template command."""
    try:
        # Run the AWS CLI command to validate the template
        result = subprocess.run(
            ["aws", "cloudformation", "validate-template", "--template-body", f"file://{TEMPLATE_PATH}"],
            capture_output=True,
            text=True,
            check=False
        )
        
        # Check if the command was successful
        if result.returncode != 0:
            pytest.fail(f"Template validation failed: {result.stderr}")

        # Parse the output to verify it's valid JSON
        validation_result = json.loads(result.stdout)
        
        # Check that the Parameters section was properly parsed
        print(validation_result)
        assert "Parameters" in validation_result, "Template validation did not return Parameters section"
        
        # Print success message
        print(f"Template validation successful: {TEMPLATE_PATH}")
        
    except Exception as e:
        pytest.fail(f"Error validating template: {str(e)}")
