# EDINET Taxonomy Repository

このリポジトリは、金融庁が公開する **EDINETタクソノミ（XBRL分類体系）** を、開発者・研究者・実務者がより使いやすく扱えるように整理・提供するものです。  
各年の公式ZIPファイルを収集・展開し、**統合された最新版の構造**も含めて提供しています。

---

## 📦 内容構成

- `versions/`  
  このディレクトリには、EDINETが公式に配布したタクソノミZIPファイルをそのまま格納しています。  
  ファイル名は配布日と版名を含み、構造的意味と歴史的文脈を明示しています。
  出典はすべて金融庁公式サイトに基づいています（下記参照）。

- `merged/`  
  複数年のタクソノミを統合し、**最新版として利用可能な構造**を提供しています。  
  利用者は `git clone` または `git pull` するだけで、展開済みのファイル群をすぐに利用できます。  

  EDINET公式のタクソノミURI（http://disclosure.edinet-fsa.go.jp/taxonomy/...）と、ローカル構造 `merged/taxonomy/` 以下のファイルパスとの対応関係を明示しています。  
  これにより、XBRL処理系や利用者がURIベースで参照する際の再現性と信頼性を担保します。


- `scripts/`  
  タクソノミのマージ処理を行うスクリプトです。構造変換の責任を明示し、再現性を確保します。  
  `unpack_and_merge.py` は、`versions/` に格納されたZIPファイルを**日付順に展開し、`merged/` に統合**する処理を行います。  
  ZIP内の最上位フォルダ（文字化けする可能性のある「タクソノミ」）は除外され、`samples/` および `taxonomy/` のみが対象となります。  
  同名ファイルが存在する場合は、**新しい定義で上書きされる**ため、`merged/` には最新版の構造が統合されます。

  実行例（Python 3.8+ 推奨）：

  ```bash
  python scripts/unpack_and_merge.py
  ```

---

## 🏛️ 出典一覧（金融庁公式）

以下は、EDINETタクソノミの公式公開ページへのリンクです。すべて金融庁のサイトより取得しています。

- [2025年版EDINETタクソノミ](https://www.fsa.go.jp/search/20241112.html)
- [2024年版EDINETタクソノミ](https://www.fsa.go.jp/search/20231211.html)
- [2023年版EDINETタクソノミ](https://www.fsa.go.jp/search/20221108.html)
- [2022年版EDINETタクソノミ](https://www.fsa.go.jp/search/20211109.html)
- [2021年版EDINETタクソノミ](https://www.fsa.go.jp/search/20201110.html)
- [2020年版EDINETタクソノミ](https://www.fsa.go.jp/search/20191101.html)
- [2019年版EDINETタクソノミ](https://www.fsa.go.jp/search/20190228.html)
- [EDINETタクソノミ（CG・IFRS詳細タグ付け対応版）](https://www.fsa.go.jp/search/20180316.html)
- [2018年版EDINETタクソノミ](https://www.fsa.go.jp/search/20180228.html)
- [2017年版EDINETタクソノミ](https://www.fsa.go.jp/search/20170228.html)
- [2016年版EDINETタクソノミ](https://www.fsa.go.jp/search/20160314.html)
- [2015年版EDINETタクソノミ（開示府令改正対応版）](https://www.fsa.go.jp/search/20150430.html)
- [2015年版EDINETタクソノミ](https://www.fsa.go.jp/search/20150310.html)
- [2014年版EDINETタクソノミ（投信法改正対応版）](https://www.fsa.go.jp/search/20140919.html)
- [2014年版EDINETタクソノミ（みなし有価証券届出書対応版）](https://www.fsa.go.jp/search/20140630.html)
- [2014年版EDINETタクソノミ](https://www.fsa.go.jp/search/20140310.html)
- [次世代EDINETタクソノミ](https://www.fsa.go.jp/search/20130821.html)

---

## 📖 利用方法（概要）

```bash
# リポジトリをクローン
git clone https://github.com/manpukupanda/edinet-taxonomy.git

# 最新版の統合タクソノミを参照
cd edinet-taxonomy/merged/
```

---

## 🛡️ ライセンス

このリポジトリに含まれるスクリプト・ドキュメント・構造整理物は MIT ライセンスのもとで提供されています。  
ただし、`versions/` および `merged/` に含まれる EDINET タクソノミ本体は、金融庁が公開する情報に基づいており、著作権は金融庁に帰属します。  
本リポジトリは非公式の整理・提供物であり、金融庁の公式見解や保証を含むものではありません。

---

## 🙌 貢献・フィードバック

構造改善・スクリプトの修正・READMEの補足など、Pull Request や Issue による貢献を歓迎します。  
公共資源の利活用を、より意味あるかたちで支えていきましょう。