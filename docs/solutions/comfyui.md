# ComfyUI

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) は、ノードベースの生成AI画像生成ツールで、Stable Diffusion や様々なモデルを組み合わせて高品質な画像を生成できます。複雑なワークフローを視覚的に構築し、画像生成プロセスを細かく制御したい場合に最適です。AWS へのデプロイには [cost-effective-aws-deployment-of-comfyui](https://github.com/aws-samples/cost-effective-aws-deployment-of-comfyui) を使用して、スケーラブルで費用対効果の高い環境を構築できます。

## 主な機能

- **ノードベースワークフロー**: ドラッグ&ドロップでワークフローを視覚的に構築
- **モデル対応**: Stable Diffusion、ControlNet、LoRA など多様なモデルをサポート
- **カスタムノード**: コミュニティ開発のカスタムノードで機能拡張が可能
- **バッチ処理**: 複数の画像を一度に処理する効率的なバッチ機能
- **API統合**: RESTful APIを通じて外部アプリケーションとの連携
- **リアルタイムプレビュー**: 生成プロセスをリアルタイムで確認

## 主要ユースケース

- **芸術的な画像生成**: 複雑なスタイルと構成を持つアート作品の作成
- **プロダクトデザイン**: コンセプトアートやプロトタイプ画像の生成
- **コンテンツ制作**: ゲーム、映画、広告用の視覚素材作成
- **研究開発**: 新しい生成技術やモデルの実験とテスト

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

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
  </div>
</div>

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **Environment**: デプロイする環境の種別（デフォルト: dev）
* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **SelfSignUp**: セルフサインアップの有効/無効（デフォルト: false）
* **AllowedSignUpEmailDomains**: サインアップを許可するメールドメイン（例: example1.co.jp, example2.co.jp）
* **AllowedIpV4AddressRanges**: アクセスを許可するIPv4アドレス範囲（例: 10.0.0.100/32, 192.168.0.0/24）
* **AllowedIpV6AddressRanges**: アクセスを許可するIPv6アドレス範囲

!!! warning "セキュリティに関する注意点"
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

    1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
    2. **セルフサインアップの制御**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成、もしくは `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可
    3. **リソース監視**: GPU 使用量とコストを定期的に監視

### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが以下の情報とともに届きます：

1. **アプリケーションURL**: ComfyUI にアクセスするためのログインURL
2. **ユーザー作成手順**: Amazon Cognito でのユーザー作成方法（セルフサインアップが無効の場合）
3. **環境設定**: デプロイされた環境の詳細情報
4. **AWS Cognito ユーザー管理URL**: ユーザー作成とグループ管理のためのコンソールリンク

### リソースの削除

デプロイしたリソースを削除するには、CloudFormation コンソールから以下のスタックを削除します：

1. ComfyUI メインスタック（環境名を含む）
2. `ComfyUIDeploymentStack` デプロイメントスタック

!!! warning "注意"
    スタック削除により、保存された画像やカスタム設定もすべて削除されます。必要なデータは事前にバックアップしてください。

## 使用方法

ComfyUI にログインした後は、以下の手順で画像生成を開始できます：

1. **ワークフローの選択**: 事前定義されたワークフローを選択、または新しく作成
2. **ノードの設定**: プロンプト、モデル、パラメータなどを設定
3. **実行**: "Queue Prompt" ボタンで画像生成を開始
4. **結果の確認**: 生成された画像をダウンロードまたは保存

## トラブルシューティング

### よくある問題

- **ログインできない**: Cognitoユーザープールでユーザーが正しく作成されているか確認
- **画像生成が失敗する**: GPU容量とメモリ使用量を確認
- **アクセスが拒否される**: IP制限設定を確認し、現在のIPアドレスが許可されているか確認

### ログの確認

CloudWatch Logsでアプリケーションのログを確認できます：

- ComfyUI アプリケーションログ
- CodeBuild デプロイメントログ
