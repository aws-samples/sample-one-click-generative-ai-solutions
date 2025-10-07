# Review & Assessment Powered by Intelligent Documentation (RAPID)

[RAPID](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation) は、生成 AI (Amazon Bedrock) を活用した書類審査ソリューションです。膨大な書類と複雑なチェックリストによる審査業務を、Human in the Loop アプローチで効率化します。チェックリストの構造化から AI による審査、そして人間の最終判断までの一連のプロセスをサポートし、審査時間の短縮と品質向上を実現します。

![overview](/docs/assets/images/solutions/rapid/rapid_overview_top.png)

![overview](/docs/assets/images/solutions/rapid/rapid_overview_detail.png)

## 主な機能

- **チェックリスト構造化**: 複雑なチェックリストを AI が理解しやすい形式に自動構造化
- **AI による書類審査**: Amazon Bedrock を活用して書類内容を自動分析・評価
- **Human in the Loop**: AI の判断結果を人間が最終確認・修正する仕組み
- **審査結果の可視化**: 審査結果を分かりやすく表示し、効率的な確認作業をサポート
- **バッチ処理対応**: 大量の書類を一括で処理可能
- **カスタマイズ可能**: 業界や用途に応じたチェックリストのカスタマイズが可能

## 主なユースケース

* 製品仕様書の要件適合レビュー
   * 製品開発における仕様書が、要求仕様や業界標準を満たしているかを効率的に確認します。年間数千件に及ぶ仕様書を、数百の確認項目と照合する作業を自動化。AI が仕様書から関連情報を抽出・構造化し、要件との照合結果を可視化。レビュアーは効率的に最終確認を行えます。
* 技術マニュアルの品質確認
   * 複雑な技術マニュアルが社内ガイドラインや業界標準に準拠しているかを確認します。年間数万ページの技術文書を、数千項目の品質基準と照合する作業を支援。必要な技術情報の記載漏れや矛盾を自動検出し、一貫性のある高品質なマニュアル作成をサポートします。
* 調達文書のコンプライアンス確認
   * 調達文書や提案書が必要な要件を満たしているかをチェックします。数百ページにわたる文書から必要情報を自動抽出し、年間数万件のドキュメントレビューを効率化。要件リストとの照合結果を人間が最終確認することで、調達プロセスのスピードと精度を向上させます。

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

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
  </div>
</div>

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **AllowedIpV4AddressRanges**: アクセス可能な IPv4 アドレス範囲（JSON配列形式）
* **AllowedIpV6AddressRanges**: アクセス可能な IPv6 アドレス範囲（JSON配列形式）
* **DisableIpv6**: IPv6 サポートを無効にするかどうか（デフォルト: false）
* **AutoMigrate**: デプロイ時に自動的にデータベースマイグレーションを実行するかどうか（デフォルト: true）
* **CognitoSelfSignUpEnabled**: Cognito User Pool のセルフサインアップ機能を有効にするかどうか（デフォルト: true）
* **CognitoUserPoolId**: 既存の Cognito User Pool ID（空の場合は新規作成）
* **CognitoUserPoolClientId**: 既存の Cognito User Pool Client ID（空の場合は新規作成）
* **CognitoDomainPrefix**: Cognito ドメインのプレフィックス（空の場合は自動生成）
* **McpAdmin**: MCP ランタイム Lambda 関数に管理者権限を付与するかどうか（デフォルト: false）
* **RepoUrl**: デプロイするリポジトリの URL
* **Branch**: デプロイするブランチ名（デフォルト: main）
* **GitTag**: デプロイする Git タグ名（指定した場合はブランチより優先）

!!! warning "セキュリティに関する注意点"
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

    1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
    2. **セルフサインアップの無効化**: `CognitoSelfSignUpEnabled` を `false` に設定し、管理者がユーザーを作成
    3. **適切なアクセス制御**: 機密性の高い書類を扱う場合は、適切なアクセス制御を実装

### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. **フロントエンドURL**: アプリケーションにアクセスするためのURL
2. **API URL**: API エンドポイントのURL
3. **Amazon Bedrock モデルアクセス設定**: 必要なモデルへのアクセス有効化手順
   - Anthropic Claude 3.7 Sonnet
   - Amazon Nova Premier
4. **ユーザー作成手順**: セルフサインアップが無効の場合のユーザー作成方法
5. **設定情報**: デプロイ時に指定したパラメータの確認

### リソースの削除

デプロイしたリソースを削除するには、CloudFormation コンソールから `RapidStack` と `RapidDeploymentStack` スタックを削除します。

## 使用方法

1. **チェックリストの作成**: 審査に使用するチェックリストを作成・アップロード
2. **書類のアップロード**: 審査対象となる書類をシステムにアップロード
3. **AI による審査実行**: システムが自動的に書類を分析し、チェックリストと照合
4. **結果の確認・修正**: AI の審査結果を人間が確認し、必要に応じて修正
5. **最終承認**: 審査結果を最終承認し、レポートを出力

