# 燕巢日常

給高師大同學的非官方校園情報站：實用60%、幽默40%。採莫蘭迪色系，以校方公開資訊與Dcard歷年校園討論呈現校園日常。不限年份、不收單日活動。現有10個條目（6則實用資料、3則社群梗、1則奶蛙來源索引）、分類搜尋、共用文章頁、校區索引與JSON下載。內容查閱基準2026-11-16；非每日自動更新。

## 本機使用
無需安裝套件。於專案根目錄執行：

```sh
python3 -m http.server 8000 --directory dist
```

瀏覽 http://localhost:8000 。不要直接雙擊HTML，資料讀取需要HTTP。

```sh
python3 scripts/validate.py
```

## 以後直接複製給AI

- [完整專案規則](AGENTS.md)：可複製全文，交給新的AI讀取。
- [一段可重用的更新指令](AI-UPDATE-PROMPT.md)：貼上主題或來源，即可要求AI整理、檢查、上傳，並在有權限時更新公開網站。
- GitHub上傳與Sites發布是兩個不同步驟，指令已要求AI分別確認結果。

## 請AI繼續新增內容
先讓AI讀AGENTS.md與data/schema.md，再說：

> 跨年份搜尋與高師大燕巢學生相關的常青資訊與Dcard校園梗，依AGENTS.md整理3則待審草稿，附來源、原文日期、梗的脈絡、讀取範圍及相關地點；排除單日活動，不用AI編造笑話充數。不要直接發布，來源無法讀取時標記缺漏。

審核後再說：

> 我核准第1則草稿。依既有格式加入文章JSON，沿用現有地點ID，不新增HTML版型。執行資料驗證，檢查首頁、分類與文章頁，說明結果。

## GitHub Pages發布
1. 在你的GitHub帳號建立儲存庫，將本專案所有原始檔案上傳；不要上傳私人草稿或憑證。
2. 儲存庫 Settings → Pages → Source 選 GitHub Actions。
3. 本專案附.github/workflows/pages.yml，會把dist部署至Pages。
4. Actions成功後，從Pages設定取得公開網址，以無痕視窗確認。

本專案已上傳GitHub，並使用Sites提供公開網站。GitHub Pages是可選的另一種發布方式，需先依上述步驟啟用。若使用其他靜態主機，發布目錄同樣為dist。

## 模擬器準備
文章與地點各自儲存JSON，以穩定ID關聯；格式與權限見data/schema.md。尚未與任何遊戲引擎串接。未知座標為null。網站原創文案可用於本專案與模擬器；原始來源及第三方影像權利不隨JSON轉移。

## 來源及編輯
校方交通查詢、校方簡介、校園無線網路說明及Dcard公開討論；每篇附原始連結與查閱日期。動態時刻表不轉錄班次，不收錄單日活動。校園梗收錄鬼山別稱、反串文章與校名誤認的討論插曲；不宣稱全校流行或最早起源。奶蛙使用維護者提供的連結，目前原文無法讀取，只作待補索引，不描述事件或位置。初版內容供維護者檢閱，未進行獨立人工事實審核。

## 連結
GitHub：https://github.com/c3xv05/yanchao-daily
公開網站：https://yanchao-daily-notes.mellowgrape4.chatgpt.site
