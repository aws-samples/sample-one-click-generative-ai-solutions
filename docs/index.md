# Why AWS Generative AI Solution Box?

## 開発に慣れていなくても、簡単に生成 AI アプリケーションを構築

:zap: **Fast** : 生成 AI の様々なソリューションをワンクリックで構築  
:four_leaf_clover: **Easy-to-use** : 初心者でも効果をすぐに実感できるソリューションを厳選  
:lock: **Secure** : Production-Ready なセキュリティでそのまま本番利用が可能  
:hammer: **Open-Source** : 各ソリューションはオープンソースでカスタマイズ可能  
:book: **Guide** : 使用方法や普及のためのガイドを併せて提供  

## 3 Step の構築手順

<div class="steps-container">
  <div class="step-card">
    <div class="step-number">1</div>
    <div class="step-title">Login AWS</div>
    <div class="step-description">AWS Account を作成し<br/>構築用のユーザーでログイン</div>
  </div>
  <div class="step-card">
    <div class="step-number">2</div>
    <div class="step-title">Choose & Click</div>
    <div class="step-description">使いたいソリューションを選択<br/>クリックして構築開始</div>
  </div>
  <div class="step-card">
    <div class="step-number">3</div>
    <div class="step-title">Start Journey</div>
    <div class="step-description">完成の通知が来たら使用開始</div>
  </div>
</div>

## 1. AWS Account の準備

[AWS を始めたい初心者向け 6 つのポイント](https://aws.amazon.com/jp/local/aws-beginner-six-points/) の "ポイントその２：AWS を使い始めるには？" を参考に AWS のアカウントを作成、サインインしてください。

## 2. Choose & Click

使いたい AWS のソリューションを決めたら、リージョンを選択し Deploy を Click します。デプロイのオプションについての説明などガイドが必要な場合は「詳しく」を参照ください。

### 課題から探す

<div class="ask-expert-section">
  <div class="ask-expert-header">
    <h3 class="ask-expert-title">
      <i class="fa-solid fa-compass"></i>
      業界ごとの課題からソリューションを選択
    </h3>
  </div>
  
  <div class="industry-tabs-container">
    <div class="industry-tabs" role="tablist">
      <button class="industry-tab active" data-industry="finance" role="tab">
        <span class="tab-icon">💰</span>
        <span class="tab-label">金融</span>
      </button>
      <button class="industry-tab" data-industry="manufacturing" role="tab">
        <span class="tab-icon">🏭</span>
        <span class="tab-label">製造業</span>
      </button>
      <button class="industry-tab" data-industry="retail" role="tab">
        <span class="tab-icon">🛒</span>
        <span class="tab-label">小売・サービス</span>
      </button>
      <button class="industry-tab" data-industry="public" role="tab">
        <span class="tab-icon">🏥</span>
        <span class="tab-label">公共・医療機関</span>
      </button>
      <button class="industry-tab" data-industry="development" role="tab">
        <span class="tab-icon">💻</span>
        <span class="tab-label">開発・IT</span>
      </button>
    </div>
    
    <div class="tab-content-area">
      <div class="tab-content active" id="finance-content">
        <div class="challenge-grid">
          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🖨</span>
              <h4>帳票読取 (OCR)</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>財務報告書をはじめとし読み取り帳票が大量にある</li>
                <li>人手での入力は時間がかかりヒューマンエラーの抑止も課題</li>
                <li>入力データに基づく審査や判断などの迅速化のボトルネックになっている</li>
              </ul>
            </p>
            <div class="solution-badges">
              <strong>💡 生成 AI による帳票読取 </strong> : <a href="solutions/generative-ai-use-cases/">GenU : 様々なモデルで帳票読取</a><br/>
              <span>📚 決算書読み取りへの生成 AI 活用 </span> : <a href="https://aws.amazon.com/jp/blogs/news/gen-ai-usecase-nowcast/" target="_blank">ナウキャスト様での決算短信データ化事例</a><br/>
              <span>📚 OCR のための学習データ作成 </span> : <a href="https://aws.amazon.com/jp/blogs/news/gen-ai-usecase-nowcast/" target="_blank">LayerX 様での領収書や請求書読み取り用 OCR 改善に向けたデータ作成事例</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📄</span>
              <h4>文書審査・レビュー</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>申請書や契約書、財務報告書など確認すべき文書量が膨大</li>
                <li>審査項目が多岐にわたり、また制度や規約の変更による修正も一定間隔で発生</li>
                <li>特定の熟練者に作業が集中し、審査時間がボトルネックとなっている</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による文書審査支援</strong> : <a href="solutions/rapid/">RAPID : 書類審査ソリューション</a><br/>
              <span>📚 広告レビューへの生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/bedrock-nomura/" target="_blank">野村グループ様での金融商品取引法に基づく広告審査事例</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📞</span>
              <h4>コールセンター</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>金融商品や保険など、扱うサービスが多くある</li>
                <li>プランの内容だけでなく補償金額、新規/廃止されたプランの把握が必要</li>
                <li>新しく入ったオペレーターが応対できるようになるまでに学習時間がかかる</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による営業訓練</strong> : <a href="solutions/roleplay/">AI 営業ロールプレイ</a><br/>
              <strong>💡 生成 AI による応答支援</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 文書に基づく回答支援</a><br/>
              <span>📚 コールセンターでの生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/sbi-life-case-study/" target="_blank">SBI 生命保険様でのオペレータ支援事例</a>
            </div>
          </div>

        </div>
        <!--
        <div class="industry-link">
          <a href="industries/finance/">金融のソリューションについて詳しく →</a>
        </div>
        -->
      </div>
      
      <div class="tab-content" id="manufacturing-content">
        <div class="challenge-grid">

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📋</span>
              <h4>要求仕様の確認・見積もり</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>製品開発やプロジェクト時の要求仕様は、数百ページに及ぶ場合がある</li>
                <li>正確な仕様の把握は、正確な見積りに不可欠であり見逃しが許されない</li>
                <li>過去事例との突合による確認も欠かせないが、ドキュメントが散逸している</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による文書審査支援</strong> : <a href="solutions/rapid/">RAPID : 書類審査ソリューション</a><br/>
              <strong>💡 生成 AI によるナレッジ基盤構築</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 知識基盤の構築</a><br/>
              <span>📚 入札書解析への活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/contribution-mitsui-tender-document-analyzer/" target="_blank">三井物産様での数百ページにおよぶ入札書類の確認時間短縮事例</a><br/>
              <span>📚 見積もり比較への活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/jfeengineering-xchat-generative-ai/" target="_blank">JFE エンジニアリング様での見積書読み取り・比較での活用事例</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📊</span>
              <h4>製造プロセスにおけるデータ活用</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>IoT 化により多様なデータが収集されているが、データ量が膨大</li>
                <li>データの意味を読み取れる人材が不足している</li>
                <li>ダッシュボードにくわえ状況に応じたデータに基づく回答を得るのが不可欠</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI を交えた分析ワークフロー構築</strong> : <a href="solutions/dify/">Dify : 画面操作での AI ワークフロー構築</a><br/>
              <span>📚 イベントデータ処理ワークフローの実装</span> : <a href="https://aws.amazon.com/jp/builders-flash/202409/dify-bedrock-automate-security-operation/" target="_blank">サイバーエージェント様で脅威検知イベント分析事例</a><br/>
              <span>📚 見積もり比較への活用</span> : <a href="https://pages.awscloud.com/rs/112-TZM-766/images/IoT%40Loft%2026%20AWS%20%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3.pdf" target="_blank">i Smart Technologies 様での IoT 分析「製造部長」の事例 (p21)</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🔍</span>
              <h4>品質検査の効率化</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>品質検査において、外観検査は未だ重要な工程</li>
                <li>工作機械や車両などはサイズが大きい他点検項目も膨大</li>
                <li>人手不足によるリソース不足・見逃しが大きな課題</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による画像認識処理</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 画像・動画解析</a><br/>
              <span>📚 監視業務への生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/genai-case-study-iwasaki/" target="_blank">岩崎電機様での冠水検知事例</a><br/>
              <span>📚 物体検出での生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/builders-flash/202506/nova-bounding-box/" target="_blank">Amazon Nova による自然言語での物体検出</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🛠</span>
              <h4>保守点検・アフターサービス</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>機械製品や精密機器をはじめ、多種多様な製品ラインナップがある</li>
                <li>各製品の仕様はもちろん、修理に必要な部品や機材などの把握が困難</li>
                <li>修理に行ったら必要な部品が欠けているなどアフターサービスの効率性に課題</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による応答支援</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 文書に基づく回答支援</a><br/>
              <span>📚 設備点検での生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/hitachi-power-solutions-genai/" target="_blank">日立パワーソリューションズ様でのベテラン保守作業員の知識継承の取り組み</a><br/>
              <span>📚 顧客応対での生成 AI 活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/genai-case-study-jsw/" target="_blank">日本製鋼所様での樹脂機械のアフターサービス対応での活用事例</a>
            </div>
          </div>

        </div>

      </div>
      
      <div class="tab-content" id="retail-content">
        <div class="challenge-grid">

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📝</span>
              <h4>マーケティング文書の作成</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>パーソナライズは重要な施策だが個々会員ごと記載内容を変えるのが難しい</li>
                <li>新商品などををタイムリーに送信したいが書き手が不足し頻度に限界</li>
                <li>テンプレートによる効率化は顧客に既視感を与えロイヤルティ低下のリスクも</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による文章作成支援</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 文書作成</a><br/>
              <span>📚 マーケティングメールでの活用</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/oisix/" target="_blank">オイシックス・ラ・大地様でのメルマガ作成・校正支援事例</a><br/>
              <span>📚 ブログ作成での活用</span> : <a href="https://aws.amazon.com/jp/builders-flash/202505/ielove-ai-content-creation/" target="_blank">いえらぶ GROUP 様での不動産業者会員向けブログ作成支援機能提供事例</a><br/>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">👗</span>
              <h4>商品クリエイティブの作成</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>EC サイトの普及により商品画像の作成量が増加</li>
                <li>季節性の商品や高価な商品は撮影の機会が限られ日程調整含めた事前準備が課題</li>
                <li>EC サイトにより要求される画像のサイズや仕様が異なり準備が手間</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI によるアパレル画像生成</strong> : <a href="solutions/genai-design-studio/">GenAI Design Studio : バーチャル試着</a><br/>
              <strong>💡 生成 AI による画像・説明文生成</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 画像生成・説明文生成</a><br/>
              <span>📚 デザイン業務での活用</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/takihyo/" target="_blank">タキヒヨー様での衣服デザインへの生成 AI 活用事例</a><br/>
              <span>📚 広告素材での活用</span> : <a href="https://www.dentsudigital.co.jp/knowledge-charge/articles/2025/2025-0124-aws" target="_blank">電通デジタル様での Amazon Nova Reel による広告用動画生成事例</a><br/>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🤵‍♀️</span>
              <h4>顧客応対</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>店舗体験は EC が普及しても顧客との重要な接点</li>
                <li>人手不足により十分な応対やトレーニングを行うのが困難</li>
                <li>社会問題化しているカスタマーハラスメントへの対策も欠かせない</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による顧客応対</strong> : <a href="solutions/brchat/">BrChat : 内部検証から API による外部公開まで実現</a><br/>
              <strong>💡 生成 AI による営業訓練</strong> : <a href="solutions/roleplay/">AI 営業ロールプレイ</a><br/>
              <span>📚 顧客応対での活用</span> : <a href="https://jinsholdings.com/jp/ja/news/jins_ai/" target="_blank">ジンズ様でのメガネ専門知識を凝縮した対話型接客事例</a>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🌎</span>
              <h4>健全な顧客コミュニティの形成</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>顧客レビューやコミュニティは商品を取り巻く重要な顧客体験</li>
                <li>"荒らし"による悪意あるいは不快な投稿はコミュニティにとって大きなリスク</li>
                <li>レビューやコメントの投稿数は膨大で十分なチェックを行うことが困難</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI によるコメント検知</strong> : <a href="solutions/brchat/">BrChat : 内部検証から API による社内システム組込みまで実現</a><br/>
              <span>📚 掲示板投稿監視での活用</span> : <a href="https://aws.amazon.com/jp/builders-flash/202501/game8-forum-monitoring-system/" target="_blank">ゲームエイト様での掲示板の誹謗中傷・スパム等検知事例</a><br/>
              <span>📚 レビュー監視での活用</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/dmm/" target="_blank">DMM.com 様でのユーザーレビューの規約違反チェック事例</a>
            </div>
          </div>

        </div>
      </div>
      
      <div class="tab-content" id="public-content">
        <div class="challenge-grid">

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">📝</span>
              <h4>公的文書作成</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>公的な文書には様々なフォーマットがありそれに応じた文書作成が必要</li>
                <li>文書作成の時間が住民や患者に向き合う時間を削ぎ残業時間の増加を招いている</li>
                <li>執筆者により記入内容にばらつきがうまれデータ活用が困難</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による文書作成支援</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 閉域ネットワーク内でも構築可能な生成 AI 基盤</a><br/>
              <span>📚 医療文書作成での活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/generative-ai-in-medical-information/" target="_blank">恵寿総合病院様での入退院サマリ作成事例</a><br/>
              <span>📚 業務文書作成での活用</span> : <a href="https://www.nii.ac.jp/event/upload/20250612-4_suzuki.pdf" target="_blank">東北大学様での議事録作成事例</a><br/>
            </div>
          </div>
          
          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🖨</span>
              <h4>文書読み取り</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>公的機関・医療の現場ではいまだ紙のデータが残る</li>
                <li>手書きの情報を読み取りデータ化するのに多大な労力がかかっている</li>
                <li>人手不足になる中、貴重な人的資源を機械的な仕事に割り当てている</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 生成 AI による文書読み取り</strong> : <a href="solutions/generative-ai-use-cases/">GenU : 様々なモデルによる画像読み取り</a><br/>
              <span>📚 医療関連情報での活用</span> : <a href="https://aws.amazon.com/jp/blogs/news/genai-case-study-cotegg/" target="_blank">コーテッグ様での診察券読み取り事例</a><br/>
            </div>
          </div>

        </div>
      </div>
      
      <div class="tab-content" id="development-content">
        <div class="challenge-grid">

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🤖</span>
              <h4>開発スキルのばらつき</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>開発の熟練度や使用する言語の習熟度にばらつきがある</li>
                <li>不慣れな言語ではレビューやテストでの手戻りが多発</li>
                <li>人手不足が深刻になる中、十分な経験者をアサインするのは実質困難</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 プロジェクトに応じた開発アシスタント構築</strong> : <a href="solutions/bedrock-engineer/"> Bedrock Engineer : 開発支援 AI エージェント作成・利用基盤</a><br/>
              <span>📚 開発エージェントによるスキル拡張</span> : <a href="https://aws.amazon.com/jp/q/developer/customers/" target="_blank">テクノブレイブ様での開発環境構築・リアルタイム開発支援事例</a><br/>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">⚙️</span>
              <h4>開発品質管理</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>特に本番のプロダクト開発ではセキュリティやパフォーマンスの懸念点を事前に特定する必要がある</li>
                <li>レビューに割ける時間に限りがあり、不慣れな領域では見逃しもリスク</li>
                <li>大きな機能・修正の場合指摘が多岐にわたり複数回のレビューバックが発生</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 部分的な開発の自動化</strong> : <a href="solutions/remote-swe-agents/">Remote SWE Agents : 自律的ソフトウェア開発エージェント</a><br/>
              <span>📚 レビューの半自動化</span> : <a href="https://aws.amazon.com/jp/solutions/case-studies/kinto-technologies/" target="_blank">KINTOテクノロジーズ様での Pull Request 一次レビュー自動化</a><br/>
            </div>
          </div>

          <div class="challenge-card">
            <div class="challenge-header">
              <span class="challenge-icon">🏗️</span>
              <h4>開発環境</h4>
            </div>
            <p class="challenge-description">
              <ul>
                <li>AI エージェントの開発等には様々なフレームワークのインストールやデプロイのための設定が必要</li>
                <li>インストール時に様々なエラーが発生したり、設定が上手くいかないことが多い</li>
                <li>AI エージェントの利用・開発の民主化に当たり環境の際と手間がボトルネックになっている</li>
              </ul>
            <p>
            <div class="solution-badges">
              <strong>💡 クラウド上の開発環境</strong> : <a href="solutions/aiagentdev/">AI Agent Development Code Server : 事前セットアップ済みの VS Code ベースの開発環境をクラウド上に構築</a><br/>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</div>

### 一覧から探す

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterSolutions('all')">すべて</button>
  <button class="filter-btn" onclick="filterSolutions('popular')">🌟 人気</button>
  <button class="filter-btn" onclick="filterSolutions('chat')">💬 チャット・会話</button>
  <button class="filter-btn" onclick="filterSolutions('development')">🔧 開発・自動化</button>
  <button class="filter-btn" onclick="filterSolutions('creative')">🎨 コンテンツ制作</button>
  <button class="filter-btn" onclick="filterSolutions('document')">📄 文書分析</button>
</div>

<style>
.solution-card {
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  margin-bottom: 2rem;
  background: white;
}

.solution-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 16px rgba(0, 0, 0, 0.1);
}

.solution-card__top {
  display: flex;
  flex-direction: row;
  min-height: 200px;
}

.solution-card__image {
  flex: 1.2;
  background: #f8fafc;
  border-right: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.solution-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.solution-card:hover .solution-card__image img {
  transform: scale(1.05);
}

.solution-card__content {
  flex: 1;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.solution-card__title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--md-primary-fg-color);
  line-height: 1.3;
}

.solution-card__tags {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.solution-card__tag {
  background: #e2e8f0;
  color: #475569;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.solution-card__tag:hover {
  background: var(--md-primary-fg-color);
  color: white;
}

.solution-card__tag.active {
  background: var(--md-primary-fg-color);
  color: white;
}

.solution-card__description {
  color: #4b5563;
  line-height: 1.6;
  font-size: 0.95rem;
}

.solution-card__actions {
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.filter-bar {
  display: flex;
  gap: 0.5rem;
  margin: 1.5rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.filter-btn {
  background: #f8fafc;
  color: #475569;
  border: 1px solid #e2e8f0;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: var(--md-primary-fg-color);
  color: white;
  border-color: var(--md-primary-fg-color);
}

.filter-btn.active {
  background: var(--md-primary-fg-color);
  color: white;
  border-color: var(--md-primary-fg-color);
}

@media screen and (max-width: 768px) {
  .solution-card__top {
    flex-direction: column;
  }
  
  .solution-card__image {
    flex: none;
    height: 150px;
    border-right: none;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  }
}

/* Ask Expert Section Styles */
.ask-expert-section {
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
}

.ask-expert-header {
  background: linear-gradient(135deg, var(--md-primary-fg-color) 0%, #4338ca 100%);
  color: white;
  padding: 1.2rem;
  text-align: center;
}

.ask-expert-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.industry-tabs-container {
  background: #ffffff;
}

.industry-tabs {
  display: flex;
  overflow-x: auto;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.industry-tab {
  flex: 1;
  min-width: 120px;
  padding: 1.2rem 1rem;
  border: none;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.industry-tab:hover {
  background: rgba(var(--md-primary-fg-color-rgb), 0.05);
}

.industry-tab.active {
  border-bottom-color: var(--md-primary-fg-color);
  background: white;
}

.tab-icon {
  font-size: 1.5rem;
}

.tab-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #475569;
}

.industry-tab.active .tab-label {
  color: var(--md-primary-fg-color);
}

.tab-content-area {
  min-height: 300px;
}

.tab-content {
  display: none;
  padding: 2rem;
}

.tab-content.active {
  display: block;
}

.challenge-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.challenge-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.2rem;
  transition: all 0.3s ease;
}

.challenge-card:hover {
  border-color: var(--md-primary-fg-color);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.challenge-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.challenge-icon {
  font-size: 1.5rem;
}

.challenge-header h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.challenge-description {
  color: #64748b;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.industry-link {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e2e8f0;
  text-align: center;
}

.industry-link a {
  color: var(--md-primary-fg-color);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
}

.industry-link a:hover {
  text-decoration: underline;
}

@media screen and (max-width: 768px) {
  .ask-expert-header {
    padding: 1.5rem;
  }
  
  .ask-expert-title {
    font-size: 1.25rem;
  }
  
  .tab-content {
    padding: 1.5rem;
  }
  
  .industry-tabs {
    flex-wrap: wrap;
  }
  
  .industry-tab {
    flex: 1 1 50%;
    min-width: 100px;
  }
}
</style>

<script>
function toggleDemo(tagElement, demoType) {
  const card = tagElement.closest('.solution-card');
  const images = card.querySelectorAll('.solution-card__image img');
  const tags = card.querySelectorAll('.solution-card__tag');
  
  tags.forEach(tag => tag.classList.remove('active'));
  tagElement.classList.add('active');
  
  images.forEach(img => img.style.display = 'none');
  
  const targetImg = card.querySelector(`[data-demo="${demoType}"]`);
  if (targetImg) {
    targetImg.style.display = 'block';
  }
}

function filterSolutions(category) {
  const cards = document.querySelectorAll('.solution-card');
  const buttons = document.querySelectorAll('.filter-btn');
  
  buttons.forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  
  cards.forEach(card => {
    const categories = card.dataset.category || '';
    if (category === 'all' || categories.includes(category)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

// Tab functionality
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.industry-tab');
  const contents = document.querySelectorAll('.tab-content');
  const industries = ['finance', 'manufacturing', 'retail', 'public', 'development'];
  
  function activateTab(industry) {
    tabs.forEach(t => t.classList.remove('active'));
    contents.forEach(c => c.classList.remove('active'));
    
    const targetTab = document.querySelector(`[data-industry="${industry}"]`);
    const targetContent = document.getElementById(industry + '-content');
    
    if (targetTab && targetContent) {
      targetTab.classList.add('active');
      targetContent.classList.add('active');
    }
  }
  
  // Check URL parameter first, then day of week
  const urlParams = new URLSearchParams(window.location.search);
  const industryParam = urlParams.get('industry');
  
  if (industryParam && industries.includes(industryParam)) {
    activateTab(industryParam);
  } else {
    // Select tab based on day of week (0=Sunday, 1=Monday, etc.)
    const dayOfWeek = new Date().getDay();
    const selectedIndustry = industries[dayOfWeek % industries.length];
    activateTab(selectedIndustry);
  }
  
  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const industry = this.dataset.industry;
      activateTab(industry);
      
      // Update URL parameter
      const url = new URL(window.location);
      url.searchParams.set('industry', industry);
      window.history.replaceState({}, '', url);
    });
  });
});
</script>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-chat.gif" alt="GenU Overview Demo" data-demo="chat" style="display: block;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-meeting-minutes.gif" alt="GenU Meeting Minutes Demo" data-demo="meeting" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-image.gif" alt="GenU Imgage" data-demo="image" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-video.gif" alt="GenU Video Demo" data-demo="video" style="display: none;">
      <img src="./assets/images/solutions/generative-ai-use-cases/genu-builder.gif" alt="GenU Builder Demo" data-demo="builder" style="display: none;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/generative-ai-use-cases/">Generative AI Use Cases</a></div>
      <div class="solution-card__description">
        <div class="solution-card__tags">
          <button class="solution-card__tag active" onclick="toggleDemo(this, 'chat')">Chat/RAG</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'meeting')">Meeting</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'image')">Image</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'video')">Video</button>
          <button class="solution-card__tag" onclick="toggleDemo(this, 'builder')">Builder</button>
        </div>
        <a href="https://github.com/aws-samples/generative-ai-use-cases-jp" target="_blank">Generative AI Use Cases</a> は、生成 AI の様々なユースケースがあらかじめ組み込まれたアプリケーションです。生成 AI の活用をこれから社内に普及するにあたり、安全かつ誰もが容易に使える環境を構築したい場合に最適です。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&amp;param_UsePreviousDeploymentParameter=true&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-sync"></i>　Update
      </a>
      <a href="solutions/generative-ai-use-cases/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
    <div class="deployment-help">
      <strong>初回デプロイ:</strong> Deploy ボタンを使用してください。<br>
      <strong>デプロイ後の更新:</strong> Update ボタンにより Environment、NotificationEmailAddress のみの入力 (他はデフォルト値のままで可) で前回の設定を引き継げます。(<a href="solutions/generative-ai-use-cases-update/" target="_blank">詳細な方法を確認</a>)
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/dify/dify-diagram.png" alt="Dify Diagram" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/dify/">Dify</a></div>
      <div class="solution-card__description">
        <a href="https://dify.ai/jp" target="_blank">Dify</a> は、生成 AI を用いたチャットボットやワークフローを GUI で作成することが出来ます。複数ステップにまたがる生成 AI の処理等を実装したい時に最適です。 AWS へのデプロイに当たっては <a href="https://github.com/aws-samples/dify-self-hosted-on-aws" target="_blank">dify-self-hosted-on-aws</a>を使うことで容易に配置できます。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/dify/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="popular chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/bedrock-chat/demo.gif" alt="Bedrock Chat Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/brchat/">Bedrock Chat</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-chat" target="_blank">Bedrock Chat</a> は、Amazon Bedrock を活用した多言語対応の生成 AI プラットフォームです。シンプルなチャット機能だけでなく、ナレッジベース (RAG) を活用したカスタムボット作成、ボットストアを通じたボット共有、エージェント機能によるタスク自動化をサポートしています。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=BrChatDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/BrChatDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/brchat/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="document">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/rapid/en_new_review_floor_plan.png" alt="RAPID Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/rapid/">Review & Assessment Powered by Intelligent Documentation (RAPID)</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation" target="_blank">RAPID</a> は、生成 AI (Amazon Bedrock) を活用した書類審査ソリューションです。膨大な書類と複雑なチェックリストによる審査業務を、Human in the Loop アプローチで効率化します。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-west-2">オレゴン</option>
        <option value="us-east-1">バージニア</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RapidDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RapidDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/rapid/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="chat">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/roleplay/demo.png" alt="AI Sales Roleplay Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/roleplay/">AI営業ロールプレイ</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-ai-sales-roleplay" target="_blank">AI営業ロールプレイ</a> は、生成AIを活用した営業スキル向上のためのロールプレイングシステムです。感情表現豊かなAIとの音声対話を通じて、実践的な営業スキルを身につけることができます。
      </div>
    </div>
  </div>
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
      <a href="solutions/roleplay/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/genai-design-studio/demo.gif" alt="GenAI Design Studio Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/genai-design-studio/">GenAI Design Studio</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-genai-design-studio" target="_blank">GenAI Design Studio</a> は、Amazon Nova Canvas を活用したバーチャル試着ソリューションです。アパレル業界やECサービスにおいて、服飾デザインから実際のモデル着用撮影まで、様々なプロセスの効率化を目指します。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-east-1">バージニア</option>
        <option value="eu-west-1">アイルランド</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenStudioDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenStudioDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/genai-design-studio/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="creative">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/comfyui/comfy.png" alt="ComfyUI Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/comfyui/">ComfyUI</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/comfyanonymous/ComfyUI" target="_blank">ComfyUI</a> は、ノードベースの生成AI画像生成ツールで、Stable Diffusion や様々なモデルを組み合わせて高品質な画像を生成できます。複雑なワークフローを視覚的に構築し、画像生成プロセスを細かく制御したい場合に最適です。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=ComfyUIDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/ComfyUIDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/comfyui/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/bedrock-engineer/agent-chat-diagram.png" alt="Bedrock Engineer Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/bedrock-engineer/">Bedrock Engineer</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/bedrock-engineer" target="_blank">Bedrock Engineer</a> は、Amazon Bedrock を活用した自律型ソフトウェア開発エージェントアプリケーションです。ファイル作成・編集、コマンド実行、Web 検索、ナレッジベース活用、マルチエージェント連携、画像生成など、様々な機能をカスタマイズして利用できます。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <a href="https://github.com/aws-samples/bedrock-engineer/releases/latest" class="download-button md-button" target="_blank">
        <i class="fa-solid fa-download"></i>　Download Latest Release
      </a>
      <a href="solutions/bedrock-engineer/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/remote-swe-agents/ss-chat.png" alt="Remote SWE Agents Demo" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/remote-swe-agents/">Remote SWE Agents</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/remote-swe-agents" target="_blank">Remote SWE Agents</a> は、AI による自律型のソフトウェア開発エージェントの実装例です。このエージェントはタスクごとに専用の開発環境内で動作し、ユーザーの PC に依存することなく開発作業を行います。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="us-west-2">オレゴン</option>
        <option value="us-east-1">バージニア</option>
      </select>
      <a href="https://us-west-2.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RemoteSweDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RemoteSweDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/remote-swe-agents/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

<div class="solution-card" data-category="development">
  <div class="solution-card__top">
    <div class="solution-card__image">
      <img src="./assets/images/solutions/aiagentdev/ai-agent-dev-code-server-top.png" alt="AI Agent Development Code Server" style="display: block;">
    </div>
    <div class="solution-card__content">
      <div class="solution-card__title"><a href="solutions/aiagentdev/">AI Agent Development Code Server</a></div>
      <div class="solution-card__description">
        <a href="https://github.com/aws-samples/sample-amazon-bedrock-agentcore-onboarding" target="_blank">AI Agent Development Code Server</a> は、Amazon Bedrock Agent Core を活用した AI エージェント開発のための専用開発環境です。ブラウザベースの VS Code (code-server) で、AWS 上で完全に動作する開発環境を提供します。
      </div>
    </div>
  </div>
  <div class="solution-card__actions">
    <div class="solution-card__deployment">
      <select class="region-selector">
        <option value="ap-northeast-1">東京</option>
        <option value="ap-northeast-3">大阪</option>
        <option value="us-east-1">バージニア</option>
        <option value="us-west-2">オレゴン</option>
      </select>
      <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=AIAgentDevDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/AIAgentDevelopmentCodeServerDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
        <i class="fa-solid fa-rocket"></i>　Deploy
      </a>
      <a href="solutions/aiagentdev/" class="detail-button">
        <i class="fa-solid fa-file-lines"></i>
        詳しく
      </a>
    </div>
  </div>
</div>

## 3. Start Journey

Generative AI Use Cases については、次のワークショップを進めることで使い方を学ぶことが出来ます。

* [生成 AI 体験ワークショップ](https://catalog.workshops.aws/generative-ai-use-cases-jp)
