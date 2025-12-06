# GenU でオリジナルのユースケースを作る・共有する

[Generative AI Use Cases](https://github.com/aws-samples/generative-ai-use-cases-jp) のユースケースビルダーモードを使用すると、独自のユースケースを追加・共有できます。

![Image](../assets/images/solutions/generative-ai-use-cases-use-case-builder/usecase_usecase_builder.gif)

さらに、各ユースケースを `.json` 形式で export/import することで共有ができます。ここでは、すぐに import してご利用いただける実践的なユースケースをご紹介します。

## ユースケースの export
作成したユースケースの画面から export アイコンをクリックするとファイルがダウンロードされます。

![ユースケースの利用方法](../assets/images/solutions/generative-ai-use-cases-use-case-builder/export-usecase.png)

## ユースケースの import
ユースケースの新規作成画面から import のアイコンをクリックし、ファイルを選択するとユースケースの文面が挿入されます。

![ユースケースのインポート方法](../assets/images/solutions/generative-ai-use-cases-use-case-builder/import-usecase.png)

## すぐに使えるユースケース

以下のユースケースは自由にダウンロードし、ご自身の環境にインポートしてお試しいただけます。

### ツール系 :hammer:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|ユースケースビルダー - ビルダー|ユースケース自体を作成するユースケースです。ユースケースの説明と入力を与えるとプロンプトテンプレートを自動生成します。|[ダウンロード](../assets/usecases/usecase_builder_builder.json){download="" }|
|プロンプト最適化|プロンプトを分析し、ベストプラクティスに基づいて最適化します。より効果的なプロンプトを作成できます。|[ダウンロード](../assets/usecases/prompt_optimizer.json){download="" }|
|Excel関数生成|自然言語の指示からExcelやGoogleスプレッドシートの数式を生成します。|[ダウンロード](../assets/usecases/excel_formula_generator.json){download="" }|
|SQLクエリ解説|複雑なSQL文を非エンジニアにも理解できる平易な日本語で解説します。|[ダウンロード](../assets/usecases/sql_query_explainer.json){download="" }|
|エラーログ解析|エラーメッセージやログを分析し、原因と解決策を提示します。|[ダウンロード](../assets/usecases/error_log_analyzer.json){download="" }|
|個人情報のマスキング|契約書や議事録から個人情報や機密情報を自動で特定し、適切にマスキング処理を行います。|[ダウンロード](../assets/usecases/pii_masking.json){download="" }|
|常体・敬体変換器|テキストを「だ・である調」と「です・ます調」の間で自然に変換します。|[ダウンロード](../assets/usecases/writing_style_converter.json){download="" }|

### ビジネス一般 :office:
|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|議事録作成アシスタント|議事録を生成するユースケースです。会議の文字起こしやメモを入力すると議事録を自動的に生成します。|[ダウンロード](../assets/usecases/generate_meeting_minutes.json){download="" }|
|やさしい日本語変換|複雑な文章を、外国人や子供にも理解しやすい「やさしい日本語」に変換します。|[ダウンロード](../assets/usecases/plain_japanese_converter.json){download="" }|

### マネジメント :chart_with_upwards_trend:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|会議アジェンダ設計|会議の目的や参加者に応じて、効率的で生産的な会議アジェンダを作成します。|[ダウンロード](../assets/usecases/meeting_agenda_designer.json){download="" }|
|チーム日報の整理|チームメンバー全員の日報を分析し、マネージャー向けに要約・分析します。|[ダウンロード](../assets/usecases/team_daily_report_organizer.json){download="" }|

### 人事・人材育成 :busts_in_silhouette:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|採用面接深掘り質問作成|候補者の履歴書・職務経歴書を分析し、効果的な深掘り質問リストを生成します。|[ダウンロード](../assets/usecases/interview_question_generator.json){download="" }|
|求人票生成|企業の魅力を最大限に引き出しながら、明確で魅力的な求人票を作成します。|[ダウンロード](../assets/usecases/job_posting_generator.json){download="" }|
|評価フィードバック文案作成|評価期間中の行動メモをもとに、建設的で具体的な評価フィードバック文を作成します。|[ダウンロード](../assets/usecases/performance_feedback_generator.json){download="" }|

### 経営 :chart_with_upwards_trend:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|SWOT分析|事業や製品の概要と競合情報をもとに、SWOT分析と戦略オプションを提案します。|[ダウンロード](../assets/usecases/swot_analysis.json){download="" }|
|事業・施策の壁うち|新規事業や施策のアイデアに対して、批判的な視点からリスクと失敗シナリオを分析します。|[ダウンロード](../assets/usecases/business_idea_critic.json){download="" }|

### 法務 :balance_scale:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|NDAチェッカー|NDA（秘密保持契約）の契約書を分析し、自社に不利な条項や不足している規定を指摘します。|[ダウンロード](../assets/usecases/nda_contract_checker.json){download="" }|
|定義語の抜け漏れチェッカー|契約書内の定義語の抜け漏れをチェックし、定義されているが使われていない用語や定義されていないのに使われている用語を特定します。|[ダウンロード](../assets/usecases/contract_term_checker.json){download="" }|
|甲・乙チェッカー|契約書において「甲」と「乙」の主語が適切に使われているかをチェックし、義務や責任の主語の整合性を確認します。|[ダウンロード](../assets/usecases/contract_party_checker.json){download="" }|

### 教育 :mortar_board:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|理解度テスト生成|資料の内容をもとに、質の高いテストと模範解答を作成します。|[ダウンロード](../assets/usecases/comprehension_test_generator.json){download="" }|
|例え話ジェネレーター|複雑で抽象的な概念を、対象者が理解できるように身近なものに例えて説明します。|[ダウンロード](../assets/usecases/analogy_generator.json){download="" }|

### 営業 :handshake:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|顧客レビュー分析|商品レビューを分析し、共通する不満点や意外な評価ポイントを抽出して改善案を提案します。|[ダウンロード](../assets/usecases/customer_review_analysis.json){download="" }|
|クレーム対応メール|顧客からのクレームに対して、適切で誠意のある対応メールを作成します。|[ダウンロード](../assets/usecases/complaint_response_email.json){download="" }|
|留守電スクリプト生成|ビジネスシーンにおける適切な留守番電話メッセージのトーク台本を作成します。|[ダウンロード](../assets/usecases/voicemail_script_generator.json){download="" }|

### マーケティング :mega:

|タイトル                |説明                                                                                                |ダウンロードリンク|
|:---------------------|:------------------------------------------------------------------------------------------------|:---:|
|キャッチコピー案作成|商品の特徴とターゲット層をもとに、魅力的なLPヘッダー用キャッチコピーを10案生成します。|[ダウンロード](../assets/usecases/catchphrase_generator.json){download="" }|