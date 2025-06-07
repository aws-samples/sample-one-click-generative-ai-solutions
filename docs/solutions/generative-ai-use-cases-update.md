# GenU のアップデートやパラメーター変更
GenU を 1 click でデプロイしたあとに、アップデートやパラメーター変更を行う方法を紹介します。GenU でサポートしている詳細なパラメーターは、[GenU のドキュメント](https://aws-samples.github.io/generative-ai-use-cases/ja/ABOUT.html)をご確認ください。

以下のステップを行います。  
- 1 click デプロイで自動生成したパラメータを [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/systems-manager-parameter-store.html) から確認
- [Amazon SageMaker Studio Code Editor](https://docs.aws.amazon.com/ja_jp/sagemaker/latest/dg/code-editor.html) で開発環境を準備
- CDK を使って、アップデートやパラメーター変更

## 1 click デプロイで自動生成したパラメータを確認

1 click デプロイでは、GenU デプロイ時に利用したパラメータが Parameter Store に JSON 形式で保存されます。

[Parameter Store のマネジメントコンソール画面 (※東京リージョン (`ap-northeast-1`) の画面です)](https://ap-northeast-1.console.aws.amazon.com/systems-manager/parameters
)を開き、パラメータを確認します。東京リージョン以外にデプロイした場合は、デプロイ先のリージョンで確認しましょう (`us-east-1` など)。

デプロイしたときに指定した Environment 名 (デフォルトは `dev`) で、以下のパラメータが保存されています  
- `/genu/dev.json` - dev 環境のすべてのパラメータをJSON形式で保存  

!!! Tip
    `staging`, `prod` でデプロイした場合はそれぞれ `/genu/staging.json` 、`/genu/prod.json` となります。 

![parameter-store-01](../assets/images/solutions/generative-ai-use-cases-update/parameter-store-01.png)


パラメータの内容は以下のようなJSON形式で保存されています：

```json
{
  "modelRegion": "us-east-1",
  "modelIds": [
    "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "us.anthropic.claude-opus-4-20250514-v1:0",
    "us.deepseek.r1-v1:0",
    "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    "us.anthropic.claude-3-5-haiku-20241022-v1:0",
    "us.amazon.nova-premier-v1:0",
    "us.amazon.nova-pro-v1:0",
    "us.amazon.nova-lite-v1:0",
    "us.amazon.nova-micro-v1:0"
  ],
  "ragKnowledgeBaseEnabled": false,
  "selfSignUpEnabled": false,
  "allowedSignUpEmailDomains": null,
  "allowedIpV4AddressRanges": null,
  "allowedIpV6AddressRanges": null
}
```

マネジメントコンソールの画面例です (`Show decrypted value` をオンにすると値を参照できます)。  
![parameter-store-02](../assets/images/solutions/generative-ai-use-cases-update/parameter-store-02.png)

この JSON データを使って、後述の手順で該当環境セクションに適用することで、パラメータの確認や変更が可能です。


## SageMaker Code Editor で開発環境を準備
GenU 環境を更新するために、SageMaker Code Editor を利用します。以下のリンクから、CloudFormation を利用して作成をします。

!!! Tip
    GenU のデプロイリージョンをデフォルトの東京から意識して変更した場合は、SageMaker Code Editor のデプロイ先リージョンも変更しましょう。意識していない場合は、以下の URL から東京リージョンにデプロイください。  

!!! Warning
    料金について、デフォルトの ml.t3.medium を東京リージョンで稼働する場合、1 時間あたり $0.065 が発生します。一定時間操作を行わない時には Code Editor が自動停止されるため、コスト最適化がされています。

[![](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/quickcreate?stackName=CodeEditorStack&templateURL=https://ws-assets-prod-iad-r-nrt-2cb4b4649d0e0f94.s3.ap-northeast-1.amazonaws.com/9748a536-3a71-4f0e-a6cd-ece16c0e3487/cloudformation/CodeEditorStack.template.yaml&param_UseDefaultVpc=true&param_EbsSizeInGb=20&param_InstanceType=ml.t3.medium&param_AutoStopIdleTimeInMinutes=180) 

CloudFormation が開かれるので、画面下部にチェックをいれて、Create stack を押します。  
![codeeditor-setup-01](../assets/images/solutions/generative-ai-use-cases-update/codeeditor-setup-01.png)

Stack の作成が始まり、約 7 分後 CREATE_COMPLETE になります。その後、Outputs タブから SageMakerSudioUrl を開きます。  
![codeeditor-setup-02](../assets/images/solutions/generative-ai-use-cases-update/codeeditor-setup-02.png)

SageMaker Studio AI の画面が開かれるので、Skip を押します。  
![codeeditor-setup-03](../assets/images/solutions/generative-ai-use-cases-update/codeeditor-setup-03.png)

Code Editor を開き、Open を押します。Stop していた場合、Start で起動をしたあと、Open を押します。  
![codeeditor-setup-04](../assets/images/solutions/generative-ai-use-cases-update/codeeditor-setup-04.png)


## CDK を使って、アップデートやパラメーター変更
SageMaker Code Editor の画面を開けました。New Terminal を押します。  
![genu-update-01](../assets/images/solutions/generative-ai-use-cases-update/genu-update-01.png)

Terminal 上で以下のコマンドを実行して、最新の GenU のソースコードを clone します。最新のソースコードを clone することで、GenU のバージョンアップが可能です。2 回目以降のバージョンアップで、既に git clone をしている場合は、[こちらの手順](#second-time-update)をご参照ください。
```shell
git clone https://github.com/aws-samples/generative-ai-use-cases.git
```

コマンドの実行する欄について画像で紹介します。以下の画像で説明しているように、画面下部に Terminal が表示されるので、ここでコマンドを実行します。  
![genu-update-02](../assets/images/solutions/generative-ai-use-cases-update/genu-update-02.png)

clone してきたフォルダを開きます。  
![genu-update-03](../assets/images/solutions/generative-ai-use-cases-update/genu-update-03.png)

Yes, I trust the authors を押します。  
![genu-update-04](../assets/images/solutions/generative-ai-use-cases-update/genu-update-04.png)

`packages/cdk/parameter.ts` を開きます。  
![genu-update-05](../assets/images/solutions/generative-ai-use-cases-update/genu-update-05.png)

再び、New Terminal を押して、Terminal を開きます。  
![genu-update-01](../assets/images/solutions/generative-ai-use-cases-update/genu-update-01.png)

GenU を clone したディレクトリに移動します。  
```shell
cd /home/sagemaker-user/generative-ai-use-cases/
```

前の手順で確認した Parameter Store の値を利用して、`parameter.ts` のファイルを編集していきます。  
Environment でデフォルトの dev を利用している場合は、コマンドを利用した自動設定が可能です。

!!! Tip
    `dev` 以外を利用している場合は、Parameter Store の値を手動でコピーして`parameter.ts` のファイルを直接編集してください。

```shell
PARAMS=$(aws ssm get-parameter --name "/genu/dev.json" --with-decryption --query "Parameter.Value" --output text)
```

次に以下のコマンドを発行して、`parameter.ts` ファイルを編集します。  

```shell
node -e "
const fs = require('fs');
const params = $PARAMS;
let content = fs.readFileSync('packages/cdk/parameter.ts', 'utf8');
const devStart = content.indexOf('dev: {');
const devEnd = content.indexOf('},', devStart) + 2;
const jsonString = JSON.stringify(params, null, 2);
const indentedJson = jsonString.split('\n').map((line, index) => {
  if (index === 0) return line;
  return '  ' + line;
}).join('\n');
const newDevSection = 'dev: ' + indentedJson + ',';
content = content.substring(0, devStart) + newDevSection + content.substring(devEnd);
fs.writeFileSync('packages/cdk/parameter.ts', content);
"
```

以下のように dev ファイルの中身が編集されているはずです。  

```ts
  dev: {
    "modelRegion": "us-east-1",
    "modelIds": [
      "us.anthropic.claude-sonnet-4-20250514-v1:0",
      "us.anthropic.claude-opus-4-20250514-v1:0",
      "us.deepseek.r1-v1:0",
      "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
      "us.anthropic.claude-3-5-haiku-20241022-v1:0",
      "us.amazon.nova-premier-v1:0",
      "us.amazon.nova-pro-v1:0",
      "us.amazon.nova-lite-v1:0",
      "us.amazon.nova-micro-v1:0"
    ],
    "ragKnowledgeBaseEnabled": true,
    "selfSignUpEnabled": false,
    "allowedSignUpEmailDomains": [
      "gmail.com"
    ],
    "allowedIpV4AddressRanges": null,
    "allowedIpV6AddressRanges": null
  },
  staging: {
    // Parameters for staging environment
  },
  prod: {
    // Parameters for production environment
  },
```

これが編集後の画面例です。  
![genu-update-06](../assets/images/solutions/generative-ai-use-cases-update/genu-update-06.png)

パラメーターを変更してみましょう。今回の手順では、利用するモデルを変更します。  
![genu-update-07](../assets/images/solutions/generative-ai-use-cases-update/genu-update-07.png)

依存関係を解決します。  
```shell
npm ci
```

実行例  
```shell
sagemaker-user@default:~/generative-ai-use-cases$ npm ci
npm warn deprecated sourcemap-codec@1.4.8: Please use @jridgewell/sourcemap-codec instead
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead
npm warn deprecated @humanwhocodes/config-array@0.13.0: Use @eslint/config-array instead
npm warn deprecated eslint@8.57.1: This version is no longer supported. Please see https://eslint.org/version-support for other options.

> generative-ai-use-cases@4.2.7 prepare
> husky


added 2416 packages, and audited 2461 packages in 2m

477 packages are looking for funding
  run `npm fund` for details

3 moderate severity vulnerabilities

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
npm notice
npm notice New minor version of npm available! 11.3.0 -> 11.4.1
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.4.1
npm notice To update run: npm install -g npm@11.4.1
npm notice
sagemaker-user@default:~/generative-ai-use-cases$ 
```


GenU を更新します。`env=dev` のパラメーターは、デプロイしたい Environent 名を指定します。デフォルトでは dev です。  

```shell
npm run cdk:deploy:quick -- -c env=dev
```


実行例  

```shell
sagemaker-user@default:~/generative-ai-use-cases$ npm run cdk:deploy:quick -- -c env=dev

> generative-ai-use-cases@4.2.7 cdk:deploy:quick
> npm -w packages/cdk run cdk deploy -- --all --asset-parallelism --asset-prebuild=false --concurrency 3 --method=direct --require-approval never --force -c env=dev


> cdk
> cdk deploy --all --asset-parallelism --asset-prebuild=false --concurrency 3 --method=direct --require-approval never --force -c env=dev

`cdk synth` may hang in Docker on Linux 5.6-5.10. See https://github.com/aws/aws-cdk/issues/21379 for workarounds.
Bundling asset GenerativeAiUseCasesStackdev/API/Predict/Code/Stage...

  packages/cdk/cdk.out/bundling-temp-d7718a9e133c5da897e2705c0897279a63ba1441a740635cdf58a04513f40f3e-building/index.js  3.3mb ⚠️

⚡ Done in 438ms

added 114 packages, and audited 120 packages in 5s

3 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

```


一定時間後、デプロイが完了します。元の GenU が更新されました。  

```shell
GenerativeAiUseCasesStackdev.WebUrl = https://xxxxxxxxx.cloudfront.net
Stack ARN:
arn:aws:cloudformation:us-east-1:xxxxxxxxxx:stack/GenerativeAiUseCasesStackdev/83dbd1f0-3ecb-11f0-a659-0e0290ae6345

✨  Total time: 378.4s

sagemaker-user@default:~/generative-ai-use-cases$ 
```

## 2 回目以降に GenU をアップデートする手順 {#second-time-update}
SageMaker Code Editor を利用して、2 回目以降に GenU をアップデートする手順を紹介します。1 回目では git clone を利用していたのに対して、2 回目は既に clone 済みなので手順がが変わります。  
SageMaker Code Editor を開いたあと、Open Folder で GenU のディレクトリを開きます。

![genu-update-repeat-01](../assets/images/solutions/generative-ai-use-cases-update/genu-update-repeat-01.png)

!!! Warning
    `packages/cdk/parameter.ts` を開いて、`dev` や `staging` や `prod` の値を手元にメモをします。**なくした場合は復元が困難なので、メモをし忘れ無いように注意しましょう！**  

![genu-update-repeat-02](../assets/images/solutions/generative-ai-use-cases-update/genu-update-repeat-02.png)

git clone をしたディレクトリに移動します。  

```shell
cd /home/sagemaker-user/generative-ai-use-cases/
```

Code Editor で編集したファイルなどの内容をすべて元の状態に戻します。`parameter.ts` 以外に編集したファイルがあればすべて消えてしまうのでご注意ください。

```shell
git reset --hard
```

以下のコマンドで最新バージョンのソースコードを取得します。

```shell
git pull
```

npm ci で依存関係を解決します。

```shell
npm ci
```

`parameter.ts` のファイルを編集します。先ほど退避した、`dev` や `staging` や `prod` の値を元に戻します。  
![genu-update-repeat-02](../assets/images/solutions/generative-ai-use-cases-update/genu-update-repeat-02.png)

GenU を更新します。`env=dev` のパラメーターは、デプロイしたい Environent 名を指定します。デフォルトでは dev です。  

```shell
npm run cdk:deploy:quick -- -c env=dev
```

これでアップデートが完了です！
