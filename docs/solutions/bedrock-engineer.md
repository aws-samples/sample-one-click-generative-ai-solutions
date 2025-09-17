# Bedrock Engineer

[Bedrock Engineer](https://github.com/aws-samples/bedrock-engineer) は、[Amazon Bedrock](https://aws.amazon.com/bedrock/) を活用したソフトウェア開発タスクのための AI アシスタントです。大規模な言語モデルと実際のファイルシステム操作、Web検索機能などを含む自律的な AI エージェントがあなたの開発を支援します。

## 概要

Bedrock Engineer は、強力な AI 機能を備えたスタンドアロンアプリケーション体験を提供します：

- 💬 Amazon Nova、Claude、Meta Llama モデルとのインタラクティブなチャットインターフェース
- 🛠️ ファイル操作、Web 検索、コード実行などのための広範なツール統合
- 🧠 様々なユースケースや専門分野に対応するカスタマイズ可能なエージェント
- 🌐 事前設定されたエージェントを共有・発見するためのエージェントディレクトリ
- 🎤 Amazon Nova Sonic によるボイスチャット機能
- 🖥️ ウェブサイトや図の生成機能

## ダウンロード

次のボタンから最新版をダウンロードできます。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <a href="https://github.com/aws-samples/bedrock-engineer/releases/latest" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-download"></i>　Download Latest Release
    </a>
  </div>
</div>

## 主な機能

### エージェントチャット：カスタマイズ可能な AI アシスタント

エージェントチャット機能は、ニーズに合わせて完全にカスタマイズできる AI アシスタントとのインタラクションのための強力なインターフェースを提供します：

![エージェントチャット](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/agent-chat-diagram.png)

#### 1. カスタマイズ可能なエージェント

左上のメニューからエージェントを選択します。デフォルトでは汎用的なソフトウェア開発に特化した Software Developer, プログラミング学習を支援する Programming Mentor, サービスやプロダクトの構想段階を支援する Product Designer を搭載しています。

![カスタムエージェント](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/custom-agents.png)

エージェントの設定をカスタマイズします。エージェントの名前と説明を入力し、システムプロンプトを入力します。システムプロンプトはエージェントの振る舞いを決定する重要な要素です。エージェントの目的や規制事項、役割、使用できるツールと使うタイミングを明確にしておくことで、より適切な回答を得ることができます。

#### 2. 統合ツール

左下の Tools アイコンをクリックして、エージェントが使用できるツールを選択します。ツールはエージェントごとに個別に設定できます。

![ツール選択](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/select-tools.png)

**ファイルシステム操作**
- フォルダとファイルの作成
- ファイル内容の読み書き
- ディレクトリ構造の一覧表示

**Web & 検索操作**
- Tavily API を使用した Web 検索
- ウェブサイトコンテンツの取得

**Amazon Bedrock 統合**
- 画像生成と認識
- ビデオ生成
- ナレッジベース検索
- Bedrock エージェントとフローの統合

**システムコマンド & コード実行**
- システムコマンドの実行
- 安全な環境での Python コードの実行
- 画面とカメラのキャプチャ

#### 3. Agent Directory：共有と発見

Agent Directoryは、優れたコントリビューターによって作成されたAIエージェントを発見してすぐに使用できるコンテンツハブです。様々なタスクや専門分野向けに設計された厳選済みのエージェントコレクションを提供しています。

![Agent Directory](https://raw.githubusercontent.com/aws-samples/bedrock-engineer/main/assets/agent-directory.png)

**機能**
- **コレクションの閲覧** - コミュニティによって作成された専門的なエージェントの拡大するライブラリを探索
- **検索とフィルタリング** - 検索機能またはタグによるフィルタリングを使用して、ニーズに合ったエージェントを素早く発見
- **詳細情報の表示** - 各エージェントの作成者、システムプロンプト、対応ツール、使用シナリオなどの包括的な情報を確認
- **ワンクリック追加** - ワンクリックで任意のエージェントを個人コレクションに追加し、すぐに使用開始
- **エージェントの投稿** - コントリビューターになって、あなたのカスタムエージェントをコミュニティと共有

## 追加リソース

- [GitHub Repository](https://github.com/aws-samples/bedrock-engineer)
- [英語プレゼンテーションデッキ](https://speakerdeck.com/gawa/introducing-bedrock-engineer-en)
- [日本語プレゼンテーションデッキ](https://speakerdeck.com/gawa/introducing-bedrock-engineer)

## ライセンス

このアプリケーションは MIT-0 ライセンスの下でライセンスされています。詳細は [LICENSE](https://github.com/aws-samples/bedrock-engineer/blob/main/LICENSE) ファイルをご覧ください。
