# Remote SWE Agents

[Remote SWE Agents](https://github.com/aws-samples/remote-swe-agents) は、AI による自律型のソフトウェア開発エージェントの実装例です。このエージェントは専用の開発環境内で動作し、ユーザーの PC を拘束することなく開発作業を行います。

AWS 上でセルフホスト型OSSソリューションとして提供され、Devin、OpenAI Codex、Google Jules などのクラウドベースの非同期コーディングエージェントと同様のエクスペリエンスを実現します。

## 主な機能

- **完全自律型のソフトウェア開発エージェント** - AI を活用した開発ワークフロー自動化
- **Web ベース管理インターフェース** - セッション管理とリアルタイムモニタリングのための Next.js ウェブアプリ
- **包括的な API** - プログラムによる統合とセッション制御のための RESTful エンドポイント
- **AWS サーバーレスサービスによる稼働** - メンテナンスコストを最小限に抑制
- **システムを使用しない間は固定費用なし**
- **効率的なトークン使用量** - プロンプトキャッシュとミドルアウト戦略による最適化

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-west-2">オレゴン</option>
      <option value="ap-northeast-1">東京</option>
      <option value="us-east-1">バージニア</option>
    </select>
    <a href="https://us-west-2.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RemoteSweDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RemoteSweDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

!!! note "事前準備するアカウント"
    - AWS アカウント
    - GitHub アカウント

### パラメーター設定

- **NotificationEmailAddress**
    - デプロイの開始・終了を通知するメールアドレスです。このアドレスは初期ウェブアプリユーザーとしても設定されます。
- **GitHubAccessTokenValue**
    - GitHub の個人アクセストークン（PAT）で、エージェントが GitHub リポジトリにアクセスするために使用します。
    - 作成方法：[GitHub Personal Access Tokenの作成](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
    - 必要なスコープ：`repo`, `workflow`, `read:org`
- **TargetEnv** (デフォルト: Prod)
    - 環境名の設定です。複数の環境をデプロイしたい場合は、この値を環境ごとにユニークな値に設定してください。
- **AllowedIpV4AddressRanges**
    - ウェブアプリにアクセス可能な IPv4 CIDR 範囲をカンマ区切りで指定します。
- **AllowedIpV6AddressRanges**
    - ウェブアプリにアクセス可能な IPv6 CIDR 範囲をカンマ区切りで指定します。
- **WorkerAdditionalPolicies**
    - ワーカーインスタンスに追加で付与する IAM マネージドポリシーをカンマ区切りで指定します。

## デプロイ後の使用方法

デプロイ完了後、通知メールに記載された URL からウェブアプリにアクセスできます。初期ユーザー情報も同じメールアドレス宛に送信されます。

ウェブアプリでは以下の操作が可能です：

- エージェントセッションの作成と管理
- GitHub リポジトリとの連携
- リアルタイムのエージェント活動モニタリング

### Slack 連携のセットアップ（オプショナル）

Slack からエージェントと対話するための連携設定：

1. **Slack Bolt App の設定**: 通知メールに記載された API エンドポイントを使用して Slack Bolt App を設定します。詳細な設定方法は[ソリューションの README.md](https://github.com/aws-samples/remote-swe-agents/blob/main/README_ja.md) を参照してください。

2. **SSM パラメーターの更新**: Slack アプリ作成後、以下の SSM パラメーターをアプリの認証情報で更新します：
    - [AWS Systems Manager パラメーター](https://console.aws.amazon.com/systems-manager/parameters/) にアクセス
    - `/remote-swe/slack/bot-token` を BOT TOKEN で更新
    - `/remote-swe/slack/signing-secret` を SIGNING SECRET で更新

3. **設定の再デプロイ**: [CodeBuild コンソール](https://console.aws.amazon.com/codesuite/codebuild/projects) から `RemoteSweDeployment` プロジェクトの新しいビルドを開始して Slack 設定を適用します。

デプロイが完了すると、Slack アプリにメンションしてエージェントと直接やり取りできるようになります。

## コスト

Remote SWE Agents は、使用量に応じた従量課金モデルです。使用しない間のコストはほぼゼロで、セッション実行中のみ課金されます。使用されるリソースには EC2 インスタンス、EBS ボリューム、Bedrock API コールなどが含まれます。

![architecture](https://raw.githubusercontent.com/aws-samples/remote-swe-agents/refs/heads/main/docs/imgs/architecture.png)

## 追加リソース

その他の詳細は、[ソリューションのREADME.md](https://github.com/aws-samples/remote-swe-agents/blob/main/README_ja.md)をご覧ください。
