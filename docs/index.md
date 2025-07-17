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

使いたい AWS のソリューションを決めたら、リージョンを選択し Deploy を Click します。デプロイのオプションについての説明などガイドが必要な場合は Deploy Guide を参照ください。

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="assets/images/usecase_generate_diagram.gif" alt="Generative AI Use Cases Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">Generative AI Use Cases</div>
    <div class="solution-card__description">
      <a href="https://github.com/aws-samples/generative-ai-use-cases-jp" target="_blank">Generative AI Use Cases</a> は、生成 AI の様々なユースケースがあらかじめ組み込まれたアプリケーションです。生成 AI の活用をこれから社内に普及するにあたり、安全かつ誰もが容易に使える環境を構築したい場合に最適です。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="ap-northeast-3">大阪</option>
          <option value="us-east-1">バージニア</option>
          <option value="us-west-2">オレゴン</option>
        </select>
        <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/generative-ai-use-cases/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/dify.png" alt="Dify Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">Dify</div>
    <div class="solution-card__description">
      <a href="https://dify.ai/jp" target="_blank">Dify</a> は、生成 AI を用いたチャットボットやワークフローを GUI で作成することが出来ます。複数ステップにまたがる生成 AI の処理等を実装したい時に最適です。 AWS へのデプロイに当たっては <a href="https://github.com/aws-samples/dify-self-hosted-on-aws" target="_blank">dify-self-hosted-on-aws</a>を使うことで容易に配置できます。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="ap-northeast-3">大阪</option>
          <option value="us-east-1">バージニア</option>
          <option value="us-west-2">オレゴン</option>
        </select>
        <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/dify/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/bedrock-chat.png" alt="Bedrock Chat Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">Bedrock Chat</div>
    <div class="solution-card__description">
      <a href="https://github.com/aws-samples/bedrock-chat" target="_blank">Bedrock Chat</a> は、Amazon Bedrock を活用した多言語対応の生成 AI プラットフォームです。シンプルなチャット機能だけでなく、ナレッジベース (RAG) を活用したカスタムボット作成、ボットストアを通じたボット共有、エージェント機能によるタスク自動化をサポートしています。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="ap-northeast-3">大阪</option>
          <option value="us-east-1">バージニア</option>
          <option value="us-west-2">オレゴン</option>
        </select>
        <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=BrChatDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/BrChatDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/brchat/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/genai-design-studio.png" alt="GenAI Design Studio Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">GenAI Design Studio</div>
    <div class="solution-card__description">
      <a href="https://github.com/aws-samples/sample-genai-design-studio" target="_blank">GenAI Design Studio</a> は、Amazon Nova Canvas を活用したバーチャル試着ソリューションです。アパレル業界やECサービスにおいて、服飾デザインから実際のモデル着用撮影まで、様々なプロセスの効率化を目指します。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="ap-northeast-3">大阪</option>
          <option value="us-east-1">バージニア</option>
          <option value="us-west-2">オレゴン</option>
        </select>
        <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenStudioDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenStudioDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/genai-design-studio/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/comfyui.png" alt="ComfyUI Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">ComfyUI</div>
    <div class="solution-card__description">
      <a href="https://github.com/comfyanonymous/ComfyUI" target="_blank">ComfyUI</a> は、ノードベースの生成AI画像生成ツールで、Stable Diffusion や様々なモデルを組み合わせて高品質な画像を生成できます。複雑なワークフローを視覚的に構築し、画像生成プロセスを細かく制御したい場合に最適です。AWSへのデプロイには <a href="https://github.com/aws-samples/cost-effective-aws-deployment-of-comfyui" target="_blank">cost-effective-aws-deployment-of-comfyui</a> を使用して、スケーラブルで費用対効果の高い環境を構築できます。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="ap-northeast-3">大阪</option>
          <option value="us-east-1">バージニア</option>
          <option value="us-west-2">オレゴン</option>
        </select>
        <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=ComfyUIDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/ComfyUIDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/comfyui/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/bedrock-engineer.png" alt="Bedrock Engineer Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">Bedrock Engineer</div>
    <div class="solution-card__description">
      <a href="https://github.com/aws-samples/bedrock-engineer" target="_blank">Bedrock Engineer</a> は、Amazon Bedrock を活用した自律型ソフトウェア開発エージェントアプリケーションです。ファイル作成・編集、コマンド実行、Web 検索、ナレッジベース活用、マルチエージェント連携、画像生成など、様々な機能をカスタマイズして利用できます。クライアントアプリケーションとして動作するため、直接ダウンロードして使用できます。
    </div>
    <div class="solution-card__actions">
      <div class="download-container">
        <a href="https://github.com/aws-samples/bedrock-engineer/releases/latest" class="download-button md-button" target="_blank">
          <i class="fa-solid fa-download"></i>　Download Latest Release
        </a>
      </div>
      <a href="solutions/bedrock-engineer/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__image">
    <!-- <img src="/assets/images/remote-swe-agents.png" alt="Remote SWE Agents Screenshot"> -->
  </div>
  <div class="solution-card__content">
    <div class="solution-card__title">Remote SWE Agents</div>
    <div class="solution-card__description">
      <a href="https://github.com/aws-samples/remote-swe-agents" target="_blank">Remote SWE Agents</a> は、AI による自律型のソフトウェア開発エージェントの実装例です。このエージェントはタスクごとに専用の開発環境内で動作し、ユーザーの PC に依存することなく開発作業を行います。
    </div>
    <div class="solution-card__actions">
      <div class="deployment-container">
        <select class="region-selector">
          <option value="ap-northeast-1">東京</option>
          <option value="us-west-2">オレゴン</option>
          <option value="us-east-1">バージニア</option>
        </select>
        <a href="https://us-west-2.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RemoteSweDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RemoteSweDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
          <i class="fa-solid fa-rocket"></i>　Deploy
        </a>
      </div>
      <a href="solutions/remote-swe-agents/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        Deploy Guide
      </a>
    </div>
  </div>
</div>

## 3. Start Journey

Generative AI Use Cases については、次のワークショップを進めることで使い方を学ぶことが出来ます。

* [生成 AI 体験ワークショップ](https://catalog.workshops.aws/generative-ai-use-cases-jp)

