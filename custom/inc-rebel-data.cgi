# 自動的に読み込まれる反乱処理およびギルド戦処理 2005/03/30 由來

@@event
	start		0
	code		rebel
	info		發生叛亂了。
	func		_local_
		main::ReadArmy();
		my $time=int($main::TIMESPAN / 3);
		$time=$time * 2 if ($main::STATE->{army} + $main::STATE->{robina} > 15000);
		$main::STATE->{safety}-=int($main::TIMESPAN / 20) if ($main::STATE->{safety} > 2500);
		$main::STATE->{develop}-=int($main::TIMESPAN / 20) if ($main::STATE->{develop} > 2500);
		my $amount=0;
		my $rebelsum=0;
		if ($main::STATE->{robinb})
		{
			$main::STATE->{robinb}-=$time;
			$main::STATE->{robinb}+=int($time/2) if (rand(100) > 75);
			$main::STATE->{robinb}=0 if $main::STATE->{robinb} < 0;
			$amount+=$time*2;
			$rebelsum+=$main::STATE->{robinb};
		}
		foreach(keys(%main::RIOT))
		{
			next if !defined($main::id2idx{$_});
			$DT[$main::id2idx{$_}]->{army}=$main::ARMY{$_};
			$main::ARMY{$_}-=$time;
			$main::ARMY{$_}=0 if ($main::ARMY{$_} < 0);
			$amount+=$time;
			$rebelsum+=$main::ARMY{$_};
		}
		if ($rebelsum < 200)
		{
		delete $main::DTevent{rebel};
		undef %main::RIOT;
		main::PushLog(2,0,"叛亂被護衛軍鎮壓了。");
		main::WriteArmy();
		return 0;
		}
		$amount+=int(rand(5));
		if ($main::STATE->{robina})
		{
		$main::STATE->{robina}-=$amount;
		$amount=0;
		$main::STATE->{robina}=0 if ($main::STATE->{robina}<0);
		}
		$main::STATE->{army}-=$amount if ($amount);
		if ($main::STATE->{army} + $main::STATE->{robina} < 200)
		{
		delete $main::DTevent{rebel};
		foreach(keys(%main::RIOT)) { delete $main::ARMY{$_}; }
		undef %main::RIOT;
		main::PushLog(2,0,"護衛軍被叛軍殲滅了。領主被趕出了城堡。");

		@DTS=sort{$b->{army}<=>$a->{army}}@DT;
		my $rebelid=$DTS[0]->{id};
		$rebelid=$DTS[1]->{id} if ($rebelid == $main::STATE->{leader});
		$rebelid=0 if ($main::STATE->{robinb} > $DTS[0]->{army});

		$main::STATE->{robina}=0;
		$main::STATE->{money}=0 if $main::STATE->{money}<0;
			if ($rebelid)
			{
			main::PushLog(2,0,"首領 ".$DT[$main::id2idx{$rebelid}]->{name}."（".$DT[$main::id2idx{$rebelid}]->{shopname}."）成為了新的領主。");
			$main::STATE->{leader}=$rebelid;
			$main::STATE->{army}=$rebelsum;
			$main::STATE->{robinb}=0;
			}
			else
			{
			main::PushLog(2,0,"首領 $main::BAL_JOB$main::BAL_NAME成為了新的領主。");
			$main::STATE->{leader}=0;
			$main::STATE->{army}=0;
			$main::STATE->{robina}=10000;
			$main::STATE->{robinb}=0;
			$main::STATE->{develop}=5001;
			$main::STATE->{safety}=5001;
			$main::STATE->{devem}=0;
			$main::STATE->{safem}=0;
			$main::DTTaxrate=0;
			my $cnt=int($main::STATE->{money} / 500) * 10 + 10;
			$main::STATE->{money}=0;
			foreach my $DTS (@DT)
				{
				$DTS->{money}+=$cnt;
				}
			main::PushLog(2,0,"$main::BAL_JOB$main::BAL_NAME將城鎮資金".main::GetMoneyString($cnt)."分配給居民了。");
			}
		}
		main::WriteArmy();
		return 0;
	_local_

@@event
	start		0
	code		guildbattle
	endfunc	_local_
			main::ReadGuild();
			main::ReadGuildData();
			@guildlist=sort{$b->{money}<=>$a->{money}}map{$main::GUILD_DATA{$_}->{guild}=$_;$main::GUILD_DATA{$_}}keys(%main::GUILD);
			my $Dguild=$guildlist[0]->{guild};
			main::SetTownData('dominion',$Dguild);
			return 1,"商會「".$main::GUILD{$Dguild}->[$GUILDIDX_name]."」在對抗戰中勝出了。恭喜。";
			_local_
	info		商會對抗戰正在進行中。


@@END #定義終了宣言(以降コメント扱い)

------------
●説明
------------

反乱データです。