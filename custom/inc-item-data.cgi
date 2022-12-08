# スタンダード版アイテムデータ 2005/01/06 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-06(SD)		#★商品データバージョン表記
					# 最後の「SD」はスタンダード版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	原料
	type2	本
	type3	藥
	type4	劍
	type5	鎧
	type6	盾
	type7	杖
	type8	飾品
	type9	地圖
	type10	道具
	
	job	drug		藥屋		#★職業コードは英小文字10文字以内
	job	tool		道具屋
	job	weapon		武器屋
	job	armor		防具屋
	job	material	山師
	job	book		書屋
	job	cow		酪農家
	job	peddle		行腳商人
	
	# 職業別時間短縮用変数設定
	set job_drug_time_rate		1.5	#★職業についていると1.5倍早くなる
	set job_tool_time_rate		1.5
	set job_weapon_time_rate	1.5
	set job_armor_time_rate		1.5
	set job_material_time_rate	1.5
	set job_book_time_rate		1.5
	set job_cow_time_rate		1.5
	set job_peddle_time_rate	1.5

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	100000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		12*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		展示架擴建拆卸工具:1:禮物卷:5	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★陳列棚操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/移動時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/移動時間(1個辺りの追加時間)
	TimeSendMoney		20m		#★資金移動時間(基本)
	TimeSendMoneyPlus	100000		#★ごみ処理時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★陳列棚1個時維持費
	CostShowcase2		2000	#陳列棚2個時維持費
	CostShowcase3		4000	#陳列棚3個時維持費
	CostShowcase4		8000	#陳列棚4個時維持費
	CostShowcase5		16000	#陳列棚5個時維持費
	CostShowcase6		32000	#陳列棚6個時維持費
	CostShowcase7		64000	#陳列棚7個時維持費
	CostShowcase8		128000	#陳列棚8個時維持費
	
	ItemUseTimeRate		0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------


@@ITEM					#★アイテムデータ定義宣言
	no		10		#★アイテム番号(重複しないように)
	type	道具			#★アイテム分類(@@DEFINEのtype?の定義を使用)
	code	book-make		#★コード(重複しないように)
	name	書本寫作工具			#★名称(重複しないように)
	info	寫書的基本工具包	#★説明
	price	5000				#★標準価格
	cost	100
	limit	20/10
	pop	20d			#★売れ行き率基準(20日に1個売れる確率)
	scale	組			#★数え単位
	plus	20m			#★市場入荷率(20分に1個入荷する確率)
	@@USE				#★アイテム使用データ定義宣言
		time	3h
		exp	2%
		exptime	1h
		job		書屋	times/job_book_time_rate
		scale	回
		action	寫作
		name	寫作『藥劑調和入門』
		info	研究藥劑調和技術，並寫成書
		okmsg	『藥劑調和入門』寫作完成了
		ngmsg	寫作失敗了…
			use		1	書本寫作工具
			use		30	藥草
			use		10	治療劑
			use		10	乙太
			get		5	藥劑調和入門	40%
	@@USE
		time	3h
		exp	2%
		exptime	1h
		name	寫作『皮革加工入門』
		info	研究皮革加工技術，並寫成書
		okmsg	『皮革加工入門』寫作完成了
		ngmsg	寫作失敗了…
			use		1	書本寫作工具
			use		50	野獸皮革
			get		5	皮革加工入門	40%
	@@USE
		time	3h
		exp	2%
		exptime	1h
		name	寫作『木工入門』
		info	研究木工加工技術，並寫成書
		okmsg	『木工入門』寫作完成了
		ngmsg	寫作失敗了…
			use		1	書本寫作工具
			use		50	樹枝
			use		10	木材
			get		5	木工加工入門	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	寫作『裝飾品加工入門』
		info	研究飾品加工技術，並寫成書
		okmsg	『裝飾品加工入門』寫作完成了
		ngmsg	寫作失敗了…
			use		1	書本寫作工具
			need		1	皮革加工入門
			need		1	木工加工入門
			use		20	鐵塊
			use		5	秘銀塊
			use		5	奧利哈鋼塊
			get		5	裝飾品加工入門	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	寫作『劍的鍛造方法』
		info	研究劍的鍛造方法，並寫成書
		okmsg	『劍的鍛造方法』寫作完成了
		ngmsg	寫作失敗了…
			needexp	20%
			need		1	鐵匠的技術
			use		1	書本寫作工具
			use		20	鐵塊
			use		1	木刀
			get		5	劍的鍛造方法	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	寫作『盾的製作方法』
		info	研究盾的構造，並寫成書
		okmsg	『盾的製作方法』寫作完成了
		ngmsg	寫作失敗了…
			needexp	20%
			use		1	書本寫作工具
			need		1	鐵匠的技術
			use		20	鐵塊
			use		1	皮盾
			get		5	盾的製作方法	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	寫作『鎧的製作方法』
		info	研究鎧的構造，並寫成書
		okmsg	『鎧的製作方法』寫作完成了
		ngmsg	寫作失敗了…
			needexp	20%
			need		1	鐵匠的技術
			use		1	書本寫作工具
			use		20	鐵塊
			use		1	皮胸甲
			get		5	鎧的製作方法	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	寫作『杖的製作方法』
		info	研究杖的構造，並寫成書
		okmsg	『杖的製作方法』寫作完成了
		ngmsg	寫作失敗了…
			needexp	20%
			need		1	魔法的知識
			use		1	書本寫作工具
			use		20	鐵塊
			use		1	木杖
			get		5	杖的製作方法	40%

@@ITEM
	no		37
	type	道具
	code	book-syugyou
	name	修行套組
	info	各種修行套件
	price	5000
	cost	500
	limit	1/1
	pop	0
	scale	組
	plus	1d
	flag	noshowcase|norequest
	@@USE
		time	12h
		exp		5%
		scale	修行
		action	修行
		name	成為鐵匠學徒
		info	學習和掌握技術鐵匠的技術
		okmsg	掌握了鐵匠的技術
			use		1	修行套組
			use		20	鐵塊
			use		5	秘銀塊
			use		3	奧利哈鋼塊
			get		1	鐵匠的技術
	@@USE
		time	12h
		exp		5%
		scale	勉強
		action	修行
		name	魔法的基礎講座
		info	學習和掌握魔術的基礎知識
		okmsg	掌握了魔法的基礎知識
			use		1	修行套組
			use		30	魔石
			get		1	魔法的知識
	@@USE
		time	12h
		exp		5%
		scale	開眼
		action	開眼
		name	成為知道差異的男人(女人)
		info	培養辨別產品之間差異的能力以及對事物的洞察力。
		okmsg	感覺已經成為一個知道差異的男人(女人)
			needexp	20%
			use		1	修行套組
			use		3	藥草
			use		3	野獸皮革
			use		3	樹枝
			use		3	木材
			use		3	鐵塊
			use		3	秘銀塊
			use		3	奧利哈鋼塊
			use		3	魔石
			get		1	行家的精隨
	@@USE
		time	12h
		exp		5%
		scale	修行
		action	修行
		name	學習解體的精髓
		info	為什麼不冒著生命危險去分解它呢？
		okmsg	覺得可以讓任何東西分崩離析
			use		1	修行套組
			use		20	皮胸甲
			use		20	皮盾
			use		20	木杖
			use		20	木刀
			get		1	解體屋之魂

@@ITEM
	no		39
	type	道具
	code	book-kaitai
	name	拆解/打包工具
	info	拆解和打包工作所需的套件
	price	500
	limit	10/3
	pop		2d
	scale	組
	plus	5h
	@@USE
		name	將木刀/木杖解體
		time	4h
		exptime	2h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	木刀
		use		10	木杖
		get		50	樹枝	80%
	@@USE
		name	將皮盾/胸甲解體
		time	4h
		exptime	2h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	皮盾
		use		10	皮胸甲
		get		50	野獸皮革	80%
	@@USE
		name	將木盾/胸甲解體
		time	4h
		exptime	2h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	木盾
		use		10	木胸甲
		get		50	樹枝	80%
	@@USE
		name	將鐵劍/杖解體
		time	4h
		exptime	3h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	鐵劍
		use		10	鐵杖
		get		50	鐵塊	80%
		get		10	魔石	50%
	@@USE
		name	將鐵盾/鎧解體
		time	4h
		exptime	3h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	鐵盾
		use		10	鐵鎧
		get		50	鐵塊	80%
	@@USE
		name	將鋼鐵劍/杖解體
		time	5h
		exptime	3.5h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	鋼鐵劍
		use		10	鋼鐵杖
		get		100	鐵塊	80%
		get		10	魔石	50%
	@@USE
		name	將鋼鐵盾/鎧解體
		time	5h
		exptime	3.5h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	鋼鐵盾
		use		10	鋼鐵鎧
		get		100	鐵塊	80%
	@@USE
		name	將秘銀劍/杖解體
		time	6h
		exptime	4h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	秘銀劍
		use		10	秘銀杖
		get		50	秘銀塊	70%
		get		20	魔石	50%
	@@USE
		name	將秘銀盾/鎧解體
		time	6h
		exptime	4h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	秘銀盾
		use		10	秘銀鎧
		get		50	秘銀塊	70%
	@@USE
		name	將奧利哈鋼劍/杖解體
		time	7h
		exptime	5h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	奧利哈鋼劍
		use		10	奧利哈鋼杖
		get		50	奧利哈鋼塊	60%
		get		30	魔石	50%
	@@USE
		name	將奧利哈鋼盾/鎧解體
		time	7h
		exptime	5h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		10	奧利哈鋼盾
		use		10	奧利哈鋼鎧
		get		50	奧利哈鋼塊	60%
	@@USE
		name	將機器人解體
		time	12h
		use		1	拆解/打包工具
		need	1	解體屋之魂
		use		1	看門機器人
		get		300	鐵塊
		get		50	秘銀塊
		get		10	奧利哈鋼塊
		get		30	魔石
		get		1	禁斷之書
		get		1	木材
	@@USE
		name	將一套皮製裝備打包
		time	4h
		exptime	2h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	皮盾
		use		10	皮胸甲
		get		10	皮製裝備一套
	@@USE
		name	將一套木製裝備打包
		time	5h
		exptime	3h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	木刀
		use		10	木盾
		use		10	木胸甲
		use		10	木杖
		get		10	木製裝備一套
	@@USE
		name	將一套鐵製裝備打包
		time	6h
		exptime	4h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	鐵劍
		use		10	鐵盾
		use		10	鐵鎧
		use		10	鐵杖
		get		10	鐵製裝備一套
	@@USE
		name	將一套鋼鐵製裝備打包
		time	7h
		exptime	4.5h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	鋼鐵劍
		use		10	鋼鐵盾
		use		10	鋼鐵鎧
		use		10	鋼鐵杖
		get		10	鋼鐵製裝備一套
	@@USE
		name	將一套秘銀製裝備打包
		time	8h
		exptime	5h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	秘銀劍
		use		10	秘銀盾
		use		10	秘銀鎧
		use		10	秘銀杖
		get		10	秘銀製裝備一套
	@@USE
		name	將一套奧利哈鋼製裝備打包
		time	9h
		exptime	6h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		10	奧利哈鋼劍
		use		10	奧利哈鋼盾
		use		10	奧利哈鋼鎧
		use		10	奧利哈鋼杖
		get		10	奧利哈鋼製裝備一套
	@@USE
		name	慶祝用品を梱包する
		time	8h
		job		道具屋	times/job_tool_time_rate
		use		1	拆解/打包工具
		use		1	整隻烤火雞
		use		1	挑剔的朗姆酒
		use		1	時髦的靴子
		get		1	慶祝用套組

@@ITEM
	no		15
	type	本
	code	book-tyougou
	name	藥劑調和入門
	info	合成藥物的技術書籍
	price	25000
	limit	40/1	#★所持最大数/市場入荷最大数(1店舗あたり)
			#  10店舗のゲームだと、この例では市場には最大10個入荷する。
			#  また、負数の場合は絶対数となる。(10/-2なら市場には最大2個)
			#  市場最大数を指定しない書式パターン1の場合は、所持最大数と同じ。
	pop	2d
	plus	20h
	scale	本
	cost	200
	@@use
		time	30m
		exp		2%
		exptime	10m
		job		藥屋	times/job_drug_time_rate
		scale	組
		action	製作
		name	製作治療劑
		info	製作治療劑
		okmsg	治療劑製作完成了
		ngmsg	製作失敗了…
			use		10	藥草
			get		20	治療劑	80%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	製作高級治療劑
		info	製作高級治療劑
		okmsg	高級治療劑製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	25
			needexp	20%
			use		10	治療劑
			get		20	高級治療劑	80%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	製作乙太
		info	製作乙太
		okmsg	乙太製作完成了
		ngmsg	製作失敗了…
			needexp	20%
			use		20	藥草
			get		20	乙太	64%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	製作高級乙太
		info	製作高級乙太
		okmsg	高級乙太製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	25
			needexp	40%
			use		10	乙太
			get		10	高級乙太	90%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	製作艾利草
		info	製作艾利草
		okmsg	艾利草製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	60%
			use		10	高級治療劑
			use		10	高級乙太
			get		5	艾利草
@@ITEM
	no		16
	type	本
	code	book-kawazaiku
	name	皮革加工入門
	info	對於那些想成為製皮匠的人
	price	25000
	limit	40/1
	pop	2d
	plus	20h
	scale	本
	cost	500
	@@use
		time	1h
		exp		2%
		exptime	20m
		job		防具屋	times/job_armor_time_rate
		scale	組
		action	製作
		name	製作皮盾
		info	製作皮盾
		okmsg	皮盾製作完成了
		ngmsg	製作失敗了…
			use		24	野獸皮革
			get		30	皮盾	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	組
		action	製作
		name	製作皮胸甲
		info	製作皮胸甲
		okmsg	皮胸甲製作完成了
		ngmsg	製作失敗了…
			use		24	野獸皮革
			get		32	皮胸甲	80%

@@ITEM
	no		17
	type	本
	code	book-mokkouzaiku
	name	木工加工入門
	info	對於那些立志成為木工的人
	price	25000
	limit	40/1
	pop	2d
	plus	20h
	scale	本
	cost	500
	@@use
		time	1h
		exp		2%
		exptime	20m
		job		武器屋	times/job_weapon_time_rate
		scale	組
		action	製作
		name	製作木刀
		info	製作木刀
		okmsg	木刀製作完成了
		ngmsg	製作失敗了…
			use		20	樹枝
			get		20	木刀	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		name	製作木杖
		info	製作木杖
		okmsg	木杖製作完成了
		ngmsg	製作失敗了…
			use		20	樹枝
			get		20	木杖	80%
	@@use
		time	2h
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		name	製作木盾
		info	製作木盾
		okmsg	木盾製作完成了
		ngmsg	製作失敗了…
			use		10	木材
			get		20	木盾	80%
	@@use
		time	2h
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		name	製作木胸甲
		info	製作木胸甲
		okmsg	木胸甲製作完成了
		ngmsg	製作失敗了…
			use		10	木材
			get		24	木胸甲	80%

@@ITEM
	no		66
	type	本
	code	book-sousyoku
	name	裝飾品加工入門
	info	對於立志成為飾品匠的人
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	本
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		道具屋	times/job_tool_time_rate
		scale	組
		action	製作
		name	製作鐵耳環
		info	製作鐵耳環
		okmsg	鐵耳環製作完成了
		ngmsg	製作失敗了…
			need	1	鐵匠的技術
			need	1	魔法的知識
			use		20	鐵塊
			get		20	鐵耳環	80%
	@@use
		time	3h
		exp		2%
		exptime	1h
		scale	組
		action	製作
		name	製作秘銀戒指
		info	製作秘銀戒指
		okmsg	秘銀戒指製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	25%
			need	1	鐵匠的技術
			need	1	魔法的知識
			use		20	秘銀塊
			use		2	魔石
			get		20	秘銀戒指	60%
	@@use
		time	4h
		exp		2%
		exptime	80m
		scale	組
		action	製作
		name	製作奧利哈鋼の腕輪
		info	製作奧利哈鋼の腕輪
		okmsg	奧利哈鋼の腕輪製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	50%
			need	1	鐵匠的技術
			need	1	魔法的知識
			use		20	奧利哈鋼塊
			use		2	魔石
			get		20	奧利哈鋼の腕輪	40%
	@@use
		time	6h
		exp	2%
		exptime	5h
		scale	組
		action	製作
		name	製作那由多的項鍊
		info	製作那由多的項鍊
		okmsg	傳奇就在你的面前！
		ngmsg	製作失敗了…
		func	lostbook
		param	200
			needexp	50%
			need	1	鐵匠的技術
			need	1	魔法的知識
			need	1	行家的精隨
			use		20	鐵塊
			use		20	秘銀塊
			use		20	奧利哈鋼塊
			use		6	魔石
			get		1	那由多的項鍊
	
@@ITEM
	no		20
	type	本
	code	book-ken
	name	劍的鍛造方法
	info	武器的代表「劍」的鍛造方法
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	本
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		武器屋	times/job_weapon_time_rate
		scale	組
		action	鍛造
		name	鍛造鐵劍
		info	讓我們來鍛造正統的鐵劍吧
		okmsg	鍛造鐵劍
		ngmsg	鍛造失敗了…
			need	1	鐵匠的技術
			use		20	鐵塊
			get		20	鐵劍	80%
	@@use
		time	3h
		exptime	1h
		name	鍛造鋼鐵劍
		info	讓我們來鍛造鋼鐵劍吧
		okmsg	鍛造鋼鐵劍
		ngmsg	鍛造失敗了…
			needexp	20%
			need	1	鐵匠的技術
			use		40	鐵塊
			get		20	鋼鐵劍	80%
	@@use
		time	3h
		exptime	1h
		name	鍛造秘銀劍
		info	讓我們來鍛造面向高級冒險者使用的秘銀劍吧
		okmsg	鍛造秘銀劍
		ngmsg	鍛造失敗了…
		func	lostbook
		param	50
			needexp	40%
			need	1	鐵匠的技術
			use		20	秘銀塊
			get		20	秘銀劍	60%
	@@use
		time	4h
		exptime	80m
		name	鍛造奧利哈鋼劍
		info	讓我們來鍛造很少見的奧利哈鋼劍吧
		okmsg	鍛造奧利哈鋼劍
		ngmsg	鍛造失敗了…
		func	lostbook
		param	50
			needexp	60%
			need	1	鐵匠的技術
			use		20	奧利哈鋼塊
			get		20	奧利哈鋼劍	40%
@@ITEM
	no		21
	type	本
	code	book-tate
	name	盾的製作方法
	info	迴避型防禦裝備「盾牌」的製作方法
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	本
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		防具屋	times/job_armor_time_rate
		scale	組
		action	製作
		name	製作鐵盾
		info	讓我們來鍛造正統的鐵盾吧
		okmsg	鐵盾製作完成了
		ngmsg	製作失敗了…
			need	1	鐵匠的技術
			use		20	鐵塊
			get		20	鐵盾	80%
	@@use
		time	3h
		exptime	1h
		name	製作鋼鐵盾
		info	讓我們來製作鋼鐵盾吧
		okmsg	鋼鐵盾製作完成了
		ngmsg	製作失敗了…
			needexp	20%
			need	1	鐵匠的技術
			use		40	鐵塊
			get		20	鋼鐵盾	80%
	@@use
		time	3h
		exptime	1h
		name	製作秘銀盾
		info	讓我們來製作面向高級冒險者使用的秘銀盾吧
		okmsg	秘銀盾製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	40%
			need	1	鐵匠的技術
			use		20	秘銀塊
			get		20	秘銀盾	60%
	@@use
		time	4h
		exptime	80m
		name	製作奧利哈鋼盾
		info	讓我們來製作很少見的奧利哈鋼盾吧
		okmsg	奧利哈鋼盾製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	60%
			need	1	鐵匠的技術
			use		20	奧利哈鋼塊
			get		20	奧利哈鋼盾	40%
@@ITEM
	no		22
	type	本
	code	book-yoroi
	name	鎧的製作方法
	info	抗打擊系防禦装備「鎧」的製作方法
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	本
	cost	1000
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		scale	組
		action	製作
		name	製作鐵鎧
		info	讓我們來鍛造正統的鐵鎧吧
		okmsg	鐵鎧製作完成了
		ngmsg	製作失敗了…
			need	1	鐵匠的技術
			use		20	鐵塊
			get		20	鐵鎧	80%
	@@use
		time	210m
		exptime	70m
		name	製作鋼鐵鎧
		info	讓我們來製作鋼鐵鎧吧
		okmsg	鋼鐵鎧製作完成了
		ngmsg	製作失敗了…
			needexp	20%
			need	1	鐵匠的技術
			use		40	鐵塊
			get		20	鋼鐵鎧	80%
	@@use
		time	210m
		exptime	70m
		name	製作秘銀鎧
		info	讓我們來製作面向高級冒險者使用的秘銀鎧吧
		okmsg	秘銀鎧製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	40%
			need	1	鐵匠的技術
			use		20	秘銀塊
			get		20	秘銀鎧	60%
	@@use
		time	270m
		exptime	90m
		name	製作奧利哈鋼鎧
		info	讓我們來製作很少見的奧利哈鋼鎧吧
		okmsg	奧利哈鋼鎧製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	60%
			need	1	鐵匠的技術
			use		20	奧利哈鋼塊
			get		20	奧利哈鋼鎧	40%

@@ITEM
	no		23
	type	本
	code	book-tue
	name	杖的製作方法
	info	魔法攻擊裝備「法杖」的製作方法
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	本
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		武器屋	times/job_weapon_time_rate
		scale	組
		action	製作
		name	製作鐵杖
		info	讓我們來鍛造正統的鐵杖吧
		okmsg	鐵杖製作完成了
		ngmsg	製作失敗了…
			need	1	魔法的知識
			use		20	鐵塊
			use		2	魔石
			get		20	鐵杖	80%
	@@use
		time	3h
		exptime	1h
		name	製作鋼鐵杖
		info	讓我們來製作鋼鐵杖吧
		okmsg	鋼鐵杖製作完成了
		ngmsg	製作失敗了…
			needexp	25%
			need	1	魔法的知識
			use		40	鐵塊
			use		4	魔石
			get		20	鋼鐵杖	80%
	@@use
		time	3h
		exptime	1h
		name	製作秘銀杖
		info	讓我們來製作面向高級冒險者使用的秘銀杖吧
		okmsg	秘銀杖製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	50%
			need	1	魔法的知識
			use		20	秘銀塊
			use		6	魔石
			get		20	秘銀杖	60%
	@@use
		time	4h
		exptime	80m
		name	製作奧利哈鋼杖
		info	讓我們來製作很少見的奧利哈鋼杖吧
		okmsg	奧利哈鋼杖製作完成了
		ngmsg	製作失敗了…
		func	lostbook
		param	50
			needexp	70%
			need	1	魔法的知識
			use		20	奧利哈鋼塊
			use		10	魔石
			get		20	奧利哈鋼杖	40%

@@ITEM
	no		12
	type	地圖
	code	book-mtsearch
	name	到附近山區的地圖
	info	收集材料完美之選的山區。
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	份
	cost	500
	flag	noshowcase
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		山師	times/job_material_time_rate
		scale	往復
		action	去探索
		name	探索山腳下
		info	可以收集各種材料
		func	lostbook
		param	10
		ngmsg	什麼都沒找到…
			get		80	藥草	90%	長了很多藥草
			get		2	野獸皮革	90%
			get		2	樹枝	90%
			get		2	木材	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	去探索
		name	探索森林
		info	可以收集各種材料
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		4	藥草	90%
			get		2	野獸皮革	90%
			get		40	樹枝	90%	收集到許多掉落的樹枝
			get		2	木材	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	去探索
		name	探索動物踪跡
		info	可以收集材料
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		4	藥草	90%
			get		40	野獸皮革	90%	獵殺了很多動物
			get		2	樹枝	90%
			get		2	木材	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	去探索
		name	探索叢林深處
		info	可以收集材料
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		4	藥草	90%
			get		2	野獸皮革	90%
			get		2	樹枝	90%
			get		40	木材	45%		發現了很多木材
	
@@ITEM
	no		9
	type	地圖
	code	book-metalsearch
	name	到附近礦山的地圖
	info	可以採集各種礦物
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	份
	cost	500
	flag	noshowcase
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		山師	times/job_material_time_rate
		scale	往復
		action	收集
		name	去鐵礦山
		info	可以收集各種礦物
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		30	鐵塊			80%
			get		2	秘銀塊		60%
			get		1	奧利哈鋼塊	80%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	收集
		name	去秘銀礦山
		info	可以收集各種礦物
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		3	鐵塊			80%
			get		20	秘銀塊		60%
			get		1	奧利哈鋼塊	80%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	收集
		name	去奧利哈鋼礦山
		info	可以收集各種礦物
		ngmsg	什麼都沒找到…
		func	lostbook
		param	10
			get		3	鐵塊			80%
			get		2	秘銀塊		60%
			get		10	奧利哈鋼塊	80%

@@ITEM
	no		14
	type	地圖
	code	shiire-ken
	name	到劍市的地圖
	info	到劍市的地圖
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	份
	cost	500
	flag	noshowcase
	@@use
		time	4h
		exp	2%
		exptime	2h
		job		行腳商人	times/job_peddle_time_rate
		scale	往復
		action	購買
		price	12000					#★使用時費用額
		name	去劍的市場收購
		info	去劍的市場收購
		func	lostbook
		param	100
		ngmsg	甚麼都沒有得到…
			get		10	木刀			40%
			get		10	鐵劍			35%
			get		10	鋼鐵劍		15%
			get		10	秘銀劍		6%	秘銀劍很便宜
			get		10	奧利哈鋼劍	3%	發現便宜的奧利哈鋼劍了!
		funcb	_local_
			# 1/10の確率で収穫量が2倍になる
			return 0 if rand(1000)>100;
			
			my $USE=$_[0];
			
			# $USE->{result}->{create}->[0..?]->{count} を2倍にする
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			# okmsg を設定する
			$USE->{result}->{message}->{resultok}='這次我們收穫的比平時多。';
			return 0;
		_local_
	

@@ITEM
	no		30
	type	藥
	code	posyon
	name	治療劑
	info	恢復體力的藥
	price	100
	limit	5000/500
	pop	20m
	plus	2h
	base	10/1000
	scale	個
	cost	5
	point	10%
@@ITEM
	no		31
	type	藥
	code	posyon-hi
	name	高級治療劑
	info	一種藥
	price	200
	limit	2500/250
	base	400/1000
	plus	-1h
	pop	30m
	scale	個
	point	10%
@@ITEM
	no		32
	type	藥
	code	eteru
	name	乙太
	info	恢復魔力的藥
	price	250
	limit	2000/200
	pop	50m
	plus	5h
	base	10/500
	scale	個
	cost	10
	point	20%
@@ITEM
	no		33
	type	藥
	code	eteru-hi
	name	高級乙太
	info	一種藥
	price	500
	limit	1000/100
	base	200/500
	plus	-1h
	pop	60m
	scale	個
	cost	50
	point	20%
@@ITEM
	no		34
	type	藥
	code	erikusa
	name	艾利草
	info	一種藥
	price	2500
	plus	-1h
	limit	400/40
	base	40/100
	pop	4h
	scale	個
	cost	100
	point	40%
@@ITEM
	no		40
	type	劍
	code	ken-ki
	name	木刀
	info	拿來當土產最好了
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	把
@@ITEM
	no		41
	type	劍
	code	ken-tetu
	name	鐵劍
	info	鐵劍
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	3h
	scale	把
@@ITEM
	no		42
	type	劍
	code	ken-hagane
	name	鋼鐵劍
	info	鋼鐵劍
	price	3200
	limit	300
	base	30/60
	plus	-1h
	pop	5h
	scale	把
	point	80%
@@ITEM
	no		43
	type	劍
	code	ken-misuriru
	name	秘銀劍
	info	秘銀劍
	price	8000
	limit	100
	base	20/40
	plus	-1h
	pop	10h
	scale	把
	point	70%
@@ITEM
	no		44
	type	劍
	code	ken-oriharukon
	name	奧利哈鋼劍
	info	奧利哈鋼劍
	price	12000
	limit	75
	base	12/24
	plus	-1h
	pop	16h
	scale	把
	point	60%

@@ITEM
	no		51
	type	鎧
	code	yoroi-kawa
	name	皮胸甲
	info	沒有防寒效果
	price	750
	limit	1000
	base	150/300
	plus	-1h
	pop	110m
	scale	個
	point	40%
@@ITEM
	no		52
	type	鎧
	code	yoroi-ki
	name	木胸甲
	info	幾乎沒什麼用的胸甲
	price	1000
	limit	750
	base	100/200
	plus	-1h
	pop	150m
	scale	個
	point	50%
@@ITEM
	no		53
	type	鎧
	code	yoroi-tetu
	name	鐵鎧
	info	鐵鎧
	price	1600
	limit	500
	base	50/100
	plus	-1h
	pop	190m
	scale	個
	point	80%
@@ITEM
	no		54
	type	鎧
	code	yoroi-hagane
	name	鋼鐵鎧
	info	鋼鐵鎧
	price	3400
	limit	300
	base	30/60
	plus	-1h
	pop	320m
	scale	個
	point	80%
@@ITEM
	no		55
	type	鎧
	code	yoroi-misuriru
	name	秘銀鎧
	info	秘銀鎧
	price	9000
	limit	100
	base	20/40
	plus	-1h
	pop	680m
	scale	個
	point	75%
@@ITEM
	no		56
	type	鎧
	code	yoroi-oriharukon
	name	奧利哈鋼鎧
	info	奧利哈鋼鎧
	price	12500
	limit	75
	base	12/24
	plus	-1h
	pop	17h
	scale	個
	point	60%

@@ITEM
	no		45
	type	盾
	code	tate-kawa
	name	皮盾
	info	有總比沒有好
	price	800
	limit	1000
	base	100/200
	plus	-1h
	pop	120m
	scale	個
	point	75%
@@ITEM
	no		46
	type	盾
	code	tate-ki
	name	木盾
	info	給小孩子練習用的
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	個
@@ITEM
	no		47
	type	盾
	code	tate-tetu
	name	鐵盾
	info	鐵盾
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	3h
	scale	個
@@ITEM
	no		48
	type	盾
	code	tate-hagane
	name	鋼鐵盾
	info	鋼鐵盾
	price	3200
	limit	300
	base	30/60
	plus	-1h
	pop	5h
	scale	個
	point	80%
@@ITEM
	no		49
	type	盾
	code	tate-misuriru
	name	秘銀盾
	info	秘銀盾
	price	7500
	limit	100
	base	20/40
	plus	-1h
	pop	10h
	scale	個
	point	70%
@@ITEM
	no		50
	type	盾
	code	tate-oriharukon
	name	奧利哈鋼盾
	info	奧利哈鋼盾
	price	11000
	limit	75
	base	12/24
	plus	-1h
	pop	15h
	scale	個
	point	60%

@@ITEM
	no		57
	type	杖
	code	tue-ki
	name	木杖
	info	玩具杖
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	把
@@ITEM
	no		58
	type	杖
	code	tue-tetu
	name	鐵杖
	info	鐵杖
	price	2000
	limit	500
	base	50/100
	plus	-1h
	pop	5h
	scale	把
@@ITEM
	no		59
	type	杖
	code	tue-hagane
	name	鋼鐵杖
	info	鋼鐵杖
	price	4000
	limit	300
	base	30/60
	plus	-1h
	pop	8h
	scale	把
	point	80%
@@ITEM
	no		60
	type	杖
	code	tue-misuriru
	name	秘銀杖
	info	秘銀杖
	price	10000
	limit	100
	base	20/40
	plus	-1h
	pop	15h
	scale	把
	point	70%
@@ITEM
	no		61
	type	杖
	code	tue-oriharukon
	name	奧利哈鋼杖
	info	奧利哈鋼杖
	price	16000
	limit	75
	base	12/24
	plus	-1h
	pop	24h
	scale	把
	point	60%

@@ITEM
	no		67
	type	飾品
	code	sousyoku-tetu
	name	鐵耳環
	info	非常有手工製作感的耳環
	price	1500
	limit	500/0
	pop	4h
	base	20/30
	scale	個
@@ITEM
	no		68
	type	飾品
	code	sousyoku-misuriru
	name	秘銀戒指
	info	秘銀戒指
	price	8000
	limit	100/0
	pop	14h
	base	20/40
	plus	-1h
	scale	個
@@ITEM
	no		69
	type	飾品
	code	sousyoku-oriharukon
	name	奧利哈鋼手鐲
	info	奧利哈鋼手鐲
	price	12000
	limit	75/0
	pop	20h
	base	12/24
	plus	-1h
	scale	個
@@ITEM
	no		70
	type	飾品
	code	sousyoku-nayuta
	name	那由多的項鍊
	info	紀念傳奇英雄的項鍊
	price	50000
	limit	1/0
	pop		2d
	scale	個
	cost	200
	funct	_local_
		#標準価格未満で陳列中の場合1日10%の無条件人気アップ
		my($ITEM,@DT)=@_;
		my $rankup=$TIMESPAN/86.4;
		$rankup=$rankup<1 && rand(1)<$rankup ? 1 : int($rankup);
		return if !$rankup;
		foreach my $DT (@DT)
		{
			next if $DT->{showcase}[0]!=$ITEM->{no} || $DT->{price}[0]>$ITEM->{price};
			
			$DT->{rank}+=$rankup;
			$DT->{rank}=10000 if $DT->{rank}>10000;
			DebugLog("item $ITEM->{name} $DT->{shopname} 人気 +".($rankup/100)."\%");
		}
	_local_

@@ITEM
	no		71
	type	道具
	code	soubiset-kawa
	name	皮製裝備一套
	info	皮製装備組合商品
	price	3000
	limit	300/0
	pop	6h
	scale	組
@@ITEM
	no		72
	type	道具
	code	soubiset-ki
	name	木製裝備一套
	info	木製装備組合商品
	price	9000
	limit	100/0
	pop	18h
	scale	組
@@ITEM
	no		73
	type	道具
	code	soubiset-tetu
	name	鐵製裝備一套
	info	鐵製装備組合商品
	price	12000
	limit	80/0
	pop	24h
	scale	組
@@ITEM
	no		74
	type	道具
	code	soubiset-hagane
	name	鋼鐵製裝備一套
	info	鋼鐵製装備組合商品
	price	27000
	limit	40/0
	pop	54h
	scale	組
@@ITEM
	no		75
	type	道具
	code	soubiset-misuriru
	name	秘銀製裝備一套
	info	秘銀製装備組合商品
	price	60000
	limit	20/0
	pop	108h
	scale	組
@@ITEM
	no		76
	type	道具
	code	soubiset-oriharukon
	name	奧利哈鋼製裝備一套
	info	奧利哈鋼製装備組合商品
	price	81000
	limit	10/0
	pop	148h
	scale	組

@@ITEM
	no		1
	type	原料
	code	yakusou
	name	藥草
	info	可以做藥的草
	price	50
	limit	4000/1000
	pop	10d
	plus	-20m
	base	200/1400
	scale	份
	cost	10
	point	25%
@@ITEM
	no		2
	type	原料
	code	kemononokawa
	name	野獸皮革
	info	鞣製野獸皮革
	price	100
	limit	2000/500
	pop	10d
	plus	-20m
	base	100/700
	scale	枚
	cost	30
	point	50%
@@ITEM
	no		3
	type	原料
	code	kinoeda
	name	樹枝
	info	跟手臂一樣粗的樹枝
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	根
	cost	40
	point	50%
@@ITEM
	no		4
	type	原料
	code	maruta
	name	木材
	info	木材
	price	240
	limit	500/100
	pop	10d
	plus	-20m
	base	100/500
	scale	捆
	cost	100
@@ITEM
	no		8
	type	原料
	code	magicstone
	name	魔石
	info	蘊含魔力的礦石
	price	250
	limit	200/50
	pop	10d
	plus	6h
	base	500/2500
	scale	個
	cost	100
@@ITEM
	no		5
	type	原料
	code	tetu
	name	鐵塊
	info	一整塊鐵
	price	200
	limit	1000/250
	pop	10d
	plus	-20m
	base	300/800
	scale	kg
	cost	60
@@ITEM
	no		6
	type	原料
	code	misuriru
	name	秘銀塊
	info	一整塊秘銀
	price	400
	limit	800/200
	pop	10d
	plus	-20m
	base	300/600
	scale	kg
	cost	80
@@ITEM
	no		7
	type	原料
	code	oriharukon
	name	奧利哈鋼塊
	info	一整塊奧利哈鋼
	price	600
	limit	600/150
	pop	10d
	plus	-20m
	base	300/600
	scale	kg
	cost	90

@@ITEM
	no		62
	type	道具
	code	cm
	name	廣告包
	info	可以變得受歡迎，但也會失敗…
	price	100000
	limit	1/1
	pop	10d
	plus	5d
	base	10/50
	scale	包
	cost	10000
	@@use
		time	10h
		exp	10%
		job		行腳商人	times/job_peddle_time_rate
		scale	回
		action	進行廣告
		name	推出自己商店的廣告
		info	提高自己商店的人氣
		arg		nocount
			use		1	廣告包
		func	_local_
				my $up=int(500*(2-$DT->{rank}/5000));
				if ( rand(1000)<250 ) {
					$DT->{rank}-=$up;
					$DT->{rank}=1000 if $DT->{rank}<1000;
					my $ret="廣告適得其反：人氣降低了".int($up/100);
					WriteLog(0,$DT->{id},$ret);
					WriteLog(3,0,$DT->{shopname}."把廣告貼出來後得到了反效果");
					return $ret;
				}
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				my $ret="進行廣告宣傳後：人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."進行了廣告宣傳");
				return $ret;
			_local_
	@@use
		time	10h
		exp	0%
		name	推出他人商店的廣告
		info	提高他人商店的人氣
		arg		target|nocount
			use		1	廣告包
		func	_local_
				return '沒辦法指定自己的商店' if ($DT==$DTS);
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="進行廣告宣傳後，".$DTS->{shopname}."的人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."對".$DTS->{shopname}."進行了廣告宣傳。");
				return $ret;
			_local_
	@@use
		time	16h
		exp	0%
		name	進行商會的廣告
		info	可以提升同商會所屬店鋪的人氣
		arg		nocount
			use		1	廣告包
		func	_local_
				return '沒有加入商會無法進行商會廣告' if !$DT->{guild};

				WriteLog(3,0,$DT->{shopname}."的商會「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」進行了廣告宣傳");
				foreach my $DTS (@DT)
				{
				next if ($DTS->{guild} ne $DT->{guild});
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="進行商會廣告後，".$DTS->{shopname}."的人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				}
				return '進行商會廣告';
			_local_

@@ITEM
	no		13
	type	本
	code	book-work
	name	資金賺取方法
	info	當需要錢的時候
	price	0
	limit	1/1
	pop	0
	plus	10h
	scale	本
	flag	noshowcase
	@@use
		time	4h
		job		行腳商人	times/job_peddle_time_rate
		scale	回
		action	工作
		name	發面紙賺錢
		info	簡單的賺錢法
		param	3000
		func	_local_
			# ★バイト
			#   param1 取得額
			$DT->{money}+=$USE->{param1}*$count;
			
			my $ret=GetMoneyString($USE->{param1}*$count).'稼ぎました';
			
			WriteLog(0,$DT->{id},"バイトし、$ret");
			WriteLog(3,0,$DT->{shopname}."がバイトしたようです");
			
			return $ret;
		_local_
	@@use
		time	8h
		job		行腳商人	times/job_peddle_time_rate
		scale	回
		action	工作
		name	去當日薪木工賺錢
		info	有點難但是賺錢可觀
		param	10000
		func	_local_1

@@ITEM
	no		63
	type	道具
	code	edit-showcase
	name	展示架擴建拆卸工具
	info	展架擴建或拆除所需的一套工具。
	price	0
	limit	1/1
	pop	0
	plus	1d
	scale	組
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	施工
		price	10000
		name	將展示架改為1個
		info	將展示架改為1個
		arg		nocount		#★使用時の選択肢指定。
							#  nocount -> 使用回数選択なし
		param	1			#★独自関数用パラメータ
			use	1	展示架擴建拆卸工具
		func	_local_
			# ★展示架数変更
			#   param1 変更後の棚数
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="展示架已經改成$DT->{showcasecount}個了";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."的展示架已經變成$DT->{showcasecount}個了");
			
			return $ret;
		_local_
	@@use
		time	2h
		price	20000
		name	將展示架改為2個
		info	將展示架改為2個
		func	_local_1
		arg		nocount
		param	2
			use	1	展示架擴建拆卸工具
	@@use
		time	3h
		price	30000
		name	將展示架改為3個
		info	將展示架改為3個
		func	_local_1
		arg		nocount
		param	3
			use	1	展示架擴建拆卸工具
	@@use
		time	4h
		price	40000
		name	將展示架改為4個
		info	將展示架改為4個
		func	_local_1
		arg		nocount
		param	4
			use	1	展示架擴建拆卸工具
	@@use
		time	5h
		price	50000
		name	將展示架改為5個
		info	將展示架改為5個
		func	_local_1
		arg		nocount
		param	5
			use	1	展示架擴建拆卸工具
	@@use
		time	6h
		price	60000
		name	將展示架改為6個
		info	將展示架改為6個
		func	_local_1
		arg		nocount
		param	6
			use	1	展示架擴建拆卸工具
	@@use
		time	7h
		price	70000
		name	將展示架改為7個
		info	將展示架改為7個
		func	_local_1
		arg		nocount
		param	7
			use	1	展示架擴建拆卸工具
	@@use
		time	8h
		price	80000
		name	將展示架改為8個
		info	將展示架改為8個
		func	_local_1
		arg		nocount
		param	8
			use	1	展示架擴建拆卸工具
		
@@ITEM
	no		65
	type	本
	code	badgossip
	name	禁斷之書
	info	當不該做卻不得不做的時候…
	price	50000
	cost	5000
	limit	1/1
	pop		0
	plus	1d
	scale	本
	@@use
		time	10h
		exp	20%
		exptime	8h
		scale	回
		price	50000
		scale	回
		action	散播謠言
		price	0
		name	散播謠言
		info	如果成功可以降低對方店舖的人氣，但也有可能會失敗…
		arg	target|nocount
			needpoint	20000
			use		1	禁斷之書
		func	_local_
			my $ret;
			if(rand(1000)<800 && !$DTS->{exp}{@@ITEMNO"廣告包"})
			{
				$DTS->{rank}-=int($DTS->{rank}/3);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰成功了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(2,0,$DTS->{shopname}.'因為謠言的關係人氣下降了。');
			}
			else
			{
				$DTS->{exp}{@@ITEMNO"廣告包"}-=100;
				$DTS->{exp}{@@ITEMNO"廣告包"}=0 if ($DTS->{exp}{@@ITEMNO"廣告包"} < 0);
				$DT->{rank}-=int($DT->{rank}/4);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰失敗了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."的策畫散佈".$DTS->{shopname}.'的謠言。');
			}
			return $ret;
			_local_
	@@use
		time	10h
		exp	25%
		exptime	8h
		scale	回
		action	偷竊
		price	50000
		name	偷竊
		info	就算追了那麼遠，也無濟於事…
		arg	target|nocount
			needpoint	20000
			use		1	禁斷之書
		func	_local_
			return '無法從自己店裡偷東西。偷竊失敗了。' if  ($DT->{id} eq $DTS->{id});
			my $ret="偷竊失敗了。賠償金".GetMoneyString(500000)."已經被扣留。";
			if($DTS->{item}[@@ITEMNO"看門機器人"-1])
			{
			$DTS->{item}[@@ITEMNO"看門機器人"-1]--;
			$DT->{rank}-=int($DT->{rank}/4);
			$DTS->{money}+=500000;
			$DTS->{saletoday}+=500000;
			$DT->{money}-=500000;
			$DT->{paytoday}+=500000;
			WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊，但破壞了看門機器人時被捉到了。");
			WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."支付了賠償金".GetMoneyString(500000)."。");
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			}
			if(rand(1000)>900)
			{
			$DTS->{money}+=500000;
			$DTS->{saletoday}+=500000;
			$DT->{money}-=500000;
			$DT->{paytoday}+=500000;
			$DT->{rank}-=int($DT->{rank}/4);
			WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊但失敗了。");
			WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."支付了賠償金".GetMoneyString(500000)."。");
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			}
			$ret="偷竊成功了";
			my $manbiki_count=0;
			foreach my $idx (0..$DTS->{showcasecount}-1)
			{
				my $itemno=$DTS->{showcase}[$idx];
				if($itemno)
				{
					my $cnt=int($DTS->{item}[$itemno-1]*3/4);
					$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
					$DTS->{item}[$itemno-1]-=$cnt;
					$DT->{item}[$itemno-1]+=$cnt;
					$manbiki_count+=$cnt*$DTS->{price}[$idx];
				}
			}
		$main::STATE->{safety}=int($main::STATE->{safety} * 18 / 19);
		WriteLog(2,0,$DTS->{shopname}."被偷了總價大概".GetMoneyString($manbiki_count)."的損失") if $manbiki_count;
		WriteLog(2,0,'闖進'.$DTS->{shopname}."的小偷什麼都沒拿就逃走了。") if !$manbiki_count;
		WriteLog(0,$DT->{id},$ret);
		return $ret;
		_local_
	@@use
		time	16h
		exp	5%
		exptime	14h
		scale	回
		action	散佈關於商品的謠言
		price	50000
		name	散佈關於某行業的不良謠言
		info	專賣店殺手
		arg		target|nocount
			needpoint	20000
			use		1	禁斷之書
		func	_local_
			my %category=qw(4 ken 5 yoroi 6 tate 7 tue); #分類番号とイベントコードの対応
			my $ret;
			my $itemno=$DTS->{showcase}->[int rand($DTS->{showcasecount})];
			my $itemtype=$ITEM[$itemno]->{type};
			my $category=$category{$itemtype};
			my $eventkey="kill-$category";
			
			#陳列棚の商品が%category外だったり，既に発動中なら失敗。
			return '造謠失敗了' if !$category || grep($_ eq $eventkey,keys(%main::DTevent));
			
			#8時間持続でイベント発動
			$main::DTevent{$eventkey}=$main::NOW_TIME+8*60*60;
			$ret='散佈有關'.$main::ITEMTYPE[$itemtype].'市場的謠言';
			WriteLog(0,$DT->{id},$ret);
			WriteLog(2,0,'有關'.$main::ITEMTYPE[$itemtype].'市場的謠言似乎正在流傳。');
			return $ret;
		_local_
@@event
	start		-1 #イベント自然発動無し
	code		kill-ken
	endmsg		反劍運動已經平息了
	info		反劍運動開始了
		param	木刀				point=0    #+-0%
		param	鐵劍				point=-100 #-10%
		param	鋼鐵劍			point=-200 #-20%
		param	秘銀劍		point=-300 #-30%
		param	奧利哈鋼劍	point=-400 #-40%
@@event
	start		-1
	code		kill-yoroi
	endmsg		反鎧運動已經平息了
	info		反鎧運動開始了
		param	皮胸甲			point=0
		param	木胸甲			point=0
		param	鐵鎧				point=-100
		param	鋼鐵鎧			point=-200
		param	秘銀鎧		point=-300
		param	奧利哈鋼鎧	point=-400
@@event
	start		-1
	code		kill-tate
	endmsg		反盾運動已經平息了
	info		反盾運動開始了
		param	皮盾				point=0
		param	木盾				point=0
		param	鐵盾				point=-100
		param	鋼鐵盾			point=-200
		param	秘銀盾		point=-300
		param	奧利哈鋼盾	point=-400
@@event
	start		-1
	code		kill-tue
	endmsg		反杖運動已經平息了
	info		反杖運動開始了
		param	木杖				point=0
		param	鐵杖				point=-100
		param	鋼鐵杖			point=-200
		param	秘銀杖		point=-300
		param	奧利哈鋼杖	point=-400

@@ITEM
	no		18
	type	飾品
	code	skill-kajiya
	name	鐵匠的技術
	info	鐵匠老爹直傳
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	技
	flag	noshowcase|norequest
@@ITEM
	no		19
	type	飾品
	code	skill-magic
	name	魔法的知識
	info	魔法的基礎知識
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	知識
	flag	noshowcase|norequest
@@ITEM
	no		24
	type	飾品
	code	skill-mekiki
	name	行家的精隨
	info	早點發現差異
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	精隨
	flag	noshowcase|norequest
@@ITEM
	no		38
	type	飾品
	code	skill-kaitai
	name	解體屋之魂
	info	拼命分解
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	魂
	flag	noshowcase|norequest

@@ITEM
	no		64
	type	飾品
	code	defence-manbiki
	name	看門機器人
	info	他們會監視商店
	price	500000
	cost	5000
	limit	1/0.5
	pop	1d
	plus	30m
	scale	架
	flag	noshowcase|onlysend

@@ITEM
	no		11
	type	飾品
	code	loto
	name	抽獎卷
	info	夢想快速致富（抽獎日<B>機率</B>大概是2天抽1次）
	price	2000
	cost	10
	limit	50/20
	plus	10m
	scale	枚
	pop	0
	flag	noshowcase|norequest

@@ITEM
	no		25
	type	道具
	code	mino
	name	米諾陶洛斯♀
	info	有點可怕的家畜
	price	10000
	cost	1000
	limit	20/1.5
	plus	1d
	scale	頭
	pop		1d
	@@use
		time	2h
		exp		1%
		job		酪農家	times/job_cow_time_rate
		scale	次
		action	擠奶
		price	0
		name	擠奶
		info	從米諾上擠奶
		param	1
			need		1	米諾陶洛斯♀
		func	_local_
			# ★米諾陶洛斯搾乳
			#   param1 搾乳レベル（１〜）
			my $val=$USE->{param1}*$count;
			
			$val*=$DT->{item}[25-1];
			$val=int(rand($val))+1;
			AddItem(26,$val,'精製了米諾牛奶');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(25,$usecount,$ITEM[25]->{name}.'因為'.($USE->{param1}==1?'壽命':'過勞').'的關係升天了') if $usecount;
			
			my $ret='精製了'.$val.'瓶米諾牛乳';
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
		
	@@use
		time	2h
		exp		1%
		job		酪農家	times/job_cow_time_rate
		scale	次
		action	榨取乳汁
		price	0
		name	用力榨取乳汁
		info	用力榨取米諾的乳汁
		param	2
		func	_local_1
			need		1	米諾陶洛斯♀

@@ITEM
	no		26
	type	藥
	code	mino_milk
	name	米諾牛乳
	info	飲用對健康管理很有幫助
	price	200
	cost	50
	pop		30m
	limit	2500/0
	scale	瓶
	point	15%
	@@use
		time	3m
		job		酪農家	times/job_cow_time_rate
		scale	瓶
		action	飲用
		price	0
		name	飲用
		info	飲用米諾牛乳
			use		1	米諾牛乳
		func	_local_
			# ★米諾牛乳を飲む
			my $val=$count;
			my $ret="";
			
			if($count>=30)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'的店長被救護車運走了');
				WriteLog(2,0,'一下子喝完'.$count.'瓶米諾牛乳簡直是瘋了');
				$ret="…醒來時已經在病床上了";
			}
			elsif($count>=10)
			{
				$ret='一下子喝完了'.$count.'瓶米諾牛乳　肚子要壞掉了';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='喝了米諾牛乳感覺更健康了';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@use
		time	72m
		job		酪農家	times/job_cow_time_rate
		scale	組
		action	輕微發酵
		price	0
		name	輕微發酵
		info	將米諾牛乳輕微發酵所製成
			need	5	米諾陶洛斯♀
			use		15	米諾牛乳
			get		2	米諾優格
	@@use
		time	144m
		job		酪農家	times/job_cow_time_rate
		scale	組
		action	大量發酵
		price	0
		name	大量發酵
		info	將米諾牛乳大量發酵所製成
			need	10	米諾陶洛斯♀
			use		15	米諾牛乳
			get		1	米諾起司

@@ITEM
	no		35
	type	藥
	code	mino_yogurt
	name	米諾優格
	info	用米諾牛乳做的高檔優格，有點米諾味
	price	3000
	cost	100
	pop	6h
	limit	300/0
	scale	個
	@@use
		time	10m
		job		酪農家	times/job_cow_time_rate
		scale	個
		action	食用
		price	0
		name	食用
		info	我要吃米諾優格
		ngmsg	似乎與庶民的口味不太合…
			use		1	米諾優格

@@ITEM
	no		36
	type	藥
	code	mino_cheese
	name	米諾起司
	info	由米諾牛乳製成的高級起司，實在太米諾了
	price	6000
	cost	200
	pop	10h
	limit	150/0
	scale	個
	@@use
		time	20m
		job		酪農家	times/job_cow_time_rate
		scale	個
		action	食用
		price	0
		name	食用
		info	食用米諾起司
		ngmsg	實在太臭所以吐出來了…
			use		1	米諾起司


@@ITEM
	no		27
	type	藥
	code	seven_face
	name	整隻烤火雞
	info	每次慶祝都不要錯過
	price	10000
	cost	0
	limit	1/0
	scale	隻
	pop		1d
	@@use
		time	1h
		scale	隻
		action	食用
		price	0
		name	食用
		info	讓我們慶祝吧
		arg		nocount
			use		1	整隻烤火雞	100%	肚子真飽

@@ITEM
	no		28
	type	藥
	code	ramusyu
	name	挑剔的朗姆酒
	info	是傳說中的英雄喜歡的朗姆酒
	price	20000
	cost	0
	limit	1/0
	scale	瓶
	pop		1d
	@@use
		time	1h
		scale	瓶
		action	喝
		price	0
		name	喝
		info	讓我們慶祝吧
		arg		nocount
			use		1	挑剔的朗姆酒	100%	感覺很好

@@ITEM
	no		29
	type	飾品
	code	boots
	name	時髦的靴子
	info	這些是非常時尚的靴子
	price	20000
	cost	0
	limit	1/0
	scale	雙
	pop		1d
	@@use
		time	1h
		scale	雙
		action	穿上
		price	0
		name	穿著出門
		info	讓我們到街上去慶祝
		arg		nocount
			use		1	時髦的靴子	100%	獨占了所有人的視線

@@ITEM
	no		77
	type	道具
	code	party
	name	慶祝用套組
	info	突然想開派對的時候
	price	200000
	cost	0
	limit	1/0
	scale	組
	@@use
		time	4h
		action	派對開始
		price	0
		name	慶祝派對
		info	今晚不用在乎禮節
		func	popup
		param	1000,開了派對
		arg		nocount
			use		1	慶祝用套組	100%	明天的活力正在沸騰

@@ITEM
	no		78
	type	本
	code	port-exp
	name	轉職指南
	info	對於那些想換工作的人
	price	10000
	limit	1
	pop		1d
	scale	組
	plus	1h
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成藥屋
		info	忘記其他職業的所有技術經驗，學習調和藥物的技術。
		okmsg	感覺自己成了藥屋
		param	15,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,drug
			use		1	轉職指南
		func	_local_
			######################################################################
			# ★熟練度交換（指定アイテムへ、他のアイテムの熟練度を移動させる）
			#   param1 熟練度をプラスしたいアイテムの番号(1~)
			#   param2 熟練度をマイナスするアイテムの番号(1~) (:区切りで複数指定化)
			#   param3 熟練度を移動する際の係数（0~) (0.5だと半分にして移動)
			#   注意：熟練度の合計チェックはしていないので、係数を1より大きくするのはやめた方がいいです。
			######################################################################
			my $ret="";
			
			if($USE->{param1})
			{
				my $exp1=$DT->{exp}{$USE->{param1}};
				my $exp2=0;
				
				foreach my $exps (split(/:/,$USE->{param2}))
				{
					my $exp=$DT->{exp}{$exps};
					next if !$exp || $exps==$exp1;
					$exp2+=$exp;
					delete($DT->{exp}{$exps});
					my $msg=$ITEM[$exps]->{name}."的熟練度從 ".int($exp/10)."% 變成 0% 了";
					$ret.=$msg."<br>";
					WriteLog(0,$DT->{id},$msg);
				}
				$exp2=int($exp2*$USE->{param3});
				$exp1+=$exp2;
				$exp1=1000 if $exp1>1000;
				my $msg=$ITEM[$USE->{param1}]->{name}."的熟練度從 ".int($DT->{exp}{$USE->{param1}}/10)."% 變成 ".int($exp1/10)."% 了";
				$ret.=$msg."<br>";
				WriteLog(0,$DT->{id},$msg);
				$DT->{exp}{$USE->{param1}}=$exp1;
			}
			$DT->{job}=$USE->{param4},$ret.='職業變成「'.$main::JOBTYPE{$USE->{param4}}.'」了' if $USE->{param4} && $USE->{param4} ne '_default_';
			$DT->{job}='',$ret.='職業變成「不定」了' if $USE->{param4} eq '_default_';
			
			return $ret;
		_local_
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成製皮匠
		info	忘記其他職業的所有技術經驗，學習製皮的技術。
		okmsg	感覺自己成了製皮匠
		func	_local_1
		param	16,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成木工
		info	忘記其他職業的所有技術經驗，學習木工的技術。
		okmsg	感覺自己成了木工
		func	_local_1
		param	17,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成飾品加工屋
		info	忘記其他職業的所有技術經驗，學習飾品加工的技術。
		okmsg	感覺自己成了飾品加工屋
		func	_local_1
		param	66,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成劍屋
		info	忘記其他職業的所有技術經驗，學習劍屋的技術。
		okmsg	感覺自己成了劍屋
		func	_local_1
		param	20,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成盾屋
		info	忘記其他職業的所有技術經驗，學習盾屋的技術。
		okmsg	感覺自己成了盾屋
		func	_local_1
		param	21,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成鎧屋
		info	忘記其他職業的所有技術經驗，學習鎧屋的技術。
		okmsg	感覺自己成了鎧屋
		func	_local_1
		param	22,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成杖屋
		info	忘記其他職業的所有技術經驗，學習杖屋的技術。
		okmsg	感覺自己成了杖屋
		func	_local_1
		param	23,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成探礦者
		info	忘記其他職業的所有技術經驗，學習探礦者的技術。
		okmsg	感覺自己成了探礦者
		func	_local_1
		param	9,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成伐木工
		info	忘記其他職業的所有技術經驗，學習伐木的技術。
		okmsg	感覺自己成了伐木工
		func	_local_1
		param	12,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成書屋
		info	忘記其他職業的所有技術經驗，學習書屋的技術。
		okmsg	感覺自己成了書屋
		func	_local_1
		param	10,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,book
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成酪農家
		info	忘記其他職業的所有技術經驗，學習酪農家的技術。
		okmsg	感覺自己成了酪農家
		func	_local_1
		param	25,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,cow
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	轉職成行腳商人
		info	忘記其他職業的所有技術經驗，學習行腳商人的技術。
		okmsg	感覺自己成了行腳商人
		func	_local_1
		param	14,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,peddle
			use		1	轉職指南
	@@USE
		time	6h
		action	開始轉職修行
		arg		nocount
		name	想放下牌子
		info	放下那個壓在肩膀上的標誌
		func	_local_1
		param	0,,0,_default_
			use		1	轉職指南

@@ITEM
	no		79
	type	道具
	code	gift
	name	禮物卷
	info	得到你想要的！
	price	10000
	cost	10
	limit	10/0
	scale	枚
	@@USE
		time	1h
		action	交換
		name	交換地圖集
		info	各種地圖的組合
		okmsg	感謝您的使用
			use		2	禮物卷
			get		1	到附近山區的地圖
			get		1	到附近礦山的地圖
			get		1	到劍市的地圖
	@@USE
		time	1h
		action	交換
		name	交換入門書籍組合
		info	各種書籍的集合
		okmsg	感謝您的使用
			use		5	禮物卷
			get		1	15
			get		1	16
			get		1	17
	@@USE
		time	1h
		action	交換
		name	交換高級書籍組合
		info	各種書籍的集合
		okmsg	感謝您的使用
			use		10	禮物卷
			get		1	20
			get		1	21
			get		1	22
			get		1	23
	@@USE
		time	1h
		action	交換
		name	交換修行套組
		info	想要提升自己的人
		okmsg	感謝您的使用
			use		2	禮物卷
			get		1	修行套組
	@@USE
		time	1h
		action	交換
		name	交換米諾陶洛斯
		info	對於喜歡米諾陶洛斯的人
		okmsg	感謝您的使用
			use		1	禮物卷
			get		1	25

@@event
	start		10%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	街上開始舉辦感謝祭了。
	endmsg		感謝祭已經結束了。
	info		街上因感謝祭而熱鬧非凡。
	func		_local_
		my $time=$main::TIMESPAN;
		$time=10*3600 if $time>10*3600; # 最大10%制限
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT				#★イベント定義宣言
	start		7%		#★イベント発動確率(1日)
	basetime	12h		#★イベント持続時間ベース
	plustime	24h		#★イベント持続時間ランダム増加。（ランダムで0〜24hプラス)
	code		boom-posyon	#★コード（ユニーク）
	startmsg	街上開始了搶購治療劑的熱潮	#★イベント発動時メッセージ
	endmsg		治療劑的熱潮結束了		#★イベント終了時メッセージ
	info		治療劑相關商品人氣提升			#★イベント発動中メッセージ
		param	藥草			pop/1.5	#★イベント内容（アイテムパラメータ増減指示）
		param	治療劑		pop/1.5	#  書式:アイテム名称,パラメータ名[+-/*]数値
		param	高級治療劑	pop/1.5 #  それぞれのアイテムのパラメータを増減させます。
		param	乙太		pop/1.5 #  パラメータ名は customize.txt と item.cgi で確認してください。
		param	高級乙太	pop/1.5 #  なお、pop==popular,money==price,base==pricebase,half==pricehalf
		param	艾利草			pop/1.5 #  で自動変換されます。
		param	藥草			point*2 #  注意点として、pop 等は値が時間(秒数)なので、
		param	治療劑		point*2 #  売れ行き率を上げたい場合は、値を減少させることになります。
		param	高級治療劑	point*3 #  ちなみにこの例では、藥草系のアイテムの売れ行き率を1.5倍。
		param	乙太		point*2 #  売却時の人気上昇率を2〜4倍に上げています。
		param	高級乙太	point*3
		param	艾利草			point*4

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		ken-sale
	startmsg	對劍的需求似乎在增加
	endmsg		劍的需求已恢復正常水平
	info		對劍的需求不斷增長
		param	木刀				pop/2
		param	鐵劍				pop/2
		param	鋼鐵劍			pop/2
		param	秘銀劍		pop/2
		param	奧利哈鋼劍	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tate-sale
	startmsg	對盾的需求似乎在增加
	endmsg		盾的需求已恢復正常水平
	info		對盾的需求不斷增長
		param	皮盾				pop/2
		param	木盾				pop/2
		param	鐵盾				pop/2
		param	鋼鐵盾			pop/2
		param	秘銀盾		pop/2
		param	奧利哈鋼盾	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		yoroi-sale
	startmsg	對鎧的需求似乎在增加
	endmsg		鎧的需求已恢復正常水平
	info		對鎧的需求不斷增長
		param	皮胸甲			pop/2
		param	木胸甲			pop/2
		param	鐵鎧				pop/2
		param	鋼鐵鎧			pop/2
		param	秘銀鎧		pop/2
		param	奧利哈鋼鎧	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tue-sale
	startmsg	對杖的需求似乎在增加
	endmsg		杖的需求已恢復正常水平
	info		對杖的需求不斷增長
		param	木杖				pop/2
		param	鐵杖				pop/2
		param	鋼鐵杖			pop/2
		param	秘銀杖		pop/2
		param	奧利哈鋼杖	pop/2
@@EVENT
	start		50%		#★発動確率は50%だが、発動は下の「startfunc」次第。
	start		-1		#発動しない
	basetime	12h		#★12hでイベント終了だが、実際終了するかどうかは下の「endfunc」次第。
	plustime	0		#
	code		priceup-yakusou
	startmsg	藥草供不應求
	endmsg		藥草供應的情況恢復了
	info		藥草供不應求，相關產品的價格上漲了
	startfunc	stock_le(1,70)		#★イベント発動条件判断の関数呼び出し。（inc-event-function.cgi）
	#endfunc		stock_ge(1,71)		#★イベント終了条件判断の関数呼び出し。（inc-event-function.cgi）
		param	藥草			price*2		#★標準価格が2倍になります。
		param	治療劑		price*1.5
		param	高級治療劑	price*1.5
		param	乙太		price*1.5
		param	高級乙太	price*1.5
		param	艾利草			price*1.5
		param	藥草			pop*2		#★この場合は売れ行き率が1/2に下がります。
		param	治療劑		pop*1.5
		param	高級治療劑	pop*1.5
		param	乙太		pop*1.5
		param	高級乙太	pop*1.5
		param	艾利草			pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-tetu
	startmsg	鐵供不應求
	endmsg		鐵供應的情況恢復了
	info		鐵供不應求，相關產品的價格上漲了
	startfunc	stock_le(5,70)
	#endfunc		stock_ge(5,71)
		param	鐵塊			price*2
		param	鐵劍			price*1.5
		param	鋼鐵劍		price*1.5
		param	鐵盾			price*1.5
		param	鋼鐵盾		price*1.5
		param	鐵鎧			price*1.5
		param	鋼鐵鎧		price*1.5
		param	鐵杖			price*1.5
		param	鋼鐵杖		price*1.5
		param	鐵塊			pop*2
		param	鐵劍			pop*1.5
		param	鋼鐵劍		pop*1.5
		param	鐵盾			pop*1.5
		param	鋼鐵盾		pop*1.5
		param	鐵鎧			pop*1.5
		param	鋼鐵鎧		pop*1.5
		param	鐵杖			pop*1.5
		param	鋼鐵杖		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-misuriru
	startmsg	秘銀供不應求
	endmsg		秘銀供應的情況恢復了
	info		秘銀供不應求，相關產品的價格上漲了
	startfunc	stock_le(6,70)
	#endfunc		stock_ge(6,71)
		param	秘銀塊			price*2
		param	秘銀劍		price*1.5
		param	秘銀盾		price*1.5
		param	秘銀鎧		price*1.5
		param	秘銀杖		price*1.5
		param	秘銀塊			pop*2
		param	秘銀劍		pop*1.5
		param	秘銀盾		pop*1.5
		param	秘銀鎧		pop*1.5
		param	秘銀杖		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-oriharukon
	startmsg	奧利哈鋼供不應求
	endmsg		奧利哈鋼供應的情況恢復了
	info		奧利哈鋼供不應求，相關產品的價格上漲了
	startfunc	stock_le(7,70)
	#endfunc		stock_ge(7,71)
		param	奧利哈鋼塊			price*2
		param	奧利哈鋼劍		price*1.5
		param	奧利哈鋼盾		price*1.5
		param	奧利哈鋼鎧		price*1.5
		param	奧利哈鋼杖		price*1.5
		param	奧利哈鋼塊			pop*2
		param	奧利哈鋼劍		pop*1.5
		param	奧利哈鋼盾		pop*1.5
		param	奧利哈鋼鎧		pop*1.5
		param	奧利哈鋼杖		pop*1.5

@@EVENT
	start		10%
	basetime	48h
	plustime	24h
	code		plusdown-yakusou
	startmsg	藥草培育業者好像不肯批發藥草了。
	endmsg		藥草培育業者恢復了藥草批發
	info		市場上的藥草供應已經停止。
		param	藥草			plus=-180		#★市場減少
@@EVENT
	start		10%
	basetime	12h
	plustime	12h
	code		plusup-tetu
	startmsg	發現新的鐵礦脈
	endmsg		新的鐵礦脈已經關閉了
	info		鐵的流通量快速增長
		param	鐵塊			plus=720		#★市場への入荷ペースが480s。
@@EVENT
	start		7%
	basetime	9h
	plustime	16h
	code		plusup-misuriru
	startmsg	發現新的秘銀礦脈
	endmsg		新的秘銀礦脈已經關閉了
	info		秘銀的流通量快速增長
		param	秘銀塊			plus=960
@@EVENT
	start		5%
	basetime	6h
	plustime	18h
	code		plusup-oriharukon
	startmsg	發現新的奧利哈鋼礦脈
	endmsg		新的奧利哈鋼礦脈已經關閉了
	info		奧利哈鋼的流通量快速增長
		param	奧利哈鋼塊			plus=1200


# 上位優先で万引きイベント
@@EVENT
	start		100% #old50%
	basetime	0h		#★持続系のイベントではないので時間は0。
	plustime	0h
	code		manbiki
	info		偷竊
	startfunc	_local_(400,200)
		#★実はこの関数がイベントの本体になってる
		my($hitproba,$breakproba)=@_;
		#狙われる確率,機器人破壊確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"看門機器人"-1])
			{
				return (0,$DT->{shopname}.'有人企圖入室行竊，但被制止了。') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"看門機器人"-1]--;
				return (0,$DT->{shopname}.'有人企圖入室行竊，'.$ITEM[@@ITEMNO"看門機器人"]->{name}.'被破壊了。');
			}
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/10);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'被偷了相當於總額'.GetMoneyString($count).'的商品。') if $count;
			return (0,'闖入'.$DT->{shopname}.'的小偷什麼都沒拿就逃走了。');
		}
		return 0;
	_local_

@@EVENT
	start		20%
	basetime	0h
	plustime	0h
	code		goutou
	info		強盗
	startfunc	_local_(700)
		#★実はこの関数がイベントの本体になってる
		my($hitproba)=@_;
		#狙われる確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"看門機器人"-1])
			{
				$DT->{item}[@@ITEMNO"看門機器人"-1]--;
				return (0,$DT->{shopname}.'有強盜闖入，'.$ITEM[@@ITEMNO"看門機器人"]->{name}.'被破壞了。');
			}
			
			$DT->{rank}-=int($DT->{rank}/5);
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/4);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'被搶了相當於總額'.GetMoneyString($count).'的商品。') if $count;
			return (0,'闖入'.$DT->{shopname}.'的強盜什麼都沒拿就逃走了。');
		}
		return 0;
	_local_


# 低資金優先で資金援助イベント
@@EVENT
	start		30%
	code		getmoney
	info		資金援助
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,$_->{shopname}.'收到了共'.GetMoneyString($money).'的補助金');
		}
		return 0;
	_local_

# 下位優先で人気アップイベント
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		getpop
	info		人氣提升
	startfunc	_local_(1000)
		my($pop)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{rank}+=$pop;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,'雜誌上介紹了'.$_->{shopname}.'，人氣提升了。');
		}
		return 0;
	_local_

# 抽獎卷イベント
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	info		抽獎卷抽選
	startfunc	_local_
		WriteLog(2,0,"抽獎卷的開獎開始了");
		foreach my $DT (@DT)
		{
			my $count=$DT->{item}[11-1];
			$DT->{item}[11-1]=0;
			next if !$count;
			
			foreach(1..$count)
			{
				my $rnd=rand(6096454);
				my $hit=0;
				
				$hit=5 if $rnd<152411;
				$hit=4 if $rnd<10000;
				$hit=3 if $rnd<216;
				$hit=2 if $rnd<6;
				$hit=1 if $rnd<1;
				
				if($hit)
				{
					my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
					
					$DT->{money}+=$getmoney;
					$DT->{money}=$main::MAX_MONEY if $DT->{money}>$main::MAX_MONEY;
					WriteLog(($hit<=3?1:2),0,$DT->{shopname}."抽中了$hit等獎，".GetMoneyString($getmoney)."！");
				}
			}
		}
		return 0;
	_local_

@@FUNCINIT
#行家的精隨を持っている場合、買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{item}[@@ITEMNO"行家的精隨"-1];

#職業が「行腳商人」の場合、買い物に必要な時間を1/2にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'peddle';

@@FUNCITEM
######################################################################
# ★本or地圖がボロボロになって破棄するという処理
######################################################################
sub lostbook
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,$ITEM[$itemno]->{name}.'已經破爛到看不懂，就扔掉了。');
	}
	return "";
}
######################################################################
# ★人気アップ(汎用)
#   param1 アップポイント
#   param2 最近の出来事用コメント 表示方式:●●商店がparam2
######################################################################
sub popup
{
	my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
	$DT->{rank}+=$up;
	$DT->{rank}=10000 if $DT->{rank}>10000;
	
	my $ret=$USE->{param2}."：人氣提升了".int($up/100)."%";
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}." ".$USE->{param2});
	
	return $ret;
}

@@FUNCUPDATE
sub UpdateResetBefore #決算直前の処理(関数名固定)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#賞品授与
		my @TOP123=(
			[
				['禮物卷',	[[@@ITEMNO "禮物卷", 5],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 4],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 3],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['機器人',	[[@@ITEMNO "看門機器人", 1],		],],
				['慶祝用品',[[@@ITEMNO "整隻烤火雞", 1],	],],
				['慶祝用品',[[@@ITEMNO "挑剔的朗姆酒", 1],	],],
				['慶祝用品',[[@@ITEMNO "時髦的靴子", 1],	],],
			],
			[
				['禮物卷',	[[@@ITEMNO "禮物卷", 3],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 3],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['禁斷之書',	[[@@ITEMNO "禁斷之書", 1],			],],
				['慶祝用品',[[@@ITEMNO "整隻烤火雞", 1],	],],
				['慶祝用品',[[@@ITEMNO "挑剔的朗姆酒", 1],	],],
				['慶祝用品',[[@@ITEMNO "時髦的靴子", 1],	],],
			],
			[
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],		],],
				['慶祝用品',[[@@ITEMNO "整隻烤火雞", 1],	],],
				['慶祝用品',[[@@ITEMNO "挑剔的朗姆酒", 1],	],],
				['慶祝用品',[[@@ITEMNO "時髦的靴子", 1],	],],
			],
			[
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 1],			],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],		],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],		],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],		],],
				['慶祝用品',[[@@ITEMNO "整隻烤火雞", 1],	],],
				['慶祝用品',[[@@ITEMNO "挑剔的朗姆酒", 1],	],],
				['慶祝用品',[[@@ITEMNO "時髦的靴子", 1],	],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"本次優勝") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"可惜第二名的") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"勉強得名的") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"作為特別獎".($i+1)."名的") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."收到".$getitem[0]."";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."作為".$ITEM->{name}."的獎品，獲得".$itemnocount[1].$ITEM->{scale},1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"但是由於超過了最大持有數量，".$cnt.$ITEM->{scale}."被丟棄了",1) if $cnt;
			}
		}
	}
}

sub UpdateResetAfter #決算直後の処理(関数名固定)
{
	UpdateTodayEraseTech();
	
	sub UpdateTodayEraseTech
	{
		foreach my $DT (@DT)
		{
			my $expsum=0;
			foreach(values(%{$DT->{exp}}))
			{
				$expsum+=$_;
			}
			#$expsum=5000 if $expsum>5000;
			
			next if $expsum<=4000;
			$expsum-=4000;
			
			foreach my $itemno (@@ITEMNO"鐵匠的技術",@@ITEMNO"魔法的知識",@@ITEMNO"解體屋之魂",@@ITEMNO"行家的精隨")
			{
				if($DT->{item}[$itemno-1] && rand(14000)<$expsum)
				{
					my $msg=$DT->{shopname}."遺忘了初心，失去了".$ITEM[$itemno]->{name};
					WriteLog(2,0,0,$msg,1);
					WriteLog(0,$DT->{id},0,"失去了".$ITEM[$itemno]->{name},1);
					$DT->{item}[$itemno-1]--;
				}
			}
		}
	}
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem の処理
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 を設定すると、システム側の最近の出来事新装開店メッセージを抑制します。
# $DEFINE_FUNCNEW_NOLOG=1;
# WriteLog(1,0,0,$DT->{shopname}."がエントリーしました",1);

# その他、新装開店時に独自の処理を追加できます。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移転時刻を記録
if($DT->{job} eq 'peddle')
{
	# 行商人(peddle)には移転消費時間の1/2を返還
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'轉移時間大概是'.GetTime2HMS($DT->{_MoveTownTime}).'會完成',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'原始轉移街道送了餞別禮，得到'.GetMoneyString(GetUserDataEx($DT,'_so_present_money')).'了',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # 滞在期間1日に付き\5000を餞別として資金へ
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} を削除
}

@@FUNCBUY
# package item です。
# 
# $item::BUY を利用できます。$item::BUY の構造はマニュアルの @@ITEM funcb をご覧ください。
# 商品毎の処理は @@ITEM funcb を利用してください。

if($BUY->{whole})
{
	# 市場からの仕入の場合、\500000に付き1枚の禮物卷を進呈する。
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"禮物卷",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'收到了市場贈送的禮物卷'.$count.'枚') if $count;
}

@@END #定義終了宣言(以降コメント扱い)

------------
●簡単な説明
------------

全ての商品/イベントはこのファイルを変換し作成されます。

このファイルをカスタマイズすることで、まったく違う世界の SOLD OUT をも
作ることが出来ます。それこそ、ゲームの方向性をも変えることが出来るはず
です。（例えば、モンスター合成ゲームとか、貿易ゲームとか）

そういう個性的なカスタマイズが出てきたら面白いだろうし嬉しいなあと思い、
スクリプトのフリー公開とカスタマイズ方法を用意した次第です。

この標準アイテムデータは、サンプルという意味合いが強いです。とは言って
もバランス調整は1年にわたって行っていますのでそれなりに遊べるレベルだと
思いますが、システムのポテンシャルを十分に引き出しているとは言えないか
もしれません。

ですので、是非、カスタマイズしてみてください。単純に商品名を変えるだけ
でも面白いですが、独自の商品/開発方法/イベントを追加することも比較的簡
単に出来ます。挑戦してみてください。

商品データの更新は、本ファイルを変更してアップロード後、管理メニューで
「商品データ生成/更新」を行うことで可能です。その際、エラーなどがあれば
表示されます。

データ定義の書式は、説明書の中のカスタマイズドキュメントと実際にこのファ
イルを参照し、研究してみてください。特に、このファイルはサンプルになる
と思います。

プログラム読める人は makeitem.cgi を解析してみてください。商品データを
編集するにあたって不便な点は makeitem.cgi を改造すると楽になるかもしれ
ません。

なお、SOLD OUT はこれからも進化させていくつもりです。その際、定義データ
の互換性が損なわれる可能性があります。もちろん、そのようなことが起こら
ないように努めますが、そういう可能性があるということをご了承下さい。

追伸

カスタマイズに興味を持ってくれるみなさんのおかげで、いろんなタイプの
SOLD OUT を目にするようになりました。大変嬉しく思っています。ありがとう
ございます。
