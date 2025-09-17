# Bedrock Engineer

[Bedrock Engineer](https://github.com/aws-samples/bedrock-engineer) is an AI assistant for software development tasks powered by [Amazon Bedrock](https://aws.amazon.com/bedrock/). Autonomous AI agents with large language models and real-world file system operations, web search capabilities, and more support your development work.

## Overview

Bedrock Engineer provides a standalone application experience with powerful AI capabilities:

- 💬 Interactive chat interface with Amazon Nova, Claude, and Meta Llama models
- 🛠️ Extensive tool integration for file operations, web search, code execution, and more
- 🧠 Customizable agents for different use cases and specializations
- 🌐 Agent Directory for sharing and discovering pre-configured agents
- 🎤 Voice chat capabilities with Amazon Nova Sonic
- 🖥️ Website and diagram generation features

## Download

Download the latest version using the button below.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <a href="https://github.com/aws-samples/bedrock-engineer/releases/latest" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-download"></i>　Download Latest Release
    </a>
  </div>
</div>

## Key Features

### Agent Chat: Customizable AI Assistants

The Agent Chat feature provides a powerful interface for interacting with AI assistants that can be fully customized to your needs:

![Agent Chat](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/agent-chat-diagram.png)

#### 1. Customizable Agents

Select agents from the top-left menu. By default, it includes Software Developer specialized for general software development, Programming Mentor to support programming learning, and Product Designer to support the conceptual stage of services and products.

![Custom Agents](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/custom-agents.png)

Customize agent settings. Enter the agent's name and description, and input the system prompt. The system prompt is a crucial element that determines the agent's behavior. By clearly defining the agent's purpose, regulations, role, available tools, and when to use them, you can obtain more appropriate responses.

#### 2. Integrated Tools

Click the Tools icon in the bottom left to select tools that the agent can use. Tools can be configured individually for each agent.

![Select Tools](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/select-tools.png)

**File System Operations**
- Create folders and files
- Read and write file contents
- List directory structures

**Web & Search Operations**
- Web search via Tavily API
- Website content retrieval

**Amazon Bedrock Integration**
- Image generation and recognition
- Video generation
- Knowledge Base retrieval
- Bedrock Agent and Flow integration

**System Command & Code Execution**
- Execute system commands
- Run Python code in secure environments
- Screen and camera capture

#### 3. Agent Directory: Sharing and Discovery

The Agent Directory is a content hub where you can discover and immediately use AI agents created by excellent contributors. It provides a curated collection of agents designed for various tasks and specializations.

![Agent Directory](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/agent-directory.png)

**Features**
- **Browse Collections** - Explore the growing library of specialized agents created by the community
- **Search and Filter** - Quickly discover agents that match your needs using search functionality or filtering by tags
- **View Detailed Information** - Check comprehensive information about each agent including creator, system prompt, supported tools, and usage scenarios
- **One-Click Addition** - Add any agent to your personal collection with one click and start using immediately
- **Agent Submission** - Become a contributor and share your custom agents with the community

## Additional Resources

- [GitHub Repository](https://github.com/aws-samples/bedrock-engineer)
- [English Presentation Deck](https://speakerdeck.com/gawa/introducing-bedrock-engineer-en)
- [Japanese Presentation Deck](https://speakerdeck.com/gawa/introducing-bedrock-engineer)

## License

This application is licensed under the MIT-0 License. See the [LICENSE](https://github.com/aws-samples/bedrock-engineer/blob/main/LICENSE) file for details.
