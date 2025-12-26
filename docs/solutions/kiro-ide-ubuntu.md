# Kiro IDE Remote - Ubuntu エディション

[Kiro](https://kiro.dev/) は仕様定義から始まる開発プロセス全体をサポートする、Enterprise Readyなアプリケーション構築に適した統合開発環境です。このUbuntuエディションは、**Ubuntu 24.04 LTS** と **事前設定済みのGNOMEデスクトップ** を使用し、Amazon Linux 2023と比較してGUIアプリケーションのセットアップが容易になっています。

![overview](../assets/images/solutions/kiro-ide/kiro-ide-remote.png)

## Amazon Linux版との主な違い

このUbuntu版には以下の利点があります:

- **GUIサポートが事前インストール済み**: Ubuntu DesktopにはGNOMEが事前設定されており、セットアップの複雑さが軽減されます
- **APTパッケージマネージャー**: Ubuntu/Debianユーザーにとって馴染みのあるパッケージ管理
- **より良いGUIアプリケーションサポート**: Ubuntu Desktopは最初からGUIアプリケーション向けに最適化されています
- **簡素化されたインストール**: 動作するデスクトップ環境を構築するために必要なステップが少なくなります

## 主な機能

- **クラウドベースの開発環境**: ブラウザからアクセス可能なリモートデスクトップ環境
- **Ubuntu 24.04 LTS**: 長期サポートと豊富なコミュニティリソース
- **Amazon DCV による高速接続**: 低レイテンシで快適な開発体験を提供
- **プリインストール済み開発ツール**: Kiro CLI、AWS CLI、AWS SAM CLI、uv、NVMなどが利用可能
- **言語サポート**: 英語または日本語用に事前設定
- **安全なアクセス**: CloudFrontとALB経由での安全な接続

## AWS へのデプロイ

以下のボタンでデプロイできます。AWSにログイン後にクリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
      <option value="ap-northeast-1">東京</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=KiroIDEUbuntuDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/KiroIDEUbuntuDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Ubuntu版をデプロイ
    </a>
  </div>
</div>

### パラメータ設定

* **UserEmail**
    * ユーザーのメールアドレス。通知配信とシステム設定に使用されます。
* **UserFullName**
    * ユーザーのフルネーム。Git設定などに使用されます（デフォルト: Kiro IDE Developer）。
* **InstanceType**
    * EC2インスタンスタイプ（デフォルト: t3.medium）。
* **InstanceVolumeSize**
    * EBSボリュームサイズ（GB単位、デフォルト: 40）。
* **RepoUrl**
    * 開発用に自動的にクローンするGitリポジトリURL（オプション）。
* **Language**
    * OS言語設定。EN（英語）またはJP（日本語）を選択（デフォルト: EN）。

デプロイが開始されると、`UserEmail`に設定したメールアドレスに通知購読を有効にするためのメールが送信されます。メールから購読して通知を受け取ってください。

## 技術的な詳細

### オペレーティングシステム
- **ベースOS**: Ubuntu 24.04 LTS（長期サポート）
- **デスクトップ環境**: GNOME Shell（ubuntu-desktop-minimal）
- **リモートアクセス**: NICE DCVサーバーとウェブビューア

### プリインストールツール
- **開発IDE**: Kiro IDE
- **クラウドツール**: AWS CLI v2、AWS SAM CLI
- **バージョンマネージャー**: NVM（Node Version Manager）、uv（Pythonパッケージマネージャー）
- **ビルドツール**: Git、build-essential、gcc、g++、make
- **CLIツール**: Kiro CLI、jq、curl、wget

### 日本語サポート
Languageパラメータを"JP"に設定すると:
- 日本語言語パックとフォント（Noto CJK）
- 日本語入力メソッド（fcitx5-mozc）
- タイムゾーンをAsia/Tokyoに設定
- ロケールをja_JP.UTF-8に設定

## デプロイ後のアクセス

デプロイが完了すると、以下の情報を含むメールが届きます。CloudFormationのOutputsタブからも確認できます。

- **KiroIDEURL**: Kiro IDEへのアクセスURL
- **Username**: ログインユーザー名
- **Password**: ログインパスワード
- **InstanceId**: EC2インスタンスID

URLにアクセスし、表示されたユーザー名とパスワードでログインします。

### アクセス時の注意事項
* Amazon DCVとOSの2回ログインを求められますが、パスワードは両方とも同じです。
* Kiroでターミナルを開いた際にフォントが伸びて見える場合は、`File > Preference > Settings`を開き、`terminal spacing`で検索し、`Integrated: Letter Spacing`の値を-2から-3程度に調整してください。
* Kiro CLIの認証が遅い場合は、`kiro-cli login --use-device-flow`を試してください。

## アーキテクチャ

デプロイにより以下が作成されます:
1. **VPC** - 2つのアベイラビリティーゾーンにまたがる2つのパブリックサブネット
2. **EC2インスタンス** - GNOMEデスクトップを搭載したUbuntu 24.04 LTSを実行
3. **Application Load Balancer** - トラフィックを分散
4. **CloudFront Distribution** - グローバルアクセスとHTTPS終端
5. **NICE DCVサーバー** - 高性能リモートデスクトップストリーミング
6. **セキュリティグループ** - CloudFrontのみへのアクセス制限

## デプロイ時間

完全なデプロイには約15〜20分かかります:
- スタック作成（5分）
- Ubuntu Desktopインストール（5〜7分）
- NICE DCVとKiro IDEのセットアップ（5〜8分）
- システム再起動とヘルスチェック（2〜3分）

## コスト見積もり

標準的な月額コスト（us-east-1リージョン）:
- **EC2 t3.medium**: 約$30/月
- **EBS gp3 40GB**: 約$3/月
- **ALB**: 約$20/月
- **CloudFront**: 最小限（使用量に依存）
- **データ転送**: 使用量により変動

**合計**: 基本インフラストラクチャで月額約$50〜60

## トラブルシューティング

### デプロイが失敗する
- CloudFormationのEventsタブで具体的なエラーを確認
- AWSアカウントに必要な権限があることを確認（EC2、VPC、IAM、CloudFormationなど）
- Systems ManagerでSSMエージェントの接続性を確認

### DCV URLにアクセスできない
- デプロイ完了後、すべてのサービスが起動するまで数分待つ
- EC2インスタンスが実行中でターゲットグループで正常であることを確認
- DCVサーバーログのCloudWatch Logsを確認

### デスクトップ環境が読み込まれない
- Systems Manager Session Manager経由でインスタンスに接続
- systemdサービスのステータスを確認: `systemctl status dcvserver`
- DCVログを確認: `journalctl -u dcvserver`

## 比較: Amazon Linux vs Ubuntu

| 機能 | Amazon Linux 2023 | Ubuntu 24.04 LTS |
|------|-------------------|------------------|
| デスクトップインストール | 手動（dnf groupinstall） | 事前設定済み（ubuntu-desktop） |
| パッケージマネージャー | DNF | APT |
| GUIアプリサポート | 追加セットアップが必要 | 標準で最適化済み |
| コミュニティサポート | AWS中心 | 大規模なUbuntuコミュニティ |
| LTSサポート | 約2年 | 5年 |
| 日本語入力 | ibus-anthy | fcitx5-mozc |

## Ubuntu版を使用すべき場合

以下の場合はUbuntu版を選択してください:
- Debian/Ubuntuエコシステムに精通している
- より良い標準GUIアプリケーションサポートが必要
- APTパッケージマネージャーを好む
- より長いLTSサポート（5年）が必要
- Ubuntuをターゲットとするアプリケーションを開発している

以下の場合はAmazon Linux版を選択してください:
- AWS固有の機能に最適化したい
- RPMベースのディストリビューションを好む
- AWSサービスとの緊密な統合が必要
- 本番環境でAmazon Linuxを使用している

## 関連リンク

- [Kiro公式ウェブサイト](https://kiro.dev/)
- [Amazon DCV](https://aws.amazon.com/jp/hpc/dcv/)
- [Ubuntu 24.04 LTSリリースノート](https://releases.ubuntu.com/24.04/)
