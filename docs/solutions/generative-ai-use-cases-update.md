# GenU のアップデートやパラメーター変更
GenU を 1 click でデプロイしたあとに、アップデートやパラメーター変更を行う方法を紹介します。基本的な手順を紹介します。GenU でサポートしている詳細なパラメーターは、[GenU のドキュメント](https://aws-samples.github.io/generative-ai-use-cases/ja/ABOUT.html)をご確認ください。

以下のステップを行います。
- 1 click デプロイで自動生成した parameter.ts をダウンロード
- SageMaker CodeEditor で開発環境を準備
- CDK を使って、アップデートやパラメーター変更

## 1 click デプロイで自動生成した parameter.ts をダウンロード

東京リージョンの CloudFormation で 1 click デプロイで作成した GenUDeploymentStack の詳細画面を開き、ParameterFileStoreBucket を開きます。  
![image-20250601221106281](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601221106281.png)

デプロイしたときに指定した Environment 名のディレクトリを開きます。デフォルトは dev です。
![image-20250601221246402](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601221246402.png)

parameter.ts ファイルが S3 に保存されているのでダウンロードします。
![image-20250601221814868](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601221814868.png)

parameter.ts ファイルを開き、23 行目付近の環境ごとのパラメーターを確認します。後の手順で利用します。

```typescript
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
    "ragKnowledgeBaseEnabled": false,
    "selfSignUpEnabled": false,
    "allowedSignUpEmailDomains": null,
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


## SageMaker CodeEditor で開発環境を準備
GenU 環境を更新するために、SageMaker CodeEditor を利用します。以下のリンクから、CloudFormation を利用して作成をします。

[![](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/quickcreate?stackName=CodeEditorStack&templateURL=https://ws-assets-prod-iad-r-nrt-2cb4b4649d0e0f94.s3.ap-northeast-1.amazonaws.com/9748a536-3a71-4f0e-a6cd-ece16c0e3487/cloudformation/CodeEditorStack.template.yaml&param_UseDefaultVpc=true&param_EbsSizeInGb=20&param_InstanceType=ml.t3.medium&param_AutoStopIdleTimeInMinutes=180) 

CloudFormation が開かれるので、画面下部にチェックをいれて、Create stack を押します。
![image-20250601211428869](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601211428869.png)

Stack の作成が始まり、約 7 分後 CREATE_COMPLETE になります。その後、Outputs タブから SageMakerSudioUrl を開きます。
![image-20250601213242980](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601213242980.png)

SageMaker Studio AI の画面が開かれるので、Skip を押します。
![image-20250601200129208](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601200129208.png)

CodeEditor を開き、Open を押します。Stop していた場合、Start で起動をしたあと、Open を押します。
![image-20250601213334293](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601213334293.png)


## CDK を使って、アップデートやパラメーター変更
SageMaker CodeEditor の画面を開けました。New Terminal を押します。
![image-20250601200716789](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601200716789.png)

Terminal 上で以下のコマンドを実行して、最新の GenU のソースコードを clone します。最新のソースコードを clone することで、GenU のバージョンアップを行えます。
```shell
git clone https://github.com/aws-samples/generative-ai-use-cases.git
```

コマンドの実行する欄について画像で紹介します。以下の画像で説明しているように、画面下部に Terminal が表示されるので、ここでコマンドを実行します。
![image-20250601200849728](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601200849728.png)

clone してきたフォルダを開きます。
![image-20250601200933404](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601200933404.png)

Yes, I trust the authors を押します。
![image-20250601201003892](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601201003892.png)

`packages/cdk/parameter.ts` を開きます。
![image-20250601201210065](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601201210065.png)


前の手順でダウンロードした parameter.ts ファイルの内容を確認して、SageMaker CodeEditor にコピーします。
デフォルトでは、dev の部分をコピーします。(23 行目付近)

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
    "ragKnowledgeBaseEnabled": false,
    "selfSignUpEnabled": false,
    "allowedSignUpEmailDomains": null,
    "allowedIpV4AddressRanges": null,
    "allowedIpV6AddressRanges": null
  },
```

これがコピーしたときの画面例です。
![image-20250601201437327](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601201437327.png)

パラメーターを変更してみましょう。今回の手順では、利用するモデルを変更します。
![image-20250601201552068](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601201552068.png)

再び Terminal を開きます。
![image-20250601201738750](/docs/assets/images/solutions/generative-ai-use-cases-update/image-20250601201738750.png)

以下のコマンドを実行します。
```shell
cd /home/sagemaker-user/generative-ai-use-cases/
```

実行例
```shell
sagemaker-user@default:~$ cd /home/sagemaker-user/generative-ai-use-cases/
sagemaker-user@default:~/generative-ai-use-cases$ 
```

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

bootstrap を実行します。

```shell
npx -w packages/cdk cdk bootstrap
```


実行例

```shell
sagemaker-user@default:~/generative-ai-use-cases$ npx -w packages/cdk cdk bootstrap
`cdk synth` may hang in Docker on Linux 5.6-5.10. See https://github.com/aws/aws-cdk/issues/21379 for workarounds.
 ⏳  Bootstrapping environment aws://xxxxxxxxxx/us-east-1...
Trusted accounts for deployment: (none)
Trusted accounts for lookup: (none)
Using default execution policy of 'arn:aws:iam::aws:policy/AdministratorAccess'. Pass '--cloudformation-execution-policies' to customize.
 ✅  Environment aws://xxxxxxxxxx/us-east-1 bootstrapped (no changes).
sagemaker-user@default:~/generative-ai-use-cases$ 
```


GenU を更新します。`env=dev` のパラメーターは、デプロイしたい Environent 名を指定する。デフォルトでは dev です。

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
