# AI ペルソナシステム

[AI ペルソナシステム](https://github.com/aws-samples/sample-ai-persona) は、Amazon Bedrock を活用し、AIペルソナの構築と、そのAIペルソナをもとにペルソナ同士の議論、インタビューそしてアンケート調査などを通じて商品企画やマーケティング戦略立案のためのインサイトを生成するためのサンプル実装です。

## 主な機能

### 🎙️ インタビュー

AIペルソナとの議論・対話を通じてインサイトを発見します。

- **ペルソナ生成**: インタビュー、調査レポート、レビュー、購買データなど多様なデータ＋自然言語の指示でAIペルソナを自動生成
- **ペルソナ管理**: ペルソナの編集・削除、長期記憶（AgentCore Memory）、知識・外部データの管理
- **議論モード**: 簡易議論（3-5分）、しっかり議論（5-15分）、インタビュー（リアルタイム）の3モード
- **議論結果**: インサイト確認（信頼度スコア付き）、カスタムカテゴリー、過去議論の検索

### 📊 アンケート調査

数百〜数千のAIペルソナに大規模アンケートを実施します。

- **ペルソナデータ設定**: オープンデータセットや自社顧客データ（CSV）のアップロード
- **テンプレート管理**: 選択式・自由記述・スケール評価の質問作成、画像添付
- **結果表示**: CSVダウンロード、ビジュアル分析（棒グラフ）、AIインサイトレポート

## 対象ユースケース

- **商品企画**: AIペルソナとの議論を通じた新商品のアイデア検証
- **マーケティング戦略**: ターゲット顧客の反応シミュレーション
- **顧客調査**: 大規模アンケートによる市場調査の効率化

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
      <option value="ap-northeast-1">東京</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=AIPersonaDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/AIPersonaDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### パラメーター設定

デプロイする際に、以下のパラメータを設定できます。

* **NotificationEmailAddress**
    * デプロイの開始・終了を通知するメールアドレスです
* **Region** (デフォルト: us-east-1)
    * デプロイ先のリージョンです（us-east-1, us-west-2, ap-northeast-1）
* **EnableLongTermMemory** (デフォルト: true)
    * AgentCore Memory による長期記憶機能の有効/無効を切り替えます
* **EnableWaf** (デフォルト: false)
    * CloudFront に AWS WAF を有効化します（レートリミット・マネージドルールによる保護）
* **SelfSignUp** (デフォルト: false)
    * セルフサインアップの有効 / 無効を切り替えます
* **AllowedIpAddresses**
    * アクセス可能な IPv4 アドレスを CIDR 形式で指定します（カンマ区切り、例: 203.0.113.0/24,198.51.100.1/32）。指定時は WAF が自動的に有効化されます

!!! warning "セキュリティに関する注意点"
    
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：
    
    1. **IP制限の設定**: `AllowedIpAddresses` を使用して、アクセス可能な IP アドレスを制限
    2. **セルフサインアップの無効化**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成
    
    IP 制限を設定しない場合は Public Access 可能な状態でデプロイされますが、SelfSignUp は false にしているためログインには AWS アカウントでのユーザー作成 (Amazon Cognito) が必要です。

## デプロイ後の設定

### ユーザー管理

1. デプロイ完了通知メールに記載されたユーザー管理コンソールURLにアクセス
2. Amazon Cognito ユーザープールでユーザーを作成（セルフサインアップ有効時はユーザー自身で登録可能）
3. アプリケーションURLからログイン

### アプリケーションへのアクセス

デプロイ完了後、通知メールに記載されたアプリケーションURL（CloudFront ドメイン）からアクセスできます。

## 詳細情報

詳細な技術情報や開発ガイドについては、[GitHub リポジトリ](https://github.com/aws-samples/sample-ai-persona)をご参照ください。
