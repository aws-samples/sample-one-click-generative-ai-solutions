# Why AWS Generative AI Solution Box?

## 開発に慣れていなくても、簡単に生成 AI アプリケーションを構築

:zap: **Fast** : 生成 AI の様々なソリューションをワンクリックで構築  
:four_leaf_clover: **Easy-to-use** : 初心者でも効果をすぐに実感できるソリューションを厳選  
:lock: **Secure** : Production-Ready なセキュリティでそのまま本番利用が可能  
:hammer: **Open-Source** : 各ソリューションはオープンソースでカスタマイズ可能  
:book: **Guide** : 使用方法や普及のためのガイドを併せて提供  

## 3 Step の構築手順

<div class="steps-container">
  <div class="step-card">
    <div class="step-number">1</div>
    <div class="step-title">Login AWS</div>
    <div class="step-description">AWS Account を作成し<br/>構築用のユーザーでログイン</div>
  </div>
  <div class="step-card">
    <div class="step-number">2</div>
    <div class="step-title">Choose & Click</div>
    <div class="step-description">使いたいソリューションを選択<br/>クリックして構築開始</div>
  </div>
  <div class="step-card">
    <div class="step-number">3</div>
    <div class="step-title">Start Journey</div>
    <div class="step-description">完成の通知が来たら使用開始</div>
  </div>
</div>

## 1. AWS Account の準備

[AWS を始めたい初心者向け 6 つのポイント](https://aws.amazon.com/jp/local/aws-beginner-six-points/) の "ポイントその２：AWS を使い始めるには？" を参考に AWS のアカウントを作成、サインインしてください。

## 2. Choose & Click

使いたい AWS のソリューションを決めたら、リージョンを選択し Deploy を Click します。デプロイのオプションについての説明などガイドが必要な場合は 詳しく を参照ください。

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterSolutions('all')">すべて</button>
  <button class="filter-btn" onclick="filterSolutions('popular')">🌟 人気</button>
  <button class="filter-btn" onclick="filterSolutions('chat')">💬 チャット・会話</button>
  <button class="filter-btn" onclick="filterSolutions('development')">🔧 開発・自動化</button>
  <button class="filter-btn" onclick="filterSolutions('creative')">🎨 コンテンツ制作</button>
  <button class="filter-btn" onclick="filterSolutions('document')">📄 文書分析</button>
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
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-chat.gif" alt="GenU Overview Demo" data-demo="chat" style="display: block;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-meeting-minutes.gif" alt="GenU Meeting Minutes Demo" data-demo="meeting" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-image.gif" alt="GenU Imgage" data-demo="image" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-video.gif" alt="GenU Video Demo" data-demo="video" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-builder.gif" alt="GenU Builder Demo" data-demo="builder" style="display: none;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Generative AI Use Cases</div>
      <div class="solution-card__description">
        <div class="solution-card__tags">
          <button class="solution-card__tag active" onclick="toggleDemo(this, 'chat')">Chat/RAG</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'meeting')">Meeting</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'image')">Image</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'video')">Video</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'builder')">Builder</button>
        </div>
        <a href="https://github.com/aws-samples/generative-ai-use-cases-jp" target="_blank">Generative AI Use Cases</a> は、生成 AI の様々なユースケースがあらかじめ組み込まれたアプリケーションです。生成 AI の活用をこれから社内に普及するにあたり、安全かつ誰もが容易に使える環境を構築したい場合に最適です。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&amp;param_UsePreviousDeploymentParameter=true&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-sync"></i>　Update
      </a>
      <a href="solutions/generative-ai-use-cases/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
    <div class="deployment-help">
      <strong>初回デプロイ:</strong> Deploy ボタンを使用してください。<br>
      <strong>デプロイ後の更新:</strong> Update ボタンにより Environment、NotificationEmailAddress のみの入力 (他はデフォルト値のままで可) で前回の設定を引き継げます。(<a href="solutions/generative-ai-use-cases-update/" target="_blank">詳細な方法を確認</a>)
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/dify/dify-diagram.png" alt="Dify Diagram" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Dify</div>
      <div class="solution-card__description">
        <a href="https://dify.ai/jp" target="_blank">Dify</a> は、生成 AI を用いたチャットボットやワークフローを GUI で作成することが出来ます。複数ステップにまたがる生成 AI の処理等を実装したい時に最適です。 AWS へのデプロイに当たっては <a href="https://github.com/aws-samples/dify-self-hosted-on-aws" target="_blank">dify-self-hosted-on-aws</a>を使うことで容易に配置できます。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/dify/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/bedrock-chat/demo.gif" alt="Bedrock Chat Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Bedrock Chat</div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-chat" target="_blank">Bedrock Chat</a> は、Amazon Bedrock を活用した多言語対応の生成 AI プラットフォームです。シンプルなチャット機能だけでなく、ナレッジベース (RAG) を活用したカスタムボット作成、ボットストアを通じたボット共有、エージェント機能によるタスク自動化をサポートしています。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=BrChatDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/BrChatDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/brchat/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/genai-design-studio/demo.gif" alt="GenAI Design Studio Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">GenAI Design Studio</div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-genai-design-studio" target="_blank">GenAI Design Studio</a> は、Amazon Nova Canvas を活用したバーチャル試着ソリューションです。アパレル業界やECサービスにおいて、服飾デザインから実際のモデル着用撮影まで、様々なプロセスの効率化を目指します。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-east-1">バージニア</option>
        <option value="eu-west-1">アイルランド</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenStudioDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenStudioDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/genai-design-studio/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/comfyui/comfy.png" alt="ComfyUI Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">ComfyUI</div>
      <div class="solution-card__description">
        <a href="https://github.com/comfyanonymous/ComfyUI" target="_blank">ComfyUI</a> は、ノードベースの生成AI画像生成ツールで、Stable Diffusion や様々なモデルを組み合わせて高品質な画像を生成できます。複雑なワークフローを視覚的に構築し、画像生成プロセスを細かく制御したい場合に最適です。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=ComfyUIDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/ComfyUIDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/comfyui/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="document">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/rapid/en_new_review_floor_plan.png" alt="RAPID Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Review & Assessment Powered by Intelligent Documentation (RAPID)</div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation" target="_blank">RAPID</a> は、生成 AI (Amazon Bedrock) を活用した書類審査ソリューションです。膨大な書類と複雑なチェックリストによる審査業務を、Human in the Loop アプローチで効率化します。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-west-2">オレゴン</option>
        <option value="us-east-1">バージニア</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RapidDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RapidDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/rapid/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/bedrock-engineer/agent-chat-diagram.png" alt="Bedrock Engineer Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Bedrock Engineer</div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-engineer" target="_blank">Bedrock Engineer</a> は、Amazon Bedrock を活用した自律型ソフトウェア開発エージェントアプリケーションです。ファイル作成・編集、コマンド実行、Web 検索、ナレッジベース活用、マルチエージェント連携、画像生成など、様々な機能をカスタマイズして利用できます。
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
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/remote-swe-agents/ss-chat.png" alt="Remote SWE Agents Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title">Remote SWE Agents</div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/remote-swe-agents" target="_blank">Remote SWE Agents</a> は、AI による自律型のソフトウェア開発エージェントの実装例です。このエージェントはタスクごとに専用の開発環境内で動作し、ユーザーの PC に依存することなく開発作業を行います。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-west-2">オレゴン</option>
        <option value="us-east-1">バージニア</option>
      </select>
      <a href="https://us-west-2.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RemoteSweDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RemoteSweDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/remote-swe-agents/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

## 3. Start Journey

Generative AI Use Cases については、次のワークショップを進めることで使い方を学ぶことが出来ます。

* [生成 AI 体験ワークショップ](https://catalog.workshops.aws/generative-ai-use-cases-jp)
