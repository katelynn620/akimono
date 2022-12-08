use utf8;
# 新規開店カスタマイズ用 2004/01/20 由來

# 新規開店時の注意事項の表示などをカスタマイズできます。
# ただし，ある程度のHTMLの知識とプログラムの理解が必要です。

$disp.=<<"HTML";
<BIG>●${\l('はじめに')}</BIG><br><br>
$TB$TR
$TD$image[0]$TD
${\l('このゲームは，ブラウザでプレイできる経営シミュレーションＲＰＧです。')}<br>
${\l('参加する前に，図書館でルールやプレイ方法をよく読んでください。')}
$TRE$TBE
<hr width=500 noshade size=1>
HTML

$i_rand=int(rand($ICON_NUMBER))+1;
$disp.="<BIG>●${\l('新規店舗オープン：残り%1名様',($MAX_USER-$DTusercount))}</BIG><br>";
$disp.=<<"HTML";
<small>${\l('登録は<b>１人１店舗</b>のみ')}</small><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="new">
<INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">
<TABLE>
  <TR>
    <TD>
<SPAN>${\l('名前')}</SPAN>：<INPUT TYPE=TEXT NAME=name> ${\l('半角全角OK')}<BR>
<SPAN>${\l('店名')}</SPAN>：<INPUT TYPE=TEXT NAME=sname> ${\l('半角全角OK')}<BR>

<SPAN>${\l('アイコン')}</SPAN>：<SELECT NAME=icon>
<OPTION value="$i_rand" selected>${\l('ランダム')}</OPTION>
HTML

foreach my $i(1..$ICON_NUMBER)
	{
	$disp.= "<OPTION value=\"$i\">".l('画像')."$i</OPTION>";
	}

$disp.=<<"HTML";
</SELECT> 
<input type="button" value="${\l('アイコン一覧')}" onclick="javascript:window.open('action.cgi?key=icon','_blank','width=450,height=380,scrollbars')">
<br>
<SPAN>${\l('パスワード')}</SPAN>：<INPUT TYPE=PASSWORD maxlength=12 NAME=pass1> ${\l('半角英数のみ')}<BR>
<SPAN>${\l('パスワードもう一度')}</SPAN>：<INPUT TYPE=PASSWORD maxlength=12 NAME=pass2><BR>
HTML

$disp.="<SPAN>${\l('出店キーワード')}</SPAN>：<INPUT TYPE=TEXT NAME=newkey><BR>" if ($NEW_SHOP_KEYWORD);

$disp.=<<"HTML";
<center><INPUT TYPE=SUBMIT VALUE="${\l('登録')}"></center>
</TD></TR>
</TABLE>
<small>※${\l('荒らしと疑われるような名前は避けましょう。')}<br>
※${\l('パスワードは他人が推測できないようなものを。')}</small>
</FORM>
HTML
1;
