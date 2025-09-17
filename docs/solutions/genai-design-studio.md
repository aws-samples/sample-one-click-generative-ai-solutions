# GenAI Design Studio

[GenAI Design Studio](https://github.com/aws-samples/sample-genai-design-studio) は、Amazon Nova Canvas を活用したバーチャル試着ソリューションです。アパレル業界やECサービスにおいて、服飾デザインから実際のモデル着用撮影まで、様々なプロセスの効率化を目指します。

## 主な機能

- **モデル生成**: テキストプロンプトを使用してバーチャルモデル画像を生成
- **バーチャル試着**: Amazon Nova Canvas を使用した高品質な服の試着機能
- **背景置換**: テキスト記述による背景の自然な置き換え
- **直感的なUI**: 簡単な操作でプロフェッショナルな結果を得られるユーザーインターフェース
- **高品質な画像生成**: Amazon Nova Canvas の最新技術による高解像度画像生成

## 対象ユーザー

- **アパレル業界**: 服飾デザインの可視化、商品撮影コストの削減
- **ECサービス**: バーチャル試着による顧客体験の向上
- **マーケティング**: 多様なモデルでの商品プロモーション
- **デザイナー**: アイデアの迅速なプロトタイピング

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

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
  </div>
</div>

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **SelfSignUp** (デフォルト: true): セルフサインアップの有効/無効を切り替えます
* **AllowedSignUpEmailDomains**: サインアップを許可するメールドメイン。メールドメインは「@」を含めずに指定してください。（例: example.co.jp）
* **AllowedIpV4AddressRanges** (デフォルト: 0.0.0.0/1,128.0.0.0/1): アクセスを許可するIPv4アドレス範囲
* **AllowedIpV6AddressRanges** (デフォルト: 0000:0000:0000:0000:0000:0000:0000:0000/1,8000:0000:0000:0000:0000:0000:0000:0000/1): アクセスを許可するIPv6アドレス範囲

!!! warning "セキュリティに関する注意点"
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

    1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
    2. **メールドメイン制限**: `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可
    3. **セルフサインアップの管理**: 必要に応じて `SelfSignUp` を `false` に設定し、管理者がユーザーを作成

    IP 制限を設定しない場合は Public Access 可能な状態でデプロイされます。 `SelfSignUp` を false にした場合、AWS アカウントでのユーザー作成 (Amazon Cognito) が必要です。

### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. アプリケーションのURL
2. Amazon Bedrockのモデルアクセス設定手順

### リソースの削除

デプロイしたリソースを削除するには、CloudFormation コンソールから以下のスタックを削除します：

1. `VtoAppStack` スタック（アプリケーション本体）
2. `GenStudioDeploymentStack` スタック（デプロイ用スタック）
