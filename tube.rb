#!/usr/bin/env ruby

#Super slim QS action (chmod 777)

require 'cgi'

`open http://www.youtube.com/results?search_query=#{CGI::escape(ARGV[0])}&search_type=&aq=f`
