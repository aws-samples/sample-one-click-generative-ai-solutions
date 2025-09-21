# AI営業ロールプレイ

[AI営業ロールプレイ](https://github.com/aws-samples/sample-ai-sales-roleplay) は、生成AIを活用した営業スキル向上のためのロールプレイングシステムです。感情表現豊かなAIとの音声対話を通じて、実践的な営業スキルを身につけることができます。若手営業担当者を対象に、AIとのインタラクティブなシミュレーションを通じて営業スキルの向上を図るシステムです。

## 主な機能

- **AIとの音声対話**: Amazon Bedrock を活用した自然な会話
- **リアルタイム感情フィードバック**: 怒りメーター、信頼度、進捗度の可視化
- **多様なシナリオ**: カスタマイズ可能な営業シーン
- **詳細な分析レポート**: セッション後の改善提案とフィードバック
- **対話中の映像分析**: セッション中の映像を分析して、効果的なアイコンタクトや身振り手振りができているか検証
- **コンプライアンス違反チェック**: コンプライアンスに違反する発言を指摘
- **リファレンスチェック**: ユーザーの発言がリファレンス(根拠資料)に準拠しているか検証

## 対象ユーザー

- **営業部門**: 新人営業担当者のスキル向上、ベテラン営業の継続的なスキル維持
- **人事・研修部門**: 営業研修プログラムの効率化、標準化された営業手法の教育
- **マネージャー**: チームの営業スキル向上、パフォーマンス分析
- **コンプライアンス部門**: 適切な営業手法の教育、法的リスクの軽減

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">東京</option>
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RoleplayDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RoleplayDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **BedrockRegion**: Amazon Bedrock のモデルを利用するリージョン（us-east-1, us-west-2, ap-northeast-1）
* **SelfSignUp** (デフォルト: false): セルフサインアップの有効/無効を切り替えます
* **AllowedSignUpEmailDomains**: サインアップを許可するメールドメイン（例: example1.co.jp, example2.co.jp）
* **AllowedIpV4AddressRanges**: アクセスを許可するIPv4アドレス範囲（例: 10.0.0.100/32, 192.168.0.0/24）。現在のパブリックIPアドレスは https://checkip.amazonaws.com/ で確認できます
* **AllowedIpV6AddressRanges**: アクセスを許可するIPv6アドレス範囲

!!! warning "セキュリティに関する注意点"
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

    1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
    2. **セルフサインアップの無効化**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成
    3. **メールドメイン制限**: `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可

## デプロイ後の設定

### ユーザー管理

セルフサインアップが無効の場合、管理者がAWS Cognitoコンソールでユーザーを作成する必要があります。

1. デプロイ完了通知メールに記載されたユーザー管理コンソールURLにアクセス
2. Amazon Cognito ユーザープールでユーザーを作成
3. 一時パスワードを設定し、ユーザーに共有
4. ユーザーは初回ログイン時にパスワードを変更

### アプリケーションへのアクセス

デプロイ完了後、通知メールに記載されたアプリケーションURLからアクセスできます。

## 詳細情報

詳細な技術情報や開発ガイドについては、[GitHub リポジトリ](https://github.com/aws-samples/sample-ai-sales-roleplay)をご参照ください。
