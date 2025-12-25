# Kiro IDE Remote

[Kiro](https://kiro.dev/) は、仕様定義から始まる開発工程全体を支援する Enterprise Ready なアプリケーション構築に適した統合開発環境です。公式サイトからインストールしてご利用いただくことももちろん可能ですが、Kiro IDE Remote ではブラウザ経由でリモートデスクトップに構築された Kiro IDE にアクセスできます。Kiro 以外に、Kiro CLI、AWS CLI、AWS SAM CLI などの開発ツールがプリインストールされておりすぐに開発を始めることができます。

![overview](../assets/images/solutions/kiro-ide/kiro-ide-remote.png)

## 主な特徴

- **クラウドベースの開発環境**: ブラウザからアクセス可能なリモートデスクトップ環境
- **Amazon DCV による高速接続**: 低遅延で快適な開発体験を提供
- **プリインストールされた開発ツール**: Kiro CLI、AWS CLI、AWS SAM CLI、uv、NVM などが利用可能
- **日本語対応**: OS 及び日本語入力をあらかじめセットアップ
- **セキュアなアクセス**: CloudFront と ALB を経由した安全な接続

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">東京</option>
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=KiroIDEDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/KiroIDEDeploymentStack.yaml&param_Language=JP" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### パラメータ設定

* UserEmail
    * ユーザーのメールアドレスです。通知の送信先およびシステム設定に使用されます。
* UserFullName
    * ユーザーのフルネームです。Git の設定などに使用されます（デフォルト: Kiro IDE Developer）。
* InstanceType
    * EC2 インスタンスタイプです（デフォルト: t3.medium）。
* InstanceVolumeSize
    * EBS ボリュームサイズ（GB）です（デフォルト: 40）。
* RepoUrl
    * 開発用に自動的にクローンする Git リポジトリの URL です（オプション）。
* Language
    * OS の言語設定です。EN（英語）または JP（日本語）を選択できます（デフォルト: EN）。

デプロイが開始すると `UserEmail` に設定したメールアドレスに通知のサブスクリプションを有効化するためのメールが届きます。メールからサブスクライブを行い通知を受け取ってください。

## デプロイ後のアクセス

デプロイが完了すると、下記の案内が書かれたメールが届きます。または、CloudFormation の Outputs タブからも確認できます。

- **KiroIDEURL**: Kiro IDE へのアクセス URL
- **Username**: ログイン用のユーザー名
- **Password**: ログイン用のパスワード
- **InstanceId**: EC2 インスタンス ID

URL にアクセスし、表示されたユーザー名とパスワードでログインしてください。

* Amazon DCV へのログイン、OS へのログインが 2 回必要求められますがパスワードは同じです。
* Kiro の中でターミナルを立ち上げたとき、フォントが間延びして見える場合は `File > Preference > Settings` を開き、 `terminal spacing` で検索し `Integrated: Letter Spacing` の値を -2~-3 ぐらいに調整してみてください
* Kiro CLI で認証がなかなか進まない場合、`kiro-cli login --use-device-flow` を試してみてください

## 関連リンク

- [Kiro 公式サイト](https://kiro.dev/)
- [Amazon DCV](https://aws.amazon.com/jp/hpc/dcv/)
