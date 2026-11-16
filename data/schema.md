# 通用資料規格 v1.1.0

兩個JSON包皆含schemaVersion。前端僅顯示posts內status=published的內容。

## 文章
- id/title/summary：唯一字串ID、標題、摘要。
- category：news（實用資訊）、meme（校園梗）；event保留舊版相容，暫不新增。
- publishedAt/updatedAt：本站發布、更新日期，YYYY-MM-DD。
- campus：yanchao、heping、university-wide。
- body：純文字段落陣列；tags：標籤字串陣列。
- placeIds：地點ID陣列，可以空陣列表示沒有已確認地點。
- sources：來源陣列，每筆有title/url/publishedAt（可null）/accessedAt。
- contentKind：fact、opinion、fiction、community（社群來源紀錄）、source-index（維護者提供的連結索引）。
- verification：verified、opinion、fiction、source-confirmed（確認來源說法，非確認事件）、link-only（只有連結）；公開資料不得包含unverified。
- status：published；草稿應另放drafts目錄。
- rights：text（本站文案使用範圍）、sourceMedia（第三方素材限制）。
- 活動另有eventStart/eventEnd（含+08:00之ISO日期時間）、location、registrationDeadline、registrationUrl、registrationStatus。未知值null；報名狀態未知填unknown。

## 地點
id/name/campus/aliases/description/coordinates/sources/rights。coordinates未知為null；有查證才填latitude、longitude與來源，並升版說明。aliases不得猜測。未來遊戲座標另放對照檔，使用同一地點ID。

## 匯出與相容
網站直接提供原始JSON下載。模擬器依ID關聯文章與地點，並依contentKind判斷真實資訊及虛構創作。新增可選欄位升次版本；刪除或改義既有欄位升主版本。不得把HTML或遊戲引擎物件塞進body。

## v1.1.0：長期收藏擴充
- contentType：guide、archive、source-index。
- sourcePeriod：已確認的來源年份或null；不能以貼文ID或搜尋相對時間猜年份。
- evidenceNote：來源讀取範圍、缺漏、編輯判讀與查證限制。
- simulatorUse：可用範圍；link-only索引不得當成遊戲事件或地點。
- sources.access：full-text、indexed-comments、user-link-only；未填的v1.0資料沿用原文備註。
新增類型與前端須同步更新。v1.0消費端遇到未知contentKind或verification應跳過該筆，不默認為fact。既有ID保留不變。本次移除單日活動與兩篇泛用原創笑話，改收跨年份資料。
