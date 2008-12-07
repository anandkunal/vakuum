#!/usr/bin/env ruby

#Super slim QS action (chmod 777)

require 'cgi'

`open http://thepiratebay.org/search/#{CGI::escape(ARGV[0])}/0/99/0`