use utf8;
# 住宅街設定ファイル 2003/10/08 由來

# 住宅街の風景をカスタマイズできます。
# 場所の番号は，次のようになっています。
#
#   [No.0]  [No.1]  [No.2] [No.3]
#   [No.4]  [No.5]  [No.6] [No.7]
#                 ・
#                 ・
#   
#  ※定義を増やせば，さらに道路が増えて下に伸ばせます。

#  ＜記述文法＞
#  ・番地コード（101〜）を指定します。
#  ・たとえば104と指定すると，その場所には104番地に家を建てた夫婦が住みます（誰もいなければ空き地）。
#  ・100と指定すると，その場所は教会となります。
#  ・0と指定すると，その場所は樹木となります。

# 順にNo.0,1,2,3…の定義

@Pcode=(100,101,0,102,103,0,104,105,106,107,108,0,109,110,0,0);


# --- キャラクターのセリフ ---
# 見よう見まねでカスタマイズしてください（ぉ

sub CharaDefine
{
@chara=();
my $i=int($NOW_TIME / 3600) % 4;
	if ($i == 1)
		{
		$chara[3]=TagChara(l("わーい わーい"),"a1").$space.$space.TagChara(l("わーい わーい"),"a2").$space;
		}
	elsif ($i == 2)
		{
		$chara[0]=TagChara(l("はやくマイホームを建てないとなぁ・・・"),"d1")
			.TagChara(l("やっと結婚できたねっ"),"d2").$vspace.$vspace;
		}
	elsif ($i == 3)
		{
		$chara[1]=$vspace.TagChara(l("待って～っ"),"c1").$space.$space.TagChara(l("きゃんきゃんっ"),"c2");
		}
	elsif ($STATE->{safety} < 4000)
		{
		$chara[2]=TagChara(l("盗っ人め・・・待て！"),"b1");
		$chara[5]=TagChara(l("この街は警戒がぬるくてラッキー♪"),"b2");
		}
}
1;

