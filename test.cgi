#!/usr/local/bin/perl
#-----------------------------
# Created on 08 October 2017
# Copyright (c) 2017 AV Sivaprasad
# Last modified on: 19 Nov, 2017 - Edit 0
#-----------------------------
sub do_main
{
  $cl = $ENV{'CONTENT_LENGTH'};
  if ($cl > 0)
  {
  }
  else
  {
print "Hello World 20!\n";
  }
}
$|=1;
&do_main;

