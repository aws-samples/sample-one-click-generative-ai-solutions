# Why AWS Generative AI Solution Box?

## Build generative AI applications easily, even without development experience

:zap: **Fast** : Build various generative AI solutions with one click  
:four_leaf_clover: **Easy-to-use** : Carefully selected solutions that even beginners can immediately experience the benefits  
:lock: **Secure** : Production-ready security for immediate production use  
:hammer: **Open-Source** : Each solution is open source and customizable  
:book: **Guide** : Provides usage instructions and guides for adoption  

## 3-Step Build Process

<div class="steps-container">
  <div class="step-card">
    <div class="step-number">1</div>
    <div class="step-title">Login AWS</div>
    <div class="step-description">Create an AWS Account and<br/>login with deployment user</div>
  </div>
  <div class="step-card">
    <div class="step-number">2</div>
    <div class="step-title">Choose & Click</div>
    <div class="step-description">Select the solution you want<br/>Click to start deployment</div>
  </div>
  <div class="step-card">
    <div class="step-number">3</div>
    <div class="step-title">Start Journey</div>
    <div class="step-description">Start using when completion<br/>notification arrives</div>
  </div>
</div>

## 1. Prepare AWS Account

Please create an AWS account and sign in by referring to "Point 2: How to start using AWS?" in [6 Points for AWS Beginners](https://aws.amazon.com/local/aws-beginner-six-points/).

## 2. Choose & Click

Once you've decided on the AWS solution you want to use, select a region and click Deploy. If you need guides such as explanations of deployment options, please refer to the detailed documentation.

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterSolutions('all')">All</button>
  <button class="filter-btn" onclick="filterSolutions('popular')">🌟 Popular</button>
  <button class="filter-btn" onclick="filterSolutions('chat')">💬 Chat</button>
  <button class="filter-btn" onclick="filterSolutions('development')">🔧 Development</button>
  <button class="filter-btn" onclick="filterSolutions('creative')">🎨 Content Creation</button>
  <button class="filter-btn" onclick="filterSolutions('document')">📄 Document Analysis</button>
</div>

<style>
.solution-card {
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  margin-bottom: 2rem;
  background: white;
}

.solution-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 16px rgba(0, 0, 0, 0.1);
}

.solution-card__top {
  display: flex;
  flex-direction: row;
  min-height: 200px;
}

.solution-card__image {
  flex: 1.2;
  background: #f8fafc;
  border-right: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.solution-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.solution-card:hover .solution-card__image img {
  transform: scale(1.05);
}

.solution-card__content {
  flex: 1;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.solution-card__title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--md-primary-fg-color);
  line-height: 1.3;
}

.solution-card__tags {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.solution-card__tag {
  background: #e2e8f0;
  color: #475569;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.solution-card__tag:hover {
  background: var(--md-primary-fg-color);
  color: white;
}

.solution-card__tag.active {
  background: var(--md-primary-fg-color);
  color: white;
}

.solution-card__description {
  color: #4b5563;
  line-height: 1.6;
  font-size: 0.95rem;
}

.solution-card__actions {
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.filter-bar {
  display: flex;
  gap: 0.5rem;
  margin: 1.5rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.filter-btn {
  background: #f8fafc;
  color: #475569;
  border: 1px solid #e2e8f0;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: var(--md-primary-fg-color);
  color: white;
  border-color: var(--md-primary-fg-color);
}

.filter-btn.active {
  background: var(--md-primary-fg-color);
  color: white;
  border-color: var(--md-primary-fg-color);
}

@media screen and (max-width: 768px) {
  .solution-card__top {
    flex-direction: column;
  }
  
  .solution-card__image {
    flex: none;
    height: 150px;
    border-right: none;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  }
}
</style>

<script>
function toggleDemo(tagElement, demoType) {
  const card = tagElement.closest('.solution-card');
  const images = card.querySelectorAll('.solution-card__image img');
  const tags = card.querySelectorAll('.solution-card__tag');
  
  tags.forEach(tag => tag.classList.remove('active'));
  tagElement.classList.add('active');
  
  images.forEach(img => img.style.display = 'none');
  
  const targetImg = card.querySelector(`[data-demo="${demoType}"]`);
  if (targetImg) {
    targetImg.style.display = 'block';
  }
}

function filterSolutions(category) {
  const cards = document.querySelectorAll('.solution-card');
  const buttons = document.querySelectorAll('.filter-btn');
  
  buttons.forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  
  cards.forEach(card => {
    const categories = card.dataset.category || '';
    if (category === 'all' || categories.includes(category)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/generative-ai-use-cases/genu-chat.gif" alt="GenU Overview Demo" data-demo="chat" style="display: block;">
      <img src="../assets/images/solutions/generative-ai-use-cases/genu-meeting-minutes.gif" alt="GenU Meeting Minutes Demo" data-demo="meeting" style="display: none;">
      <img src="../assets/images/solutions/generative-ai-use-cases/genu-image.gif" alt="GenU Imgage" data-demo="image" style="display: none;">
      <img src="../assets/images/solutions/generative-ai-use-cases/genu-video.gif" alt="GenU Video Demo" data-demo="video" style="display: none;">
      <img src="../assets/images/solutions/generative-ai-use-cases/genu-builder.gif" alt="GenU Builder Demo" data-demo="builder" style="display: none;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/generative-ai-use-cases/">Generative AI Use Cases</a></div>
      <div class="solution-card__description">
        <div class="solution-card__tags">
          <button class="solution-card__tag active" onclick="toggleDemo(this, 'chat')">Chat/RAG</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'meeting')">Meeting</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'image')">Image</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'video')">Video</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'builder')">Builder</button>
        </div>
        <a href="https://github.com/aws-samples/generative-ai-use-cases-jp" target="_blank">Generative AI Use Cases</a> is an application with various generative AI use cases pre-built. It's ideal for building a safe and easy-to-use environment for everyone when promoting the adoption of generative AI within your organization.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="ap-northeast-3">Osaka</option>
        <option value="us-east-1">Virginia</option>
        <option value="us-west-2">Oregon</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&amp;param_UsePreviousDeploymentParameter=true&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-sync"></i>　Update
      </a>
      <a href="solutions/generative-ai-use-cases/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
    <div class="deployment-help">
      <strong>Initial deployment:</strong> Use the Deploy button.<br>
      <strong>Updates after deployment:</strong> Use the Update button to inherit previous settings by entering only Environment and NotificationEmailAddress (leave others as default values). (<a href="solutions/generative-ai-use-cases-update/" target="_blank">Check detailed method</a>)
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/dify/dify-diagram.png" alt="Dify Diagram" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/dify/">Dify</a></div>
      <div class="solution-card__description">
        <a href="https://dify.ai" target="_blank">Dify</a> allows you to create chatbots and workflows using generative AI through a GUI. It's ideal when you want to implement multi-step generative AI processing. For AWS deployment, you can easily deploy using <a href="https://github.com/aws-samples/dify-self-hosted-on-aws" target="_blank">dify-self-hosted-on-aws</a>.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="ap-northeast-3">Osaka</option>
        <option value="us-east-1">Virginia</option>
        <option value="us-west-2">Oregon</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/dify/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/bedrock-chat/demo.gif" alt="Bedrock Chat Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/brchat/">Bedrock Chat</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-chat" target="_blank">Bedrock Chat</a> is a multilingual generative AI platform powered by Amazon Bedrock. It supports not only simple chat functionality but also custom bot creation using knowledge bases (RAG), bot sharing through a bot store, and task automation using agent functionality.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="ap-northeast-3">Osaka</option>
        <option value="us-east-1">Virginia</option>
        <option value="us-west-2">Oregon</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=BrChatDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/BrChatDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/brchat/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/genai-design-studio/demo.gif" alt="GenAI Design Studio Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/genai-design-studio/">GenAI Design Studio</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-genai-design-studio" target="_blank">GenAI Design Studio</a> is a virtual try-on solution powered by Amazon Nova Canvas. It aims to streamline various processes in the apparel industry and e-commerce services, from fashion design to actual model photography.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="us-east-1">Virginia</option>
        <option value="eu-west-1">Ireland</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenStudioDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenStudioDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/genai-design-studio/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/comfyui/comfy.png" alt="ComfyUI Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/comfyui/">ComfyUI</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/comfyanonymous/ComfyUI" target="_blank">ComfyUI</a> is a node-based generative AI image generation tool that combines Stable Diffusion and various models to generate high-quality images. It's ideal for visually building complex workflows and having fine-grained control over the image generation process.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="ap-northeast-3">Osaka</option>
        <option value="us-east-1">Virginia</option>
        <option value="us-west-2">Oregon</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=ComfyUIDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/ComfyUIDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/comfyui/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="document">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/rapid/en_new_review_floor_plan.png" alt="RAPID Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/rapid/">Review & Assessment Powered by Intelligent Documentation (RAPID)</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation" target="_blank">RAPID</a> is a document review solution powered by generative AI (Amazon Bedrock). It streamlines review processes involving extensive documents and complex checklists using a Human in the Loop approach.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="us-west-2">Oregon</option>
        <option value="us-east-1">Virginia</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RapidDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RapidDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/rapid/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="document">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/c360/c360-demo.gif" alt="Customer 360 Data Fusion Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/c360/">Customer 360 Data Fusion</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-c360-text2sql-segmentation-entityresolution" target="_blank">Customer 360 Data Fusion</a> leverages AWS Entity Resolution to match and integrate customer data across different data sources, enabling natural language segment creation for comprehensive Customer 360 implementation.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="us-east-1">Virginia</option>
        <option value="us-west-2">Oregon</option>
        <option value="ap-northeast-1">Tokyo</option>
      </select>
      <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=C360DeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/C360DeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/c360/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/bedrock-engineer/agent-chat-diagram.png" alt="Bedrock Engineer Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/bedrock-engineer/">Bedrock Engineer</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-engineer" target="_blank">Bedrock Engineer</a> is an autonomous software development agent application powered by Amazon Bedrock. You can customize and use various features such as file creation/editing, command execution, web search, knowledge base utilization, multi-agent collaboration, and image generation.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <a href="https://github.com/aws-samples/bedrock-engineer/releases/latest" class="download-button md-button" target="_blank">
        <i class="fa-solid fa-download"></i>　Download Latest Release
      </a>
      <a href="solutions/bedrock-engineer/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="../assets/images/solutions/remote-swe-agents/ss-chat.png" alt="Remote SWE Agents Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/remote-swe-agents/">Remote SWE Agents</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/remote-swe-agents" target="_blank">Remote SWE Agents</a> is an example implementation of a fully autonomous software development AI agent. This agent operates in a dedicated development environment for each task, performing development work without depending on the user's PC.
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">Tokyo</option>
        <option value="us-west-2">Oregon</option>
        <option value="us-east-1">Virginia</option>
      </select>
      <a href="https://us-west-2.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RemoteSweDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RemoteSweDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/remote-swe-agents/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Details
      </a>
    </div>
  </div>
</div>

## 3. Start Journey

For Generative AI Use Cases, you can learn how to use it by following the next workshop.

* [Generative AI Experience Workshop](https://catalog.workshops.aws/generative-ai-use-cases-jp)
