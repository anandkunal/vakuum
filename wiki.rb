#!/usr/bin/env ruby

#Super slim QS action (chmod 777)

require 'cgi'

`open http://en.wikipedia.org/wiki/Special:Search?search=#{CGI::escape(ARGV[0])}&go=Go`
