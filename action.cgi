#!/usr/bin/perl
# 処理窓口プログラム 2003/11/03 由來
use utf8;
use Encode qw(decode_utf8);
binmode(STDOUT, ':encoding(utf8)');

require './_config.cgi';
RequireFile('inc-func.cgi');
GetQuery();
OutError("bad request") if ($Q{key} =~ /inc/ || $Q{key} =~ /[^\w-]/);
$Q{key}||='main';
RequireFile($Q{key}.'.cgi');
exit;
