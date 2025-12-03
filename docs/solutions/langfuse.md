# Langfuse

[Langfuse](https://langfuse.com/) は、オープンソースの LLMOps プラットフォームです。生成 AI アプリケーションの観測と深い分析を提供し、評価・改善・デバッグを容易にします。

## 主な機能

- **トレース**: LLM アプリケーション / エージェントの応答やツール等の呼び出しを完全に追跡
- **メトリクス監視**: LLM アプリケーションのパフォーマンスやコストに関わるトークン数等をモニタリング
- **プロンプトマネジメント**: LLM アプリケーション / エージェントのプロンプトのバージョン管理と適用
- **プレイグラウンド**: 異なるプロンプトやパラメーターでアドホックに挙動を検証
- **評価**: トレースからデータセットを作成し、オンライン / オフラインの評価を実行
- **アノテーション**: 蓄積された応答に対し Positive / Negative 等のフィードバックを実施
- **Public API**: API による Langfuse の機能の操作

## アーキテクチャ

AWS の Managed Service を使用したデプロイを行います。詳細は [Hosting Langfuse V3 on Amazon ECS with Fargate using CDK Python](https://github.com/aws-samples/deploy-langfuse-on-ecs-with-fargate/tree/main/langfuse-v3) を参照してください。参照先の GitHub にある CDK を用いデプロイを行います。

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">東京</option>
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=LangfuseDeploymentStack&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/LangfuseDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=LangfuseDeletionStack&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/LangfuseDeploymentStack.yaml&amp;param_ExecuteDelete=true" class="deployment-button md-button md-button--danger" target="_blank">
      <i class="fa-solid fa-trash"></i>　Delete
    </a>
  </div>
  <div class="deployment-help">
    <strong>初回デプロイ:</strong> Deploy ボタンを使用してください。<br>
    <strong>完全削除:</strong> Delete ボタンにより既存の Langfuse スタックをすべて削除できます（再デプロイは行われません）。
  </div>
</div>

### パラメーター設定

デプロイする際に、以下のパラメータを設定します。

#### 通知設定

- **NotificationEmailAddress** (必須): デプロイの開始と完了を通知するメールアドレス

#### デプロイオプション

- **ExecuteDelete** (デフォルト: false): デプロイ済みの Langfuse スタックを削除します（警告: すべてのデータが削除されます）

#### Langfuse 設定

- **LangfuseWorkerDesiredCount** (デフォルト: 1): バックグラウンド処理用のワーカータスク数
- **DatabaseInstanceType** (デフォルト: db.t4g.medium): Aurora PostgreSQL インスタンスタイプ
    - 選択肢: db.t4g.medium, db.t4g.large, db.r6g.large, db.r6g.xlarge
- **CacheNodeType** (デフォルト: cache.t4g.micro): ElastiCache Redis ノードタイプ
    - 選択肢: cache.t4g.micro, cache.t4g.small, cache.t4g.medium, cache.r6g.large
- **TelemetryEnabled** (デフォルト: true): Langfuse テレメトリを有効化
- **ExperimentalFeaturesEnabled** (デフォルト: true): 実験的機能を有効化

#### 初期セットアップ

- **OrganizationId** (デフォルト: my-org): 組織識別子
- **OrganizationName** (デフォルト: My Org): 組織表示名
- **ProjectId** (デフォルト: my-project): プロジェクト識別子
- **ProjectName** (デフォルト: My Project): プロジェクト表示名

### デプロイ時間

- 初回デプロイ: 25-35 分
- スタック削除: 15-20 分

## 使い方

デプロイが完了すると、Langfuse の URL とログイン情報がメールで送信されます。

### 1. ログイン

1. メールに記載された Langfuse URL をブラウザで開きます
2. メールに記載されたメールアドレスとパスワードでログインします
3. **重要**: 初回ログイン後、必ずパスワードを変更してください

### 2. アプリケーションとの統合

Langfuse は様々なエージェント開発フレームワークと統合できます

* [Amazon Bedrock AgentCore](https://langfuse.com/integrations/frameworks/amazon-agentcore)
* [Strands Agents](https://langfuse.com/integrations/frameworks/strands-agents)
* [LangChain & LangGraph Integration](https://langfuse.com/integrations/frameworks/langchain)

## セキュリティに関する考慮事項

### 現在の構成

- Application Load Balancer はパブリックアクセス可能 (0.0.0.0/0)
- 認証は Langfuse アプリケーションで処理
- シークレットは自動生成され AWS Secrets Manager に保存
- すべてのデータは保存時に暗号化 (RDS, S3, EFS)

### 本番環境での推奨事項

1. **ネットワークセキュリティ**: VPN/Direct Connect アクセスを使用したプライベートサブネットへのデプロイを検討
2. **IP 制限**: CDK コードを変更して IP 許可リストのセキュリティグループルールを追加
3. **HTTPS**: ALB 用の ACM 証明書を使用したカスタムドメインの設定
4. **モニタリング**: リソース使用率の CloudWatch アラームを設定
5. **バックアップ**: Aurora の自動バックアップと定期的なスナップショットを有効化

## コスト最適化

### デフォルト構成のコスト（概算）

- Aurora PostgreSQL (db.t4g.medium): 約 $59/月
- ElastiCache Redis (cache.t4g.micro): 約 $12/月
- ECS Fargate (3 サービス): 約 $72/月
- Application Load Balancer: 約 $16/月
- データ転送とストレージ: 変動

**月額合計: 約 $160-180** ( + S3、EFS、データ転送)

### 最適化のヒント

1. 開発/テスト環境では小さいインスタンスタイプを使用
2. 非本番環境では Aurora の自動一時停止を有効化
3. 実際のワークロードに基づいてワーカー数を調整
4. S3 ストレージのライフサイクルポリシーを監視・最適化

## トラブルシューティング

### デプロイの問題

CodeBuild ログを確認:
```bash
aws logs tail /aws/codebuild/CodeBuild-for-LangfuseDeploymentStack --follow
```

### アプリケーションの問題

CloudWatch Logs で ECS タスクログを確認:
- `/ecs/langfuse-web`
- `/ecs/langfuse-worker`
- `/ecs/clickhouse`

### よくある問題

1. **デプロイタイムアウト**: CDK ブートストラップまたは ECR イメージプルに予想以上の時間がかかる場合があります
2. **データベース接続エラー**: セキュリティグループルールと Aurora のステータスを確認
3. **ワーカーが処理しない**: Redis 接続とワーカータスクのステータスを確認

## クリーンアップ

1. 既存のデプロイスタック (`LangfuseDeploymentStack`) を削除
2. 「削除」のボタンを押す (スタック名は自動的に `LangfuseDeletionStack` に設定されます)
3. CloudFormation の画面で内容を確認して実行
4. CodeBuild 経由で `cdk destroy --force --all` が実行される

**警告**: すべてのデータ (トレース、プロンプト、設定) が削除されます。削除前に重要なデータをエクスポートしてください。

## 参考資料

- [Langfuse 公式ドキュメント](https://langfuse.com/docs)
- [Langfuse セルフホスティングガイド](https://langfuse.com/self-hosting)
- [GitHub リポジトリ](https://github.com/aws-samples/deploy-langfuse-on-ecs-with-fargate)
- [GenAIOps ワークショップ](https://catalog.workshops.aws/genaiops-langfuse)
