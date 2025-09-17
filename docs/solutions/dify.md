# Dify

[Dify](https://dify.ai/jp)は、LLMアプリケーション開発のためのオープンソースプラットフォームです。直感的なGUIを通じて、生成AIを活用したチャットボットやエージェント、複雑なワークフローを簡単に作成できます。Amazon Bedrockなどの様々なLLMと連携し、企業やデベロッパーが独自のAIアプリケーションを迅速に構築・展開することを可能にします。

## 主な特徴

- **直感的なGUIインターフェース**: コーディング不要でAIアプリケーションを構築
- **複数LLMサポート**: Amazon Bedrockを含む様々なLLMとの連携
- **RAG（検索拡張生成）**: ナレッジベースを活用した精度の高い回答生成
- **APIとプラグイン**: 既存システムとの連携や機能拡張が容易
- **マルチステップワークフロー**: 複雑なAIワークフローの視覚的な構築
- **セルフホスティング**: AWSマネージドサービスを活用した安全な環境構築


## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">バージニア</option>
      <option value="ap-northeast-1">東京</option>
      <option value="ap-northeast-3">大阪</option>
      <option value="us-west-2">オレゴン</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### パラメータ設定

* NotificationEmailAddress
    * デプロイの開始・終了を通知するメールアドレスです。
* Region
    * デプロイするAWSリージョンです。
* AutoPause
    * データベースの自動停止をON/OFFにします。自動停止後は復旧に約10秒かかります。
* AllowedIpV4Ciders
    * 接続を許可するIPv4 CIDRレンジを指定します（例：0.0.0.0/1）。
* AllowedIpV6Ciders
    * 接続を許可するIPv6 CIDRレンジを指定します（例：::/1）。
